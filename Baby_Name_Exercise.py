# Cynthia Cho
# DSC 430
# Due: February 5, 2019

# I have not given or received any unauthorized assistance on this assignment.



### Problem 1 ###

import os

def names(boyNames,girlNames):
    """takes two files for names as arguments: boys and girls, and counts the number of times a name ends in a particular letter."""

    ## ensure that the working directory is updated
    os.getcwd()  ## assigns working directory where file is located
    
    #os.chdir(dir)  ## change working directory to where files are located
    infile = open(boyNames, 'r')  ## open text file
    Boys = infile.read().splitlines()  ## creates list for boy names
    infile.close()  ## close file
     
    ## repeat steps for Girls as done for Boys
    infile = open(girlNames, 'r')  ## open text file
    Girls = infile.read().splitlines()  ## creates list for girl names
    infile.close()

    boys_Dictionary = {}  ## create empty dictionary for the boy names
    for name in Boys:  ## look at each name in the lines in list: Boys
        letter = name[-1]  ## assign the last letter of each name to variable name 'letter'
        if letter in boys_Dictionary:  ## look at letter and see if in the dictionary
            boys_Dictionary[letter] = boys_Dictionary[letter] + 1  ## if letter already in dictionary, add 1
        else:  ## otherwise...
            boys_Dictionary[letter] = 1  ##  if not in dictionary, assign value of 1

    girls_Dictionary = {}  ## create empty dictionary for the girl names
    ## the below code is the same process as for boys_Dictionary
    for name in Girls:
        letter = name[-1]
        if letter in girls_Dictionary:
            girls_Dictionary[letter] = girls_Dictionary[letter] + 1
        else:
            girls_Dictionary[letter] = 1
    
    ## list is created using 'list comprehension'
    ## using for loop with ascii code starting from 'a' to 'z'
    ## a is equal to 97 and because upper bound is not inclusive, run to 123 since 122 is 'z'
    alphabet = [chr(letter) for letter in range(97,123)]  ## creates an alphabet list 
    

    ## now that both the girls and boys dictionary has been created, creating printout loop
    print('{:<8} {:>8} {:>8}'.format("Letter","Boys","Girls"))  ## prints the header for the printout
    for alph in alphabet:  ## for loop runs through entire alphabet list
        if alph in boys_Dictionary.keys():  ## starts by looking at first letter to see if the dictionary
            boys_count = boys_Dictionary[alph]  ## if letter in dictionary, assigns value to boys_count
        else: ## otherwise...
            boys_count = 0  ## letter has no value and is zero
        if alph in girls_Dictionary.keys():  ## same process is repeated for girls dictionary
            girls_count = girls_Dictionary[alph]
        else:
            girls_count = 0
        print('{:8} {:8} {:8}'.format(alph,boys_count, girls_count))  ## prints out results


##---------------------------------------------------------------------------------------##
        
## Test function call:
names('namesBoys.txt','namesGirls.txt')

## Comment on findings:
print("Comment: Boy names appear to end mostly with consonants - specificaly 'n' (340 occurences).  Girl names end more with the vowel 'a' (380 occurences).")



## Below is what prints out when the function is called using the files from Assignment 2
'''
names('namesBoys.txt', 'names.Girls.txt')
Letter       Boys    Girls
a               9      380
b               4        0
c               8        1
d              31        3
e             102      188
f               2        0
g               3        0
h              35       64
i              28       35
j               1        0
k              21        0
l              61       28
m              15        3
n             340      147
o              76        0
p               3        0
q               0        0
r              73       12
s              68       14
t              26        9
u               1        0
v               3        0
w               4        2
x               8        1
y              75      112
z               3        1
'''





