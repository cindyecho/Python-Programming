# Cynthia Cho
# DSC 430
# Due: March 5, 2019

# I have not given or received any unauthorized assistance on this assignment.



## Problem 2 ##

import re
from urllib.request import urlopen
from bs4 import BeautifulSoup 
from collections import Counter
from string import punctuation
from urllib.parse import urljoin
from html.parser import HTMLParser
import os

class Collector(HTMLParser):
    '''collects hyperlink URLs into a list'''

    def __init__(self, url):
        '''initializes parser, the url, and a list'''
        HTMLParser.__init__(self)
        self.url = url
        self.links = []
        self.text = ''

    def handle_starttag(self, tag, attrs):
        '''collects hyperlink URLs in their absolute format'''
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    # construct absolute URL
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:26] == 'https://www.cdm.depaul.edu': # collect HTTP URLs
                        self.links.append(absolute)
    
    def handle_data(self, data):
        '''collects and concatenates text data'''
        self.text += data

    def getData(self):
        '''returns the concatenation of all text data'''
        return self.text
    
    def getLinks(self):
        '''returns hyperlinks URLs in their absolute format'''
        return self.links



def analyze(url):
    '''returns list of http links in url, in absolute format'''
    
    #print('\n\nVisiting', url)           # for testing
    # obtain links in the web page
    content = urlopen(url).read().decode()
    collector = Collector(url)
    collector.feed(content)
    urls = collector.getLinks()          # get list of links
    return urls



def getText(webpage):
    ''' using BeautifulSoup grab texts from html '''
    html = urlopen(webpage).read().decode()  ## read in the webpage 
    soup = BeautifulSoup(html, 'html.parser')
    text = (''.join(ingredient.findAll(text=True))for ingredient in soup.findAll('p'))  ## grabs words from within html tags that are in format <p>
    words = [punc.rstrip(punctuation).lower() for t in text for punc in t.split()]  ## strips and removes punctuation from each line
    return words



def freqCount(words):  ## adds to global dictionary
    ''' counts the occurence of words and adds to dictionary '''
    for word in words:  
        if word in word_dict:  ## counts the words and if not already in dictionary, addds it
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict[word] = 1


def printWords(dictionary, n):
    ''' takes dictionary input and prints the top 'n' words '''
    w_dict = Counter(dictionary)  
    lst = w_dict.most_common(n)  ## converts dictionary
    print("Displays", n,  "of the most frequent words in descending order",'\n')
    print('{:10} \t {:>8}'.format('WORD:', 'COUNT:'))
    for i in lst:   ##prints words
        print('{:10}\t{:>8}'.format(i[0], i[1]))


#visited = set()  # supressed here because it is called in the main function
def crawler(url):
    ''' Crawls the url for up to 1000 pages, obtains words from each url, and counts occurence of words '''

    print(len(visited),url)  #- used to make sure that function stops at desginated page limit
    #global visited  ## added to main function   
    visited.add(url)  ## appends to visited set
    links = analyze(url)  ## grabs links to pages from url/link called by crawler function
    for link in links:
        if link not in visited:  ## checked the visited set and if not in there, proceeds
            if len(visited) >= 1000:  ## max visited # of pages set at 1000
                break  ## breaks loop if condition is met
            else:
                try:
                    words = getText(link)  ## grabs words from html
                    freqCount(words)  ## counts words
                    crawler(link)  ## recurisvely calls the link within the url
                except:
                    pass


def topsWordFromWebcrawler(url, n):
    ''' returns top n words after crawling url '''
    global word_dict
    word_dict = {}  ## creates empty dictionary
    global visited
    visited = set()  ## creates empty set
    crawler(url)  ## calls in helper function
    return printWords(word_dict ,n)  ##returns output printWords function

#----------------------------------------------------------------------------------------------------------_


## Test call on function ##

#url = 'https://www.cdm.depaul.edu'
#topsWordFromWebcrawler(url, 25)

# Note:
# Due to length of the time that it takes to run the program, I had my crawler set to visit a max of 1000 pages.
# Below is a printout of the 25 most frequent words after crawling 1000 pages.
# I did not call the function for this problem to generate when the file is opened because it would run through 1000 links, 
# and therefore only the printout was provided.


'''
url = 'https://www.cdm.depaul.edu'
topsWordFromWebcrawler(url, 25)

>>> topsWordFromWebcrawler(url, 25)
Displays 25 of the most frequent words in descending order 

WORD:      	   COUNT:
the       	   13079
and       	    8761
of        	    6369
to        	    6071
in        	    5278
a         	    4782
students  	    4458
for       	    3299
are       	    2521
is        	    2417
be        	    2259
courses   	    2252
course    	    1939
that      	    1833
as        	    1830
with      	    1829
on        	    1771
will      	    1768
or        	    1640
at        	    1556
this      	    1333
program   	    1248
depaul    	    1244
requirements	    1174
they      	    1169
>>> 
'''
