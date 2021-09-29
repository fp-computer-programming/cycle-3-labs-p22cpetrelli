# author CJP 9/39/ 2021

x = int(input("How many points did the team score? "))
if x >= 15:
    print("Win Gold Medal")
else:
    if x >= 12:
        print("Win Silver Medal")
    else:
        if x < 9:
            print("no medal")
        else:
            print("Win Bronze Medal")

