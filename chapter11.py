#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2021 All rights reserved.
#
#   Author        : Augists
#   Email         : awzyc2010@163.com
#   File Name     : chapter11.py
#   Last Modified : 2021-01-21 23:49
#
# ====================================================


# ==================================================
## test @ name_function.py
# def get_formatted_name(first, last):
#     """Generate a neatly formatted full name."""
#     full_name = first + ' ' + last
#     return full_name.title()

## @ names.py
# from name_function impoort get_formatted_name

# print("Enter 'q' at any time to quit.")
# while True:
#     first = input("\nPlease give me a first name:")
#     if first == 'q':
#         break
#     last = input("Please give me a last name:")
#     if last == 'q':
#         break
#     formatted_name = get_formatted_name(first, last)
#     print("\tNeatly formatted name:" + formatted_name + ".")


# ==================================================
## unittest @ test_name_function.py
# import unittest
# from name_function import get_formatted_name

# class NamesTestCase(unittest.TestCase): # must inheritance
#     """test name_function.py"""
#     def test_first_last_name(self):
#         """can deal with names like Janis Joplin"""
#         formatted_name = get_formatted_name('janis', 'joplin')
#         self.assertEqual(formatted_name, 'Janis Joplin')

# unittest.main()


# ==================================================
## @ name_function.py
# def get_formatted_name(first, middle, last):
#     full_name = first + ' ' + middle + ' ' + last
#     return full_name.title()

## traceback if error
# E
# ==============================================================================
# ERROR: test_first_last_name(__main__.NamesTestCase)
# ------------------------------------------------------------------------------
# Traceback (most recent call last):
#     File "test_name_function.py", line 8, in test_first_last_name
#         formatted_name = get_formatted_name('janis', 'joplin')
# TypeError: get_formatted_name() missing 1 required positional argument: 'last'

# ------------------------------------------------------------------------------
# Ran 1 test in 0.000s

# FAILED (errors=1)


# ==================================================
## modify @ name_function.py
# def get_formatted_name(first, last, middle=''):
#     if middle:
#         full_name = first + ' ' + middle + ' ' + last
#     else:
#         full_name = first + ' ' + last
#     return full_name.title()


# ==================================================
# import unittest
# from name_function import get_formatted_name

# class NamesTestCase(unittest.TestCase):
#     """test name_function.py"""
#     def test_first_last_name(self):
#         """can deal with names like Janis Joplin"""
#         formatted_name = get_formatted_name('janis', 'joplin')
#         self.assertEqual(formatted_name, 'Janis Joplin')

#     def test_first_last_middle_name(self):  # must begin with `test_`
#         """can deal with names like Wolfgang Amadeus Mozart"""
#         formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
#         self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

# unittest.main()


# ==================================================
# | method                  | usage               |
# |-------------------------|---------------------|
# | assertEqual(a, b)       | if a == b           |
# | assertNotEqual(a, b)    | if a != b           |
# | assertTrue(x)           | if x == True        |
# | assertFalse(x)          | if x == False       |
# | assertIn(iten, list)    | if item in list     |
# | assertNotIn(item, list) | if item not in list |


# ==================================================
## test class @ survey.py
# class AnonymousSurvey():
#     def __init__(self, question):
#         self.question = question
#         self.responses = []

#     def show_question(self):
#         print(question)

#     def store_response(self, new_response):
#         self.responses.append(new_response)

#     def show_results(self):
#         print("Survey results:")
#         for response in responses:
#             print("- " + response)

## @ language_survey.py
# from survey import AnonymousSurvey

# question = "What language did you first learn to speak?"
# my_survey = AnonymousSurvey(question)

# my_servey.show_question()
# print("Enter 'q' at any time to quit.\n")
# while True:
#     response = input("Language: ")
#     if response == 'q':
#         break
#     my_survey.store_response(response)

# print("\nThank you to everyone who participated in the survey!")
# my_survey.show_results()


# ==================================================
## @ test_survey.py
# import unittest
# from survey import AnonymousSurvey

# class TestAnonmyousSurvey(unittest.TestCase):
#     def test_store_single_response(self):
#         question = "What language did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#         my_survey.store_response('English')

#         self.assertIn('English', my_survey.responses)

#     def test_store_three_responses(self):
#         question = "What language did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#         responses = ['English', 'Spanish', 'Mandarin']
#         for response in responses:
#             my_survey.store_response(response)
#         for response in responses:
#             self.assertIn(response, my_survey.responses)

# unittest.main()


# ==================================================
## setUp
# import unittest
# from survey import AnonymousSurvey

# class TestAnonmyousSurvey(unittest.TestCase):
#     def setUp(self):        # will done first
#         question = "What language did you first learn to speak?"
#         self.my_survey = AnonymousSurvey(question)
#         self.responses = ['English', 'Spanish', 'Mandarin']

#     def test_store_single_response(self):
#         self.my_survey.store_response(self.responses[0])
#         self.assertIn(self.responses[0], self.my_survey.responses)

#     def test_store_three_responses(self):
#         for response in responses:
#             self.my_survey.store_response(response)
#         for response in responses:
#             self.assertIn(response, self.my_survey.responses)

# unittest.main()
