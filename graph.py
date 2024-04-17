import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import seaborn as sns
import plotly.express as px

# Load the Excel file
file_path_1 = 'failure time distribution.xlsx'
df1 = pd.read_excel(file_path_1)

file_path_2 = 'MTBF.xlsx'
df2 = pd.read_excel(file_path_2)

component = df1['component']
failure_time_distribution = df1['failure time distribution']
downtime = df1['downtime']
# print(component)
# print(failure_time_distribution)
# print(downtime)


# --------------------------------- POSTE DE CONTRÔLE ---------------------------------
result_POSTE_DE_CONTROLE = np.where(df1 == "POSTE DE CONTRÔLE")
# print(result_POSTE_DE_CONTROLE)     # return the index of POSTE DE CONTRÔLE in df1 (tuple)

rows_POSTE_DE_CONTROLE, columns_POSTE_DE_CONTROLE = result_POSTE_DE_CONTROLE
# print(rows)			# return the index of rows of POSTE DE CONTRÔLE (numpy.ndarray)
# print(columns)		# return the index of columns of POSTE DE CONTRÔLE (numpy.ndarray)

data_failure_time_distribution_POSTE_DE_CONTROLE = df1.loc[rows_POSTE_DE_CONTROLE, "failure time distribution"] # pandas.core.series.Series
# print(data_failure_time_distribution_POSTE_DE_CONTROLE)
# print(type(data_failure_time_distribution_POSTE_DE_CONTROLE))
# print(data_failure_time_distribution_POSTE_DE_CONTROLE.shape)



# --------------------------------- CONNECTEURS ---------------------------------
result_CONNECTEURS = np.where(df1 == "CONNECTEURS")
rows_CONNECTEURS, columns_CONNECTEURS = result_CONNECTEURS
data_failure_time_distribution_CONNECTEURS = df1.loc[rows_CONNECTEURS, "failure time distribution"] 



# --------------------------------- POSTE 09 : MONTAGE CÔTÉ A (RETOURNEMENTS) ---------------------------------
result_POSTE_09 = np.where(df1 == "POSTE 09 : MONTAGE CÔTÉ A (RETOURNEMENTS)")
rows_POSTE_09, columns_POSTE_09 = result_POSTE_09
data_failure_time_distribution_POSTE_09 = df1.loc[rows_POSTE_09, "failure time distribution"]



# --------------------------------- POSTE 04  : EMMANCHEMENTS ROULEMENTS (PRESSE) ---------------------------------
result_POSTE_04 = np.where(df1 == "POSTE 04  : EMMANCHEMENTS ROULEMENTS (PRESSE)")
rows_POSTE_04, columns_POSTE_04 = result_POSTE_04
data_failure_time_distribution_POSTE_04 = df1.loc[rows_POSTE_04, "failure time distribution"]



# --------------------------------- CONVOYEURS ---------------------------------
result_CONVOYEURS = np.where(df1 == "CONVOYEURS")
rows_CONVOYEURS, columns_CONVOYEURS = result_CONVOYEURS
data_failure_time_distribution_CONVOYEURS = df1.loc[rows_CONVOYEURS, "failure time distribution"] 



# --------------------------------- LIGNE DE MONTAGE MOTG02 ---------------------------------
result_LIGNE_DE_MONTAGE_MOTG02 = np.where(df1 == "LIGNE DE MONTAGE MOTG02")
rows_LIGNE_DE_MONTAGE_MOTG02, columns_LIGNE_DE_MONTAGE_MOTG02 = result_LIGNE_DE_MONTAGE_MOTG02
data_failure_time_distribution_LIGNE_DE_MONTAGE_MOTG02 = df1.loc[rows_LIGNE_DE_MONTAGE_MOTG02, "failure time distribution"]
# print(len(data_failure_time_distribution_LIGNE_DE_MONTAGE_MOTG02))



# # Creating the one-dimensional strip plot
# x_label = [data_failure_time_distribution_POSTE_DE_CONTROLE, data_failure_time_distribution_CONNECTEURS, data_failure_time_distribution_POSTE_09, data_failure_time_distribution_POSTE_04, data_failure_time_distribution_CONVOYEURS, data_failure_time_distribution_LIGNE_DE_MONTAGE_MOTG02]
# y_label = ['POSTE DE CONTRÔLE', 'CONNECTEURS', 'POSTE 09 : MONTAGE CÔTÉ A (RETOURNEMENTS)', 'POSTE 04  : EMMANCHEMENTS ROULEMENTS (PRESSE)', 'CONVOYEURS', 'LIGNE DE MONTAGE MOTG02']
# length_y = [len(data_failure_time_distribution_POSTE_DE_CONTROLE), len(data_failure_time_distribution_CONNECTEURS), len(data_failure_time_distribution_POSTE_09), len(data_failure_time_distribution_POSTE_04), len(data_failure_time_distribution_CONVOYEURS), len(data_failure_time_distribution_LIGNE_DE_MONTAGE_MOTG02)]
# data = {
# 	'x_label': np.concatenate(x_label),
# 	'y_label': np.repeat(y_label, length_y)
# }
# plt.figure(figsize=(20, 6))
# sns.stripplot(x='x_label', y='y_label', data=data, jitter=False, color='red', size=4)
# plt.title('Distribution of Failure on Each Component')
# plt.xlabel('Time')
# plt.ylabel('Component')
# plt.xlim(-10, 6000)
# # plt.show()




data_downtime_POSTE_DE_CONTROLE = df1.loc[rows_POSTE_DE_CONTROLE, "downtime"]
data_downtime_CONNECTEURS = df1.loc[rows_CONNECTEURS, "downtime"]  
data_downtime_POSTE_09 = df1.loc[rows_POSTE_09, "downtime"]
data_downtime_POSTE_04 = df1.loc[rows_POSTE_04, "downtime"]
data_downtime_CONVOYEURS = df1.loc[rows_CONVOYEURS, "downtime"] 
data_downtime_LIGNE_DE_MONTAGE_MOTG02 = df1.loc[rows_LIGNE_DE_MONTAGE_MOTG02, "downtime"]


data_POSTE_DE_CONTROLE = [(x, y) for x, y in zip(data_failure_time_distribution_POSTE_DE_CONTROLE, data_downtime_POSTE_DE_CONTROLE)]
data_CONNECTEURS = [(x, y) for x, y in zip(data_failure_time_distribution_CONNECTEURS, data_downtime_CONNECTEURS)]
data_POSTE_09 = [(x, y) for x, y in zip(data_failure_time_distribution_POSTE_09, data_downtime_POSTE_09)]
data_POSTE_04 = [(x, y) for x, y in zip(data_failure_time_distribution_POSTE_04, data_downtime_POSTE_04)]
data_CONVOYEURS = [(x, y) for x, y in zip(data_failure_time_distribution_CONVOYEURS, data_downtime_CONVOYEURS)]
data_LIGNE_DE_MONTAGE_MOTG02 = [(x, y) for x, y in zip(data_failure_time_distribution_LIGNE_DE_MONTAGE_MOTG02, data_downtime_LIGNE_DE_MONTAGE_MOTG02)]
# print(data_POSTE_DE_CONTROLE)



MTBF_POSTE_DE_CONTROLE = df2.loc[np.where(df2 == "POSTE DE CONTRÔLE")[0], "90% MTBF"]
MTBF_CONNECTEURS = df2.loc[np.where(df2 == "CONNECTEURS")[0], "90% MTBF"]
MTBF_POSTE_09 = df2.loc[np.where(df2 == "POSTE 09 : MONTAGE CÔTÉ A (RETOURNEMENTS)")[0], "90% MTBF"]
MTBF_POSTE_04 = df2.loc[np.where(df2 == "POSTE 04  : EMMANCHEMENTS ROULEMENTS (PRESSE)")[0], "90% MTBF"]
MTBF_CONVOYEURS = df2.loc[np.where(df2 == "CONVOYEURS")[0], "90% MTBF"]
MTBF_LIGNE_DE_MONTAGE_MOTG02 = df2.loc[np.where(df2 == "LIGNE DE MONTAGE MOTG02")[0], "90% MTBF"]
# print(MTBF_POSTE_DE_CONTROLE)



# Horizontal bar plot with gaps
fig, ax = plt.subplots()
ax.broken_barh(data_POSTE_DE_CONTROLE, (63, 4), facecolors='blue')
ax.broken_barh(data_CONNECTEURS, (53, 4), facecolors='green')
ax.broken_barh(data_POSTE_09, (43, 4), facecolors='orange')
ax.broken_barh(data_POSTE_04, (33, 4), facecolors='red')
ax.broken_barh(data_CONVOYEURS, (23, 4), facecolors='black')
ax.broken_barh(data_LIGNE_DE_MONTAGE_MOTG02, (13, 4), facecolors='purple')
ax.set_xlim(-100, 5500)
ax.set_ylim(7, 75)
ax.set_xlabel('Time')
ax.set_ylabel('Component')
ax.set_yticks([65, 55, 45, 35, 25, 15], labels=['POSTE DE CONTRÔLE', 'CONNECTEURS', 'POSTE 09 : MONTAGE CÔTÉ A (RETOURNEMENTS)', 'POSTE 04  : EMMANCHEMENTS ROULEMENTS (PRESSE)', 'CONVOYEURS', 'LIGNE DE MONTAGE MOTG02'])     # Modify y-axis tick labels

plt.scatter(data_failure_time_distribution_POSTE_DE_CONTROLE, 65*np.ones(len(data_failure_time_distribution_POSTE_DE_CONTROLE)), color='blue', marker = 'x', s = 15, label = 'Failure time')
plt.scatter(data_failure_time_distribution_CONNECTEURS, 55*np.ones(len(data_failure_time_distribution_CONNECTEURS)), color='green', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_POSTE_09, 45*np.ones(len(data_failure_time_distribution_POSTE_09)), color='orange', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_POSTE_04, 35*np.ones(len(data_failure_time_distribution_POSTE_04)), color='red', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_CONVOYEURS, 25*np.ones(len(data_failure_time_distribution_CONVOYEURS)), color='black', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_LIGNE_DE_MONTAGE_MOTG02, 15*np.ones(len(data_failure_time_distribution_LIGNE_DE_MONTAGE_MOTG02)), color='purple', marker = 'x', s = 15)

plt.scatter(int(MTBF_POSTE_DE_CONTROLE)*np.array([i for i in range(1, int(5500/MTBF_POSTE_DE_CONTROLE) + 1)]), 64*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_POSTE_DE_CONTROLE) + 1)]))), color='brown', marker = 'o', s = 10, label = 'Estimated repair time')
plt.scatter(int(MTBF_CONNECTEURS)*np.array([i for i in range(1, int(5500/MTBF_CONNECTEURS) + 1)]), 54*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_CONNECTEURS) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(int(MTBF_POSTE_09)*np.array([i for i in range(1, int(5500/MTBF_POSTE_09) + 1)]), 44*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_POSTE_09) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(int(MTBF_POSTE_04)*np.array([i for i in range(1, int(5500/MTBF_POSTE_04) + 1)]), 34*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_POSTE_04) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(int(MTBF_CONVOYEURS)*np.array([i for i in range(1, int(5500/MTBF_CONVOYEURS) + 1)]), 24*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_CONVOYEURS) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(int(MTBF_LIGNE_DE_MONTAGE_MOTG02)*np.array([i for i in range(1, int(5500/MTBF_LIGNE_DE_MONTAGE_MOTG02) + 1)]), 14*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_LIGNE_DE_MONTAGE_MOTG02) + 1)]))), color='brown', marker = 'o', s = 10)

plt.title('Distribution of Failure on Each Component and estimated repair time')
ax.grid(True, linestyle=':')                                       # Make grid lines visible
plt.legend(loc='upper right')
plt.show()

