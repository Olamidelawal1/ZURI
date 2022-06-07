import random
R ="Rock"
P ="Paper"
S ="Scissors"
possible_options =["R", "P", "S"]

#using while loop
while True:
    user_input= input("Pick an option between R, P and S - ")
    if user_input not in possible_options:
        print("Error! Try again.")
        continue
    computer_choice =random.choice(possible_options)
    print("Player({0}) : CPU({1})".format(user_input, computer_choice))

    if user_input=="Rock" and computer_choice== "Scissors":
        print("Rock smashes scissors! You win!")

    elif user_input=="Paper" and computer_choice== "Rock":
        print("Paper covers rock! You win!")

    elif user_input=="Scissors" and computer_choice== "Paper":
        print("Sissors cuts paper! You win!")

    elif user_input==computer_choice:
        print("Both the player and the computer selected the same option. It is a tie!")
        continue
    else:
        print("The CPU won")
    break
print("Thanks for playing the game. We hope you will be back shortly.")
    