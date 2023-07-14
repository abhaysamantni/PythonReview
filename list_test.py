from statistics import mean 
grades = open("student_grades.txt","r")
gradelist = [];
for grade in grades:
    print (grade.rstrip()[-3:],type(grade))
    gradelist.append(int(grade[-3:]))
print(gradelist)
gradelist.sort()
gradelist.remove(min(gradelist))
print(gradelist, mean(gradelist))
grades.close()