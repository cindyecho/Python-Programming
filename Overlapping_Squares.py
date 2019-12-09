# Cynthia Cho
# DSC 430
# Due: January 22, 2019

# I have not given or received any unauthorized assistance on this assignment.


### Problem 1 ###


def rec_1(a):
        """calculates the upper right hand corner coorindates of 1st rectangle"""
        rec1=[]
        for i in a:
            res=i +a[2]  #adds a[2] number to x and y coordinate
            rec1.append(res)  #appends to list to create coordinates
        return(rec1)

def rec_2(b):
        """calculates the upper right hand corner coorindates of 2nd rectangle"""
        rec2=[]
        for i in b:
            res= i +b[2]  #adds a[2] number to x and y coordinate
            rec2.append(res)  #appends to list to create coordinates
        return(rec2)

def overlap(a,b):
        """ calculates the area of the overlap between two rectangles, if there is overlap."""
        rec1_r=rec_1(a)  #calls in rec_1 function and assigned to rec1_r
        rec2_r=rec_2(b)  #calls in rec_1 function and assigned to rec2_r
        min_right = min(rec1_r[0], rec2_r[0])  #assigns the minimum x-value of right rectangles
        max_left = max(abs(a[0]),abs(b[0]))  #assigns the maximum x-value of left rectangles
        min_top = min(rec1_r[1],rec2_r[1])  #assigns the minimum y-value of top rectangles
        max_bottom = max(abs(a[1]),abs(b[1]))  #assigns the maximum y-value of bottom rectangles
        width = min_right - max_left  #assigns width of rectangle
        length =min_top-max_bottom  #assigns length of rectangle
        area = width * length  #assigns variable "area"
        #if statements created to be exhaustive.
        if max_left > min_right:  #if there is no overlap on sides
                return(0)
        elif max_bottom > min_top:  #if there is no overlap on sides
                return(0)
        elif area < 0:  #is area is negative
                return(0)
        elif area > 0:  #is area is positive and doesn't meet the conditions of all previous checks, the returns area
                return(area)



#check for points:


        
totalScore = 0

S1 = [1,5,3]
S2 = [5,6,2]
S3 = [2,1,2]
S4 = [9,6,2]
S5 = [7,2,3]
S6 = [3,2,5]
S7 = [5,3,1]

#---------- ---------- ---------- ---------- ----------
print( "Test 1: " + str(S1) + str(S6) )
print( "Correct Answer: 2" )
r1 = overlap(S1,S6)


r2 = overlap(S6,S1)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 2:
        s1 = s1 + 1
if r2 == 2:
        s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1
    
#---------- ---------- ---------- ---------- ----------
print( "Test 2: " + str(S2) + str(S6) )
print( "Correct Answer: 2" )
r1 = overlap(S2,S6)
r2 = overlap(S6,S2)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 2:
        s1 = s1 + 1
if r2 == 2:
        s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 3: " + str(S3) + str(S6) )
print( "Correct Answer: 1" )
r1 = overlap(S3,S6)
r2 = overlap(S6,S3)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 1:
        s1 = s1 + 1
if r2 == 1:
        s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 4: " + str(S4) + str(S6) )
print( "Correct Answer: 0" )
r1 = overlap(S4,S6)
r2 = overlap(S6,S4)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 0:
        s1 = s1 + 1
if r2 == 0:
        s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 5: " + str(S5) + str(S6) )
print( "Correct Answer: 3" )
r1 = overlap(S5,S6)
r2 = overlap(S6,S5)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 3:
        s1 = s1 + 1
if r2 == 3:
        s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 6: " + str(S6) + str(S6) )
print( "Correct Answer: 25" )
r1 = overlap(S6,S6)
r2 = overlap(S6,S6)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 25:
        s1 = s1 + 1
if r2 == 25:
        s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 7: " + str(S7) + str(S6) )
print( "Correct Answer: 1" )
r1 = overlap(S7,S6)
r2 = overlap(S6,S7)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 1:
        s1 = s1 + 1
if r2 == 1:
        s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print ( "Total Score: " + str(totalScore) )
print ( "Percentage: " + str(100*totalScore/14) )



