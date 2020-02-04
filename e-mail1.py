import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "sinabhi1997@gmail.com"
toaddr = "abhineetsingh192@gmail.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "TEST"

body = "hello from python"

msg.attach(MIMEText(body, 'plain'))

filename = "id.jpg"
attachment = open(r"C:\Users\ABHINEET SINGH\Desktop\email\id.jpg", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "a1b9h9i7")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
