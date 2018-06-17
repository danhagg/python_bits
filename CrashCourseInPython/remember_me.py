#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 13:30:21 2017
@author: danielhaggerty

"""

# saving and reading user generated data
# store data or it will disappear once program finishes

import json

def get_stored_username():
    """Get stored username if available"""
    filename = 'username.json'
    try:
        with open (filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None  # good practice
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """greet user by username"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username
                + "!")
greet_user()