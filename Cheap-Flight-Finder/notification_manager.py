import smtplib
import os


class NotificationManager:

    def send_emails(self, message_body):
        my_email = os.getenv("MY_EMAIL")
        my_password = os.getenv("MY_PASSWORD")
        target_email = os.getenv("TARGET_EMAIL")


        with smtplib.SMTP("://gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)

            connection.sendmail(
                from_addr=my_email,
                to_addrs=target_email,
                msg=f"Subject:🚨 CHEAP FLIGHT ALERT!\n\n{message_body}".encode('utf-8')
            )
