def compute_grade(score):
        if score>= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'

grades = input("enter student grade :").split()
#take each grade in grades list > store it in scores list
scores= [float(grade) for grade in grades]
scores = [compute_grade(score) for score in scores]
for i in range(len(scores)):
        print(f" Grade = {grades[i]}, Score = {scores[i]} ")
