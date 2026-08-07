# Read the number of scores
n = int(input())

# Read and store scores in a list
scores = []
for i in range(n):
    scores.append(int(input()))

# Display the scores list
print(scores)

# Analyze scores
total_score = sum(scores)
highest_score = max(scores) if n > 0 else 0
lowest_score = min(scores) if n > 0 else 0
average_score = total_score / n if n > 0 else 0

print(f"Total: {total_score}")
print(f"Highest: {highest_score}")
print(f"Lowest: {lowest_score}")
print(f"Average: {average_score}")
