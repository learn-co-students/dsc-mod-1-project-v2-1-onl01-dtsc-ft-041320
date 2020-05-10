import gzip
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import my_functions
import string

def remove_punctuations(text):
    for punctuation in string.punctuation:
        text = text.lower().replace(punctuation, '')
    return text



def med_and_mean(column):
    mean = pd.column.mean
    median = pd.column.median
    print(f'------The average value of {column} is {mean}------\n')
    print(f'------The average value of {column} is {median}------\n')
    return 