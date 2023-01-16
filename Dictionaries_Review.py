
#dictionaries with multiple values
test_scores={"Kayla":[88, 92, 102, 123],
             "Luis": [82, 98, 100, 111]}
#print all test scores             
print(test_scores)

#print Kayla's test scores
print(test_scores["Kayla"])

#try to print a test score with incorrect key
#print(test_scores["Sophie"])

#add a new test score
test_scores["Sophie"]=[99, 123, 111]

print(test_scores)

#mixed-update
mixed_up={"abc":1, 999:"yada yada", (3, 5, 6):[1, 2, 3]}

print(mixed_up)

employee={"name":"Kevin Smith", "id":12345, "payrate":24.33}

print(employee["name"])

print(employee.get("name"))

print(employee.items())

for key, value in employee.items():
    print(key, value)
    
print(employee.pop("name","Element not found"))
print(employee)
