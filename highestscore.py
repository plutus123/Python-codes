student_scores=input("Input the list of student scores ").split()
for n in range(0,len(student_scores)):
    student_scores[n]=int(student_scores[n])
print(student_scores)
c=0
for score in student_scores:
    if score>c:
        c=score
print(c)
