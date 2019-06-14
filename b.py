#sending a mail


import smtplib
FROM="bogadipayal573@gmail.com"
TO="xxx@gmail.com"
SUBJECT="mail test"
TEXT="pyhton"
pwd="xxxxxxxxxxxxx"
message="SUBJECT:%s\n\n%s"%(SUBJECT,TEXT)
print(message)
server=smtplib.SMTP("smtp.gmail.com",587)
server.ehlo()
server.starttls()
server.login(FROM,pwd)
server.sendmail(FROM,TO,message)
server.close()
print("successfully sent mail")