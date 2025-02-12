import random

'''
     1 for snake
    -1 for water
     0 for gun
'''

computer = random.choice([1, -1, 0])

youStr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youStr]

print(f"You choose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if computer == you:
    print("It's a tie!")

else:
    # if ((computer == -1 and you == 0) or (computer == 1 and you == -1) or (computer == 0 and you == 1)):
    #     print("You Lose!")
    # else:
    #     print("You Win!")
    
    if computer - you == 1 or computer - you == -2:
        print("You Lose!")
    else:
        print("You win!")
    