import smtplib

session = smtplib.SMTP('smtp.gmail.com',587)
session.starttls()
session.login("shubhamcomputer33@gmail.com","06572291366")
message = "This is a Python file"
session.sendmail("shubhamcomputer33@gmail.com","shubhamcomputer33@gmail.com",message)
session.quit()
