#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : Augists
#   Email         : awzyc2010@163.com
#   File Name     : chapter2.py
#   Last Modified : 2020-05-27 09:26
#
# ====================================================


# ==================================================
## hello world @ hello_world.py
# print("Hello Python World!")


# ==================================================
## value
# message = "Hello Python World!"
# print(message)

# message = "Hello Python Crash Course World!"    # reuse
# print(message)


# ==================================================
## error: wrong spell
# message = "Hello Python World!"
# print(mesage)


# ==================================================
## string surrounding with "" or ''
# print('This is a string')
# print("This is also a string")


# ==================================================
## "" or ''
# message1 = 'I told my friend, "Python is my favorite language!"'
# message2 = "The language 'Python' is named after Monty Python, not the snake."
# message3 = "One of Python's strengths is its diverse and supportive community."


# ==================================================
## string.method @ name.py
# name = "ada lovelace"
# print(name.title())
# print(name.upper())
# print(name.lower())


# ==================================================
## string cat
# first_name = "ada"
# last_name = "lovelace"
# full_name = first_name + " " + last_name
# print("Hello, " + full_name.title() + "!")


# ==================================================
## \character
# print("Python")
# print("\tPython")     # \t for tab

# print("Languages:\n\tPython\n\tC\n\tJavaScript")  # \n for new line


# ==================================================
## rstrip
# favorite_language = 'python '
# print(favorite_language)
# print(favorite_language.rstrip())
# print(favorite_language)


# ==================================================
## lstrip & strip
# favorite_language = ' python '
# print(favorite_language.rstrip())
# print(favorite_language.lstrip())
# print(favorite_language.strip())


# ==================================================
## common syntax error @ apostrophe.py
# message = 'One of Python's strengths is its diverse community.'
# print(message)

# print "Hello Python2.7 world!"  # python2 syntax


# ==================================================
## + - * /
# print(2 + 3)
# print(3 - 2)
# print(2 * 3)
# print(3 / 2)    # auto detect float


# ==================================================
## power ^
# print(3 ** 2)


# ==================================================
## arithmetic priority
# print(2 + 3 * 4)
# print((2 + 3) * 4)


# ==================================================
## float
# print(0.2 + 0.1)    # actually 0.30000000000000004
# print(3 * 0.1)      # actually 0.30000000000000004


# ==================================================
## str(int) @ birthday.py
# age = 23
# # message = "Happy" + age + "rd Birthday!"  # error
# message = "Happy " + str(age) + "rd Birthday!"
# print(message)


# ==================================================
## comment @ comment.py
# This is a comment
# say hello
# print("Hello Python people!")
