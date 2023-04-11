# topp student with maximun total

#import pandas as indu

# data = indu.read_csv(r'student_marks.csv')
# marks = data.max()
# print(f"the maximum total student is \"student\" with marks \n{marks}")
import csv

with open('C:/Users/yalla/OneDrive/Desktop/test_practice/testpractice/assignment.py/student_marks.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    total_marks = {}
    for row in reader:
        marks = (int(row['Telugu']), int(row['English']), int(row['Maths']), int(row['Physics']), int(row['Chemistry']), int(row['Social']))
        total = sum(marks)
        total_marks[row['studentname']] = total
    students = sorted(total_marks.items(), key=lambda x: x[1], reverse=True)
print(f"The Top Student is {students[0][0]} and his top mark is {students[0][1]}")


