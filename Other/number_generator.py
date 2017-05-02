#!/usr/bin/env python

"""
Emulate a spinning drum containing numbers from 1-47 and pick six numbers from it
"""

import os
import sys
import random
from collections import deque
import time

def pre_spool():
    """
    Generate a 'pipe' (array) of numbers to put into a circular drum
    Accepts no arguments
    Returns randomly assorted list with numbers from 1-47
    """
    operations = 1
    init_array = [i for i in xrange(1,48)] #  initial untouched array
    first_list = list()
    modul = random.randint(2,4) 
    while len(first_list) < 47:
        operations += 1
        for i in xrange(0,47):
            operations += 1
            if i == 0 or modul == 0:
                if init_array[i] in first_list:
                    pass
                else:
                    first_list.append(init_array[i])
            else: 
                if i %modul == 0:
                    if init_array[i] in first_list:
                        pass
                    else:
                        first_list.append(init_array[i])
        modul = random.randint(0,47)
    #print 'Total operations: ' + str(operations)
    return first_list

    
class NumDrum(object):
    """
    Number Drum class
    """
    def __init__(self):
        #  5 slots of data to drop into drums
        #self.drum_wall_n = [[],[],[]] #  3,3,4
        #self.drum_wall_e = [[],[],[]]
        #self.drum_wall_s = [[],[],[]]
        #self.drum_wall_w = [[],[],[]]
        #self.drum_base = [[],[],[],[]] #  2,2,2,1 
        #self.drum_base[3][1] is the main number outlet
        #  screw it, use deque instead
        self.drum_wall_n = deque()
        self.drum_wall_e = deque()
        self.drum_wall_s = deque()
        self.drum_wall_w = deque()
        self.drum_base = deque()


    def put_drum(self, indata):
        token = 'n'
        data = indata

        while len(self.drum_base) < 7:
            self.Bfill(data.pop())

        for i in xrange(40): #  the rest of the 40 numbers
            try:
                if token == 'n':
                    self.Nfill(data.pop())
                    token = 'e'
                elif token == 'e':
                    self.Efill(data.pop())
                    token = 's'
                elif token == 's':
                    self.Sfill(data.pop())
                    token = 'w'
                elif token == 'w':
                    self.Wfill(data.pop())
                    token = 'n'
            except IndexError:
                print 'index error'
                break
                
    def Bfill(self, indata):
        #3 is lowest level, higher number, deeper reach
        if len(self.drum_base) < 7:
            self.drum_base.append(indata)
            
    def Nfill(self, indata):
        if len(self.drum_wall_n) < 10:
            self.drum_wall_n.append(indata)
            
    def Efill(self, indata):
        if len(self.drum_wall_e) < 10:
            self.drum_wall_e.append(indata)
    
    def Wfill(self, indata):
        if len(self.drum_wall_w) < 10:
            self.drum_wall_w.append(indata)
    
    def Sfill(self, indata):
        if len(self.drum_wall_s) < 10:
            self.drum_wall_s.append(indata)
            
    def CurNumDrum(self):
        print 'North: ' + str(self.drum_wall_n)
        print 'South: ' + str(self.drum_wall_s)
        print 'East: ' + str(self.drum_wall_e)
        print 'West: ' + str(self.drum_wall_w)
        print 'Base: ' + str(self.drum_base)

    def Rotater(self):
        #  N-> [3],[3],[4] 
        #  S-> [3],[3],[4]
        #  E-> [3],[3],[4]
        #  W-> [3],[3],[4]
        #  B-> [2],[2],[2],[1]
        self.drum_wall_n.rotate(1)
        self.drum_wall_s.rotate(1)
        self.drum_wall_w.rotate(1)
        self.drum_wall_e.rotate(1)
        self.drum_base.rotate(1)
    
    @staticmethod
    def SwapNum(nlist):
        ntop = nlist[:3]
        nmid = nlist[3:6]
        nbot = nlist[6:9]
        nend = list()
        nend.append(nlist[-1])
        ntmp = nmid
        nmid = nbot
        nbot = ntmp #  Swapping 'bottom' array with middle
        ntmp = ntop
        ntop = nmid
        nmid = ntmp #  Swapping 'top' array with middle
        return ntop + nmid + nbot + nend
            
    def RepNum(self, wall):
        if wall == 'n' or wall == 'a':
            nlist = self.SwapNum(list(self.drum_wall_n))
            self.drum_wall_n = deque(nlist)
        if wall == 'e' or wall == 'a':
            nlist = self.SwapNum(list(self.drum_wall_e))
            self.drum_wall_e = deque(nlist)
        if wall == 'w' or wall == 'a':
            nlist = self.SwapNum(list(self.drum_wall_w))
            self.drum_wall_w = deque(nlist)
        if wall == 's' or wall == 'a':
            nlist = self.SwapNum(list(self.drum_wall_s))
            self.drum_wall_s = deque(nlist)
            
    def BaseRep(self):
        reflist = list(self.drum_base)
        pairwise = {'npair':(reflist[0],reflist[1]),'epair':(reflist[2],reflist[3]),'wpair':(reflist[4],reflist[5])}
        for pair in pairwise.keys():
            if sum(pairwise[pair]) == 0:
                self.ShuntBase(pair,0)
            elif sum(pairwise[pair]) % 2 == 0:
                self.ShuntBase(pair, 0)
            else:
                self.ShuntBase(pair, 1)
        self.ShuntBase('s',0)

    def ShuntBase(self, location, skew):
        nskew,eskew,wskew = 0,1,2
        blist = list(self.drum_base)
        if location == 'npair':
            nval = self.drum_wall_n.pop()
            tempbval = blist.pop(skew+nskew)
            self.drum_wall_n.append(tempbval)
            blist.insert(skew+nskew, nval)
            self.drum_base = deque(blist)
        elif location == 'epair':
            eval = self.drum_wall_e.pop()
            tempbval = blist.pop(skew+eskew)
            self.drum_wall_e.append(tempbval)
            blist.insert(skew+eskew, eval)
            self.drum_base = deque(blist)
        elif location == 'wpair':
            wval = self.drum_wall_w.pop()
            tempbval = blist.pop(skew+wskew)
            self.drum_wall_w.append(tempbval)
            blist.insert(skew+wskew, wval)
            self.drum_base = deque(blist)        
        elif location == 's':
            tempwsval = self.drum_wall_s.pop()
            tempbsval = self.drum_base.pop()
            self.drum_wall_s.append(tempbsval)
            self.drum_base.append(tempwsval)
    
    def IsNullNum(self):
        if self.drum_base[-1] == 0:
            return True
         
    def PopNum(self):
        """
        Return the last index of base deque as number choice
        The drum size will not be changing, instead 'zero' numbers
        will be placed as replacements for popped numbers, which will be 
        ignored if selected for 'popping'
        """
        retval = self.drum_base.pop()
        self.drum_base.append(0)
        return retval
        
def main():
    print 'beginning draw...'
    endlist = list()
    thedrum = NumDrum()
    thedrum.put_drum(pre_spool())
    #thedrum.CurNumDrum()
    while len(endlist) < 6:
        print 'drum is spinning fast'
        for i in xrange(32):
            thedrum.Rotater()
            thedrum.RepNum('a')
            thedrum.BaseRep()
        time.sleep(.4)
        print 'drum slows down'
        for i in xrange(random.randint(3,9)):
            thedrum.Rotater()
            time.sleep(.2)
        if thedrum.IsNullNum():
            #print 'base is currently: ' + str(thedrum.drum_base)
            continue
        else:
            pot_num = thedrum.PopNum()
            endlist.append(pot_num)
            print 'picked ' + str(pot_num) +' !'
    
    print 'final selection:'
    print sorted(endlist)
    
if __name__=='__main__':
    main()
