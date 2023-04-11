# faculty with least pass percentage <=40%
import csv
Telugu = 0
English = 0
Maths = 0
Physics = 0
Chemistry = 0
Social = 0

sub_faculty = {
    'Maths' : 'Murali Krishna',
    'Telugu' : 'Amarnath',
    'English' : 'Samuel',
    'Social' : 'Krishna Reddy',
    'Physics' : 'Raja Gopal',
    'Chemistry' : 'Ravi'
}

least_mark = {}

with open('C:/Users/yalla/OneDrive/Desktop/test_practice/testpractice/assignment.py/student_marks.csv','r') as csvfile:
    data = csv.DictReader(csvfile)
    for marks in data:
        if int(marks['Telugu']) <= 40:
            Telugu += 1
        if int(marks['English']) <= 40:
            English += 1
        if int(marks['Maths']) <= 40:
            Maths += 1
        if int(marks['Physics']) <= 40:
            Physics += 1
        if int(marks['Chemistry']) <= 40:
            Chemistry += 1
        if int(marks['Social']) <= 40:
            Social += 1
    
    least_mark['Telugu'] = Telugu
    least_mark['English'] = English
    least_mark['Maths'] = Maths
    least_mark['Physics'] = Physics
    least_mark['Chemistry'] = Chemistry
    least_mark['Social'] = Social

print(least_mark)
least_pass_perc = max(least_mark.items(),key=lambda x:x[1])
print(f"Least Pass Percentage is {least_pass_perc}")
faculty = (least_pass_perc); (sub,marks) = faculty
print(least_pass_perc)
print(sub_faculty[sub])
