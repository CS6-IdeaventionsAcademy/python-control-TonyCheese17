# Tony Yu
# 11/21/17
# Python Beginnings
# 7 Favorite Color
import time

color = ("green")

print("$" * 50)
print("Welcome to Tony's color guesser!!!")
print("$" * 50)

print()

time.sleep(0.5)

print("You will have to guess my favorite color!")

print()

time.sleep(0.5)

print("If you get it right, you get to get a message saying you did!")

print()

time.sleep(0.5)

print("If you don't, you get a message saying you didn't! Good luck!!!")

print()

time.sleep(0.5)

guess = input("What is your guess: ")

guess = guess.lower()

while guess != color:
    print("You got it wrong. Guess again!")
    guess = input("What is your guess: ")
    guess = guess.lower()
print("Good job! You got it right.")
