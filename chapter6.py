#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : Augists
#   Email         : awzyc2010@163.com
#   File Name     : chapter6.py
#   Last Modified : 2020-05-28 08:43
#
# ====================================================


# ==================================================
## dictionary @ alien.py
# alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['color'])
# print(alien_0['points'])


# ==================================================
## get value from dictionary
# alien_0 = {'color': 'green', 'points': 5}

# new_points = alien_0['points']
# print("You just earned " + str(new_points) + " points!")


# ==================================================
## append in dictionary
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25

# print(alien_0)


# ==================================================
## empty dictionary
# alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['points'] = 5

# print(alien_0)


# ==================================================
##  modify value
# alien_0 = {'color': 'green'}
# print("The alien is " + alien_0['color'] + ".")

# alien_0['color'] = 'yellow'
# print("The alien is now " + alien_0['color'] + ".")


# ==================================================
## usage of dictionary
# alien_0 = {'x_position' : 0, 'y_position': 25, 'speed': 'medium'}
# print("Original x-position: " + str(alien_0['x_position']))

# # go right
# # distance depend on speed
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3

# # new position
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print("New x-position: " + str(alien_0['x_position']))


# ==================================================
## remove key-value
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# del alien_0['points']
# print(alien_0)


# ==================================================
## format of dictionary and print @ favorite_languages.py
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',   # notice: , unnecessary
# }

# print("Sarah's favorite language is " +
#         favorite_languages['sarah'].title() +
#         ".")


# ==================================================
## for in dictionary.items @ user.py
# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi'
# }

# for key, value in user_0.items():
#     print("\nKey: " + key)
#     print("Value: " + value)


# ==================================================
## for in dictionary.items @ favorite_languages.py
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " +
#             language.title() + ".")


# ==================================================
## for in dictionary.key (omit)
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():    # also for name in favorite_languages:
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
                ", I see your favorite language is " +
                favorite_languages[name].title() + "!")


# ==================================================
# ==================================================
