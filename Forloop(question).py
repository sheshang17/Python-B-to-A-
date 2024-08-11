######################################################################################################
# 1.Take 10 integer inputs from user and store them in a list.
# Now, copy all the elements in another list but in reverse order.
######################################################################################################
my_list = []
l = int(input("enter length of the list "))
for i in range(l):
    num = int(input(f"enter number {i+1} = "))
    my_list.append(num)

result = []
for i in range(l - 1, -1, -1):
    result.append(my_list[i])

print(my_list)
print(result)
######################################################################################################
# 2.Make a list. Write a simple program for addition of the 2nd element from start and 2nd element from the end.
######################################################################################################
my_list = [1, 2, 4, 5, 6, 7, 8, 9]
print(my_list[1] + my_list[-1])

######################################################################################################
# Ask 10 numbers from the user and put them into the list. Now remove all the even numbers from that list.
######################################################################################################
my_list = []
l = int(input("enter length of the list "))
for i in range(l):
    num = int(input(f"enter number {i+1} = "))
    my_list.append(num)

result = []
for num in my_list:
    if num % 2 != 0:
        result.append(num)
print(result)
######################################################################################################
# Write a python program which prints all the values whose count is greater than 3.
# (Make sure to make a list with at least 15 numbers)
######################################################################################################
my_list = [3, 8, 7, 3, 5, 5, 5, 5, 3, 8, 3, 3, 3, 1, 3, 8, 9, 6, 7, 8, 9]
result = []

for num in my_list:
    if my_list.count(num) > 3:
        result.append(num)
print(result)
######################################################################################################
# Write a program to remove the nth index element from a list using a function.
######################################################################################################
from typing import List


def removeNth(lst: List, index: int) -> None:
    n = len(lst)
    if index >= n:
        print("Cannot pop, index is out of range")
        return  # To get out from function
    lst.pop(index)


my_list = [34, 11, 91, 59, 33, 22]
removeNth(my_list, 0)
print(my_list)

######################################################################################################
# Make two lists ofsame lengthand pass it to a function.
# Return a third list where each element is the sum of index.
######################################################################################################
from typing import List


def additionOfList(lst1: List[int], lst2: List[int]) -> List[int]:
    n = len(lst1)
    result = []
    for i in range(n):
        total = lst1[i] + lst2[i]
        result.append(total)
    return result


list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 4, 3, 1]

ans = additionOfList(list1, list2)
print(ans)
######################################################################################################
# Write a Python Program to fi nd sum and average of List in Python.
######################################################################################################
my_list = [2, 3, 4, 5, 6, 7]
n = len(my_list)

total = 0
for i in range(n):
    total = total + my_list[i]

print(total)
print(total / n)
######################################################################################################
# Make a list of your own. Make two more empty list like odd and even.
# Put all the even numbers from original list to even and odd numbers to odd
# and print both lists. (Don’t remove anything from original one).
######################################################################################################
my_list = [2, 3, 4, 5, 6, 7, 8]
odd = []
even = []

for num in my_list:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(odd)
print(even)
######################################################################################################
# Make your own list of numbers. Ask a start and end position from User.
# Print the list from start position to end position using Slicing.
######################################################################################################
from typing import List


def lsliceing(lst: List, n: int, m: int):
    result: list = []
    for i in range(n, m + 1):
        result.append(lst[i])
    print(result)


my_list = ["python", 1, 2, 3, 4, "good", 432, 32, 543]
lsliceing(my_list, 3, 5)
# ######################################################################################################
# Make your own list of numbers. Ask a start and end position from User.
# Make another diff erent list which will contain number from start to end position. Use slicing logic.
######################################################################################################
from typing import List


def listsilce(lis: list, start: int, end: int):
    print(lis[start : end + 1])


my_list = ["python", 1, 2, 3, 4, "good", 432, 32, 543]
listsilce(my_list, 3, 5)
# ######################################################################################################
# Make your own list. Write a Python program that takes an integer as an input,
# and make a new list containing the last n elements of the original list. Using slicing logic..
######################################################################################################
from typing import List


def listLastNSlice(lst: List, n: int):
    l = len(lst)
    print(lst[l - n :])


my_list = ["python", 6, 4, 114, True, -54]
listLastNSlice(my_list, 2)
# ######################################################################################################
# Make your own list. Write a Python program that takes an integer as an input,
# and make a new list containing the last n elements of the original list but in reverse order. Using slicing logic.
######################################################################################################
from typing import List


def reverselistLastNSlice(lst: List, n: int):
    l = len(lst)
    result = lst[: l - n - 1 : -1]
    print(result)


my_list = ["python", 1, 2, 3, 4, "good", 432, 32, 543]
reverselistLastNSlice(my_list, 3)
# ######################################################################################################
# Write a python program to interchange fi rst and last elements in a list.
######################################################################################################
from typing import List


def changeposition(lst: int):
    lst[0], lst[-1] = lst[-1], lst[0]


my_list = ["python", 1, 2, 3, 4, "good", 432, 32, 543]
changeposition(my_list)
print(my_list)
# ######################################################################################################
# Write a Python code to split a list into two halves using list slicing. (Keep the length of list even).
######################################################################################################
from typing import List


def splitlist(lst: int):
    mid: int = len(lst) // 2
    fisrt_half = lst[:mid]
    second_half = lst[mid:]
    print(fisrt_half)
    print(second_half)


my_list = ["python", 1, 2, 3, 4, "good", 432, 32, 543]
splitlist(my_list)
# ######################################################################################################
# Ask an integer n from the user. Write a Python program to generate a list of powers of 2 from 1 to n
# using List Comprehension
######################################################################################################
n = int(input("enter number: "))

s = [i**2 for i in range(1, n + 1)]
print(s)
# ######################################################################################################
# Count how many numbers are divisible by 3 and 6 between 1 to 1000 by using list comprehension.
######################################################################################################
div = [i for i in range(1, 1001) if i % 6 == 0]
cont = len(div)
print(cont)
