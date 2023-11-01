import math

num1 = -10
num2 = 5

# Calculate the absolute value of a number using abs()
absolute_value = abs(num1)
print(f"The absolute value of {num1} is {absolute_value}")

# Find the maximum of two numbers using max()
maximum = max(num1, num2)
print(f"The maximum between {num1} and {num2} is {maximum}")

# Find the minimum of two numbers using min()
minimum = min(num1, num2)
print(f"The minimum between {num1} and {num2} is {minimum}")

# Using math.sqrt() to calculate the square root of a number
num = 25
square_root = math.sqrt(num)
print(f"Square root of {num} is {square_root}")

# Using math.pow() to calculate the power of a number
base = 2
exponent = 3
result = math.pow(base, exponent)
print(f"{base} raised to the power of {exponent} is {result}")

# Using math.exp() to calculate the exponential value
x = 2.0
exponential = math.exp(x)
print(f"e^{x} is approximately {exponential}")

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
