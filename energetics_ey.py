# Energy and entropy map 
# calculation for pdb files

import pandas as pd
import numpy as np 
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt
import seaborn as sns
from MD_Analysis import *
import easygui as eg

# Getting the phi/psi angles
# pdb = eg.fileopenbox(msg="Select the pdb to calculate angles from")

# AC = Angle_Calc(pdb)
# AC.get_phi_psi()
# AC.angles.to_csv("sADP5_wt_metad100ns_phi_psi.csv")

# get the cos/sin data from phi/psi using pedros
name = 'sADP5_WT_3ms'         
data = pd.read_csv(name + '.csv')
# del data['Unnamed: 0']

sc_df = pd.DataFrame()

for col in data.columns:
    sc_df['Sin - ' + col] = data[col].map(lambda x: np.sin(x))
    sc_df['Cos - ' + col] = data[col].map(lambda x: np.cos(x))


# PCA
scaled_data = preprocessing.scale(data)
scaled_data = np.nan_to_num(scaled_data)
pca = PCA()   # creating the PCA object
pca.fit(scaled_data)   # math
pca_data = pca.transform(scaled_data)   # PCA coordinates
per_var = np.round(pca.explained_variance_ratio_ * 100, decimals=1)

# Labeling and calculating explained variance
labels = ['PC' + str(x) for x in range(1, len(per_var)+1)]
pca_df = pd.DataFrame(pca_data, columns=labels)

# Making a histogram of the relative frequencies of each Principal component
hist = np.histogram2d(pca_df.PC1, pca_df.PC2, bins= 40) # bin size somewhat arbitrary

# Converting histogram from frequencies to probabilities
prob = hist[0]/(sum(sum(hist[0])))

# Energetics
# Defining variables
kb = 1.38064852 * 10**-23 # Boltzmann's costant (J/K)
T = 300 # temperature (K)

# Creating Gibbs Free energy histogram
G = -kb * T * np.log(prob/(1-prob))  # free energy (J)
G[G == np.inf] = 2.86157e-20


# Creating Entropy histogram
S = -kb * T * prob * np.log(prob)       # entropy (J/K)
# replaces elements of large and small elements of array with  
# np arbitrary infinite and infitisimally small numbers
S = np.nan_to_num(S)
# ENTHALPY  
H = G + S
# Plotting

# Plotting Entropy 2D histogram
sdata = S

fig1 = plt.figure(figsize = (10.0, 10.0))
ax = sns.heatmap(sdata, cmap = 'terrain_r')
title = 'PC1/PC2 Entropy - ' + name
plt.title(title)
plt.show()
#fig1.savefig('Entr_' + sname + '.png')


# Plotting Gibbs free energy 2D histogram
gdata = G
fig1 = plt.figure(figsize = (10.0, 10.0))
ax = sns.heatmap(gdata)
title = 'PC1/PC2 Energy - '+ name
plt.title(title)
plt.show()
#fig1.savefig('Ener_' + sname + '.png')


        
    


