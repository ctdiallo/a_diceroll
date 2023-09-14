## Question: roll a dice between 1 and 6. Print result. 
## Ask if wants to roll again the dice. 
## If no stop
## Will need: random, input, fn to express the result

## Set variables
min_val = 1
max_val = 6
dice = [1,2,3,4,5,6]

## Code
import random

while True:
    roll = random.choice(dice)
    print("Your roll number is {}".format(roll))
    ## ask to roll again
    roll_again = input("One more time? (yes/no)? ").lower()
    if roll_again != "Yes":
        break
    else:
        print("Your roll number is {}".format(roll))
## 5 Test