##################### Hard Starting Project ######################
from dataclasses import dataclass

import datetime as dt
import pandas
import smtplib
import random



# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes.
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
now = dt.datetime.now()
now_tuple = (now.month, now.day)
my_email = "arthurreynolds2121@gmail.com"
password = "fgvp bpmr wfvk vwlt"
# 2. Check if today matches a birthday in the birthdays.csv

piece = pandas.read_csv("birthdays.csv")
checked =  {(piece_row["month"], piece_row["day"]): piece_row for (index, piece_row) in piece.iterrows()}

if now_tuple in checked:
    birthday_person = checked[now_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path, "r") as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP_SSL("smtp.gmail.com", port= 465) as connection:
        # connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}"
                            )
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



