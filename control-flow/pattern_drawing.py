# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# While loop for each row
while row < size:
    # For loop to print asterisks in each column of the current row
    for col in range(size):
        print("*", end="")  # Print without moving to a new line
    print()  # Move to the next line after each row
    row += 1
