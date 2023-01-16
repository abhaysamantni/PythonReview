

phonebook_dict = {'Clint':'505-2612', 'Katie':'505-3451'}
print(phonebook_dict)


quiz_dict = {'jwt254':[83, 92, 89], 'fkw928':[85, 94, 96]}
print(quiz_dict)



print(quiz_dict["jwt254"])



phonebook_dict = {'Clint':'505-2612', 'Katie':'505-3451'}
print(phonebook_dict['Katie'])



phonebook_dict = {'Clint':'505-2612', 'Katie':'505-3451'}
for key in phonebook_dict:
  print(key)

for key in phonebook_dict:
  print(key, phonebook_dict[key])



phonebook_dict = {'Clint':'505-2612', 'Katie':'505-3451'}
phonebook_dict['Caryn'] = '505-2662'
print(phonebook_dict)
print(len(phonebook_dict))


search_item=input("Enter name of the person you wish to search for ")
if search_item in phonebook_dict:
    print(phonebook_dict[search_item])
else:
    print("Search item not in dictionary")



print(phonebook_dict.get("clint", "888-8888"))
print(phonebook_dict.items())
print(phonebook_dict.keys())
print(phonebook_dict.pop("Clint"))
print(phonebook_dict.items())
print(phonebook_dict.popitem())
#dict.values()
#dict.clear()




