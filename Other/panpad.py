#!/usr/bin/env python2

import curses
import curses.panel

def main(win):
    global stdscr
    global max_y,max_x,mult
    stdscr = win
    curses.initscr()
    curses.cbreak()
    curses.noecho()
    stdscr.keypad(1)
    curses.curs_set(0)
    y,x = 0,1
    mult = 1
    maxcoords = stdscr.getmaxyx()
    max_y, max_x = maxcoords[y],maxcoords[x]
    pad = curses.newpad(max_y,2000)
    bpad = curses.newpad(max_y,2000)
    drawstuff(pad)
    running = True
    while running:
        mvmt = stdscr.getch()
        if mvmt == ord('a'):
            mult += 1
            pad.refresh(1,1,1,1,max_y,mult)
            bpad.refresh(1,1,1,1,max_y,mult-1)
        if mvmt == ord('b'):
            mult += 1
            pad.refresh(1,1,1,1,max_y,mult)
            bpad.refresh(1,1,1,1,max_y,mult-1)
        if mvmt == ord('Q'):
            running = False
            return
        curses.doupdate()
    #padp = curses.panel.new_panel(pad)
    #winp = curses.panel.new_panel(win)

    #curses.panel.update_panels()

    #pad.getch()
    curses.endwin()

def drawstuff(pad):
    for i in xrange(max_x):
        for j in xrange(max_y):
            if i % 2 == 0:
                pad.addch(j,i,'+')
            else:
                pad.addch(j,i,'-')

if __name__ == '__main__': 
    curses.wrapper(main)




