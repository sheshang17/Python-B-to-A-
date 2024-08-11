my_tuple = (56, 87, 74, 41, 53)
# print(my_tuple)
# print(type(my_tuple))

# my_tuple[0] = 100
# print(my_tuple)

# for i in my_tuple:
#     print(i)

my_list = list(my_tuple)
print(my_tuple)
my_list.append(100)
my_tuple = tuple(my_list)
print(my_tuple)
