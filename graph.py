import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load the Excel file
file_path = 'failure time distribution.xlsx'  # Replace 'path_to_your_file.xlsx' with the actual path to your file
df = pd.read_excel(file_path)

component = df['component']
failure_time_distribution = df['failure time distribution']
# print(component)
# print(failure_time_distribution)


# --------------------------------- POSTE DE CONTRÔLE ---------------------------------
result_POSTE_DE_CONTROLE = np.where(df == "POSTE DE CONTRÔLE")
# print(result)     # return the index of POSTE DE CONTRÔLE in df (tuple)

rows_POSTE_DE_CONTROLE, columns_POSTE_DE_CONTROLE = result_POSTE_DE_CONTROLE
# print(rows)			# return the index of rows of POSTE DE CONTRÔLE (numpy.ndarray)
# print(columns)		# return the index of columns of POSTE DE CONTRÔLE (numpy.ndarray)

data_failure_time_distribution_POSTE_DE_CONTROLE = df.loc[rows_POSTE_DE_CONTROLE, "failure time distribution"] # pandas.core.series.Series
print(failure_time_distribution)
print(type(failure_time_distribution))
print(failure_time_distribution.shape)


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

plt.show()