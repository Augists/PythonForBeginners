#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : Augists
#   Email         : awzyc2010@163.com
#   File Name     : chapter7.py
#   Last Modified : 2020-06-03 08:00
#
# ====================================================


# ==================================================
## input @ parrot.py
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

## input @ greeter.py
# name = input("Please enter your name: ")
# print("Hello, " + name + "!")


# ==================================================
## input(varible) @ greeter.py
# PEP8 indent: no more than 80 chacaters in a line
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "

# name = input(prompt)
# print("\nHello, " + name + "!")


# ==================================================
## int(input)
# age = int(input("How old are you? "))
# print(age)

## int(input) @ rollercoaster.py
# height = input("How tall are you, in inches? ")
# height = int(height)

# if height >= 36:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")


# ==================================================
## mod
# print(4 % 3)
# print(5 % 3)
# print(6 % 3)
# print(7 % 3)


# ==================================================
## combination input and % @ even_or_odd.py
# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)

# if number % 2 == 0:
#     print("\nThe number " + str(number) + " is even.")
# else:
#     print("\nThe number " + str(number) + " is odd.")


# ==================================================
## while @ counting.py
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1


# ==================================================
## user choose @ parrot.py
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)

## prompt
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)


# ==================================================
## use signal @ parrot.py
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)


# ==================================================
## break @ cities.py
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.)"

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to " + city.title() + "!")


# ==================================================
## continue @ counting.py
# current_number = 0
# while current_number < 10:
#     current_number += 1

#     if current_number % 2 == 0:
#         continue

#     print(current_number)


# ==================================================
## avoid  countless @ counting.py
# x = 1
# while x <= 5:
#     print(x)
#     x += 1  # error without this line


# ==================================================
## while in list @ confirmed_users.py
# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print("Verifying user: " + current_user.title())
#     confirmed_users.append(current_user)

# print("\nThe following users have been confirmed:")
# for confirmed_users in confirmed_users:
#     print(confirmed_users.title())


# ==================================================
## while 'xxx' in @ pets.py
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)


# ==================================================
## full dictionary with user input @ mountain_poll.py
# responses = {}
# polling_active = True

# while polling_active:
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")

#     responses[name] = response

#     repeat = input("Would you like to let another person respond?(yes / no)")
#     if repeat == 'no':
#         polling_active = False

# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(name + " would like to climb " + response + ".")
