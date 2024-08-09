#! /usr/bin/env python3
# -*- coding utf-8 -*-
"""
-------------------------------------------------
   File Name：     bulls_and_cows.py
   Author :        Mallikarjun
   time：          Aug 9 2024
   Description :
-------------------------------------------------
"""

import random

# Generates a 4 digit number
# with no repeated digits
def genrateNum():
    while True:
        num = random.randint(1000, 9999)
        if len(set(str(num))) == 4:
            return num
    return num


def check_bulls_cows(guess_num, secretcode):
    c, b = 0, 0
    break_loop = False
    
    # Loop through gussed number and secret code to identity bulls and cows
    for i, j in zip(str(guess_num), str(secretcode)):
        if i == j:
            b += 1
            if b == 4:
                result = "Yay! You guessed right!"
                break_loop = True
                break
        elif i in str(secretcode):
            c += 1

    if break_loop == False:
        #print(f"{b} Bulls, {c} Cows")
        result = f"{b} Bulls, {c} Cows"

    return result


def main():
    # Prompt the user for Number of tries and gussed number

    your_tries = 0
    secretcode = genrateNum() 
    print("Secret Code is: ", secretcode)

    while True:
        try:
            tries =int(input('Enter number of tries: '))
            break
        except ValueError:
            print("Please enter a valid number of tries: ")
            continue

    while your_tries < tries:
        gussed_number=input('Whats the 4 digit number you gussed : ')
        your_tries +=1
        print(check_bulls_cows(gussed_number, secretcode))
        if check_bulls_cows(gussed_number, secretcode)  == 'Yay! You guessed right!':
            break
        if your_tries == tries:
            print(f"Sorry you ran out of tries. The secret code was {secretcode}")
    
if __name__ == "__main__":
    main()