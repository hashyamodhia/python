#Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
#area = (1/2)*base*height

'''def calculate_area(b,h):
    area = (1/2) * (base * height)
    return area

base = float(input("Enter base\n"))
height = float(input("Enter height\n"))

area = calculate_area(base,height)
print(area)'''

#Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
#rectangle area=length*width

'''def calculate_area(shape,a,b):
    if shape == "triangle":
        area = (1/2) * a * b
        return area
    elif shape == "rectangle":
        area = a * b
        return area
    else:
        area = (1/2) * a * b
        return area

shape = input("Enter shape")
a = float(input("Enter a\n"))
b = float(input("Enter b\n"))
area = calculate_area(shape,a,b)
print(area)'''

#Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
#*
#**
#***
#if input is 4 then it should print

#*
#**
#***
#****
#Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)