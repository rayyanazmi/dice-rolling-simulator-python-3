import random

def main(min_val, max_val): 
    roll_again = "y"

    while roll_again == "y":
        print ("The value is:")
        print (random.randint(min_val, max_val))
        roll_again = input("roll the dices again? ")

main(min_val=1, max_val=6)