name = "Diogo"
machine = "Welly"

interpolation = True

if interpolation:
    print("Hello {0}, I'm a machine and my name is {1}".format(name, machine))
else:
    #String Interpolation sample
    print(f"Hello {name}, I'm a machine and my name is {machine}.")