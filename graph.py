import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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
# print(failure_time_distribution)
# print(type(failure_time_distribution))
# print(failure_time_distribution.shape)


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
print(len(data_failure_time_distribution_POSTE_04))

# --------------------------------- CONVOYEURS ---------------------------------
result_CONVOYEURS = np.where(df == "CONVOYEURS")
rows_CONVOYEURS, columns_CONVOYEURS = result_CONVOYEURS
data_failure_time_distribution_CONVOYEURS = df.loc[rows_CONVOYEURS, "failure time distribution"] 


# --------------------------------- LIGNE DE MONTAGE MOTG02 ---------------------------------
result_LIGNE_DE_MONTAGE_MOTG02 = np.where(df == "LIGNE DE MONTAGE MOTG02")
rows_LIGNE_DE_MONTAGE_MOTG02, columns_LIGNE_DE_MONTAGE_MOTG02 = result_LIGNE_DE_MONTAGE_MOTG02
data_failure_time_distribution_LIGNE_DE_MONTAGE_MOTG02 = df.loc[rows_LIGNE_DE_MONTAGE_MOTG02, "failure time distribution"]


# Creating the one-dimensional strip plot











# Creating the one-dimensional scatter plot
plt.figure(figsize=(10, 1))  # Setting the figure size to emphasize the one-dimensionality
plt.scatter(data_failure_time_distribution_POSTE_09, np.zeros_like(data_failure_time_distribution_POSTE_09), color='blue', marker='x')  # Scatter plot along one axis
plt.yticks([])  # Hide y-axis ticks
plt.gca().axes.get_yaxis().set_visible(False)  # Hide the y-axis
plt.title('Failure Time Distribution of POSTE DE CONTRÔLE')
plt.xlabel('Data Points')
plt.show()



    



