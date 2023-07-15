# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 11:38:46 2023

@author: santosh
"""

import numpy as np
import csv

def read_file_ch1(data_file_np, data_file_pn):
    head = 17

    #Read from CSV file
    temp_1_np = np.array([])
    field_1_np = np.array([])
    current_1_np = np.array([])
    res_1_np = np.array([])
    phase_1_np = np.array([])


    temp_1_pn = np.array([])
    field_1_pn = np.array([])
    current_1_pn = np.array([])
    res_1_pn = np.array([])
    phase_1_pn = np.array([])

    temp_1_np = np.append(temp_1_np, "Temperature (K)")
    field_1_np = np.append(field_1_np, "Mag Field (Oe)")
    current_1_np = np.append(current_1_np, "Current Ch1(mA)")
    res_1_np = np.append(res_1_np, "Resistance Ch1 (ohms)")
    phase_1_np = np.append(phase_1_np, "Phase Ch1")

    temp_1_pn = np.append(temp_1_pn, "Temperature (K)")
    field_1_pn = np.append(field_1_pn, "Mag Field (Oe)")
    current_1_pn = np.append(current_1_pn, "Current Ch1(mA)")
    res_1_pn = np.append(res_1_pn, "Resistance Ch1 (ohms)")
    phase_1_pn = np.append(phase_1_pn, "Phase Ch1")


    with open(data_file_np, 'r') as file:
        line = csv.reader(file)
        for skip in range(head):
            next(line)  
        for row in line:
            if len(row):
                if row[13]:
                    temp_1_np = np.append(temp_1_np, [float(row[2])])
                    field_1_np = np.append(field_1_np, [float(row[3])])
                    current_1_np = np.append(current_1_np, [float(row[13])])
                    res_1_np = np.append(res_1_np , [float(row[6])])
                    phase_1_np = np.append(phase_1_np , [float(row[8])])
                
    with open(data_file_pn, 'r') as file:
        line = csv.reader(file)
        for skip in range(head):
            next(line)  
        for row in line:
            if len(row):
                if row[13]:
                    temp_1_pn = np.append(temp_1_pn, [float(row[2])])
                    field_1_pn = np.append(field_1_pn, [float(row[3])])
                    current_1_pn = np.append(current_1_pn, [float(row[13])])
                    res_1_pn = np.append(res_1_pn , [float(row[6])])
                    phase_1_pn = np.append(phase_1_pn , [float(row[8])])
  
        return (temp_1_np, field_1_np, current_1_np, res_1_np, phase_1_np, temp_1_pn, field_1_pn, current_1_pn, res_1_pn, phase_1_pn)
    
# =============================================================================    
# =============================================================================
def read_file_ch2(data_file_np, data_file_pn):
    head = 17

    #Read from CSV file
    temp_2_np = np.array([])
    field_2_np = np.array([])
    current_2_np = np.array([])
    res_2_np = np.array([])
    phase_2_np = np.array([])


    temp_2_pn = np.array([])
    field_2_pn = np.array([])
    current_2_pn = np.array([])
    res_2_pn = np.array([])
    phase_2_pn = np.array([])

    temp_2_np = np.append(temp_2_np, "Temperature (K)")
    field_2_np = np.append(field_2_np, "Mag Field (Oe)")
    current_2_np = np.append(current_2_np, "Current Ch2(mA)")
    res_2_np = np.append(res_2_np, "Resistance Ch2 (ohms)")
    phase_2_np = np.append(phase_2_np, "Phase Ch2")

    temp_2_pn = np.append(temp_2_pn, "Temperature (K)")
    field_2_pn = np.append(field_2_pn, "Mag Field (Oe)")
    current_2_pn = np.append(current_2_pn, "Current Ch2(mA)")
    res_2_pn = np.append(res_2_pn, "Resistance Ch2 (ohms)")
    phase_2_pn = np.append(phase_2_pn, "Phase Ch2")


    with open(data_file_np, 'r') as file:
        line = csv.reader(file)
        for skip in range(head):
            next(line)  
        for row in line:
            if len(row):
                if row[33]:
                    temp_2_np = np.append(temp_2_np, [float(row[2])])
                    field_2_np = np.append(field_2_np, [float(row[3])])
                    current_2_np = np.append(current_2_np, [float(row[33])])
                    res_2_np = np.append(res_2_np , [float(row[26])])
                    phase_2_np = np.append(phase_2_np , [float(row[28])])
                
    with open(data_file_pn, 'r') as file:
        line = csv.reader(file)
        for skip in range(head):
            next(line)  
        for row in line:
            if len(row):
                if row[33]:
                    temp_2_pn = np.append(temp_2_pn, [float(row[2])])
                    field_2_pn = np.append(field_2_pn, [float(row[3])])
                    current_2_pn = np.append(current_2_pn, [float(row[33])])
                    res_2_pn = np.append(res_2_pn , [float(row[26])])
                    phase_2_pn = np.append(phase_2_pn , [float(row[28])])
  
        return (temp_2_np, field_2_np, current_2_np, res_2_np, phase_2_np, temp_2_pn, field_2_pn, current_2_pn, res_2_pn, phase_2_pn)