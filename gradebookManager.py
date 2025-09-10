global new_gradebook
new_grade = []
roman_grades = [96, 93, 87]
adam_grades = [100, 97, 78]
edin_grades = [67, 77, 82]
gradebook = {'Roman': roman_grades, 'Adam': adam_grades, 'Edin': edin_grades}
def add_student():
    new_grade.clear()
    global new_gradebook
    new_student_name = input("Enter name: ")
    for i in range(3):
        new_student_grade = input("Enter grade:")
        new_student_grade = int(new_student_grade)
        new_grade.append(new_student_grade)
    new_students = {new_student_name:new_grade}
    new_gradebook = gradebook | new_students
add_student()
print(new_gradebook)
add_student()
print(new_gradebook)



