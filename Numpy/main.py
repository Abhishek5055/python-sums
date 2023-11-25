def display_student_info(students):
    for student in students:
        print(f"Name: {student['name']}, Department: {student['department']}")

def calculate_average_cgpa(students):
    total_cgpa = sum(student['CGPA'] for student in students)
    average_cgpa = total_cgpa / len(students)
    return average_cgpa

# Sample student dictionary data
students = [
    {
        "name": "Alice",
        "age": 20,
        "department": "Computer Science",
        "CGPA": 3.7,
    },
    {
        "name": "Bob",
        "age": 21,
        "department": "Electrical Engineering",
        "CGPA": 3.2,
    },
    {
        "name": "Charlie",
        "age": 22,
        "department": "Mechanical Engineering",
        "CGPA": 3.9,
    },
]

# Display name and department of each student
print("Student Information:")
display_student_info(students)

# Calculate and display the average CGPA of all students
average_cgpa = calculate_average_cgpa(students)
print(f"Average CGPA: {average_cgpa:.2f}")
