import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
msg = "\r\n".join([
  "From: piege.photographique1@gmail.com",
  "To: chikouche.hadjer@gmail.com",
  "Subject: Just a message",
  "",
  "ERWAN le BAWSr!!"
  ])
server.login("piege.photographique1@gmail.com", "azertyuiop1")
server.sendmail("piege.photographique1@gmail.com", "chikouche.hadjer@gmail.com", msg)
server.quit()
