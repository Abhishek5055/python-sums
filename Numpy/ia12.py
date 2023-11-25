# Initialize variables to store the total and the number of scores
total = 0
num_scores = 3  # You can change this if you want to input a different number of scores

# Use a for loop to input scores
for i in range(num_scores):
    try:
        # Input a score from the user as a string and convert it to a float
        score = float(input(f"Enter score #{i + 1}: "))
        total += score  # Add the score to the total
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Calculate the average score
average = total / num_scores

# Round the average score to two decimal places
average_rounded = round(average, 2)

# Display the total and the rounded average
print(f"Total score: {total}")
print(f"Average score (rounded to 2 decimal places): {average_rounded}")
