def what():
    age = int(input("Enter your Age: "))
    if age:
        print("Your age is " + str(age))
    else:
        print("You did not input an age")
    name = str(input("Enter your Name: "))
    if name:
        print("Your name is " + str(name))
    else:
        print("You did not input a name")
    return
what()