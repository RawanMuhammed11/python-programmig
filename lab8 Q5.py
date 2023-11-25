def studentscore(score):
    score = float(score)
    if score >= 90:
        return "A"
    elif score >= 85:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

scorelst = input("enter the score:").split()
gradelst = []
for score in scorelst:
    grade = studentscore(score)
    gradelst.append(grade)

print("studentscore=", scorelst)
print("studentgrade=", gradelst)
