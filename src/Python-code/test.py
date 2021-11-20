import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "R.M.T.D2019@gmail.com"  # Enter your address
receiver_email = "naorfarjun@gmail.com"  # Enter receiver address
password = "RTDapp2019"
message = """\
Subject: Account Verification

Your verification code is: A159633."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)