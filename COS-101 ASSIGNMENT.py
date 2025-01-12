import math
print("This is a program created for Math calculations.")
print("A: Area of a Triangle")
print("B: Area of a Square")
print("C: Area of a Trapezium")
print("D: Volume of a Cylinder")
print("E: Quadratic Equation")
print("Choose an operation between A-E:")
# Ask for user input
inputMsg = input().lower()

# A function to perform area of a triangle
def a():
    print("Enter the hypotenuse of the triangle:")
    num1 = float(input())
    print("Enter the base of the triangle:")
    num2 = float(input())
    result = 0.5 * num1 * num2
    print(f"The area of the triangle is {result}cm2.")

# A function to perform area of a square
def b():
    print("Enter the length of the square:")
    num1 = float(input())
    result = num1 ** 2
    print(f"The area of the square is {result}cm2.")

# A function to perform area of a trapezium
def c():
    print("Enter the first side of the trapezium:")
    num1 = float(input())
    print("Enter the second side of the trapezium:")
    num2 = float(input())
    print("Enter the height of the trapezium:")
    num3 = float(input())
    result = 0.5 * (num1 + num2) * num3
    print(f"The area of this trapezium is {result}cm2")

# A function to perform division
def d():
    print("Enter the radius of the cylinder:")
    num1 = float(input())
    print("Enter the height of the cylinder:")
    num2 = float(input())
    result = math.pi * (num1) ** 2 * num2
    print(f"The volume of the cylinder is {result} cm3")

# A function to solve quadratic equations
def e():
    print("Enter the coefficient a :")
    a = float(input())
    while a == 0:
        print("Coefficient 'a' cannot be zero. Enter a valid value:")
        a = float(input())
    print("Enter the coefficient b:")
    b = float(input())
    print("Enter the coefficient c:")
    c = float(input())
    d = b**2 - 4*a*c
    if d > 0:
        root1 = (-b + d**0.5) / (2*a)
        root2 = (-b - d**0.5) / (2*a)
        print(f"The roots are real and different: {root1}, {root2}")
    elif d == 0:
        root = -b / (2*a)
        print(f"The roots are real and the same: {root}")
    else:
        realPart = -b / (2*a)
        imagPart = (abs(d)**0.5) / (2*a)
        print(f"The roots are complex: {realPart} + {imagPart}i, {realPart} - {imagPart}i")

# Ensures user input provided is case-insensitive
if inputMsg == "a":
    a()
elif inputMsg == "b":
    b()
elif inputMsg == "c":
    c()
elif inputMsg == "d":
    d()
elif inputMsg == "e":
    e()
# Prints an error provided that user input is invalid
else:
    print("Invalid input. Use letters between A-E.")
