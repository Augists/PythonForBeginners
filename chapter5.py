#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : Augists
#   Email         : awzyc2010@163.com
#   File Name     : chapter5.py
#   Last Modified : 2020-05-26 15:31
#
# ====================================================


# ==================================================
## if @ cars.py
# cars = ['audi', 'bmw', 'subaru', 'toyota']

# for car in cars:
#     if car == 'bmw':      # double '==' is used for comparing an object or variable to a specific value or another object or variable
#         print(car.upper())
#     else:
#         print(car.title())


# ==================================================
## case sensitive
# car = 'Audi'
# print(car == 'audi')


# ==================================================
## not equal @ toppings.py
# requested_topping = 'mushrooms'

# if requested_topping != 'anchovies':
#     print("Hold the anchovies")

## not equal @ magic_number.py
# answer = 17

# if answer != 42:
#     print("That is not the correct answer. Please try again!")


# ==================================================
## condition A and condition B
# age_0 = 22
# age_1 = 18
# print(age_0 >= 21 and age_1 >= 21)  # both are true

# age_1 = 22
# print(age_0 >= 21 and age_1 >= 21)


# ==================================================
## condition A or condition B
# age_0 = 22
# age_1 = 18
# print(age_0 >= 21 or age_1 >= 21)   # either is true

# age_0 = 18
# print(age_0 >= 21 or age_1 >= 21)


# ==================================================
## check if in the list
# requested_toppings = ['mushrooms', 'onions', 'pineapple']
# print('mushrooms' in requested_toppings)

# print('pepperoni' in requested_toppings)


# ==================================================
## check if not in the list @ banned_users.py
# banned_users = ['andrew', 'carolina', 'david']
# user = 'marie'

# if user not in banned_users:
#     print(user.title() + ", you can post a response if you wish.")


# ==================================================
## simply if @ voting.py
# age = 19
# if age >= 18:
#     print("You are old enough to vote!")
#     print("Have you registered to vote yet?")


# ==================================================
## if else
# age = 17
# if age >= 18:
#     print("You are old enough to vote!")
#     print("Have you registered to vote yet?")
# else:
#     print("Sorry, you are too young to vote.")
#     print("Please register to vote as soon as you turn 18!")


# ==================================================
## if elif else @ amusement_park,py
# age = 12
# if age < 4:     # first
#     print("Your admission cost is $0.")
# elif age < 18:  # second
#     print("Your admission cost is $5.")
# else:           # third
#     print("Your admission cost is $10.")


# ==================================================
## if elif ... elif else
# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price = 10
# else:
#     price = 5

# print("Your admission cost is $" + str(price) + ".")


# ==================================================
## no else
# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price = 10
# elif age >= 65:
#     price = 5

# print("Your admission cost is $" + str(price) + ".")


# ==================================================
## if if if ... @ toppings.py
# requested_toppings = ['mushrooms', 'extra cheese']
# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese")

# print("\nFinished making your pizza!")

## error if use if elif elif
# requested_toppings = ['mushrooms', 'extra cheese']
# if 'mushrooms' in requested_toppings:   # true and jump over
#     print("Adding mushrooms")
# elif 'pepperoni' in requested_toppings:
#     print("Adding pepperoni")
# elif 'extra cheese' in requested_toppings:
#     print("Adding extra cheese")

# print("\nFinished making your pizza!")


# ==================================================
## treat specially @ toppings.py
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print("Adding " + requested_topping + ".")

# print("\nFinish making your pizza!")


# ==================================================
## check if empty
# requested_toppings = []
# if requested_toppings:    # check if empty
#     for requested_topping in requested_toppings:
#         print("Adding " + requested_topping + ".")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")


# ==================================================
## lists
# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print("Adding " + requested_topping + ".")
#     else:
#         print("Soryy, we don't have " + requested_topping + ".")
# print("\nFinished making your pizza!")
