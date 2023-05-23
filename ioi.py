# Задание №1.
# Напишите программу, где я ввожу логин и пароль. И если данные были введены верно,
# то мы выводим Authentication completed, иначе Invalid login or password.
# (Логин должен быть user, пароль - qwerty)

login="user"
password="qwerty"
login1=input()
password1=input()
if login==login1 and password==password1:
    print("Authentication completed")
else:
    print("Invalid login or password")

print()
print()
print()



# Задание №2.
# Напишите программу обмена валют, где я ввожу сумму в тенге и выбираю на какую
# валюту хочу перевести. (Курс USD – 420, EUR – 510, RUB - 5.8).
tenge=int(input("Insert amount in KZT: "))
currency=int(input("Choose currency: "))
if currency==1:
    print(round(tenge/420,2))
elif currency==2:
    print(round(tenge/510,2))
elif currency==3:
    print(round(tenge/5.8,2))




for i in range(1,1001):
   print(i, "ее квадрат", i**2)