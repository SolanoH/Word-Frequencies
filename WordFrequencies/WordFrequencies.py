#!/usr/bin/env pypy

'''
Created on Jan 19, 2017

@author: Hector
'''
from _collections import defaultdict
import re
import sys



#######################   PART A ######################################################

### Recieves a filepath and return a list of alphanumeric tokens found in text file ###
def tokenize(Filepath):
    tokens = []
    prog = re.compile('[^0-9a-zA-Z]+')
    with open(Filepath) as infile:
        for line in infile:
            line = prog.sub(' ',line).split()
            for  word in line:
                tokens.append(word)
    return tokens
            

def computeWordFrequencies(tokens):
    wordFrequencies = defaultdict(int)
    for token in tokens:
        wordFrequencies[token.lower()] += 1
    return wordFrequencies


def printFrequencies(wordFrequencies):
    wordfrequencycounts = wordFrequencies.items()
    sortedlist = sorted(wordfrequencycounts, key = lambda tup: tup[1], reverse = True)
    print sortedlist

    
def PartA():
    infile = sys.argv[1]
    tokens = tokenize(infile)
    printFrequencies(computeWordFrequencies(tokens))



if __name__ == '__main__':
    PartA()
    