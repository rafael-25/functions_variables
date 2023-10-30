# Check the data types of different values
print(type("Hello, world"))
print(type(10))
print(type(-3.5))
print(type(False))

# Convert 45 to a string
x = str(45)

# Convert True to a string
t = str(True)

# Check the data types after conversion
print(type(x))
print(type(t))

# Convert the string "1010" to an integer (could also be converted to a float)
print(type(int("1010")))

# Trying to convert "True" to a boolean would not work for 'true'. 
# This is because the input should be either 'True' or 'False' for bool
print(type(bool("True")))
