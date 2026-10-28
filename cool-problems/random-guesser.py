import random as r

n = 100

r_num = r.randint(1, n)

def guess():
    guessed_num = input(f"Guess a number from 1 to {n}: ")
    try: 
        guessed_num = int(guessed_num)
    except:
        return guess()
    return int(guessed_num)

while True:
    guess_num = guess()
    if guess_num == r_num:
        print("Correct!")
        break
    elif guess_num > r_num:
        print("Try lower.")
    elif guess_num < r_num:
        print("Try higher.")

