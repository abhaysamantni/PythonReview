#This code demonstrates how to read contents of a file and stores it to a dictionary
dict={}

file=open('contactinfo.txt','r')
for line in file:
    mylist=[]
    line=line.rstrip('\n')
    name=line.split(',')
    
    mylist.append(name[1])
    mylist.append(name[2])
    mylist.append(name[3])
   
    dict[name[0]]=mylist
file.close()
for key in dict:
    print(key)
for key in dict:
    print(dict[key])
searchItem=input('Enter name of the contact to search: ')
if searchItem in dict:
    print(dict[searchItem])
else:
    print('Seach Item not found')




