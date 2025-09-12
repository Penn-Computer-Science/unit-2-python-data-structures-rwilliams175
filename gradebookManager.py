global new_grade
new_grade = []
roman_grades = [96, 93, 87]
roman_average = sum(roman_grades)/3
adam_grades = [100, 97, 78]
adam_average = sum(adam_grades)/3
edin_grades = [67, 77, 82]
edin_average = sum(edin_grades)/3
gradebook = {'Roman': roman_grades, 'Adam': adam_grades, 'Edin': edin_grades}
def add_student():
    global grade_average
    global new_grade
    new_name = input('Enter name: ')
    new_grade = []
    for i in range(3):
        new_student_grade = input("Enter grade:")
        new_student_grade = int(new_student_grade)
        new_grade.append(new_student_grade)
    gradebook.update({new_name:new_grade})
    grade_average = sum(new_grade)/3
add_student()
print(gradebook)
print(grade_average)
print(roman_average)