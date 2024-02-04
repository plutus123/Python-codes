student_scores={
    "Harrry":81,
    "Ron":78,
    "Brook":62,
    "Randy":99,
    "Lisa":63
}
student_grades={}
grade=""
for score in student_scores:
    if student_scores[score]>=90 and student_scores[score]<=100:
        grade="Outstanding"
    elif student_scores[score]>=80 and student_scores[score]<90:
        grade="Excellent"
    elif student_scores[score]>=70 and student_scores[score]<80:
        grade="Acceptable"
    elif student_scores[score]>=60 and student_scores[score]<70:
        grade="Average"
    student_grades[score]=grade
print(student_grades)