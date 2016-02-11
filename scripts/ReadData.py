__author__ = 'alireza'
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter, MaxNLocator
from numpy import linspace
plt.ion()


def load_file(filenum):
    myfile = open(filenum, 'r')
    mydata = myfile.readlines()
    myfile.close()

    file_data = []

    for line in mydata:
        split_data = line.split()
        temp = []
        # for elements in split_data:
            # temp.append(float(elements))
        # temp[3] = (temp[3] / 1000000) - 35
        # if 292636800 > temp[3] > 292550400:
        file_data.append(split_data)

    return file_data
#Data = load_file('/home/alireza/Desktop/Weather Project/Simulator Results/Test Result-0725/'
#                 'Test Result-0725/VD50m.Dat')
Data = load_file('/Users/Vamsee/Work/dropzone/2016-Transportation/SPMD Sample/DAS_1_BSM_Data/BsmP1_04_11_13.csv')

