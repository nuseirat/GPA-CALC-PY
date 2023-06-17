total_grade_points = 0
total_hours = 0

print("@MohaNuseirat")
print("نظام الجامعة العربية المفتوحة كالتالي:")
print("A=4,   B+=3.5,   B=3,   C+=2.5,   C=2,   D=1.5,   F=0")
print("--------------")

while True:
    # get the grade input from the user
    grade_str = input("Enter the subject grade (or -1 to exit): ")
    if grade_str == "-1":
        break
    grade = float(grade_str)

    # get the hours studied from the user
    hours_str = input("Enter the hours studied (or -1 to exit): ")
    if hours_str == "-1":
        break
    hours = float(hours_str)

    # Calculate the corresponding grade points based on the scale
    if grade == 4.0:
        grade_points = 4.0
    elif grade >= 3.5:
        grade_points = 3.5
    elif grade >= 3.0:
        grade_points = 3.0
    elif grade >= 2.5:
        grade_points = 2.5
    elif grade >= 2.0:
        grade_points = 2.0
    elif grade >= 1.5:
        grade_points = 1.5
    else:
        grade_points = 0

    # Add the grade points and hours to the total
    total_grade_points += grade_points * hours
    total_hours += hours

# Calculate the GPA
gpa = total_grade_points / total_hours

# Print the result
print("Total hours studied: ", total_hours)
print("GPA: ", gpa)