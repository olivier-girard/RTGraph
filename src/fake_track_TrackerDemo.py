#!/usr/bin/python3

import time
import sys
"""
Fake data acquisition. 
Returns a timestamp followed by 512 uint16 values
Uses tabs as separator.

Data is taken as tracks measured by the TrackerDemo on 5 October 2016
The approx. geometry representing this config. (first 100000 events)
is in file /home/lphe/cosmic_analysis/python-scripts/RTGraph/cfg_TrackerDemo/geometry_full_tracker_approx.csv
uplink 80, 81, 84, 85 and 86 are connected
Use pedestal file: /home/lphe/scifi-data/vata64-data/TrackerDemo/full_tracker_first_try/pedestal3.csv
"""


if __name__ == "__main__":
    freq = 10 # Hz
    evCounter = 0
    # sensor position file:
    # setup_examples/geometry_pebs_approx.csv
    while 1:
        with open('/home/lphe/scifi-data/vata64-data/TrackerDemo/full_tracker_first_try/cosmics_72.4V_DACon_allLayers_Crepainted.csv') as csvfile:
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
