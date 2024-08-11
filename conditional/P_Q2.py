# Q1
num = int(input("enter number to check = "))
if num ==0:
    print("It is equal to zero")
elif num%2==1:
    print("odd")
else:
    print("Even")

# Q2
num = int(input("enter number = "))
if num%2==0 and num%3==0 and num%8!=0:
    print("it is divisible by 2 ,3 but not 8")
else:
    print("No")

# Q3
num = int(input("enter number you want = "))
last_digi = num%10
print(last_digi)

# Q4
num = int(input("enter the number you want"))
last_digi = num%10
print("last number is",last_digi)
if last_digi%5==0:
    print("this number is divisble by 5")
else:
    print("this number is not divisble by 5 ")

# Q5
bill_a = float(input("enter your bill amount =  "))
if bill_a>=50000:
    discount=30
elif bill_a>=40000 and bill_a<=50000:
    discount=25
elif bill_a>=30000 and bill_a<=40000:
    discount=20
elif bill_a>=10000 and bill_a<=20000:
    discount=10
else:
    discount=0
print(f"you got the {discount}% discount")
final_bill = bill_a -(bill_a*discount/100)
print(f"your final bill is {final_bill}")

# Q6
num1=int(input("enter value of num1 = "))
num2=int(input("enter value of num2 = "))
num3=int(input("enter value of num3 = "))
num4=int(input("enter value of num4 = "))
if num1<num2 and num1<num3 and num1<num4:
    print("num1 is smallest")
elif num2<num1 and num2<num3 and num2<num4:
    print("num2 is smallest")
elif num3<num1 and num3<num3 and num3<num4:
    print("num3 is smallest")
else:
    print("num4 is the smallest")

# Q7
num =int(input("enter the number = "))
if num%3==0 and num%5==0:
    print("Fizzbuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("buzz")
else:
    print(num)