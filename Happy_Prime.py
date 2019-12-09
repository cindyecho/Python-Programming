# Cynthia Cho
# DSC 430
# Due: January 22, 2019

# I have not given or received any unauthorized assistance on this assignment.


### Problem 2 ###


# 2a)

import math

def prime(x):
    """ 'x' is a positive number greater than 1. If the number is prime, returns True, else False"""
    if x > 1:  #condition that x needs to be greater than 1
        for i in range(2,int(math.sqrt(x))+1):  #range is 2 to sqrt(x) + 1
            if x%i == 0:  #is remainder of x divided by the range is 0, then not a prime.
                return False
        return True  #if x is prime
    return False  #if x is 1 or less, returns False



# 2b)

def happy(x):
    """Returns True if 'x' is a happy number, otherwise returns False."""
    num_lst = []  #numbers are appended to list if it falls into a loop.
    while True: 
        num = 0  #accumulator
        for i in str(x):
            num += int(i)**2  #updates "num variable"
        if num == 1:  #if "num" is 1, return True
            return True
        elif num in num_lst:  #if "num" in list, indicates loop, so returns False and not a happy number.
            return False
        else:
            num_lst.append(num)  #if "num" not 1 or in "num_lst," appends to the num_lst.
            x = num  #after number is appended, "num" becomes "x" and repeats cycle.
    


# 2c)

def happyPrime(x):
    """Returns True if 'x' is a prime and a happy number, otherwise returns False."""
    prime_num = prime(x)  #calls in the prime function
    happy_num = happy(x)  #calls in the happy function
    if prime_num and happy_num == True:  #if both functions return true, returns True
        return True
    return False  #else False



# 2d)

def prime_lst(n):
    """generates a print of n prime numbers"""
    begin = 1  #begining number
    counter = 0  #counter
    while (counter < n):  #while loop continues for as long as counter is less than n.
        if prime(begin)== True:  #calls in prime function and checks the sequence of numbers.
            print(begin, end = ' ')  #if prime function is True, then it is a prime number and adds to print
            counter += 1  #if prime, counter is incremented by 1, else, no increment
        begin += 1  #increments begin by 1 to increase next sequence


#  2e)

def happy_lst(n):
    """ generates a print of n happy numbers """
    counter = 0
    begin = 1
    while (counter < n):  #while loop continues for as long as counter is less than n.
        if happy(begin) == True:  #calls in happy function and checks number.
            print(begin, end=' ')  #if happy, then prints and repeats sequence
            counter += 1   #if prime, counter is incremented by 1, else, no increment
        begin += 1  #increments begin by 1 to increase next sequence


        
# 2f)

def happyPrime_lst(n):
    """ generates a print of n happy and prime numbers"""
    counter = 0
    begin = 1
    while (counter < n):  #while loop continues for as long as counter is less than n.
        if happyPrime(begin) == True:  #calls in happyPrime function and checks number.
            print(begin, end = ' ')  #if happy prime is True, then prints and repeats sequence
            counter += 1   #if prime, counter is incremented by 1, else, no increment
        begin += 1  #increments begin by 1 to increase next sequence



# 2g)

def sadPrime_lst(n):
    """ generates a print of n sad prime numbers"""
    counter = 0
    begin = 1
    while (counter < n):
        if (happy(begin) == False) and (prime(begin)== True):  #checks both happy and prime functions
            #if happy function returns False, the number is sad
            #if the prime function is True, the number is prime
            print(begin, end = ' ')  #prints if number is sad and prime
            counter +=1   #if prime, counter is incremented by 1, else, no increment
        begin += 1  #increments begin by 1 to increase next sequence

