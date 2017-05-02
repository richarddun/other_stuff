#! /usr/local/bin/python2
"""
https://www.hackerrank.com/contests/w23/challenges/lighthouse
"""
import sys
class CircleRadius(object):
    def __init__(self):
        self.radius = 0
        self.curradius = 0
        self.curloc = (0,0)
        self.bestloc = (0,0)
        self.bestradius = 0

def test_cardinal(array,yval,xval,reach):
    """
    Test cardinal directions, takes a list and indices as
    arguments, returns True if no obstructions in n,s,e,w
    else returns False. Also takes 'reach' parameter which
    is the distance from the
    origin
    """
    North=South=East=West=False
    if yval - reach < 0:
        return False
    if xval - reach < 0:
        return False
    #print 'Cardinals : xval - ' + str(xval) +', yval - ' + str(yval) + ', Reach - ' +str(reach)
    try:
        if array[yval-reach][xval] == '.':
            North = True
        if array[yval+reach][xval] == '.':
            South = True
        if array[yval][xval+reach] == '.':
            East = True
        if array[yval][xval-reach] == '.':
            West = True
    except:
        return False
    if North and South and East and West:
        return True
    else:
        return False

def test_expansion(array,yval,xval,reach):
    """
    Test the remaining ne,se,sw,nw.  takes a list and indices
    as arguments, returns True if no obstructions, else returns
    False.  Also takes 'reach' parameter which is the distance from the
    origin
    """
    NE=SE=SW=NW=False
    if yval - reach < 0:
        return False
    if xval - reach < 0:
        return False
    for i in xrange(reach+1):
        try:
            if array[yval+reach][xval+reach] == '.': #  NE
                NE = True
            else:
                NE = False
            if array[yval-reach][xval+reach] == '.': #  SE
                SE = True
            else:
                SE = False
            if array[yval-reach][xval-reach] == '.': #  SW
                SW = True
            else:
                SW = False
            if array[yval+reach][xval-reach] == '.': #  NW
                NW = True
            else:
                NW = False
        except:
            return False
    if NE and SE and SW and NW:
        return True
    else:
        return False

def main():
    #  some useful data
    raw_data = []
    junk_data = []
    input_num = []
    for line in sys.stdin.readlines():
        junk_data.append(line)

    for item in junk_data[1:]:
        for char in item:
            if char != '\n':
                raw_data.append(char)
    input_num = int(junk_data[0])

    plotmap = []
    int_row = []
    reach = 1
    mapcounter = 0
    thecircle = CircleRadius()
    #  build the 2d array
    raw_grid = raw_data
    for point in raw_grid:
        if mapcounter == input_num:
            plotmap.append(int_row) #  add another row to the 2d array
            int_row = [] #  clear the list for re-population later
            int_row.append(point)
            mapcounter = 0
        else:
            int_row.append(point)
        mapcounter += 1
    plotmap.append(int_row)
    for yval in xrange(input_num):
        for xval in xrange(input_num):
            if plotmap[yval][xval] == '.':
                for i in xrange(input_num):
                    if test_cardinal(plotmap,yval,xval,i):
                        if i > thecircle.bestradius:
                            thecircle.bestradius = i
                    if not test_expansion(plotmap, yval,xval,i):
                        break

    sys.stdout.write(str(thecircle.bestradius) + '\n')

if __name__ == '__main__':
    main()
