# Collins Wanga            


def sayHello(name, gender, academicTitle):
    name = name.split()
    last_name = name[1]
    if academicTitle == "":
        if gender == "M":
            print("Hello Mr. ",last_name)
        else:
            print("Hello Ms. ",last_name)
    else:
        print("Hello ",academicTitle, "",last_name)
sayHello("Nana Kotei", "F", "Dr")
