# Cynthia Cho
# DSC 430
# Due: February 19, 2019

# I have not given or received any unauthorized assistance on this assignment.




## Problem 2 ##


### NOTE:  Problem 1 is included in order to call in Dice and Cups function for Problem 2
#          Scroll down for Problem 2
import random


## SixSidedDie ##
class SixSidedDie:
    """ This is a class for rolling a six-sided die"""

    def __init__(self, sides=6):  ## Assigns default value of six sides
        """initializes to a 6 sided die"""
        self.sides = sides
        self.value = []  ## initializes the container to zero for value

    def roll(self):
        """rolls the die"""
        self.value.append(random.randint(1, self.sides))  ## random number between 1 and six
        return self.value[-1]  ## returns the number rolled. Not assigning to variable allows for multiple rolls
            
    def getFaceValue(self):  ## Default Face Value is 1 when starting game
        """returns the face value of a die after roll.  Default is 1"""
        if self.value == []:  ## scenario when "getFaceValue" function is called before roll
            return 1  ## returns 1 (can be any number between [1,6], just chose 1)
        else:
            return self.value[-1]  ## returns roll value which is new face value of die
    
    def __repr__(self):  ## Canonical representation
        """returns the die used and the last value rolled"""
        return 'SixSidedDie({})'.format(self.value[-1])

    

## TenSidedDie ##
## Comments are essentially the same as SixSidedDie due to inheritance
class TenSidedDie(SixSidedDie):  ## using inheritance of SixSiedDie
    """ This is a class for rolling a ten-sided die"""
    
    def __init__(self, sides=10):  
        """initializes to a 10 sided die"""
        self.sides = sides
        self.value = []
        
    def __repr__(self):
        """returns the die used and the value rolled"""
        return 'TenSidedDie({})'.format(self.value[-1])



## TwentySidedDie ##
## Comments are essentially the same as SixSidedDie due to inheritance
class TwentySidedDie(SixSidedDie):  ## using inheritance of SixSiedDie
    """ This is a class for rolling a twenty-sided die"""
    
    """initializes to a 20 sided die"""
    def __init__(self, sides=20):
        self.sides = sides
        self.value = []
        
    def __repr__(self):
        """returns the die used and the value rolled"""
        return 'TwentySidedDie({})'.format(self.value[-1])


## Cups ##
class Cup():
    """The Cup class rolls and returns sum of the values rolled on die/dice in cup. Default die count is one of each six, ten, and twenty sided die."""
    
    def __init__(self, six = 1, ten = 1, twenty = 1):
        """ initializes to default of one six, ten, twenty sided die"""
        self.six = six  ## Assigns values for each die
        self.ten = ten
        self.twenty = twenty
        #self.dieLst = []
        self.total=0
          
    def roll(self):
        """rolls all the die/dice in a cup"""
        self.total=0  ##initializes sum to zero

        self.dieLst = [] ## by adding the empty list here allows for new rolls
                       ## without appending to an existing list
        for i in range(1, self.six+1):  ## rolls for each die entered into Cup function
            self.sdie = SixSidedDie()  ## creates a variable for SixSidedDie()
            self.total += self.sdie.roll()  ## assigns variable for roll
            self.dieLst.append(self.sdie)  ## appends repr from SixSidedDie return to dieLst for Cup repr
            
        for i in range(1, self.ten+1):  ## repeats the above for ten-sided die
            self.tdie = TenSidedDie()
            self.total += self.tdie.roll()
            self.dieLst.append(self.tdie)

        for i in range(1, self.twenty+1):  ## repeats the above for twenty-sided die
            self.twendie = TwentySidedDie()
            self.total += self.twendie.roll()
            self.dieLst.append(self.twendie)
            
        return self.total  ##returns the total from roll

    def getSum(self):
        """returns the sum of rolled die/dice in the cup.  Default is 0"""
        if self.total == 0:  ## scenario when "getFaceValue" function is called before roll
            return 0  ## returns 0
        else:
            return self.total  ## returns sum of all rolled die/dice

    def __repr__(self):
        ''' returns the face value of the dice combinations entered'''
        return 'Cup{}'.format(tuple(self.dieLst))

#_________________________________________________________________________________________________________________________________________________#
#_________________________________________________________________________________________________________________________________________________#
#_________________________________________________________________________________________________________________________________________________#



import random

## Problem 2 ##

def CupsDiceGame():
    """Cup and dice game with user inputs"""
    
    ## User input ##
    name = input("Hello!  What is your name? ")
    if name == "" or not name.strip():
        name = "person-with-no-name"
        print("Hello,",name+"!")
    else:
        print("Hello", name+"!"+'\n'+"You have a starting balance of 100 dollars.")


    ## Answer from user ##
    answer = input("Would you like to play a game? (Y for yes, or any key to escape): ")

    balance = 100  ## balance starts at 100 and is updated based on bet

    while answer == 'Y':  ## game keeps going as long as user enters Y.


        if balance == 0:  ## if user enters Y, but has balance of 0, the game ends
            print("You don't have enough in your balance to play.")
            break
        print()
        goal = random.randint(1, 100)  ## random value is assigned to goal
        print("Your goal is: ", str(goal))  ## prints goal for player

        
        while True:  ## while True for creating the variable BET
            try:
                bet = int(input("Place your bet (format: X): "))
                if 0 < bet <=balance:
                    print()
                    break  ## if the "if" condition is met,breaks out of loop
                else:  ## any other condition, the print statement is executed and the loop restarts.
                    print("Bet has to be a positive number to the dollar not to exceed your balance.","\n")
            except ValueError:
                print("Bet has to be a positive number to the dollar not to exceed your balance.","\n")
                continue  ## loop restarts for ValueErrors like entering strings and floats.
        
        while True:  ## loops while True... breaks when IF conditions are met
            try:  
                x = int(input("Enter the number of six-sided die. (format: X): "))  ## assigns value for each number of die to x, y, and z
                y = int(input("Enter the number of ten-sided die. (format: X): ")) 
                z = int(input("Enter the number of twenty-sided die. (format: X): ")) 
                if x>=0 and y>= 0 and z>=0 and (x+y+z)>=1:
                    print()
                    break  ## breaks only when the above IF statement is satisfied
                else:
                    print("There must be at least one die in the cup and the number of die needs to be a positive integer.","\n")
            except ValueError:  ##ValueErrors include floats and strings that are entered.  prints message below.
                print("There must be at least one die in the cup and the number of die needs to be a positive integer.","\n")
                

        c = Cup(x, y, z)  ## assigns the values for x, y, and z to Cup function
        roll = c.roll()  ## roll the dice in the cup
        
        if roll == goal:  ## if roll is equal to roll...
            winnings = bet * 10  ## user wins 10x bet
            balance+= winnings  ## adds winning to balance
            print('You rolled {} and you win {}  {dollar}.'.format(roll,winnings, dollar = "dollar" if bet ==1 else "dollars" ))  ## prints out how much is won
            print('{}, your balance is now {} {dollar}.'.format(name, balance, dollar = "dollar" if balance ==1 else "dollars" ))
            ## prints out user's name and updated balance

            
        elif abs(goal - roll) <= 5:  ## if user rolls within 5... (INCLUSIVE:  if goal is 20, and 15 is rolled, still within 5)
            winnings = bet * 5  ## user wins 5x bet
            balance +=winnings
            print('You rolled {} and you win {} {dollar}.'.format(roll,winnings, dollar = "dollar" if bet ==1 else "dollars" ) )
            print('{}, your balance is now {} {dollar}.'.format(name, balance, dollar = "dollar" if balance ==1 else "dollars" )) 
            
        elif abs(goal - roll) <= 10:  ## if user rolls within 10... (INCLUSIVE)
            winnings = bet * 2  ## user wins 2x bet
            balance += winnings
            print('You rolled {} and you win {} {dollar}.'.format(roll,winnings, dollar = "dollar" if bet ==1 else "dollars" ) )
            print('{}, your balance is now {} {dollar}.'.format(name, balance, dollar = "dollar" if balance ==1 else "dollars" )) 
      
        else:
            winnings = bet
            balance -= winnings  ## subtracts from balance
            print('You rolled {} and you lose {} {dollar}.'.format(roll,winnings, dollar = "dollar" if bet ==1 else "dollars" ) )
            print('{}, your balance is now {} {dollar}.'.format(name, balance, dollar = "dollar" if balance ==1 else "dollars" )) 
      
        ## Ask the player again if they want to play the game again.  If yes, loops back up and checks balance
        answer = input("Would you like to play again? (Y for yes, or any key to escape): ")

    ## prints "Goodbye" when game is finished.
    print("Goodbye!")


#_________________________________________________________________________________________________________________________________________________#

# Testing of function call:

CupsDiceGame()


## Below are a few print-outs when the function is called along with some errors:


## 1.  Function working without any user error
'''
Hello!  What is your name? Cindy
Hello Cindy!
You have a starting balance of 100 dollars.
Would you like to play a game? (Y for yes, or any key to escape): Y

Your goal is:  51
Place your bet (format: X): 50

Enter the number of six-sided die. (format: X): 1
Enter the number of ten-sided die. (format: X): 0
Enter the number of twenty-sided die. (format: X): 5

You rolled 56 and you win 250 dollars.
Cindy, your balance is now 350 dollars.
Would you like to play again? (Y for yes, or any key to escape): N
Goodbye!
'''

## 2.  Function with user error from bet:  try/except
'''
Hello!  What is your name? Cindy
Hello Cindy!
You have a starting balance of 100 dollars.
Would you like to play a game? (Y for yes, or any key to escape): Y

Your goal is:  79
Place your bet (format: X): -5
Bet has to be a positive number to the dollar not to exceed your balance. 

Place your bet (format: X): 5.6
Bet has to be a positive number to the dollar not to exceed your balance. 

Place your bet (format: X): ten
Bet has to be a positive number to the dollar not to exceed your balance. 

Place your bet (format: X): fifty
Bet has to be a positive number to the dollar not to exceed your balance. 

Place your bet (format: X): 0
Bet has to be a positive number to the dollar not to exceed your balance. 

Place your bet (format: X): 
Bet has to be a positive number to the dollar not to exceed your balance. 

Place your bet (format: X): 50

Enter the number of six-sided die. (format: X): 0
Enter the number of ten-sided die. (format: X): 0
Enter the number of twenty-sided die. (format: X): 9

You rolled 124 and you lose 50 dollars.
Cindy, your balance is now 50 dollars.
Would you like to play again? (Y for yes, or any key to escape): N
Goodbye!
'''

## 3.  Function with user error on entering number of die/dice: try/except
'''
Hello!  What is your name? Cindy
Hello Cindy!
You have a starting balance of 100 dollars.
Would you like to play a game? (Y for yes, or any key to escape): Y

Your goal is:  90
Place your bet (format: X): 50

Enter the number of six-sided die. (format: X): -5
Enter the number of ten-sided die. (format: X): 5.6
There must be at least one die in the cup and the number of die needs to be a positive integer. 

Enter the number of six-sided die. (format: X): ten
There must be at least one die in the cup and the number of die needs to be a positive integer. 

Enter the number of six-sided die. (format: X): 7.6
There must be at least one die in the cup and the number of die needs to be a positive integer. 

Enter the number of six-sided die. (format: X): -5
Enter the number of ten-sided die. (format: X): 0
Enter the number of twenty-sided die. (format: X): 0
There must be at least one die in the cup and the number of die needs to be a positive integer. 

Enter the number of six-sided die. (format: X): 0
Enter the number of ten-sided die. (format: X): 0
Enter the number of twenty-sided die. (format: X): 0
There must be at least one die in the cup and the number of die needs to be a positive integer. 

Enter the number of six-sided die. (format: X): 1
Enter the number of ten-sided die. (format: X): 1
Enter the number of twenty-sided die. (format: X): 1

You rolled 21 and you lose 50 dollars.
Cindy, your balance is now 50 dollars.
Would you like to play again? (Y for yes, or any key to escape): N
Goodbye!
'''

## 4.  Function with user not wanting to play the game
'''
Hello!  What is your name? Cindy
Hello Cindy!
You have a starting balance of 100 dollars.
Would you like to play a game? (Y for yes, or any key to escape): N
Goodbye!
'''
