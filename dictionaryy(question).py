######################################################################################################
# Ask number of subjects from the user. Ask the subject name and marks
# from the user and store that into the dictionary and print it.
######################################################################################################
from typing import Dict
from typing import List


def stored_details() -> Dict[str, int]:
    result = {}
    number_of_subject = int(input("Enter number of subject"))
    for _ in range(number_of_subject):
        name = input("enter subject name= ")
        marks = int(input("enter number of subject= "))
        result = [name] = marks
    return result


print(stored_details)


######################################################################################################
# Given a list of integers, create a dictionary that stores each unique integer as a key
# and its frequency as the value. Find the integer with the maximum frequency.
######################################################################################################
def max_frequency(lst: List[int]) -> None:
    max_freq = 0
    max_freq_element = None
    my_dict = {}
    for num in lst:
        my_dict[num] = my_dict.get(num, 0) + 1

    for ele, freq in my_dict.items():
        if freq > max_freq:
            max_freq = freq
            max_freq_element = ele

    print(f"{max_freq_element} has the highest frequency of {max_freq}")


my_list = [1, 4, 6, 9, 7, 2, 8, 4, 3, 1, 3, 8, 6, 5]
max_frequency(my_list)


######################################################################################################
# Create two list. One would be subject name and other would be marks. Join both the list to make it as a dictionary.
# (The length of two lists should be the same).
######################################################################################################
def create_dictionary(subjects: List[str], marks: List[int]) -> Dict[str, int]:
    my_dict = {}
    for i in range(len(subjects)):
        my_dict[subjects[i]] = marks[i]
    return my_dict


s = ["chemistry", "english", "hindi"]
m = [56, 43, 121]

ans = create_dictionary(s, m)
print(ans)


######################################################################################################
# Write a function that takes a dictionary and a key, and returns True
# if the key is found in the dictionary, otherwise False
######################################################################################################
def does_key_exists(dictnry, key) -> bool:
    return key in dictnry


d = {"anirudh": 45, 56: 78, "gender": "Male", 11: 22}
print(does_key_exists(d, "xyz"))


######################################################################################################
# Given two dictionaries, write a function to merge them into a new dictionary.
# If there is any overlap of keys, the value from the second dictionary should overwrite the one from the first dictionary.
######################################################################################################
def merge_dict(dict1: Dict, dict2: Dict) -> Dict:
    # dict1.update(dict2)
    for key, value in dict2.items():
        # dict1.update({key: value})
        dict1[key] = value
    return dict1


d1 = {"a": 54, "b": 11, "c": 90}
d2 = {"a": 100, "b": 200, "d": 56}

print(merge_dict(d1, d2))
######################################################################################################
# Given two dictionaries, write a function to merge them into a new dictionary.
# If there is any overlap of keys, the value from the second dictionary should overwrite the one from the first dictionary.
######################################################################################################


def multiply_factor(dictionary: Dict, factor: int) -> Dict:
    new_dict = dictionary.copy()  # We dont want to change the original one
    for key, value in new_dict.items():
        if isinstance(value, int):
            new_dict[key] = value * factor
    return new_dict


d = {"a": 56, "b": "hello", "c": 55.67, "d": True, "e": 100}

print(multiply_factor(d, 3))
######################################################################################################
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are squares of the keys..
######################################################################################################
my_dict = {}

for i in range(1, 16):
    my_dict[i] = i**2

print(my_dict)


######################################################################################################
# Given a dictionary, write a function that returns a new dictionary containing only the keys that have values of type str.
######################################################################################################
def updateDict(dictnry: Dict) -> Dict:
    new_dict = {}
    for key, value in dictnry.items():
        if isinstance(value, str):
            new_dict[key] = value
            # new_dict.update({key: value})
    return new_dict


my_dict = {"a": "b", "z": 12, "adult": True, "gender": "Male"}
new_d = updateDict(my_dict)
print(new_d)


######################################################################################################
# Ask a string from user. Store the frequency of each character in the dictionary. Then print the character with themaximum
# frequency.
# Input:
# Please enter a string: hello world
# Output:
# The character with the maximum frequency is 'l'.
######################################################################################################
def max_frequency(lst: str) -> None:
    max_freq = 0
    max_freq_element = None
    my_dict = {}
    for num in lst:
        my_dict[num] = my_dict.get(num, 0) + 1

    for ele, freq in my_dict.items():
        if freq > max_freq:
            max_freq = freq
            max_freq_element = ele

    print(f"{max_freq_element} has the highest frequency of {max_freq}")


s = "helllo world"
max_frequency(s)


######################################################################################################
# Write a Python program to combine two dictionary by adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}
######################################################################################################
def mergeDict(dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, int]:
    result = {}
    result.update(dict1)  # Add all the values of dict1 to result first

    for key, value in dict2.items():
        if key in result:
            result[key] = result[key] + value
        else:
            result[key] = value

    return result


d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}
print(mergeDict(d1, d2))
