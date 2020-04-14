# crossposty

<a href="url"><img src="https://github.com/sscottie/crossposty/blob/master/static/images/bg.gif" align="right" height="240" width="360" ></a>

Тестовое задание для Future CTO School.

* Сервис одновременной публикации фото в соц. сетях
* Сложность: задача со звездочкой

## Проектирование сервиса

* Backend - Python (Microframework Flask); JS for working with GeoAPI
* Frontend - JavaScript (Vanilla js and jQuery), CSS, HTML
* UserInterface - Progressive WebApp
* API - vk_api, tweepy

Входные данные: пользователь вводит текст и загружает картинку;

Формат ответа: если не возникает ошибки, выводится сообщение, что команда выполнена, и проверить соц. сети - там Ваше фото и текст. Если произошла ошибка - Error, попробуйте снова.

## Демо

Ссылка на видео: https://drive.google.com/open?id=14gCk9NVHRLBIpm2bkGE4masyehdE5DQt

![crossposty.gif](https://github.com/sscottie/crossposty/blob/master/crossposty.gif)

## Процесс работы программы

* На главном экране можно наблюдать две кнопки:
  * Кнопка FAQ проводит ликбез по пользованию программы;
  * Кнопка начать - основной функционал;
* После нажатия кнопки начать будет предложенно загрузить фотографию (выбрать из ваших файлов) и приложить к ней текст;
* После подтверждения отправки экран отчета - выполнено удачно, или нет, и кнопка "Заново", чтобы вернуться в начало WebApp

## Подготовка и запуск

Подготовка: установлены Python 3, Git

* Склонировать репозиторий и перейти в скачанную директорию:

```sh
$ git clone https://github.com/sscottie/crossposty.git
$ cd crossposty
```
* Установить виртуальное окружение (python или python3, в зависимости от настроек)

```sh
$ python3 -m venv venv
$ source venv/bin/activate
(Windows: venv\bin\activate.bat)
```

* Установить зависимости и пакеты. Запустить приложение

```sh
$ (venv) pip install -r requirements.txt
$ (venv) python3 main.py
```

* Открыть localhost:8080

## Как улучшить проект? Больше соц. сетей!

### License
MIT
By Andrei Titov for Future CTO School

