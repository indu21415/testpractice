import csv
Telugu = 0
English = 0
Maths = 0
Physics = 0
Chemistry = 0
Social = 0

faculty = {
    'Maths':'Murali Krishna',
    'Telugu':'Amarnath',
    'English':'Samuel',
    'Social':'Krishna Reddy',
    'Physics':'Raja Gopal',
    'Chemistry':'Ravi'
}
fac = {}
with open('C:/Users/yalla/OneDrive/Desktop/test_practice/testpractice/assignment.py/student_marks.csv','r') as file:
    data = csv.DictReader(file)
    for record in data:
        if int(record['Telugu'])>=90:
            Telugu+=1
        if int(record['English']) >= 90:
            English+=1
        if int(record["Maths"]) >= 90:
            Maths+=1
        if int(record["Physics"]) >= 90:
            Physics+=1
        if int(record["Chemistry"]) >= 90:
            Chemistry+=1
        if int(record["Social"]) >= 90:
            Social+=1
        
    fac['Telugu'] = Telugu
    fac["English"] = English
    fac['Maths'] = Maths
    fac['Physics'] = Physics
    fac["Chemistry"] = Chemistry
    fac["Social"] = Social


print(fac)
sub = max(fac.items(),key=lambda x:x[1])
print('highest count:',sub)
a = sub
(subj,score) = a
print(faculty[subj])
