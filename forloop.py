student_heights=input("Input a list of student heights ").split()
for n in range(0,len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(student_heights)
c=0
for height in student_heights:
    c=int(height)+c
d=0
for height in student_heights:
    d+=1
print(c/d)