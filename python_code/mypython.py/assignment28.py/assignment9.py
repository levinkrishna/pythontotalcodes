#question 9
no_of_per=int(input("How many people do you want to invite?"))
if no_of_per<10:
    for n in range(0,no_of_per):
        names=(input("Enter the name of the people:"))
        print(f"{names} has been invited")
else:
    print("Too many people")