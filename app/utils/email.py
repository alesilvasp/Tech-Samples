
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import getenv



def send_login_information(user_email: str, user_password: str, user_name: str):
    email = getenv('EMAIL')
    password = getenv('EMAIL_PASSWORD')
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Welcome to Tech Samples!'
    msg['From'] = email
    msg['To'] = user_email
    msg.attach(MIMEText(f'''
        Welcome to Tech Samples, {user_name}!

        Now you have access to the Tech Samples plataform.
        Login: {user_email}
        Password: {user_password}

        Access the Tech Samples plataform now![1]

        [1] https://tech-samples.vercel.app/
    ''', 'plain'))
    msg.attach(MIMEText(f'''
        <html>
            <head></head>
            <body>
                <h1>Welcome to Tech Samples, {user_name}!</h1>
                <p>Now you have access to the Tech Samples plataform.<p/>
                <p>Login: <em>{user_email}</em><p/>
                <p>Password: <em>{user_password}</em><p/>
                <br/>
                <br/>
                <p>Access the Tech Samples plataform <a href='https://tech-samples.vercel.app/'>now!</a><p/>
            </body>
        </html>
    ''', 'html'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as smtp:
        smtp.login(email, password)
        smtp.sendmail(email, user_email, msg.as_string())