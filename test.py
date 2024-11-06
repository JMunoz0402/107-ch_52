def print_divider():
    print("****************************")


# ====== Variables ======
first_name = "clark"
last_name = "kent"
class_number = 75
is_enrolled = True

print(first_name + " " + last_name + " #" + str(class_number))

integer_value = 20  # Integer
pi_value = 3.14159  # Float
greeting = "Hi there!"  # String
is_rainy = False  # Boolean

print_divider()

# ====== Type conversion ======
decimal_num = 7.85
print(int(decimal_num))  # Convert a float to an integer

years_old = 22
print(str(years_old))  # Convert an integer to a string

cost = "45.60"
print(float(cost))  # Convert a string to a float, output: 45.60

# Challenge
# Create some variables called: first_name, last_name, age and show them in a print
# "Hello, <first_name> <last_name>, you are <age> years old."
first_name = "bruce"
last_name = "wayne"
age = 35
print(f"Hello, {first_name} {last_name}, you are {str(age)} years old.")

print_divider()

# ====== Operators ======
m = 8
n = 4

print(m + n)  # Addition
print(m - n)  # Subtraction
print(m * n)  # Multiplication
print(m / n)  # Division
print(m % n)  # Modulus
print(m ** n)  # Exponentiation

print_divider()

# ====== Comparison Operators ======
p = 15
q = 10

print(p == q)  # Equal to
print(p != q)  # Not equal to
print(p > q)  # Greater than
print(p < q)  # Less than
print(p >= q)  # Greater than or equal to
print(p <= q)  # Less than or equal to

m = 6
n = 12
print(".......")
print(m > 3 and n < 15)  # True, because both conditions are true
print(m > 3 or n > 15)  # True, because at least one condition is true
print(not (m > 3))  # False, because m is greater than 3, and we are applying not

print_divider()

# ====== Lists ======
colors = ["red", "green", "blue", "yellow"]
print(colors)  # Print all items
print(colors[0])  # Access the first item
print(colors[-1])  # Access the last item

# List methods
colors.append("purple")  # Adds "purple" to the list
print(colors)

colors.remove("green")  # Removes "green"
print(colors)

print(colors.pop(1))  # Removes and prints item at index 1 ("blue")
print(colors)

print(colors.index("purple"))  # Returns index of "purple"

colors.append("red")
print(colors)  # Print list with duplicate "red"
print(colors.count("red"))  # Count occurrences of "red"

print_divider()

# ====== if statements ======
age = 17

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

num = 15

if num > 10:
    print("num is greater than 10")
elif num == 10:
    print("num is equal to 10")
else:
    print("num is less than 10")

print_divider()

# ====== for loops ======

for i in range(5):  # Loop from 0 to 4
    print(i)

colors = ["red", "green", "blue"]  # Color list

for color in colors:
    print(f"Color: {color}")

print_divider()


# ====== Functions ======
def welcome():
    print("Welcome from the welcome function!")


welcome()  # Calls the function


def greet_person(person_name):
    print("Hello, " + person_name)


greet_person("Lois")
