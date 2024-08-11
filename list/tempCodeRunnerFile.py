my_list=[2,5,7,8,9,10,11,13,17]
for num in range(1,num +1):
    factors = 0 
    for i in range(1,num +1):
        if num % i == 0:
            factors+=1
    if factors == 2:
        print(num)
