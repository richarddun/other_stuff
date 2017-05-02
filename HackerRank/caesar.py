#!/usr/bin/env python2

"""
https://www.hackerrank.com/challenges/caesar-cipher-1
"""
import sys
from collections import deque

n = int(raw_input().strip()) #length of string (not used in this solution)
s = raw_input().strip() #string to be encrypted
k = int(raw_input().strip()) #rotation key

def rotchar(ch,rot):
    if ch.isalpha():
        upperalphalist = [chr(x) for x in xrange(65,91)]
        loweralphalist = [chr(x) for x in xrange(97,123)]
        upperalpharot = deque(upperalphalist)
        loweralpharot = deque(loweralphalist)
        if ch.isupper():
            charloc = upperalphalist.index(ch)
            upperalpharot.rotate(-rot)
            return upperalpharot[charloc]
        elif ch.islower():
            charloc = loweralphalist.index(ch)
            loweralpharot.rotate(-rot)
            return loweralpharot[charloc]
    else:
        return ch

charlist = list(s)
retlist = []

for i in charlist:
    retlist.append(rotchar(i,k))
print ''.join(retlist)