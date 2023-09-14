## Question: Roll a dice between 1 and 6. Print result. 
## Ask if wants to roll again the dice. 
## If no stop
## Will need: random, input, fn to express the result

## Set variables
min_val = 1
max_val = 6

## Code
import random

while True:
    roll = random.randint(min_val, max_val)
    print(f"Your roll number is {roll}")
    ## ask to roll again
    roll_again = input("One more time? (yes/no)? ").lower()
    if roll_again != "Yes":
        print("Thank you. Hope you liked it :)")
        break

## 5 Test




