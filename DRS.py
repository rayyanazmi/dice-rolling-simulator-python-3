import random

def main(min_val, max_val): 
    roll_again = "y"

    while roll_again == "y":
        print (f'The value is: {random.randint(min_val, max_val)}')
        roll_again = input("roll the dice again? ")

main(min_val=1, max_val=6)