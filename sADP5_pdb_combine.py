# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 20:13:01 2020

@author: evan
"""
from MD_Analysis import *
import pandas as pd
import easygui as eg

# Getting the phi/psi angles
pdb = eg.fileopenbox(msg="Select the pdb to calculate angles from")

AC = Angle_Calc(pdb)
AC.get_phi_psi()
AC.angles.to_csv("sADP5_WT_500ns_SIM6_phi_psi.csv")

# Loading in Data
names = ['sADP5_WT_500ns_SIM1_phi_psi', 'sADP5_WT_500ns_SIM2_phi_psi',
          'sADP5_WT_500ns_SIM3_phi_psi', 'sADP5_WT_500ns_SIM4_phi_psi',
          'sADP5_WT_500ns_SIM5_phi_psi', 'sADP5_WT_500ns_SIM6_phi_psi']

# Iterates through list of pdb files, reads them, deletes unamed column 
# and creates a list of the dataframes
sim_combined = []
for name in names: 
    data = pd.read_csv(name + '.csv')
    del data['Unnamed: 0']
    sim_combined.append(data)

# concatenates the dataframes into a single df
df = pd.concat(sim_combined, sort = False)

df.to_csv('sADP5_WT_3ms.csv')
    