"""
Create an interactive program that:

    (1) Prompts the user to input the radius of a circle.

    (2) Computes the area of the circle using the provided radius.

    (3) Displays the calculated area, rounded to two decimal places.
"""
import math # Only import this module if necessary.

radius = float(input("What is the radius of the circle? "))

area = 2 * math.pi * radius**2

print(f"The area of the circle is {area:.2}")
