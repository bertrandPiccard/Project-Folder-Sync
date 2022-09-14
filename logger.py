import logging
import sys

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
