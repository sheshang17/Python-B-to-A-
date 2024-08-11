# num1 = int(input("enter number 1 = "))
# num2 = int(input("enter number 2 = "))

# if num1>num2:
#     print("num1 is greater")
# elif num2>num1:
#     print("num2 is greater")
# else:
#     print("both number are equal")



maths=int(input("enter marks in maths = "))
science=int(input("enter marks in science = "))
english=int(input("enter marks in english = "))
hindi=int(input("enter marks in hindi = "))
Chistory=int(input("enter marks in Chistory = "))

total = maths+science+english+hindi+Chistory

per = (total/500)*100
print(f"percentage scored = {per}")

if per>=91 and per<=100:
    print("A gread ")
elif per>=81 and per<=90:
    print("B grade")
if per>=71 and per<=80:
    print("C gread ")
elif per>=61 and per<=70:
    print("D grade")
elif per>=1 and per<=60:
    print("FAIL")
else:
    print("INVALID PERCENTAGE")