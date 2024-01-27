users={'Nathan':2313,'Geez':'pass231','Abebe':'092313133','Miki':"pl3s34D0n'tH4ckM3"}

user_name = input('enter your name: ')
user_pass = input('enter the password: ')
i = 0
if user_name and user_pass == users:
    print("Welcome to GTST Company!")

else:
    if i <= 5:
        print("Incorrect login")
        i = i+1
    else:
        print("Sorry you are limited")

for i in range(5):
    user_name = input('enter your name: ')
    user_pass = input('enter the password: ')

