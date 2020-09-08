#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : Augists
#   Email         : awzyc2010@163.com
#   File Name     : chapter8.py
#   Last Modified : 2020-06-06 15:43
#
# ====================================================


# ==================================================
## function @ greeter.py
# def greet_user():
#     """print hello"""   # docstring
#     print("Hello")

# greet_user()


# ==================================================
## reference
# def greet_user(username):
#     """print hello"""
#     print("Hello, " + username.title() + "!")

# greet_user('jesse')


# ==================================================
## pass location argument @ pets.py
# def describe_pet(animal_type, pet_name):
#     """show information of pets"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet('hamster', 'harry')


# ==================================================
## use several times
# def describle_pet(animal_type, pet_name):
#     """shwo information of pets"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describle_pet('hamster', 'harry')
# describle_pet('dog', 'willie')


# ==================================================
## wrong order
# def describle_pet(animal_type, pet_name):
#     """shwo information of pets"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describle_pet('harry', 'hamster')


# ==================================================
## key-value argument
# def describle_pet(animal_type, pet_name):
#     """show information of pets"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describle_pet(animal_type = 'hamster', pet_name = 'harry')
# describle_pet(pet_name = 'harry', animal_type = 'hamster')


# ==================================================
## default value
# def describle_pet(pet_name, animal_type = 'dog'):
#     """show information of pets"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describle_pet(pet_name = 'willie')


# ==================================================
## error: lose argument
# def describe_pet(animal_type, pet_name):
#     """show information of pet"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet()


# ==================================================
## return value @ formatted_name.py
# def get_formatted_name(first_name, last_name):
#     """return formatted name"""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)


# ==================================================
## empty default middle name
# def get_formatted_name(first_name, last_name, middle_name=''):
#     """return formatted name"""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# musician = get_formatted_name('jimi', 'hendrix', 'lee')
# print(musician)


# ==================================================
## return dictionary @ person.py
# def build_person(first_name, last_name):
#     """return a dictionary including information of a person"""
#     person = {'first': first_name, 'last': last_name}
#     return person

# musician =build_person('jimi', 'hendrix')
# print(musician)


# ==================================================
## return dictionary @ person.py
# def build_person(first_name, last_name, age = ''):
#     """return a dictionary including information of a person"""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person

# musician = build_person('jimi', 'hendrix', 27)
# print(musician)


# ==================================================
## combine with while loop @ greeter.py
# def get_formatted_name(first_name, last_name):
#     """ return formatted name """
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")

#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")


# ==================================================
## pass list @ greet_users.py
# def greet_users(names):
#     """ shwo a simply greet to everyone in list """
#     for name in names:
#         msg = "Hello, " + name.title() + "!"
#         print(msg)

# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)


# ==================================================
## modify list in function @ printint_models.py
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print("Printing model: " + current_design)
#     completed_models.append(current_design)

# print("\nThe following models have been printed: ")
# for completed_model in completed_models:
#     print(completed_model)


# ==================================================
## forbid changing the list in function
# function_name(list_name[:])   # create a copy


# ==================================================
## @ pizza.py
# def make_pizza(*toppings):
#     print(toppings)

# make_pizza('peperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


# ==================================================
# def make_pizza(*toppings):
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print("- " +topping)

# make_pizza('peperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


# ==================================================
## @ user_profile.py
# def build_profile(first, last, **user_info):  # empty dictionary
#     """ create a dictionary including everything we know about user """
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile

# user_profile = build_profile('albert', 'einstein', location = 'princeton',
#         field = 'physics')
# print(user_profile)


# ==================================================
## import
# @ pizza.py
# def make_pizza(size, *toppings):
#     print("\nMaking a " +str(size) + "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)

# @ making_pizzas.py
# import pizza

# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# ==================================================
## import function
# from module_name import function_name


# ==================================================
## alias function
# from pizza import make_pizza as mp

# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')


# ==================================================
## import all funxtion
# from pizza import *


# ==================================================
## no space ... at both sides of = (PEP 8)
# function_name(value_0, parameter_1='value')
