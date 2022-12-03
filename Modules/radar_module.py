import numpy as np
import csv

# Convert data in csv file to nunpy array
def getRadarData(filename):
    data = []
    with open(filename) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            data.append(row)

    data_arr = np.array(data)

    return data_arr