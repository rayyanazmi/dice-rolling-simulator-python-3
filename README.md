Dice Rolling Simulator!
This is a simple Python 3 script for a Dice Rolling Simulator. It allows users to simulate rolling a standard six-sided die and receive a random outcome.

How to Use,
1. Clone the Repository:
git clone https://github.com/rayyanazmi/dice-rolling-simulator.git

2. Navigate to the Project Directory:
cd dice-rolling-simulator

3. Run the Script:
python dice_roller.py

4. Follow On-Screen Prompts:
> You will be prompted to roll the dice.
> Type 'y' to roll again or any other key to exit.

Code Explanation,
The main functionality is implemented in the main function, which takes two parameters min_val and max_val to represent the range of the dice (default is 1 to 6 for a standard six-sided die).

import random

def main(min_val, max_val): 
    roll_again = "y"

    while roll_again == "y":
        print(f'The value is: {random.randint(min_val, max_val)}')
        roll_again = input("Roll the dice again? ")

main(min_val=1, max_val=6)


The script uses Python's random module to generate a random integer within the specified range and prints the result. It then prompts the user if they want to roll the dice again.
Feel free to modify the min_val and max_val parameters in the main function to simulate dice with different numbers of sides.

Happy rolling!

