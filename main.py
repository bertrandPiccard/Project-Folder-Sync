 
import argparse
import os 
import time
from datetime import datetime

import logger

from synchronisation import synchroniseFolder



def start(args):
     #Affect the variables for better visibility
    srcF = os.path.abspath(args.source)
    repF = os.path.abspath(args.replica)
    logF = os.path.abspath(args.log)
    interval = args.interval

    # Configure the logger 
    log = logger.getLogger(logF)

    # Clear terminal for better visibility
    os.system('cls')


    #The synchronisation will be executed periodically with interval
    counter=0
    while counter < 10:
        counter += 1
        print(">>> Synchronisation N°: " + str(counter) + " "+ str(time.asctime(time.localtime())))
        synchroniseFolder(srcF,repF,log)
        time.sleep(interval)


    print(">>> Synchronisation finished...")





#Define the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--source", help="Path of source folder",required=True)
parser.add_argument("-r", "--replica", help="Path of replica folder",required=True)
parser.add_argument("-i", "--interval", help="Interval between synchronisation (seconds)",type=int,default=5,required=True)
parser.add_argument("-l", "--log", help="Path of log folder",required=True)
args = parser.parse_args()


#Check if the path are existing and if the value of the interval is higher or equal 5 seconds
if os.path.isdir(args.source) == False:
    print("The path specified for the source is not existing or is invalid...")  
elif os.path.isdir(args.replica) == False:
    print("The path specified for the replica is not existing or is invalid...")
elif os.path.isdir(args.log) == False:
    print("The path specified for the log is not existing or is invalid...")
elif args.interval < 5:
    print("The value of the interval has to be higher than 5 seconds...")
else:
    start(args)
   
