# author CJP 9/39/ 2021

x = int(input("How many points did the team score? "))
if x >= 15:
    print("Win Gold Medal")
elif x >= 12:
    print("Win Silver Medal")
elif x < 9:
    print("No Medal")
else:
    print("Win Bronze Medal")
