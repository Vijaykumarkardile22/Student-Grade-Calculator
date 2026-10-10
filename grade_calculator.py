
# Student Grade Calculator
# Calculate total, average, percentage, and grade.

print("================================")
print("     STUDENT GRADE CALCULATOR")
print("================================")

name = input("Enter student name: ")

mark1 = float(input("Enter marks for Subject 1 (out of 100): "))
mark2 = float(input("Enter marks for Subject 2 (out of 100): "))
mark3 = float(input("Enter marks for Subject 3 (out of 100): "))
mark4 = float(input("Enter marks for Subject 4 (out of 100): "))
mark5 = float(input("Enter marks for Subject 5 (out of 100): "))

marks = [mark1, mark2, mark3, mark4, mark5]

if any(mark < 0 or mark > 100 for mark in marks):
    print("Error: Marks must be between 0 and 100.")
else:
    total = sum(marks)
    average = total / len(marks)
    percentage = (total / 500) * 100

    if any(mark < 35 for mark in marks):
        grade = "F"
        result = "FAIL"
    elif percentage >= 90:
        grade = "A+"
        result = "PASS"
    elif percentage >= 80:
        grade = "A"
        result = "PASS"
    elif percentage >= 70:
        grade = "B"
        result = "PASS"
    elif percentage >= 60:
        grade = "C"
        result = "PASS"
    elif percentage >= 35:
        grade = "D"
        result = "PASS"

    print("\n========== RESULT ==========")
    print("Student Name:", name)
    print("Total Marks:", total, "/ 500")
    print(f"Average Marks: {average:.2f}")
    print(f"Percentage: {percentage:.2f}%")
    print("Grade:", grade)
    print("Result:", result)
    print("============================")
