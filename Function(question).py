######################################################################################################
# 1. check number odd or even
######################################################################################################
def check_even_odd(n: int):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"


n = int(input())
print(check_even_odd(n))


######################################################################################################
# 2  write a functoin check_divisibility(a:int, b : int) check 1st interger checks is divisible by the second interger
######################################################################################################
def check_divisible(n: int, m: int):
    if n % m == 0:
        print("Ture")
    else:
        print("False")


n = int(input())
m = int(input())
check_divisible(n, m)


######################################################################################################
# 3. Function name celcius_to_fahrenheit that convert celsius to fahrenheit and print the result
######################################################################################################
def celcius_to_ferenheit(c: int):
    f = c * 9 / 5 + 32
    return f


c = float(input())
print(celcius_to_ferenheit(c))


######################################################################################################
# 4. simple calculator
######################################################################################################
def simple_cal(n: int, m: int, operation: str):
    if operation == "+":
        print(n + m)
    elif operation == "-":
        print(n - m)


n = int(input())
m = int(input())
operation = input()


simple_cal(n, m, operation)


######################################################################################################
# 5 Return largest of three
######################################################################################################
def large(a: int, b: int, c: int):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


a = int(input())
b = int(input())
c = int(input())


larges = large(a, b, c)
print(larges)


######################################################################################################
# 6. return odd_even
######################################################################################################
def odd_even(n: int):
    return n % 2 == 0


a = int(input())
result = odd_even(a)
print(result)


######################################################################################################
# 7. avg and compare
######################################################################################################
def c_avg(a: int, b: int, c: int):
    return a + b + c / 3


def comp_avg(avg: float, d: int):
    return avg >= d


a = int(input())
b = int(input())
c = int(input())
d = int(input())


avg = c_avg(a, b, c)
result = comp_avg(avg, d)
print(result)


######################################################################################################
# 8. curzon number
######################################################################################################
def curzon(num):
    return (2**num + 1) % (2 * num + 1) == 0


n = int(input())
print(curzon(n))


######################################################################################################
# 9.cube the number
######################################################################################################
def cube(a: int):
    return a * a


a = int(input())
print(cube(a))
######################################################################################################
