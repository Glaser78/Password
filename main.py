import random
import string


characters = list(string.ascii_letters + string.digits + "@#!%()^*&")


def generator():
    length = int(input("Kolik znaků má mít heslo: "))
    random.shuffle(characters)
    password = []
    for x in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    print("".join(password))


generator()
