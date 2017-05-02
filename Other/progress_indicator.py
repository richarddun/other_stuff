#!/usr/bin/env python
import time
import sys

syms = ['\\','|','/','-']
spinner = 0
recordnum = 613
for i in range(recordnum):
    sys.stdout.write("{:.2%} percent done ".format(float(i)/float(recordnum)))
    sys.stdout.write('\r')
    sys.stdout.flush()
    time.sleep(0.2)


    
