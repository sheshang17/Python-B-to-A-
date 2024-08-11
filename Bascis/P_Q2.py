# ADD two number enter by user 
a = int(input("enter the 1st number"))
b = int(input("enter the 2nd number"))
c=a+b
print(f"your adition of two number is = ", c)

#convert the string into integer 
n_s = "234"
print(n_s,type(n_s))
num = int(n_s)
print(num,type(num))

# calculate the area of rectangale using user inpte 
l=int(input("enter the Lenght = "))
w=int(input("enter the widht = "))
z= l*w
print("area of retangle is = ",z)

#calculte the average of the three number 
p = int(input("enter the 1st number = "))
q = int(input("enter the 2nd number = "))
r = int(input("enter the 3rd number = "))
s = (p+q+r)/3
print("avarge of the numbers is" ,s)

#convert the float into integer 
t = 5.55
print(t,type(t))
o =int(t)
print(o,type(o))

#convert the tempreture in ferenheit to celsius
F = int(input("enter the Fehrenheit ="))
c=(F-32)*5/9
print("The tempreture in the celsisus is =",c)

#calculate the sum of 5 subject and find the percentage 
sub1 = int(input("enter marks of 1st subject = "))
sub2 = int(input("enter marks of 2st subject = "))
sub3 = int(input("enter marks of 3st subject = "))
sub4 = int(input("enter marks of 4st subject = "))
sub5 = int(input("enter marks of 5st subject = "))
total =(sub1+sub2+sub3+sub4+sub5)/500*100
print(total)


