
student_list = ["Diogo", "Marilia", "Douglas", "Ricardo", "Antonio"]
x = 0

for name in student_list:
    print("{0} is an student of the course.".format(name))

# loop 10 times
for index in range(10):
    x+= 1
    print(x)

print("Loop from 5 to 10")
for index in range(5,10):
    print(index)

print("Loop from 5 to 10 incrised by 2")
for index in range(5,10,2):
    print(index)



for name in student_list:
    if name == "Douglas":
        print(f"Encontrei o {name}")
        break
    print(f"Condicao de nome {name}")