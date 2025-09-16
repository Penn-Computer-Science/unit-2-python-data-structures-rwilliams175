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
    global new_name
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
average_dict = {'Roman': roman_average, 'Adam': adam_average, 'Edin': edin_average, new_name: grade_average}
val_based = {k: v for k, v in sorted(average_dict.items(), key=lambda item: item[1])}
print(val_based)
highest_grade_person = list(val_based.keys())[-1]
highest_grade = list(val_based.values())[-1]
print(str(highest_grade_person) + " has the highest grade, which is a " + str(highest_grade))
def user_input():
    u_choice = input("Would you like to 'add' a student, 'change' a grade, or 'view' the grade book?")
    if u_choice == "":
        print("Have a nice day!")
    elif u_choice == 'add':
        add_student()
    elif u_choice == 'change':
        print(val_based.keys())
        grade_change = input("Which persons grade would you like to change? ")
        if grade_change == "":
            print("Please pick a name")
        elif grade_change == "Roman":
            val_based['Roman'] = input("Please input 3 grades")
        elif grade_change == "Adam":
            val_based['Adam'] = input("Please input 3 grades")
        elif grade_change == "Edin":
            val_based['Edin'] = input("Please input 3 grades")
        elif grade_change == new_name:
            val_based[new_name] = input("Please input 3 grades")
        else:
            print("Have a nice day")
    elif u_choice == 'view':
        print(average_dict)
        print("Have a nice day!")
            
    
