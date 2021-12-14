
import smtplib, ssl
from email.message import EmailMessage
from os import getenv



def send_login_information(user_email: str, user_password: str, user_name: str):
    email = getenv('EMAIL')
    password = getenv('EMAIL_PASSWORD')
    msg = EmailMessage()
    msg['Subject'] = 'Welcome to Tech Samples!'
    msg['From'] = email
    msg['To'] = user_email
    msg.set_content(f'''
        <h1>Welcome to Tech Samples, {user_name}!</h1>
        <br/>
        <p>Now you have access to the Tech Samples plataform.<p/>
        <p>Login: <em>{user_email}</em><p/>
        <p>Password: <em>{user_password}</em><p/>
        <br/>
        <br/>
        <p>Access the Tech Samples plataform <a href='https://tech-samples.vercel.app/'>now!</a><p/>
    ''')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as smtp:
        smtp.login(email, password)
        smtp.send_message(msg)

send_login_information('lucasrozado@gmail.com', '123', 'Lucas')