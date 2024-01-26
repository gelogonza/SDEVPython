# Author: Angelo Gonzalez
# file name: student.py
# desc: asks for student names and gpa then determines if the student qualifies for deans list or honor roll

def student_transcript():
    while True:
        last_name =input("Enter the student's last name(or type 'ZZZ' to quit):")
        if last_name == 'ZZZ':
            break
        
        first_name = input("Enter student's first name:")

        try:
            gpa = float(input("Enter student's GPA:"))
        except ValueError:
            print("Input is invalid. Only enter numeric values.")
            continue
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List. Congratulations!")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} hasn't met the qualifications for either.")

student_transcript()