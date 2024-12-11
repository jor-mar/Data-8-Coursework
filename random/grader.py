def compute_letter_grades(grade):
    rubric = {90: 'A', 80: 'B', 70: 'C'}
    for i in rubric:
        if grade >= i:
            return rubric[i]
    return 'F'

print(compute_letter_grades(95))
print(compute_letter_grades(85))
print(compute_letter_grades(75))
print(compute_letter_grades(65))
print(compute_letter_grades(55))