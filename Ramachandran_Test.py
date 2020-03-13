# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:31:20 2019

@author: evan
"""

from MD_Analysis import *
import easygui as eg

pdb = eg.fileopenbox(msg = "Select the pdb to calculate angles from")

AC = Angle_Calc(pdb)
AC.get_phi_psi()

R = Ramachandran("D:\GEMSEC\PDB files\sADP5_WT\sADP5_WT\SIM 6\\")
R.plt_all(AC.angles, "sADP5_WT_500ns_SIM6")
#R.plt_one(AC.angles, '1', "sADP5_WT_500ns_SIM6" )