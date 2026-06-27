import smtplib

print("SMTP FILE:", smtplib.__file__)

server = smtplib.SMTP("smtp.gmail.com", 587)
server.set_debuglevel(1)

server.ehlo()
server.starttls()
server.ehlo()

print("SMTP WORKING ✔")

server.quit()