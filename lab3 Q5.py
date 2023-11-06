grades = []
invalid = 0

count=0
avg_grade=0
sum_grade=0

high_grade=0
low_grade=0

print("Enter grades (0-100), -1 to end: ")
grade = int(input())
while grade != -1:
    grades.append(grade)
    grade = int(input())

#a) Check grade validity
print("\nGrade Validation:")
for grade in grades:
    if 0 <= grade <= 100:
        print(f"{grade} is Valid")
        count += 1
        sum_grade += grade
    else:
        print(f"{grade} is Invalid")
        invalid += 1

print(f"\nInvalid Grades: {invalid}")

#to calculate average valid grades
avg_grade = sum_grade / count
print("average grade =",avg_grade)
#b) corresponding list with zeros and ones to the original grade list

lst_valid=[]
for grade in grades:
    if 0<=grade<=100 :
        lst_valid.append(1)
    else:
        lst_valid.append(0)

print(lst_valid)

#d) to find lowest and highest grades and specify their location

high_grade=max(grades)

low_grade = high_grade
for i in grades:
     if i < low_grade and i > 0:
        low_grade = i
index_high=grades.index(high_grade)
print('highest grade is:',high_grade , 'and location is:',index_high)
index_low=grades.index(low_grade)
print('lowest grade is:',low_grade , 'and location is:',index_low)

#e)
student_grade=[x for x in grades if x>85]
print("students which are above 85% :",student_grade    ,"their count are :",len(student_grade))

#f)
greater_avg=[y for y in grades if y>avg_grade]
print('student which are greater than average',greater_avg,"their count =",len(greater_avg))








