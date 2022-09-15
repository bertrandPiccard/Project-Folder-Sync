import logging
import sys


# Logger path will be configured based on the argument
# Two handlers are needed for the file output and console output
def getLogger(logF):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(logF+"\log.txt"),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging
