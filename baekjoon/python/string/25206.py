N = 20
credits = []
grades = []
for _ in range(N):
    subject, credit, grade = input().split()
    credits.append(float(credit))
    grades.append(grade)
grade_to_score_map = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

total_credit, total_grade = 0.0, 0.0
for credit, grade in zip(credits, grades):
    if grade == 'P':
        continue
    else:
        total_credit += credit
        total_grade += credit * grade_to_score_map[grade]
avg_grade = total_grade / total_credit
print(avg_grade)
        