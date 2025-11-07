def grading_system():
    def grade_letters(grade):
        if grade >= 80:
            return "A (Excellent!)"
        elif grade >= 70:
            return "B (Good job!)"
        elif grade >= 60:
            return "C (Average!)"
        elif grade >= 50:
            return "D (Fair!)"
        elif grade >= 40:
            return "F (Fail!)"
        else:
            return "-"

    student={}
    n = int(input("Number of students: "))

    for i in range(n):
        name =input (f"Enter name of the student{i+1}: ").title().strip()
        grade = float(input("Enter grade of student: "))
        student[name]=grade

    print("\n -----STUDENTS RESULTS------")

    for name, grade in student.items():
        letters = grade_letters(grade)
        print(f"{name},{grade} [{letters}]")

    high = max(student,key=student.get)
    low = min(student,key=student.get)
    average = sum(student.values()) / len(student)
    print(f"{name} has the highest grade {high}")
    print(f"{name} has the lowest grade {low}")
    print(f"Average: {average}")

grading_system()