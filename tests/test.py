from random import randint
from main import pydb


scores = pydb("scores")
try:
    scores.importdb("guesserscores")
except:
    print("could not load scores, please run test2.py to set up the scores table")
    quit()

num = randint(0, 100000)
guesses = 0
skip = False

while True:
    guess = input("guess > ")
    try:
        guesses = int(guess)
    except:
        if guess == "reexport":
            scores.exportdb("guesserscores")
        skip = True
        break
    guesses += 1
    if guess < num:
        print("higher!")
    elif guess > num:
        print("lower!")
    else:
        break

if not skip:
    print("you win!")
    print(f"you guessed {guesses} times before you chose the correct answer {num}")
    name = input("please enter your name to be put on the scores list > ")
    scores.add(0, name)
    scores.add(1, str(guesses))
    scores.add(2, str(num))

    scores.exportdb("guesserscores")

print("""
other players' scores
============================""")
for i in range(len(scores.columns[0])):
    print(f"{scores.get(0,i)} - {scores.get(1,i)} guesses - target was {scores.get(2,i)}")