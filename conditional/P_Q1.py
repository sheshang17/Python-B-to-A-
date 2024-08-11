# Q1
 A =int(input("enter number = "))
if A>=0:
    print("p")
else:
    print("N")

# Q2
char = input("enter single charecter =")

# Q3
if char=="a" or char=="e" or char=="i" or char=="0" or char=="u":
    print("vowel")
else:
    print("consonant")

# Q4
num1 = int(input("enter number 1 = "))
num2 = int(input("enter number 2 = "))

if num1%num2==0:
    print("Yes")
else:
     print("NO")

# Q5
class_held= int(input("enter total class held = "))
class_attend= int(input("enter total class attend = "))

class_per=(class_attend/class_held)*100
print(f"percentange of class attented = {class_per}")
 
if class_per>=75:
    print("yes you can sit to the exam")
else:
    print("no you can't sit to the exam")