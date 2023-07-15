# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 11:38:46 2023

@author: santosh
"""

import numpy as np
import csv

def read_file():
    #data_file = input("Enter file name:")
    #data_file = "../" + data_file
    data_file = "../d.dat"
    out_file = '../s.txt'
    head = 17
    
    #Read from CSV file
    temp_1 = np.array([])
    field_1 = np.array([])
    current_1 = np.array([])
    res_1 = np.array([])
    phase_1 = np.array([])

    temp_2 = np.array([])
    field_2 = np.array([])
    current_2 = np.array([])
    res_2 = np.array([])
    phase_2 = np.array([])
    
    
    temp_1 = np.append(temp_1, "Temperature (K)")
    field_1 = np.append(field_1, "Mag Field (Oe)")
    current_1 = np.append(current_1, "Current Ch1(mA)")
    res_1 = np.append(res_1 , "Resistance Ch1 (ohms)")
    phase_1 = np.append(phase_1 , "Phase Ch1")

    temp_2 = np.append(temp_2, "Temperature (K)")
    field_2 = np.append(field_2, "Mag Field (Oe)")
    current_2 = np.append(current_2, "Current Ch2(mA)")
    res_2 = np.append(res_2 , "Resistance Ch2 (ohms)")
    phase_2 = np.append(phase_2, "Phase_2")


    with open(data_file, 'r') as file:
        line = csv.reader(file)
        for skip in range(head):
            next(line)  
            for row in line:
                print(row)
# =============================================================================
#                 if len(row):
#                     if row[2]:
#                         temp_1 = np.append(temp_1, [float(row[2])])
#                         field_1 = np.append(field_1, [float(row[3])])
#                         current_1 = np.append(current_1, [float(row[13])])
#                         res_1 = np.append(res_1 , [float(row[6])])
#                         phase_1 = np.append(phase_1 , [float(row[8])])
#                     else:
#                         temp_2 = np.append(temp_2, [float(row[2])])
#                         field_2 = np.append(field_2, [float(row[3])])
#                         current_2 = np.append(current_2, [float(row[33])])
#                         res_2 = np.append(res_2 , [float(row[26])])
#                         phase_2 = np.append(phase_2, [float(row[28])])
# =============================================================================
  
        return (temp_1, field_1, current_1, res_1, phase_1)