import sqlite3
from pprint import pprint
import asyncio
from email.message import EmailMessage
import smtplib
from aiosmtplib import SMTP

ya_email = 'your_email@yandex.ru'
ya_password = 'your_password'

async def send_email(receiver, first_name):
    # print(receiver)
    # создаем экземпляр класса EmailMessage
    message = EmailMessage()
    message["From"] = f"{ya_email}"
    message["To"] = receiver
    message["Subject"] = f"Уважаемый, {first_name}!"
    message.set_content("Спасибо, что пользуетесь нашим сервисом объявлений.")
    # создаем экземпляр класса SMTP
    smtp_client = SMTP(hostname="smtp.yandex.ru", port=465, username=f"{ya_email}",
                       password=f"{ya_password}", use_tls=True)

    await smtp_client.connect()
    result = await smtp_client.send_message(message)
    await smtp_client.quit()
    return result


async def main():
    # соединяемся с БД
    conn = sqlite3.connect('contacts.db')
    # создаем объект cursor, что бы делать SQL-запросы к базе
    curs = conn.cursor()
    # выполняем запрос
    curs.execute("SELECT * FROM contacts;")
    # получаем все результаты в contacts
    contacts = curs.fetchall()
    # for contact in contacts:
    #     print(contact[3], contact[1])
    # запускаем одновременную отправку сообщений с помощью gather()
    mail = await asyncio.gather(*[send_email(contact[3], contact[1]) for contact in contacts])
    return mail

if __name__ == "__main__":
    asyncio.run(main())


