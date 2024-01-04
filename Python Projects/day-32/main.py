import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "joeydon21@gmail.com"
MY_PASSWORD = "hsrlelkbiiaihwgg"

today = dt.datetime.now()
today_tuple = (today.month, today.day)
try:
    data = pandas.read_csv("birthdays.csv")
    birthday = {(row.month, row.day): row for (index, row) in data.iterrows()}
    birthday_name = birthday[today.month, today.day]["name"]
    birthday_email = birthday[today.month, today.day]["email"]

    if today_tuple in birthday:
        random_number = random.randint(1, 3)
        with open(file=f"letter_templates/letter_{random_number}.txt") as letter:
            letter = letter.read()
            letter = letter.replace("[NAME]", birthday_name)
            letter = letter.replace("Angela", "Joey")
            print(letter)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=birthday_email,
                                msg=f"Subject:Happy Birthday!\n\n{letter}")
except KeyError:
    print("No birthdays today!")
