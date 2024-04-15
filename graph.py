import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px

# Load the Excel file
file_path = 'failure time distribution.xlsx'  # Replace 'path_to_your_file.xlsx' with the actual path to your file
df = pd.read_excel(file_path)

component = df['component']
failure_time_distribution = df['failure time distribution']
downtime = df['downtime']
# print(component)
# print(failure_time_distribution)
# print(downtime)


# --------------------------------- POSTE DE CONTRÔLE ---------------------------------
result_POSTE_DE_CONTROLE = np.where(df == "POSTE DE CONTRÔLE")
# print(result)     # return the index of POSTE DE CONTRÔLE in df (tuple)

rows_POSTE_DE_CONTROLE, columns_POSTE_DE_CONTROLE = result_POSTE_DE_CONTROLE
# print(rows)			# return the index of rows of POSTE DE CONTRÔLE (numpy.ndarray)
# print(columns)		# return the index of columns of POSTE DE CONTRÔLE (numpy.ndarray)

data_failure_time_distribution_POSTE_DE_CONTROLE = df.loc[rows_POSTE_DE_CONTROLE, "failure time distribution"] # pandas.core.series.Series
# print(data_failure_time_distribution_POSTE_DE_CONTROLE)
# print(type(data_failure_time_distribution_POSTE_DE_CONTROLE))
# print(data_failure_time_distribution_POSTE_DE_CONTROLE.shape)



# --------------------------------- CONNECTEURS ---------------------------------
result_CONNECTEURS = np.where(df == "CONNECTEURS")
rows_CONNECTEURS, columns_CONNECTEURS = result_CONNECTEURS
data_failure_time_distribution_CONNECTEURS = df.loc[rows_CONNECTEURS, "failure time distribution"] 



# --------------------------------- POSTE 09 : MONTAGE CÔTÉ A (RETOURNEMENTS) ---------------------------------
result_POSTE_09 = np.where(df == "POSTE 09 : MONTAGE CÔTÉ A (RETOURNEMENTS)")
rows_POSTE_09, columns_POSTE_09 = result_POSTE_09
data_failure_time_distribution_POSTE_09 = df.loc[rows_POSTE_09, "failure time distribution"]



# --------------------------------- POSTE 04  : EMMANCHEMENTS ROULEMENTS (PRESSE) ---------------------------------
result_POSTE_04 = np.where(df == "POSTE 04  : EMMANCHEMENTS ROULEMENTS (PRESSE)")
rows_POSTE_04, columns_POSTE_04 = result_POSTE_04
data_failure_time_distribution_POSTE_04 = df.loc[rows_POSTE_04, "failure time distribution"]



# --------------------------------- CONVOYEURS ---------------------------------
result_CONVOYEURS = np.where(df == "CONVOYEURS")
rows_CONVOYEURS, columns_CONVOYEURS = result_CONVOYEURS
data_failure_time_distribution_CONVOYEURS = df.loc[rows_CONVOYEURS, "failure time distribution"] 



# --------------------------------- LIGNE DE MONTAGE MOTG02 ---------------------------------
result_LIGNE_DE_MONTAGE_MOTG02 = np.where(df == "LIGNE DE MONTAGE MOTG02")
rows_LIGNE_DE_MONTAGE_MOTG02, columns_LIGNE_DE_MONTAGE_MOTG02 = result_LIGNE_DE_MONTAGE_MOTG02
data_failure_time_distribution_LIGNE_DE_MONTAGE_MOTG02 = df.loc[rows_LIGNE_DE_MONTAGE_MOTG02, "failure time distribution"]
# print(len(data_failure_time_distribution_LIGNE_DE_MONTAGE_MOTG02))



# Creating the one-dimensional strip plot
x_label = [data_failure_time_distribution_POSTE_DE_CONTROLE, data_failure_time_distribution_CONNECTEURS, data_failure_time_distribution_POSTE_09, data_failure_time_distribution_POSTE_04, data_failure_time_distribution_CONVOYEURS, data_failure_time_distribution_LIGNE_DE_MONTAGE_MOTG02]
y_label = ['POSTE DE CONTRÔLE', 'CONNECTEURS', 'POSTE 09 : MONTAGE CÔTÉ A (RETOURNEMENTS)', 'POSTE 04  : EMMANCHEMENTS ROULEMENTS (PRESSE)', 'CONVOYEURS', 'LIGNE DE MONTAGE MOTG02']
length_y = [len(data_failure_time_distribution_POSTE_DE_CONTROLE), len(data_failure_time_distribution_CONNECTEURS), len(data_failure_time_distribution_POSTE_09), len(data_failure_time_distribution_POSTE_04), len(data_failure_time_distribution_CONVOYEURS), len(data_failure_time_distribution_LIGNE_DE_MONTAGE_MOTG02)]
data = {
	'x_label': np.concatenate(x_label),
	'y_label': np.repeat(y_label, length_y)
}
plt.figure(figsize=(20, 6))
sns.stripplot(x='x_label', y='y_label', data=data, jitter=False, color='red', size=4)
plt.title('Distribution of Failure on Each Component')
plt.xlabel('Time')
plt.ylabel('Component')
plt.xlim(-10, 6000)
# plt.show()




data_downtime_POSTE_DE_CONTROLE = df.loc[rows_POSTE_DE_CONTROLE, "downtime"]
data_downtime_CONNECTEURS = df.loc[rows_CONNECTEURS, "downtime"]  
data_downtime_POSTE_09 = df.loc[rows_POSTE_09, "downtime"]
data_downtime_POSTE_04 = df.loc[rows_POSTE_04, "downtime"]
data_downtime_CONVOYEURS = df.loc[rows_CONVOYEURS, "downtime"] 
data_downtime_LIGNE_DE_MONTAGE_MOTG02 = df.loc[rows_LIGNE_DE_MONTAGE_MOTG02, "downtime"]


data_POSTE_DE_CONTROLE = [(x, y) for x, y in zip(data_failure_time_distribution_POSTE_DE_CONTROLE, data_downtime_POSTE_DE_CONTROLE)]
data_CONNECTEURS = [(x, y) for x, y in zip(data_failure_time_distribution_CONNECTEURS, data_downtime_CONNECTEURS)]
data_POSTE_09 = [(x, y) for x, y in zip(data_failure_time_distribution_POSTE_09, data_downtime_POSTE_09)]
data_POSTE_04 = [(x, y) for x, y in zip(data_failure_time_distribution_POSTE_04, data_downtime_POSTE_04)]
data_CONVOYEURS = [(x, y) for x, y in zip(data_failure_time_distribution_CONVOYEURS, data_downtime_CONVOYEURS)]
data_LIGNE_DE_MONTAGE_MOTG02 = [(x, y) for x, y in zip(data_failure_time_distribution_LIGNE_DE_MONTAGE_MOTG02, data_downtime_LIGNE_DE_MONTAGE_MOTG02)]
# print(data_POSTE_DE_CONTROLE)



# Horizontal bar plot with gaps
fig, ax = plt.subplots()
ax.broken_barh(data_POSTE_DE_CONTROLE, (63, 4), facecolors='tab:blue')
ax.broken_barh(data_CONNECTEURS, (53, 4), facecolors='tab:green')
ax.broken_barh(data_POSTE_09, (43, 4), facecolors='tab:orange')
ax.broken_barh(data_POSTE_04, (33, 4), facecolors='tab:red')
ax.broken_barh(data_CONVOYEURS, (23, 4), facecolors='black')
ax.broken_barh(data_LIGNE_DE_MONTAGE_MOTG02, (13, 4), facecolors='tab:pink')
ax.set_xlim(-100, 5500)
ax.set_ylim(0, 70)
ax.set_xlabel('Time')
ax.set_ylabel('Component')
ax.set_yticks([65, 55, 45, 35, 25, 15], labels=['POSTE DE CONTRÔLE', 'CONNECTEURS', 'POSTE 09 : MONTAGE CÔTÉ A (RETOURNEMENTS)', 'POSTE 04  : EMMANCHEMENTS ROULEMENTS (PRESSE)', 'CONVOYEURS', 'LIGNE DE MONTAGE MOTG02'])     # Modify y-axis tick labels
ax.grid(True)                                       # Make grid lines visible
plt.show()
