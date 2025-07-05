students = {
    "Amina": (90, 85, 88),
    "Omar": (70, 60, 75),
    "Lina": (100, 98, 95),
    "Youssef": (55, 40, 60),
    "Hana": (80, 82, 85)
}
def calculate_average(students):
    averages = {}
    for student, scores in students.items():
        average = sum(scores) / len(scores)
        if average >= 85:
            grade = 'pass'
        else:
            grade = 'fail'
        print(f"{student}:{grade}({average:.2f})")
        averages[student] =  grade
    return averages
    
calculate_average(students)
print(calculate_average(students))