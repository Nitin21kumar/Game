import random

while True: 
    choises=["rock","paper","scissors"]
    computer=random.choice(choises)    #input By computer
    player=None

    while player not in choises:
        player=input("rock, paper or scissors?:").lower()   #Enter the choise By player
        
    if player==computer:
        print("Computer:",computer)
        print("Player:",player)
        print("Tie!")
    elif player=="rock":
        if computer=="paper":
            print("Computer:",computer)
            print("Player:",player)
            print("You lose!")
        if computer=="scissors":
            print("Computer:",computer)
            print("Player:",player)
            print("You Win ")
    elif player=="paper":
        if computer=="scissors":
            print("Computer:",computer)
            print("Player:",player)
            print("You lose!")
        if computer=="rock":
            print("Computer:",computer)
            print("Player:",player)
            print("You Win")
    else:
        if computer=="rock":
            print("Computer:",computer)
            print("Player:",player)
            print("You lose!")
        if computer=="paper":
            print("Computer:",computer)
            print("Player:",player)
            print("You win")
    Play_again=input("You want play again (yes/no): ").lower()
    if Play_again != "yes":
        break
        
print("Bye!")
