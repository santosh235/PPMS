"""
@author: santosh
"""

# MH Analysis of PPMS data file

import numpy as np
import csv
from read_file import read_file_ch1, read_file_ch2

print("This is the Program for analysing our dept PPMS data :\n")

#data_file = input("Enter file name:")
#data_file = "../" + data_file

#out_file = input("Enter output file name: ")
#out_file = "../" + out_file

data_file_np = "../np.dat"
data_file_pn = "../pn.dat"


temp_1_np, field_1_np, current_1_np, res_1_np, phase_1_np, temp_1_pn, field_1_pn, current_1_pn, res_1_pn, phase_1_pn = read_file_ch1(data_file_np, data_file_pn)

temp_2_np, field_2_np, current_2_np, res_2_np, phase_2_np, temp_2_pn, field_2_pn, current_2_pn, res_2_pn, phase_2_pn = read_file_ch2(data_file_np, data_file_pn)


temp_1_np_new = np.array([])
field_1_np_new = np.array([])
current_1_np_new = np.array([])
res_1_np_new = np.array([])
phase_1_np_new = np.array([])


temp_1_pn_new = np.array([])
field_1_pn_new = np.array([])
current_1_pn_new = np.array([])
res_1_pn_new = np.array([])
phase_1_pn_new = np.array([])

temp_1_np_new = np.append(temp_1_np_new, "Temperature (K)")
field_1_np_new = np.append(field_1_np_new, "Mag Field (Oe)")
current_1_np_new = np.append(current_1_np_new, "Current Ch1(mA)")
res_1_np_new = np.append(res_1_np_new, "Resistance Ch1 (ohms)")
phase_1_np_new = np.append(phase_1_np_new, "Phase Ch1")

temp_1_pn_new = np.append(temp_1_pn_new, "Temperature (K)")
field_1_pn_new = np.append(field_1_pn_new, "Mag Field (Oe)")
current_1_pn_new = np.append(current_1_pn_new, "Current Ch1(mA)")
res_1_pn_new = np.append(res_1_pn_new, "Resistance Ch1 (ohms)")
phase_1_pn_new = np.append(phase_1_pn_new, "Phase Ch1")


# temp_1_np_new = np.copy(temp_1_np)
# field_1_np_new = np.copy(field_1_np)
# current_1_np_new = np.copy(current_1_np)
# res_1_np_new = np.copy(res_1_np)
# phase_1_np_new = np.copy(phase_1_np)


# temp_1_pn_new = np.copy(temp_1_pn)
# field_1_pn_new = np.copy(field_1_pn)
# current_1_pn_new = np.copy(current_1_pn)
# res_1_pn_new = np.copy(res_1_pn)
# phase_1_pn_new = np.copy(phase_1_pn)



# =============================================================================
# for i in range(max(len(field_1_np), len(field_1_pn))):
#     if abs(field_1_pn[i]) - abs(field_1_np[i])> 500 :
#         
#         temp_1_np_new = np.append(temp_1_np_new, temp_1_np[i])
#         field_1_np_new = np.append(field_1_np_new, field_1_np[i])
#         current_1_np_new = np.append(current_1_np_new, current_1_np[i])
#         res_1_np_new = np.append(res_1_np_new, res_1_np[i])
#         phase_1_np_new = np.append(phase_1_np_new, phase_1_np[i])
# 
#         temp_1_pn_new = np.append(temp_1_pn_new, temp_1_pn[i])
#         field_1_pn_new = np.append(field_1_pn_new, field_1_pn[i])
#         current_1_pn_new = np.append(current_1_pn_new, current_1_pn[i])
#         res_1_pn_new = np.append(res_1_pn_new, res_1_pn[i])
#         phase_1_pn_new = np.append(phase_1_pn_new, phase_1_pn[i])
#         
#     elif abs(field_1_np[i]) - abs(field_1_pn[i]) > 500:
#         temp_1_np_new = np.append(temp_1_np_new, temp_1_np[i])
#         field_1_np_new = np.append(field_1_np_new, field_1_np[i])
#         current_1_np_new = np.append(current_1_np_new, current_1_np[i])
#         res_1_np_new = np.append(res_1_np_new, res_1_np[i])
#         phase_1_np_new = np.append(phase_1_np_new, phase_1_np[i])
# 
#         temp_1_pn_new = np.append(temp_1_pn_new, temp_1_pn[i])
#         field_1_pn_new = np.append(field_1_pn_new, field_1_pn[i])
#         current_1_pn_new = np.append(current_1_pn_new, current_1_pn[i])
#         res_1_pn_new = np.append(res_1_pn_new, res_1_pn[i])
#         phase_1_pn_new = np.append(phase_1_pn_new, phase_1_pn[i])
#         
#     else:
#         temp_1_np_new = np.append(temp_1_np_new, temp_1_np[i])
#         field_1_np_new = np.append(field_1_np_new, field_1_np[i])
#         current_1_np_new = np.append(current_1_np_new, current_1_np[i])
#         res_1_np_new = np.append(res_1_np_new, res_1_np[i])
#         phase_1_np_new = np.append(phase_1_np_new, phase_1_np[i])
# 
#         temp_1_pn_new = np.append(temp_1_pn_new, temp_1_pn[i])
#         field_1_pn_new = np.append(field_1_pn_new, field_1_pn[i])
#         current_1_pn_new = np.append(current_1_pn_new, current_1_pn[i])
#         res_1_pn_new = np.append(res_1_pn_new, res_1_pn[i])
#         phase_1_pn_new = np.append(phase_1_pn_new, phase_1_pn[i])
#     
# =============================================================================

x = 1
y = 1

for i in range(1, min(len(field_1_np), len(field_1_pn))):
    if abs(float(field_1_pn[x])) - abs(float(field_1_np[y]))> 500 :
        x = x+1
    elif abs(float(field_1_np[y])) - abs(float(field_1_pn[x])) > 500:
        y = y+1
    else:
        temp_1_pn_new = np.append(temp_1_pn_new, temp_1_pn[x])
        field_1_pn_new = np.append(field_1_pn_new, field_1_pn[x])
        current_1_pn_new = np.append(current_1_pn_new, current_1_pn[x])
        res_1_pn_new = np.append(res_1_pn_new, res_1_pn[x])
        phase_1_pn_new = np.append(phase_1_pn_new, phase_1_pn[x])
        
        
        temp_1_np_new = np.append(temp_1_np_new, temp_1_np[y])
        field_1_np_new = np.append(field_1_np_new, field_1_np[y])
        current_1_np_new = np.append(current_1_np_new, current_1_np[y])
        res_1_np_new = np.append(res_1_np_new, res_1_np[y])
        phase_1_np_new = np.append(phase_1_np_new, phase_1_np[y])

        x = x+1
        y = y+1
        


print(len(field_1_np))
print(len(field_1_np_new))

out_file = '../raw.txt'
with open(out_file, 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(zip(temp_1_np, field_1_np, current_1_np, res_1_np, phase_1_np, temp_1_pn, field_1_pn, current_1_pn, res_1_pn, phase_1_pn))
    
# out_file = '../s2.txt'
# with open(out_file, 'w') as f:
#     writer = csv.writer(f, delimiter='\t')
#     writer.writerows(zip(temp_2_np, field_2_np, current_2_np, res_2_np, phase_2_np, temp_2_pn, field_2_pn, current_2_pn, res_2_pn, phase_2_pn))

out_file = '../processed.txt'
with open(out_file, 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(zip(temp_1_np_new, field_1_np_new, current_1_np_new, res_1_np_new, phase_1_np_new, temp_1_pn_new, field_1_pn_new, current_1_pn_new, res_1_pn_new, phase_1_pn_new))
