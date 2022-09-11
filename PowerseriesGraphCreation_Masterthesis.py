#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 14:29:34 2022

@author: Jessica
"""

#%% ------ libraries, general styling and folder paths -----
# -- libraries --
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from matplotlib.ticker import ScalarFormatter

# -- general plot styles --
matplotlib.rcParams['font.monospace'] = "Arial"
matplotlib.rcParams['font.family'] = "monospace"
matplotlib.rc('font', size=11)
matplotlib.rcParams['axes.linewidth'] = 1

# -- data folder path --
data_path = "<path of sample data>" + "/" # enter path of sample data
filename_width = "linewidth_data.txt" # this is the name of the sample data file
filename_height = "intensity_data.txt" # this is the name of the sample data file
filename_position = "position_data.txt" # this is the name of the sample data file

#%% ------ choose x-axis setting and save option ------ 
saveFigure = True
xAxis_P_Pth = False
P_th = 5.62 # threshold power

#%% ------ create data lists from the input files ------ 
powerList = []
widthList = []
heightList = []
positionList = []

# -- get width data --
fileWidth = open(data_path + filename_width)
linesWidth = fileWidth.readlines()
for i in range(0,len(linesWidth)):
    powerList.append(float(linesWidth[i].split(',')[0]))
    widthList.append(float(linesWidth[i].split(',')[1]))
    
widthList = [x * 1000 for x in widthList] # convert eV to meV

# -- get height data --
fileHeight = open(data_path + filename_height)
linesHeight = fileHeight.readlines()
for i in range(0,len(linesHeight)):
    heightList.append(float(linesHeight[i].split(',')[1]))
    
# -- get position data --
filePosition = open(data_path + filename_position)
linesPosition = filePosition.readlines()
for i in range(0,len(linesPosition)):
    positionList.append(float(linesPosition[i].split(',')[1]))
    
positionList = [x * 1000 for x in positionList] # convert eV to meV

# -- calculate energyshift from position --
energyPositionAtLowestPower = positionList[0]
positionList = [x - energyPositionAtLowestPower for x in positionList]

# -- rescale power-axis if desired --
if xAxis_P_Pth:
    powerList[:] = [x / P_th for x in powerList]


#%% ----- plot all data in one plot -----
# -- plot style parameter --
margin = 0.08
markerSize = 5
lineWidth = 1.5

# -- create figure environment --
fig, (ax1, ax3) = plt.subplots(2, sharex=True, gridspec_kw={'height_ratios': [2.5, 1]}, figsize=(5,5))
fig.subplots_adjust(wspace=-1)

# -- add first axis for the PL intensity --
ax1.plot(powerList, heightList, color="#004873", marker="o", linewidth=lineWidth, markersize=markerSize)
ax1.set_ylabel("PL Intensity (a. u.)",fontsize=14, color="#004873")
    
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.tick_params(which="major", direction='in', color="#004873", labelcolor="#004873", width=1.3)
ax1.tick_params(which="minor", direction='in', color="#004873", width=1.3)
ax1.yaxis.set_ticks_position('both')
ax1.xaxis.set_ticks_position('both')

ax1.spines['left'].set_color('#004873') 
ax1.tick_params(which='both', axis='x', colors='black')


# -- twin object for two different y-axis on the sample plot for the linewidth --
ax2=ax1.twinx()
ax2.plot(powerList, widthList,color="#A20059",marker="o", linewidth=lineWidth, markersize=markerSize)
ax2.set_ylabel("Linewidth (meV)",fontsize=14, color="#A20059")

ax2.tick_params(which="major", direction='in', color="#A20059", labelcolor="#A20059", width=1.3)
ax2.tick_params(which="minor", direction='in', color="#A20059", width=1.3)

ax2.spines['right'].set_color('#A20059') 

# -- add third axis to create the second plot for the energy shift -- 
ax3.plot(powerList, positionList, color="#6CA714", marker="o", linewidth=lineWidth, markersize=markerSize)
ax3.set_ylabel("Energy shift (meV)",fontsize=14)
if xAxis_P_Pth:
    ax3.set_xlabel("Excitation power ($P/P_{th}$)",fontsize=14)
else:
    ax3.set_xlabel("Excitation power (mW)",fontsize=14)

plt.xscale('log', subs=[2, 3, 4, 5, 6, 7, 8, 9]) # adjust x-axis
ax3.tick_params(which="major", direction='in', width=1.3)
ax3.tick_params(which="minor", direction='in', width=1.3)

# -- tick and margin settings --
plt.minorticks_on()
ax3.minorticks_on()
ax2.minorticks_on()
ax1.minorticks_on()
ax3.yaxis.set_ticks_position('both')
ax3.xaxis.set_ticks_position('both')

ax1.margins(margin)
ax2.margins(margin)
ax3.margins(margin + 0.1)

ax1.xaxis.set_major_formatter(ScalarFormatter())
ax1.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

fig.tight_layout()

#fig.savefig('test.png')

# plt.show()

# -- safe files and create txt file with the resulting data used for the plots -- 
if xAxis_P_Pth:
    powerTitle = 'P/Pth'
    filename = "Results_P_Pth"
else:
    powerTitle = 'Power (mW)'
    filename = "Results"

if saveFigure: 
    # save plot
    fig.savefig(data_path + filename + ".png", bbox_inches='tight', dpi=1000)
    
    # Create file 
    file = open(data_path + filename + ".txt", "w+")
    
    # Saving the array in a text file
    file.write(powerTitle + ' , Energyshift (meV), Linewidth (meV), PL Intensity (a. u.) \n')
    for idx, x in np.ndenumerate(powerList):
      file.write(str(x))
      file.write(', ')
      file.write(str(positionList[idx[0]]))
      file.write(', ')
      file.write(str(widthList[idx[0]]))
      file.write(', ')
      file.write(str(heightList[idx[0]]))
      file.write('\n')
     
    file.close()

