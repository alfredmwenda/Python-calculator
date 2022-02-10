import math 
print("""
CALCULATOR
[1]Sub          [2]Add
[3]Multi        [4]Divide
[5]power        [6]Reminder
[7]square root  [8]Cos
[9]Sine         [10]Tan
""")
print("Enter number for your operation")
a= input(" NO:")
def main():
   if a=="1":
    b= int(input("First no: "))
    c= int(input("Second no: "))
    print(b - c) 
   elif a=="2":
    b= int(input("First no: "))
    c= int(input("Second no: "))
    print(b+c)
   elif a=="3":
    b= int(input("First no: "))
    c= int(input("Second no: "))
    print(b*c)
   elif a=="4":
    b= int(input("First no: "))
    c= int(input("Second no: "))
    print(b/c)
   elif a=="5":
    b= int(input("First no: "))
    c= int(input("Second no: "))
    print(b**c)
   elif a=="6":
    b= int(input("First no: "))
    c= int(input("Second no: "))
    print(b%c)
   elif a=="7":
    x=int(input("Enter no:"))
    print(math.sqrt(x))
   elif a=="8":
    x=int(input("Enter no:"))
    print(math.cos(x))
   elif a=="9":
    x=int(input("Enter no:"))
    print(math.sin(x))
   elif a=="10":
    x=int(input("Enter no:"))
    print(math.tan(x))       

main()

