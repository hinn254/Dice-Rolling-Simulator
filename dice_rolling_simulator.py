'''
The dice rolling simulator will imitate the experience of rolling a dice.
It will generate a random number and the user can play again and again
to get a number from the dice until the user decides to quit the program.
'''

# imports
import random

#Function to generate a dice number 
def dice_roller():
    '''
    Takes user input and rolls dice
    '''

    while True:
        # User input
        dice_number = random.choice([1,2,3,4,5,6])
        print('Do you want to roll a dice (Y/N)')
        try:
            roll = input('>>> ').lower()
            if roll == 'n':
                print("Welcome back to play again.")
                break
            elif roll == 'y':
                print('Rolling Dice...')
                print(f'Your dice number is {dice_number}')
        except KeyboardInterrupt:
            print('Program Terminated')
            break
        except:
            print("Please enter a valid response.")


if __name__ == '__main__':
    dice_roller()
    