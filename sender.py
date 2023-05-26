import smtplib, ssl

def send_email(port, smtp_server, sender_email, password, receiver_email, message):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


if __name__ == "__main__":
    #$ python3 -m smtpd -c DebuggingServer -n localhost:1025
    send_email(1025, "https://localhost","test@test.cz", "test", "receiver@test.cz", "Test Message \n\n This is my last resort!")
