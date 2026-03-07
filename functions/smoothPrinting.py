
import time
import sys

def smooth_printing(text, delay):
    #loop through each letter in the sentence or word
    for each in text:
        print(each, end="", flush=True)
        #delay is the sleeping time after every loop happens
        time.sleep(delay)
    
    print("\n")



def smooth_word_printing(sentence, delay, escape=True):
    #convert sentence to array
    sentence_arr = sentence.split()
    #loop through array
    for word in sentence_arr:
        print(word, end=" ", flush=True)
        time.sleep(delay)
    if escape:
        print("\n")
    