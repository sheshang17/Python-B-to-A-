# my_list = [5, 1, "python is best", 56.32, "panda", 1, 1, "python is best"]
# result = []
# for num in my_list:
#     if num not in result:
#         result.append(num)
# print(result)


# value = int(input("enter values : "))
# my_list = [5, 1, 56.32, 1, 1, 45, 345, 23, 76]
# if value in my_list:
#     index = my_list.index(value)
#     print(f, "index= {index}")
# else:
#     print(-1)


# my_list = []
# for i in range(5):
#     Value = int(input(f"Enter values at index {i} = "))
#     my_list.append(Value)
# result = []
# for i in range(len(my_list) - 1, -1, -1):
#     result.append(my_list[i])
# print(result)

# my_list = [5, 1, "python is best", 56.43, 5, 5, 1, "python", 2, 4, "python"]
# result = []
# for i in my_list:
#     if i not in result:
#         result.append(i)
# print(result)
# highest_occ_element = 0
# highest_occurence = 0
# for num in result:
#     c = my_list.count(num)
#     print(f"{num} occurs {c} times")
#     if c > highest_occurence:
#         highest_occurence = c
#         highest_occ_element = num
# print(f"highest_occurence_element ={highest_occ_element}")

# my_list1 = [1, 2, 3, 4, 5, 6, 7, 7, 8]
# my_list12 = [6, 7, 8]
# result = []
# for num in my_list1:
#     if num in my_list12:
#         if num not in result:
#             result.append(num)
# print(result)

# my_list = [54, 32, 27, 67, 43, 11, 87, 44, 54, 32, 70]
# largest = float("-inf")
# second_largest = float("-inf")

# for num in my_list:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num < largest:
#         second_largest = num
# print(second_largest)

# my_list = [41, 87, 85, 44]
# product = 1
# for num in my_list:
#     product = product * num
# print(product)

# my_list = [2, 5, 7, 8, 9, 10, 11, 13, 17]
# for num in my_list:
#     factors = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             factors += 1
#     if factors == 2:
#         print(num)
