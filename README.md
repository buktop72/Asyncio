# Домашнее задание к лекции «Asyncio»
Инструкцию по сдаче домашнего задания вы найдете на главной странице репозитория.

Задание 1
Написать на asyncio + aiopg скрипт. Скрипт выгружает людей из sqlite базы, и отправляет им email с заданным шаблоном:

Уважаемый <Имя пользователя>! 
Спасибо, что пользуетесь нашим сервисом объявлений.
Сообщения должны отправляться конкурентно.
Для отправки email можно использовать aiosmtplib или любую другую асинхронную бибилиотеку.
Шаблон можете задавать любым способом.
Результатом работы является скрипт рассылки.

