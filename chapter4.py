#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : Augists
#   Email         : awzyc2010@163.com
#   File Name     : chapter4.py
#   Last Modified : 2020-05-25 19:55
#
# ====================================================


# ==================================================
## for @ magicians.py
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician)


# ==================================================
## for x & action x
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician.title() + ", that was a great trick!")
#     print("I can't wait to see your next trick, " + magician.title() + ".\n")
# print("Thank you, everyone. That was a great magic show!")


# ==================================================
## indent
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
# print(magician)     # wrong indent


# ==================================================
## indent lines
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician.title() + ", that was a great trick!")
# print("I can't wait to see your next trick, " + magician.title() + ".\n")   # indent lines


# ==================================================
## unexpected indent
# message = "Hello Python World"
#     print(message)  # no need to indent


# ==================================================
## unexpected indent after loop
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician.title() + ", that was a great trick!")
#     print("I can't wait to see your next trick, " + magician.title() + ".\n")
#     print("Thank you, everyone. That was a great magic show!")  # not the same as imagination

## notice: no error of the code below
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician.title() + ", that was a great trick!")
#     print("I can't wait to see your next trick, " + magician.title() + ".\n")

#     print("Thank you, everyone. That was a great magic show!")  # although unexpected indent


# ==================================================
## range @ numbers.py
# for value in range(1, 5):
#     print(value)    # no 5


# ==================================================
## range for number list
# numbers = list(range(1, 6))
# print(numbers)


# ==================================================
## range for number list with gap
# even_numbers = list(range(2, 11, 2))
# print(even_numbers)


# ==================================================
## number list full of ^2 @ squares.py
# squares = []              # empty list
# for value in range(1, 11):
#     square = value ** 2   # temp value
#     squares.append(square)

# print(squares)


# ==================================================
## min max sum
# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))


# ==================================================
## list comprehension (faster, more readable, mmore beautiful)
# squares = [value ** 2 for value in range(1, 11)]    # no : at the end of for line
# print(squares)


# ==================================================
## slice @ players.py
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0 : 3])   # no 3

## more convenient
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[: 3])   # omit 0
# print(players[2 :])     # omit 5

## minus index
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[-3 :])


# ==================================================
## for in slice
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print("Here are the first three players on my team:")
# for player in players[: 3]:
#     print(player.title())


# ==================================================
## list to slice @ foods.py
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[ : ]

# my_foods.append('cannoli')
# friend_foods.append('ice cream')

# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite foods are:")
# print(friend_foods)


# ==================================================
## list to list without slice
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods     # duplicate from my to friend

# my_foods.append('cannoli')
# friend_foods.append('ice cream')


# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite foods are:")
# print(friend_foods)


# ==================================================
## tuple stores const value @ dimensions.py
# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# dimensions[0] = 250     # error: not support item assignment


# ==================================================
## for in tuple
# dimensions = (200, 50)
# for dimension in dimensions:
#     print(dimension)


# ==================================================
## change the whole value of tuple
# dimensions = (200, 50)
# print("Original dimensions:")
# for dimension in dimensions:
#     print(dimension)

# dimensions = (400, 100)
# print("\nModified dimensions:")
# for dimension in dimensions:
#     print(dimension)
