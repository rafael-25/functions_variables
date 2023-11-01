import math

# Built-in math fuctions: abs(), max(), min()
neg = -100
absolute_value = abs(num1)
print(f"The absolute value of {neg} is {absolute_value}")

# Find the max of two or more numbers
maximum = max(10, 0, 12, 32, -9,  6)
print(f"The maximum is {maximum}")

# Find the min of two or more numbers
minimum = min(100, 99, 98, 100 - 4)
print(f"The minimum is {minimum}")

# Using math.sqrt() to calculate the square root of a number
num = 25
square_root = math.sqrt(num)
print(f"Square root of {num} is {square_root}")

# Using math.sin() and math.cos() to calculate trigonometric values
angle = math.pi / 4  # 45 degrees in radians
sin_value = math.sin(angle)
cos_value = math.cos(angle)
print(f"sin({angle}) is approximately {sin_value}")
print(f"cos({angle}) is approximately {cos_value}")

# Using math.log() to calculate the natural logarithm
number = 10
natural_log = math.log(number)
print(f"Natural logarithm of {number} is approximately {natural_log}")

# Using math.degrees() and math.radians() to convert between degrees and radians
angle_degrees = 45
angle_radians = math.radians(angle_degrees)
print(f"{angle_degrees} degrees is approximately {angle_radians} radians")

# Using math.pi and math.e to access constants
print(f"Value of pi: {math.pi}")
print(f"Value of e: {math.e}")
