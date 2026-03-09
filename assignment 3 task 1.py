# Define the function
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

# Take number from user
number = int(input("Enter a number: "))

# Call the function
result = factorial(number)

# Print the result
print("Factorial of", number, "is:", result)