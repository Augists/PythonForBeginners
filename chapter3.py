#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : Augists
#   Email         : awzyc2010@163.com
#   File Name     : hello.py
#   Last Modified : 2020-05-24 22:00
#
# ====================================================

# ==================================================
## hello
# print("hello world")


# ==================================================
## append
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# motorcycles.append('ducati')
# print(motorcycles)


# ==================================================
## append empty list
# motorcycles = []

# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')

# print(motorcycles)


# ==================================================
## insert
# motorcycles = ['honda', 'yamaha', 'suzuki']

# motorcycles.insert(0, 'ducati')
# print(motorcycles)


# ==================================================
## del
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# del motorcycles[0]
# print(motorcycles)


# ==================================================
## del second
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# del motorcycles[1]
# print(motorcycles)


# ==================================================
## pop
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# popped_motorcyle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcyle)


# ==================================================
## pop(number)
# motorcycles = ['honda', 'yamaha', 'suzuki']

# first_woned = motorcycles.pop(0)
# print("THe first motorcycle I owned was a " + first_woned.title() + '.')


# ==================================================
## remove
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)

# motorcycles.remove('ducati')
# print(motorcycles)


# ==================================================
## remove(value)
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)

# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print("\nA " + too_expensive.title() + " is too expensive for me.")


# ==================================================
## sort
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)


# ==================================================
## sort reverse=True
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort(reverse=True)
# print(cars)


# ==================================================
## sorted
# cars = ['bmw', 'audi', 'toyota', 'subaru']

# print("Here is the original list:")
# print(cars)

# print("\nHere is the sorted list:")
# print(sorted(cars))

# print("\nHere is the original list again:")
# print(cars)


# ==================================================
## reverse
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(cars)

# cars.reverse()
# print(cars)


# ==================================================
## lengthA of the list
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(len(cars))


# ==================================================
## out of range
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3])     # list index out of range


# ==================================================
## -1 index
# motorcycles = ['handa', 'yamaha', 'suzuki']
# print(motorcycles[-1])    # only error when list is empty
