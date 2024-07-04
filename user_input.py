# Initialize an empty list to store student data
students = []

# Loop to get name and score for 5 students
for i in range(5):
  name = input(f"Enter student {i+1} name: ")
  score = float(input(f"Enter student {i+1} score: "))

  # Create a dictionary for each student (alternative: use a list)
  student_data = {"name": name, "score": score}  # You can also use a list with [name, score]

  # Append the student data to the students list
  students.append(student_data)

# Print the list (optional)
print(students)



