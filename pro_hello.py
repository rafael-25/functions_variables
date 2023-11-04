def hello(to="world"):
    """Print a greeting to a recipient or 'world' if no recipient is provided."""
    print("hello," + to)

name = input("What's your name? ")
hello(name)
hello()
print("Program End")
