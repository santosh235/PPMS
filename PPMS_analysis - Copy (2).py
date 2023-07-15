"""
@author: santosh
"""

# MH Analysis of PPMS data file

import numpy as np
import csv
from read_file import read_file_ch1

print("This is the Program for analysing our dept PPMS data :\n")

#data_file = input("Enter file name:")
#data_file = "../" + data_file

#out_file = input("Enter output file name: ")
#out_file = "../" + out_file

data_file_np = "../np.dat"
data_file_pn = "../pn.dat"
out_file = '../s.txt'

# head = int(input("Enter the number of starting line to omit: "))
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
current_pn = np.append(current_1_pn, "Current Ch1(mA)")
res_1_pn = np.append(res_1_pn, "Resistance Ch1 (ohms)")
phase_1_pn = np.append(phase_1_pn, "Phase Ch1")

# =============================================================================
# temp_2 = np.array([])
# field_2 = np.array([])
# current_2 = np.array([])
# res_2 = np.array([])
# phase_2 = np.array([])
# =============================================================================

# =============================================================================
# temp_1 = np.append(temp_1, "Temperature (K)")
# field_1 = np.append(field_1, "Mag Field (Oe)")
# current_1 = np.append(current_1, "Current Ch1(mA)")
# res_1 = np.append(res_1 , "Resistance Ch1 (ohms)")
# phase_1 = np.append(phase_1 , "Phase Ch1")
# 
# temp_2 = np.append(temp_2, "Temperature (K)")
# field_2 = np.append(field_2, "Mag Field (Oe)")
# current_2 = np.append(current_2, "Current Ch2(mA)")
# res_2 = np.append(res_2 , "Resistance Ch2 (ohms)")
# phase_2 = np.append(phase_2, "Phase_2")
# 
# =============================================================================


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
    
# =============================================================================
# for i in range(1, len(temp_1) - 1):
#     if float(field_1[i+1]) - float(field_1[i]) > -200:
#         temp_1_np = np.append(temp_1_np, temp_1[i])
#         flag = flag+1
#         field_1_np = np.append(field_1_np, field_1[i])
#         current_1_np = np.append(current_1_np, current_1[i])
#         res_1_np = np.append(res_1_np, res_1[i])
#         phase_1_np = np.append(phase_1_np, phase_1[i])
#         
#     else:
#         temp_1_pn = np.append(temp_1_pn, temp_1[i])
#         field_1_pn = np.append(field_1_pn, field_1[i])
#         current_1_pn = np.append(current_1_pn, current_1[i])
#         res_1_pn = np.append(res_1_pn, res_1[i])
#         phase_1_pn = np.append(phase_1_pn, phase_1[i])
# =============================================================================
            
            
            

with open(out_file, 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(zip(temp_1_np,field_1_np, field_1_pn))



