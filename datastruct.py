students = ["Amit", "Bhairav", "Chinmay"]

first_student = students[0]#access 0th index student
last_student = students[-1]#access last index student

students.append("Ashok")# Add element at the last
students.append("Sardar")
students.append("Vallabh")
students.append("Shrikant")
students.append("Ajay")
students.append("Chaitanya")
students.remove("Bhairav")#Remove given element
students.pop();#pops last data element 
students[1] = "Parth";#modifies the 1st indexes element
new_student = students[2:4]
for stud in students:
    print(stud);

print(first_student)#print 
print(last_student)
print(students[0:7])
print(new_student)


