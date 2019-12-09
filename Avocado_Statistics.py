# Cynthia Cho
# DSC 430
# Due: March 5, 2019

# I have not given or received any unauthorized assistance on this assignment.



## Problem 1(a-f)

import statistics as stat
import math
import os


os.getcwd()


## add file name here:
filename = 'avocado.csv'


def readColumn(filename, feature):
    ''' reads in the values for specified feature from filename into a list '''

    infile = open(filename, 'r')  ## open text file
    content = infile.readlines()  ## read in lines
    infile.close()  ## close file

    lst = [] ## empty list

    for line in content:  ## iterative process working with each line
        line = line.strip().split(",")  ## strip and split the lines
        if feature in line:  ## reads first line and provides index of feature 
            idx = line.index(feature)   ## assign index
        else:
            lst.append(float(line[idx]))  ## append the index of line to lst
    return lst  ## outputs the lst of values to readFile function

#--------------------------------------------------------------------------#

## Problem 1(a-c)
## Statistics module calculation for mean, standard deviation, and median

## Problem 1a
def readAndComputeMean_SM(feature):
    ''' Calculates mean for feature using statistics module '''

    lst = readColumn(filename, feature)
    mean_SM = stat.mean(lst)
    return mean_SM  # mean is 850644.013008932
    
## Problem 1b
def readAndComputeSD_SM(feature):
    ''' Calculates standard deviation for feature using statistics module '''
    
    lst = readColumn(filename, feature)
    sd_SM = stat.stdev(lst)
    return sd_SM  # stdev is 3453545.3553994712

## Problem 1c
def readAndComputeMedian_SM(feature):
    ''' Calculates median for feature using statistics module '''

    lst = readColumn(filename, feature)
    median_SM = stat.median(lst)
    return median_SM  # median is 107376.76



#--------------------------------------------------------------------------#


## Problem 1d
## Homegrown functions for mean, standard deviation, and median


def readAndComputeMean_HG(feature):
    ''' Calculates mean for feature '''
    
    lst = readColumn(filename, feature)
    accumulator = 0  ## iniates accumulator
    for num in lst:  ## iterates through lst
        accumulator += num  ## updated accumulator
    mean_HG = accumulator/len(lst)  ## divide updated accmulator by total numbers in lst
    return mean_HG  # mean is 850644.013008932
        

def readAndComputeSD_HG(feature):
    ''' Calculates standard deviation for feature '''

    lst = readColumn(filename, feature)
    mean_HG = readAndComputeMean_HG(feature)  ## calls in mean from readdAndComputeMean_HG
                                                ## this is a helper function
    accumulator = 0
    for num in lst:
        accumulator+= (num - mean_HG)**2  ## calculates the (number in lst - mean) and updates accumulator
    sd_HG = math.sqrt(accumulator/(len(lst)-1))  ## calculates the standard dev
    return sd_HG


def readAndComputeMedian_HG(feature):
    ''' Calculates median for feature '''

    lst = readColumn(filename, feature)
    lst.sort()
    len_lst = len(lst)
    
    if len_lst % 2 == 0:  # if the length of lst of even
        middle = int(len_lst/2)  ## finds middle number
        median_HG = (lst[middle]+lst[middle-1])/2  ## returns the median of lst
        return median_HG
    
    else:  # if the length of lst of odd
        middle = int(len_lst/2)
        median_HG = lst[middle]
        return median_HG



#--------------------------------------------------------------------------#

    
## Problem 1e
## Functions using memoryless calculations for mean, standard deviation, and median


def readAndComputeMean_MML(feature):
    ''' Memoryless calculation of mean '''
    
    accumulator = 0  ## accumulator variable 
    counter = 0  ## counter variable
    
    infile = open(filename, 'r')  ## open text file and reads the feature column one at a time
    for line in infile:
        line = line.strip().split(",")
        if feature in line:
            idx = line.index(feature)
        else:
            accumulator += float(line[idx])  ## value from feature column is added to accumulator
            counter += 1  ## keeps count of numbers read in
    infile.close
    
    Mean_MML = accumulator/counter  ## calculate memoryless mean

    return Mean_MML

        
def readAndComputeSD_MML(feature):
    ''' Memoryless calculation of standard deviation '''

    mean_MML = readAndComputeMean_MML(feature)  ## mean value for stdev calculation
    accumulator = 0  ## initiate accumulator to sum values
    counter = 0  ## count the number of values in list
    infile = open(filename, 'r')  ## open text file
    for line in infile:
        line = line.strip().split(",")
        if feature in line:
            idx = line.index(feature)
        else:
            accumulator += (float(line[idx]) - mean_MML)**2  ## calculates sum of squares
            counter += 1
    infile.close()

    SD_MML = math.sqrt(accumulator/(counter-1))  ## calculates std.dev with accumulator
    return SD_MML


##
##
##
##
##  The below are helper functions to help calculate the readAndComputeMedian_MML:
##             
##             
##             
##             


def MinMaxandN(feature):
    ''' Memoryless calculation of min, max, and total count of values for specified feature '''
    global n
    n = 0
    
    minimum = math.inf  ## set to infinity for min calculation
    maximum = 0
    
    infile = open(filename, 'r')  ## open text file
    for line in infile:
        line = line.strip().split(",")
        if feature in line:
            idx = line.index(feature)
        else:
            if float(line[idx]) <= minimum:  ## checks to see if new value is less than minimum
                minimum = float(line[idx])
            if float(line[idx])>= maximum:  ## checks to see if new value is less than minimum
                maximum = float(line[idx])
            n+=1  ## increments n so that n is the total count of values
    infile.close()
    
    return minimum, maximum, n



def getCount(minimum, maximum, n, feature):
    ''' calculates the number of values below min, above max, provides counter , and passes through min and max '''

    aboveCounter = belowCounter = 0  ## initiate to zero

    ## each time, the bin range is recalculated and this helps create the boundaries to bin the values read in
    bin_diff = (maximum - minimum)/5  
    bin_diff1 = bin_diff + minimum
    bin_diff2 = bin_diff + bin_diff1 
    bin_diff3 = bin_diff + bin_diff2
    bin_diff4 = bin_diff + bin_diff3
    bin_diff5 = bin_diff + bin_diff4
    
    counter = {"bin1":0,"bin2":0 , "bin3":0 , "bin4":0, "bin5":0}  ## dictionary of bin and respective count
    
    infile = open(filename, 'r')
    for line in infile:
        line = line.strip().split(",")
        if feature in line:
            idx = line.index(feature)
        else:
            if float(line[idx]) < minimum:  ## calculates the number of values that fall below the new bin range
                belowCounter += 1
            elif float(line[idx]) > maximum:  ## calculates the number of values that fall above the new bin range
                aboveCounter +=1
            if minimum <= float(line[idx]) <= bin_diff1:  ## the below bins the values read in memorylessly
                counter["bin1"]+=1
            elif bin_diff1 < float(line[idx]) <= (bin_diff2):
                counter["bin2"]+=1
            elif bin_diff2 < float(line[idx]) <= (bin_diff3):
                counter["bin3"]+=1
            elif bin_diff3 < float(line[idx]) <= (bin_diff4):
                counter["bin4"]+=1
            elif bin_diff4 < float(line[idx]) <= (bin_diff5):
                counter["bin5"]+=1
    infile.close()
    return belowCounter, aboveCounter, counter, minimum, maximum


def computeNewMinMax(belowCounter, aboveCounter, counter, minimum, maximum, word):
    ''' Given the parameters, the function narrows down the bin where the median number would be and returns the min and max for that bin '''

    bin_diff = (maximum - minimum)/5
    bin_diff1 = bin_diff + minimum
    bin_diff2 = bin_diff + bin_diff1 
    bin_diff3 = bin_diff + bin_diff2
    bin_diff4 = bin_diff + bin_diff3
    bin_diff5 = bin_diff + bin_diff4

    freq = 0.500  ## frequency is always set to 50%

    ## the below if/elif statements search for the bin that is at least 50%
    if float(belowCounter/n + counter['bin1']/n) > freq:
        minimum = minimum
        maximum = bin_diff1
    elif float(belowCounter/n + counter['bin1']/n +counter['bin2']/n) >= freq:
        minimum = bin_diff1
        maximum = bin_diff2
    elif float(belowCounter/n + counter['bin1']/n +counter['bin2']/n + counter['bin3']/n)  >= freq:
        minimum = bin_diff2
        maximum = bin_diff3
    elif (belowCounter/n + counter['bin1']/n +counter['bin2']/n+ counter['bin3']/n +counter['bin4']/n) >= freq:
        minimum = bin_diff3
        maximum = bin_diff4
    elif float(belowCounter/n + counter['bin1']/n +counter['bin2']/n+ counter['bin3']/n + counter['bin4']/n +counter['bin5']/n) >= freq:
        # statement above made explicit
        minimum = bin_diff4
        maximum = bin_diff5

    return minimum, maximum

def getMedian(minimum, maximum, feature):
    ''' using min and max values, returns the median when 'n' is odd '''
    
    odd_median_MML = 0
    infile = open(filename, 'r')
    for line in infile:
        line = line.strip().split(",")
        if feature in line:
            idx = line.index(feature)
        else:
            if minimum <=float(line[idx]) <= maximum:  ## There should only be one number between minimum and maximum
                odd_median_MML = float(line[idx])
    infile.close()
    return odd_median_MML
    

def evenMedian(minimum, feature):
    ''' if n is an even number, evenMedian returns the second number to calculate the median '''
    maximum = math.inf
    infile = open(filename, 'r')

    for line in infile:
        line = line.strip().split(",")
        if feature in line:
            idx = line.index(feature)
        else:
            if minimum < float(line[idx]) < maximum:  ## iterates through each number to see which one
                maximum = float(line[idx])
    infile.close()
    return maximum


def dupMiddle(minimum, maximum, feature):
    ''' calculates the mean if the two numbers to calculate the median are the same '''
    total = 0
    infile = open(filename, 'r')
    for line in infile:
        line = line.strip().split(",")
        if feature in line:
            idx = line.index(feature)
        else:
            if minimum < float(line[idx]) < maximum: ## iterates through each number to see which one
                total += float(line[idx])
    infile.close()
    median_calc = total/2  ## the total will just be a duplicate of the two numbers, but left here to make explicit
    return median_calc

   
def readAndComputeMedian_MML(feature):

    ''' memoryless calculation of the median for a feature '''

    minimum, maximum, n = MinMaxandN(feature)  # min,max,n (helper function)

    if n % 2 != 0:  ## if the total count of values for specified feature is odd:
        start = True  ## initializes to true to begin loop  
        while start == True:  ## starts iteration while start value is True
            belowCounter, aboveCounter, counter, minimum, maximum = getCount(minimum,maximum, n, feature)  ## starts binning data
            minimum, maximum = computeNewMinMax(belowCounter, aboveCounter, counter, minimum, maximum, feature) ## calculates new min max

            if sum(counter.values()) == 1:  ## if N is off, this returns the median.  If N is even, this returns the smaller of two numbers to calculate median
                start = False  ## if the above is true, start is now False
        odd_median_MML = getMedian(minimum, maximum, feature)  ## function to narrow down to single number between min and max
        return odd_median_MML

    if n % 2 == 0:  ## if the total count of values for specified feature is even:
        start = True
        while start == True:  ## starts iteration while start value is True
            belowCounter, aboveCounter, counter, minimum, maximum = getCount(minimum,maximum, n, feature)  ## starts binning data
            minimum, maximum = computeNewMinMax(belowCounter, aboveCounter, counter, minimum, maximum, feature) ## calculates new min max
            
            if sum(counter.values()) == 1:  ## if two median numbers are not the same takes smaller of two numbers to calculate median
                start = False  ## if the above is true, start is now False
                median_MML = getMedian(minimum, maximum, feature)  ## function to narrow down to single number between min and max
                minimum = median_MML  ## the new minimum is the median from the above part of the function
                maximum = evenMedian(minimum, feature)
                even_median_MML = (minimum+maximum)/2
                return even_median_MML

            if sum(counter.values()) == 2:  ## if N is off, this returns the median.  If N is even, this returns the smaller of two numbers to calculate median
                start = False  ## if the above is true, start is now False
                even_median_MML = dupMiddle(minimum, maximum, feature)
                return even_median_MML
            
            minimum = round(minimum,10)
            maximum = round(maximum,10)
            if minimum == maximum:  ## this case is used for all other corner cases - for instance when there are more than 2 occurences of the median number in the data
                start = False
                even_median_MML = minimum
                return even_median_MML


#----------------------------------------------------------------------------------------------#


## Problem 1f

# Test call of function and printout of means, standard deviations, and medians from all functions above:

mean_SM = readAndComputeMean_SM('Total Volume')
sd_SM = readAndComputeSD_SM('Total Volume')
median_SM = readAndComputeMedian_SM('Total Volume')


mean_HG = readAndComputeMean_HG('Total Volume')
sd_HG = readAndComputeSD_HG('Total Volume')
median_HG = readAndComputeMedian_HG('Total Volume')


mean_MML = readAndComputeMean_MML('Total Volume')
sd_MML = readAndComputeSD_MML('Total Volume')
median_MML = readAndComputeMedian_MML('Total Volume')

        
print('{:20}\t{:8}\t{:}\t{:}'.format('Method','Mean', 'St. Deviation', 'Median'))
print('{:20}\t{:8.3f}\t{:8.3f}\t{:8.3f}'.format('Statistics Module (a-c)',mean_SM, sd_SM, median_SM))
print('{:20}\t{:8.3f}\t{:8.3f}\t{:8.3f}'.format('Homegrown (d)', mean_HG, sd_HG, median_HG))
print('{:20}\t{:8.3f}\t{:8.3f}\t{:8.3f}'.format('Memoryless (e)', mean_MML, sd_MML, median_MML))



