import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


gmail_user = 'pythonemailservice7@gmail.com'
gmail_password = 'zvsblugnslnsbufr'

to_emails = ['ardaozturk0560@gmail.com']


subject = 'Gelişmiş Test Maili'
body = """
<html>
  <body>
    <h1>Merhaba!</h1>
    <p>Bu bir <b>test</b> mailidir.</p>
  </body>
</html>
"""


msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = ', '.join(to_emails)
msg['Subject'] = subject

msg.attach(MIMEText(body, 'html'))

file_path = '/dosya/yolu/dosyaadi.pdf'

try:
    with open(file_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {file_path}')
        msg.attach(part)
except Exception as e:
    print(f'Dosya ekleme hatası: {e}')


try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, to_emails, msg.as_string())
    server.quit()
    print('E-posta başarıyla gönderildi!')
except Exception as e:
    print(f'E-posta gönderme hatası: {e}')