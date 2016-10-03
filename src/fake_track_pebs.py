#!/usr/bin/python3

import time
import sys
"""
Fake data acquisition. 
Returns a timestamp followed by 512 uint16 values
Uses tabs as separator.

Data is taken as tracks measured by PEBS
The approx. geometry representing this config.
is in file geometry_pebs_approx.csv
"""


if __name__ == "__main__":
    freq = 10 # Hz
    evCounter = 0
    # sensor position file:
    # setup_examples/geometry_pebs_approx.csv
    while 1:
        with open('/home/lphe/scifi-data/vata64-data/Pebs_cp-from-tell22/signal.csv') as csvfile:
            for i, row in enumerate(csvfile):
                rowsplit = row.split()
                rowsplit[0] = evCounter+1
                rowsplit[1] = int(time.time())
                for element in rowsplit:
                    print("{}\t".format(element), end="")
                time.sleep(1/freq)
                sys.stdout.flush()
                print("\t")
                evCounter += 1	
