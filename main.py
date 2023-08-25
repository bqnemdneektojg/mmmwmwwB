import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from telegram.ext import Updater, CommandHandler

def start(update, context):
    # Настройки SMTP Sendinblue
    smtp_host = 'smtp-relay.sendinblue.com'
    smtp_port = 587
    smtp_username = 'YOUR_SENDINBLUE_USERNAME'
    smtp_password = 'YOUR_SENDINBLUE_PASSWORD'

    # Создаем сообщение
    message = MIMEMultipart()
    message['Subject'] = 'Тестовое письмо'
    message['From'] = 'sender@example.com'
    message['To'] = 'recipient@example.com'

    # Добавляем текст письма
    text = MIMEText('Привет, это тестовое письмо!')
    message.attach(text)

    # Отправляем письмо через SMTP Sendinblue
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.login(smtp_username, smtp_password)
        server.sendmail(message['From'], message['To'], message.as_string())

    update.message.reply_text('Письмо успешно отправлено!')

def main():
    
    updater = Updater('YOUR_TELEGRAM_BOT_TOKEN', use_context=True)
    dp = updater.dispatcher

    
    dp.add_handler(CommandHandler('start', start))

    
    updater.start_polling()
    updater.idle()

if name == 'main':
    main()
