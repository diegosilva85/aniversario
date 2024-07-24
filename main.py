import smtplib
import datetime as dt
import pandas


def send_mail(quote):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs="diegomelosilva85@gmail.com",
                            msg=f"Subject: Lembrete de "
                            f"aniversario!"
                            f"\n\n{quote}")

print("RODANDO")
email = "diegoestudosmtp@gmail.com"
password = "odom tupg ypqn odqp"


birthdays = pandas.read_csv('birthdays.csv')
dict_birth = birthdays.to_dict(orient="records")


today = dt.date.today()
day = today.day
month = today.month
for birthday in dict_birth:
    if day == birthday['day'] and month == birthday['month']:
        with open("letter.txt", "r") as file:
            letter = file.read()
            letter = letter.replace("NOME", birthday['name'])
        send_mail(letter)
print('fim do script')