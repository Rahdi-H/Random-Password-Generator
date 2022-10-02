import string
import random

characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')

def password_generator():
    password_length = int(input('Enter, How long the password should be?'))
    random.shuffle(characters)
    password = []
    for _ in range(password_length):
        password.append(random.choice(characters))
    random.shuffle(password)
    password = "".join(password)
    print(password)

option = input('Would you like to generate random password? Yes / No')
if option.lower == 'yes':
    password_generator()
elif option.lower == 'no':
    quit()
else:
    print('please enter a valid input')
    password_generator()
