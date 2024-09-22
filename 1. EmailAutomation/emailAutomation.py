import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


gmail_user = 'sender@gmail.com'
gmail_password = 'password'

to_emails = ['receiver@gmail.com']


subject = 'Test Mail'
body = """
<html>
  <body>
    <h1>Hello World!</h1>
    <p>This is a <b>test</b> mail.</p>
  </body>
</html>
"""


msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = ', '.join(to_emails)
msg['Subject'] = subject

msg.attach(MIMEText(body, 'html'))

file_path = 'path/To/File.pdf'

try:
    with open(file_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {file_path}')
        msg.attach(part)
except Exception as e:
    print(f'Failed to attach file: {e}')


try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, to_emails, msg.as_string())
    server.quit()
    print('The mail was sent successfully!')
except Exception as e:
    print(f'A problem occurred while trying to send the mail: {e}')
