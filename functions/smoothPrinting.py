
import time
import sys

def smooth_printing(text, delay):
    for each in text:
        print(each, end="", flush=True)
        time.sleep(delay)
    
    print("\n")



def smooth_word_printing(sentence, delay, escape=True):
    sentence_arr = sentence.split()
    for word in sentence_arr:
        print(word, end=" ", flush=True)
        time.sleep(delay)
    if escape:
        print("\n")
    