import random
 # Random function
print("This is our dice Simulator")
x="Yes"
# loop statment

while x=="Yes":
    name = random.randint(1,6)
    # Random function
    if name == 1:
        print("------------")
        print("|          |")
        print("|     0    |")
        print("|          |")
        print("------------")

    if name == 2:
        print("------------")
        print("|          |")
        print("|0        0|")
        print("|          |")
        print("------------")

    if name == 3:
        print("------------")
        print("|     0    |")
        print("|     0    |")
        print("|     0    |")
        print("------------")

    if name == 4:
        print("------------")
        print("|0        0|")
        print("|          |")
        print("|0        0|")
        print("------------")

    if name == 5:
        print("------------")
        print("|0        0|")
        print("|     0    |")
        print("|0        0|")
        print("------------")

    if name == 6:
        print("------------")
        print("|0        0|")
        print("|0        0|")
        print("|0        0|")
        print("------------")

    x=input("Roll again Yes or No : ")
