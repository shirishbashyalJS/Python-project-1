
import time
import sys

def smooth_printing(text):
    for each in text:
        print(each, end="", flush=True)
        time.sleep(0.1)