
def add(x, y):
    return x+y

def subtract(x, y):
    return x-y
    
def multiply(x, y):
    return x*y
    
def divide(x, y):
    return x/y
    
def square(x, y):
    return x**y
    
def quotient(x, y):
    return x//y
    
def remainder(x, y):
    return x%y
    
print("\n------Welcome In Python Calculator------")
    
num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

print("\n-------Operation Types-------\n")

print("1 for addition")
print("2 for subtraction")
print("3 for multiplocation")
print("4 for division")
print("5 for square")
print("6 for quotient")
print("7 for remainder\n")

choice = input("Enter your choice: ")

if choice == "1":
    print("\n",num1,"+",num2,"=",add(num1, num2))
    
elif choice == "2":
    print("\n",num1,"-",num2,"=",subtract(num1, num2))

elif choice == "3":
    print("\n",num1,"*",num2,"=",multiply(num1, num2))
    
elif choice == "4":
    print("\n",num1,"/",num2,"=",divide(num1, num2))
   
elif choice == "5":
    print("\n",num1,"**",num2,"=",square(num1, num2))
    
elif choice == "6":
    print("\n",num1,"//",num2,"=",quotient(num1, num2))
    
elif choice == "7":
    print("\n",num1,"%",num2,"=",remainder(num1, num2))
    
else:
    print("\nPlease enter a valid value")
    
    

