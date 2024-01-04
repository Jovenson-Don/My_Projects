import pandas
import smtplib
import datetime as dt
import random

my_email = "joeydon21@gmail.com"
password = "hsrlelkbiiaihwgg"

data = pandas.DataFrame(open(file="quotes.txt"))
quotes = data.to_dict(orient="records")
random_quote = random.choice(quotes)

today = dt.datetime(year=2023, day=19, month=7)
today = today.weekday()

if today == 2:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Motivational Monday!\n\n{random_quote[0]}")
