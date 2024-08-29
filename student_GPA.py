
""" 
Header

Name: Jacob McDaniels

File name: studentGPA.py

Description: This python app prompts for student information 
to determine whether or not the student is on Honor Roll or
the Deans List and acts a an open search until ZZZ is entered 
as the students last name.
"""


student_last = input("What is the students last name?")

while student_last != "ZZZ":
    student_first = input("What is the students first name?")
    student_gpa = float(input("What is the students GPA?"))

    if student_gpa >= 3.5:
        print(student_first, student_last, "has made the Deans List!")
    elif student_gpa >= 3.25:
        print(student_first, student_last, "has made Honor Roll!")
    else:
        print(student_first, student_last, "did not make Honor Roll or the Deans List.")
    
    student_last = input("What is the students last name?")

    
