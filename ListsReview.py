
#Examples of list
grade_list = [98, 76, 89, 90, 65, 86]
print(grade_list)

name_list = ['Mickey Mouse','Cinderella']
print(name_list)
             
employee_list = ['Jon Smith', 65000.00, 24]
print(employee_list)
             
course_list = []
print(course_list)


grade_list = [98, 76, 89, 90, 65, 86]
for grade in grade_list:
  print(grade)
print(grade_list)


grade_list = [98, 76, 89, 90, 65, 86]
print(grade_list[0])
print(grade_list[5])
print(grade_list[6])
print(len(grade_list))


my_list=[5,10,15,20,25]
my_list2=my_list
count=len(my_list)
for i in range(count):
    tmp=my_list[i] * 2
    my_list[i]=tmp
print(my_list)
print(my_list2)


grade_list = [98, 76, 89, 90, 65, 86]
grade_list2 = grade_list
grade_list.append(78)
print(grade_list)
grade_list.insert(2, 84) 
print(grade_list)
print(grade_list2)
print("The number of grades is", len(grade_list))


num_list=[1,2,3,4]
new_list=[]
for num in num_list:
    new_list.append(num)
print(new_list)
num_list.append(5)
print(new_list)



#List Slicing
grade_list = [98, 76, 89, 90, 65, 86]
print(grade_list[1:4])
print(grade_list[:3])
print(grade_list[3:])
print(grade_list[1:5:2])


#List Searching
name_list = ["Belle", "Gaston", "Beast"]
name = input("Enter a character’s name: ")
if name in name_list:
   print(name, "was found in the list")
else:
   print(name, "was not found in the list")


list_name=['Abhay', 12344, 1.34]
print(list_name.index('Abhay'))


list_name.remove(12344)
print(list_name)

list_name.reverse()
print(list_name)

list_name=['Trupti','Ishika']
list_name.sort()
print(list_name)

print(min(list_name))

print(max(list_name))

del list_name[1]
print(list_name)

