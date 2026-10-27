students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter name: ")
    marks = float(input("Enter aggregate marks: "))
    subject_marks = float(input("Enter minimum subject marks: "))
    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter family income: "))

    if (marks >= 75 and subject_marks >= 40
            and attendance >= 75 and income <= 200000):
        students.append((name, marks))

students.sort(key=lambda x: x[1], reverse=True)

print("\nEligible Students:")
for student in students:
    print(student[0], "-", student[1], "marks")