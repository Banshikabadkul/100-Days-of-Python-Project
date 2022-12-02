
import smtplib
import datetime as dt
import random

now = dt.datetime.now()
curr_day = now.weekday()
quo_list = []

if curr_day == 1:
    with open("quotes.txt", "r") as file:
        data = file.read()
        quo_list = data.split('\n')

    new_quote = random.choice(quo_list)

    my_email = "avnibadkul@gmail.com"
    password = "gnkqprqxgowljjaj"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="atharvdesai064@gmail.com",
                            msg=f"Subject:Hello Message\n\n {new_quote}")
else:
    print("sorry wrong attempt!")





