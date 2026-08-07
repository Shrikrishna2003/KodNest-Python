# Read the limit
limit = int(input())
number = 1
total = 0

# Initialize the loop variable and total
while number <= limit:
    if number % 2 == 0:
        total = total + number

    # Examine every number from 1 to limit
    number = number + 1

# Display the result
print(f"Even Sum: {total}")
