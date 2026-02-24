# Project 1: User Configuration Manager
# Part of the freeCodeCamp "Python Certification" 
# Description: A tool to manage user settings using dictionary CRUD operations.
# Features: Case-insensitivity, input validation, and dynamic state display.

from functools import update_wrapper

def add_setting(dictionary_setting, my_tuple):
    lower_my_tuple = tuple(s.lower() for s in my_tuple)
    check_add = []
    for key in dictionary_setting:
        if key.lower() == lower_my_tuple[0]:
            check_add.append(False)
            return f"Setting '{lower_my_tuple[0]}' already exists! Cannot add a new setting with this name."

        else:
            check_add.append(True)

    if all(check_add):
        dictionary_setting.update({lower_my_tuple[0]: lower_my_tuple[1]})
        # print(dictionary_setting)
        return f"Setting '{lower_my_tuple[0]}' added with value '{lower_my_tuple[1]}' successfully!"


def update_setting(dictionary_setting, my_tuple):
    lower_my_tuple = tuple(s.lower() for s in my_tuple)
    check_update = []
    for key in dictionary_setting:
        if key.lower() == lower_my_tuple[0]:
            dictionary_setting.update({lower_my_tuple[0]: lower_my_tuple[1]})
            # print(dictionary_setting)
            return f"Setting '{lower_my_tuple[0]}' updated to '{lower_my_tuple[1]}' successfully!"
        else:
            check_update.append(False)


    if not all(check_update):
        # print(dictionary_setting)
        return f"Setting '{lower_my_tuple[0]}' does not exist! Cannot update a non-existing setting."

def delete_setting(dictionary_setting, my_key):
    lower_my_key = my_key.lower()

    check_delete = []
    for key in dictionary_setting:
        if key.lower() == lower_my_key:
            dictionary_setting.pop(key)
            # print(dictionary_setting)
            return f"Setting '{lower_my_key}' deleted successfully!"
        else:
            check_delete.append(False)

    if not all(check_delete):
        return "Setting not found!"


def view_settings(dictionary_setting):
    view_result = "Current User Settings:\n"
    if dictionary_setting == {}:
        return "No settings available."
    else:
        for key, value in dictionary_setting.items():
            view_result += f"{key.capitalize()}: {value}\n"
        return view_result


result = view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'})
print(result)
