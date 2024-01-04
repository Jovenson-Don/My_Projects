# import smtplib
#
# my_email = "joeydon21@gmail.com"
# password = "hsrlelkbiiaihwgg"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="jovensondon@yahoo.com",
#                         msg="Subject:Hello\n\nThis is the body of email.")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1991, month=3, day=30)
print(date_of_birth)