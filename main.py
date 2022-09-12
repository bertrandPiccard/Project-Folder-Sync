 
import argparse
import os 





parser = argparse.ArgumentParser()
parser.add_argument("-s", "--source", help="Path of source folder",required=True)
parser.add_argument("-r", "--replica", help="Path of replica folder",required=True)
parser.add_argument("-i", "--interval", help="Interval between synchronisation (seconds)",type=int,default=5,required=True)
parser.add_argument("-l", "--log", help="Path of log folder",required=True)

args = parser.parse_args()


if os.path.isdir(args.source) == False:
    print("The path specified for the source is not existing or is invalid...")  
elif os.path.isdir(args.replica) == False:
    print("The path specified for the replica is not existing or is invalid...")
elif os.path.isdir(args.log) == False:
    print("The path specified for the log is not existing or is invalid...")



