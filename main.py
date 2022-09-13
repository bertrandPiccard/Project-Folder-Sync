 
import argparse
import os 
import threading
from datetime import datetime
import logging
import sys
import filecmp

from synchronisation import synchroniseFolder

def start(args):
     #Affect the variables for better visibility
    srcF = args.source
    repF = args.replica
    logF = args.log
    interval = args.interval

    # Configure the logger 
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(logF+"log.txt"),
            logging.StreamHandler(sys.stdout)
        ]
    )
    # Start the synchronisation of the folder
    synchroniseFolder(srcF,repF,logging)



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
   


def printit():
  threading.Timer(3.0, printit).start()
  print("Hello, World!" + str(datetime.now()))
