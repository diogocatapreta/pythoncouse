student_list = ["Diogo", "Marilia", "Douglas", "Ricardo", "Antonio"]

print(student_list[0])

print(f"In this moment we have {len(student_list)} elements on the list")

if "Marilia" in student_list:
    print("Marilia is in the list")
if "Jose" in student_list:
    print("Jose is in the list")
else:
    print("Jose is not in the list")
    student_list.append("Jose")


# print the last element on the list
print(student_list[-1])

print(f"In this moment we have {len(student_list)} elements on the list")

del student_list[2]

print(f"In this moment we have {len(student_list)} elements on the list")

# print the last element on the list
print(student_list[1])


#slicing list
print(student_list)
# we will ignore the first element of the list
print(student_list[1:])

#we will ignore the last element of the list
print(student_list[:-1])


# print all element using loop
