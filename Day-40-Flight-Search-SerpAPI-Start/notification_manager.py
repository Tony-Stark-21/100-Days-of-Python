import smtplib
import os


class NotificationManager:

    def send_emails(self, message_body, destination_email):
        my_email = os.getenv("MY_EMAIL")
        my_password = os.getenv("MY_PASSWORD")



        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)

            connection.sendmail(
                from_addr=my_email,
                to_addrs=destination_email,
                msg=f"Subject:🚨 CHEAP FLIGHT ALERT!\n\n{message_body}".encode('utf-8')
            )
