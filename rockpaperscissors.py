import random 
import os
import time

selections = ["Rock", "Paper", "Scissors"]

os.system("cls")

i = 1

while i < 10:
    botanswer = random.choice(selections)
    print("Rock, Paper, or Scissors?")
    useranswer = input("> ")

    if useranswer == "Rock" and botanswer == "Paper":
        i = 11
        os.system("cls")
        print("Your opponent picked paper, you lose!")
        time.sleep(0.7)
        print("Returning to play another game...")
        time.sleep(1)
        os.system("cls")
        i = 1
    elif useranswer == "Rock" and botanswer == "Scissors":
        i = 11
        os.system("cls")
        print("Your opponent picked Scissors, you win!")
        time.sleep(0.7)
        print("Returning to play another game...")
        time.sleep(1)
        os.system("cls")
        i = 1
    elif useranswer == "Paper" and botanswer == "Scissors":
        i = 11
        print("Your opponent picked Scissors, you lose!")
        time.sleep(0.7)
        os.system("cls")
        print("Returning to play another game...")
        time.sleep(1)
        os.system("cls")
        i = 1
    elif useranswer == "Paper" and botanswer == "Rock":
        i = 11
        print("Your opponent picked Rock, you win!")
        time.sleep(0.7)
        os.system("cls")
        print("Returning to play another game...")
        time.sleep(1)
        os.system("cls")
        i = 1
    elif useranswer == "Scissors" and botanswer == "Rock":
        i = 11
        print("Your opponent picked Rock, you lose!")
        time.sleep(0.7)
        os.system("cls")
        print("Returning to play another game...")
        time.sleep(1)
        os.system("cls")
        i = 1
    elif useranswer == "Scissors" and botanswer == "Paper":
        i = 11
        print("Your opponent picked Scissors, you lose!")
        time.sleep(0.7)
        os.system("cls")
        print("Returning to play another game...")
        time.sleep(1)
        os.system("cls")
        i = 1
    elif useranswer == botanswer:
        i = 11
        print("Tie!")
        time.sleep(0.7)
        os.system("cls")
        print("Returning to play another game...")
        time.sleep(1)
        os.system("cls")
        i = 1
