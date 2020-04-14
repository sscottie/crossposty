from flask import Flask, render_template, request, redirect, url_for
import json
from werkzeug.utils import secure_filename
from flask import send_from_directory
import tweepy
import os
from instapy_cli import client
import vk_api
from vk_api import VkUpload
import requests

app = Flask(__name__)
#instagram
# INSTAGRAM_USERNAME = 'trepadeira0ru'
# INSTAGRAM_PASSWORD = '135978462'
#twitter - tweepy
TWITTER_consumer_key = ''
TWITTER_consumer_secret = ''
TWITTER_access_token = ''
TWITTER_access_token_secret = ''
#vk_API
VK_LOGIN = 'fyutk5ltvjy'
VK_PASSWORD = 'Trepadeira26841397'

MAIN_FOL = os.path.dirname(os.path.realpath(__file__))

app.config["IMAGE_UPLOADS"] = os.path.join(MAIN_FOL, 'static')
app.config["RESULTS"] = os.path.join(MAIN_FOL, 'results')
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG"]

def allowed_image(filename):
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

def post_to_vk(login, password, post_text, post_image):
    # Авторизация
    vk_session = vk_api.VkApi(login, password)
    vk_session.auth()
    
    upload = VkUpload(vk_session)  # Для загрузки изображений
    
    # Загрузка картинок на сервера вк и получение их id
    photos = [post_image]
    photo_list = upload.photo_wall(photos)
    attachment = ','.join('photo{owner_id}_{id}'.format(**item) for item in photo_list)
    
    # Добавление записи на стену
    vk_session.method("wall.post", {
        'owner_id': None,  # Посылаем себе на стену
        'message': post_text,
        'attachment': attachment,
    })

def post_to_twitter(TWITTER_consumer_key, TWITTER_consumer_secret, TWITTER_access_token, TWITTER_access_token_secret, post_text, post_image):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(auth)
    
    # создать юзера
    user = api.me()
     
    print('Имя: ' + user.name)
    print('тест локейшн: ' + user.location)
    print('друзи: ' + str(user.friends_count))
    
    # load image
    imagePath = post_image
    status = post_text
    
    # Send
    api.update_with_media(imagePath, status)

def post_to_insta(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD, post_text, post_image):
    image = post_image
    
    text = post_text
    
    with client(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD) as cli:
        cli.upload(image, text)

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route("/loaded", methods=["GET", "POST"])
def loaded():
    if request.method == "POST":
        text = request.form.get('text')
        if request.files:
            image = request.files["file-6[]"]
            if image.filename == "":
                print("Неверное имя")
                return render_template("error.html")
            if allowed_image(image.filename):
                filename = secure_filename(image.filename)
                image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
                pathfile = os.path.join(app.config["IMAGE_UPLOADS"], filename)
                file_path = "http://localhost:8080/static/" + filename
                print(file_path)
                post_text = text
                post_image = pathfile
                post_to_vk(VK_LOGIN, VK_PASSWORD, post_text, post_image)
                #post_to_twitter(TWITTER_consumer_key, TWITTER_consumer_secret, TWITTER_access_token, TWITTER_access_token_secret, post_text, post_image)
                # post_to_insta(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD, post_text, post_image)
                return render_template("loaded.html", pathfile=pathfile, text=text)
            else:
                print("Неверное расширение")
                return render_template("error.html")
        post_image = "http://localhost:8080/static/sample.jpg"
        post_text = text
        try:
            post_to_vk(VK_LOGIN, VK_PASSWORD, post_text, post_image)
            #post_to_twitter(TWITTER_consumer_key, TWITTER_consumer_secret, TWITTER_access_token, TWITTER_access_token_secret, post_text, post_image)
            # post_to_insta(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD, post_text, post_image)
        except:
            return render_template("loaded.html", pathfile=pathfile, text=text)
        return render_template("loaded.html", pathfile=pathfile, text=text)
    return render_template("loaded.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)

#Thnks - Made with help of MayorovYuri
