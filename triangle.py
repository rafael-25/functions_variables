import math

a = float(input("What is the length of side a? "))
b = float(input("What is the length of side b? "))
c = float(input("What is the length of side c? "))

perimeter = a + b + c

s = perimeter / 2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))

area = round(area, 2)

print(f"The perimeter and area of the triangle are {perimeter} and {area}.")
