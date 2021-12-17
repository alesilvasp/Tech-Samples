
import smtplib, ssl

from os import getenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.models.users_model import UserModel
from app.models.analysis_model import AnalysisModel

def get_all_analysts() -> list[UserModel]:
    return UserModel.query.filter_by(is_admin=False).all()

def get_pending_analysis(analyst_id: int) -> list[AnalysisModel]:
    return AnalysisModel.query.filter_by(
        analyst_id=analyst_id,
        is_concluded=False
    ).all()

def send_email_report():
    email = getenv('EMAIL')
    password = getenv('EMAIL_PASSWORD')
    
    for analyst in get_all_analysts():
        all_analysis = get_pending_analysis(analyst.id)
        analysis_as_html = ''

        if len(all_analysis) == 0:
            continue

        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'Your daily report!'
        msg['From'] = email
        msg['To'] = analyst.email

        for analysis in all_analysis:
            analysis_as_html += f'''
                <tr>
                    <td>{analysis.batch}</td>
                    <td>{analysis.name}</td>
                    <td>{analysis.category}</td>
                    <td>{analysis.made}</td>
                </tr>
            '''
        table = f'''
            <table>
                <thead>
                    <tr>
                        <th>Batch</th>
                        <th>Name</th>
                        <th>Category</th>
                        <th>Made</th>
                    </tr>
                </thead>
                <tbody>{analysis_as_html}</tbody>
            </table>
        '''
        
        msg.attach(MIMEText(f'''
            Hi, {analyst.name}!

            Something went wrong with your daily report

            Please contact your manager.
        ''', 'plain'))

        msg.attach(MIMEText(f'''
            <html>
                <head></head>
                <body>
                    {table}
                </body>
            </html>
        ''', 'html'))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as smtp:
            smtp.login(email, password)
            smtp.sendmail(email, analyst.email, msg.as_string())
