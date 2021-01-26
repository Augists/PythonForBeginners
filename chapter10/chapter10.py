#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2021 All rights reserved.
#
#   Author        : Augists
#   Email         : awzyc2010@163.com
#   File Name     : chapter10.py
#   Last Modified : 2021-01-20 23:27
#   Describe      :
#
# ====================================================


# ==================================================
# with open('pi_digits.txt') as file_object:  # auto close
#     contents = file_object.read()   # return an empty string
#     print(contents)                 # when end of file


# ==================================================
# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())        # remove the empty string


# ==================================================
## file path
# file_path = '/home/augists/.../PythonForBeginners/pi_digits.txt'
# with open(file_path) as file_object:


# ==================================================
## read line by line
# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())


# ==================================================
## store in a list
# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
#     for line in lines:
#         print(line.rstrip())


# ==================================================
# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
#     pi_string = ""
#     for line in lines:
#         pi_string += line.strip()
#     print(pi_string)
#     print(len(pi_string))


# ==================================================
## @ write_message.py
## w for write
## r for read (default)
## a for append
## r+ for read and write
# filename = 'programming.txt'
# with open(filename, 'w') as file_object:
#     '''
#     if no file named 'programming.txt', python will create
#     if there is one, python will clear it
#     '''
#     file_object.write("I love programming.")
#     '''
#     if not use \n at the end of the string
#     it will be close to the last
#     '''
#     file_object.write("I love creating new games.")
#     file_object.write("I love creating new games.\n")


# ==================================================
## deal with traceback
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero.")


# ==================================================
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number:")
#     if first_number == 'q':
#         break
#     second_number = input("Second number:")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0.")
#     else:
#         print(answer)


# ==================================================
## @ alice.py
# filename = 'alice.txt'
# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     msg = "Sorry, the file " + filename + " does not exist."
#     print(msg)
# else:
#     words = contents.split()
#     num_words = len(words)
#     print("The file " + filename  + " has about " + str(num_words) + " words.")


# ==================================================
## @ cout_word.py
# def cont_words(filename):
#     try:
#         with open(filename) as f_obj:
#             contents = f_obj.read()
#     except FileNotFoundError:
#         msg = "Sorry, the file " + filename + "does not exist."
#         print(msg)
#     else:
#         words = contents.splist()
#         num_words = len(words)
#         print("The file " + filename + " has about " + str(num_words) + " words.")

# filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
# for filename in filenames:
#     count_words(filename)


# ==================================================
## do nothing in except
# def count_words(filename):
#     try:
#         ...
#     except FileNotFoundError:
#         pass
#     else:
#         ...


# ==================================================
## @ number_writer.py
# import json
# numbers = [2, 3, 5, 7, 11, 13]
# filename = 'numbers.json'
# with open(filename, 'w') as f_obj:
#     json.dump(numbers, f_obj)

# with open(filename) as f_obj:
#     numbers_list = json.load(f_obj)
#     print(numbers_list)


# ==================================================
## @ remember_me.py
# import json

# username = input("What is your name>")
# filename = 'username.json'
# with open(filename, 'w') as f_obj:
#     json.dump(username, f_obj)
#     print("We'll remember you when you come back, " + username + ".")

## @ greet_user.py
# import json

# filename = 'username.json'
# with open(filename) as f_obj:
#     username = json.load(f_obj)
#     print("Welcome back, " + username + ".")
