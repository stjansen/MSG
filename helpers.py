import numpy as np
import csv

# Convert data in csv file to nunpy array
def getData(filename):
    data = []
    with open(filename) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            data.append(row)

    data_arr = np.array(data)
    return data_arr


def isDetected(input):
    
    even = 0
    odd = 0

    # # for entry in output:
    # for i in range(len(output)):
    #     entry = output[i]
    #     if i % 2 a


# Convert representation of string to digit.
def convertToDigit(output):
    digit = 0
    idx = 0
    for i in output[::-1]:
        digit += int(i) * 2 ** idx
        idx += 1
    
    return digit