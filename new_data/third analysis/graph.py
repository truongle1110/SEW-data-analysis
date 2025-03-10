import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import seaborn as sns
import plotly.express as px

# Load the Excel file
file_path = 'Failure distribution plots.xlsx'
all_sheets = pd.read_excel(file_path, sheet_name=None)
sheet = ["ASCENSEUR SORTIE", "ASCENSEUR (in POSTE4)", "Ascenseur (in POSTE2)", "POSTE 15   CONTRÔLE HAUTE TENSI"]
for i in sheet:
    data = all_sheets[i]


    # component = data['Appellation']
    # failure_time_distribution = data['Time']
    unique_component =pd.Series(data['Appellation'].unique()).dropna().tolist()
    # failure_time = pd.Series(data['Time'].unique()).dropna().tolist()

    x_values = []
    y_values = []

    for idx, number in enumerate(unique_component):
        filtered_data = data[data['Appellation'] == number]
        failure_time_point = filtered_data['Time']
        x_values.extend(failure_time_point)
        y_values.extend([idx] * len(failure_time_point))  # Use index as y-value for each unique component

    # Plotting with matplotlib
    plt.figure(figsize=(10, 6))
    plt.scatter(x_values, y_values, alpha=0.7, color='blue', marker = 'x', s = 15)
    plt.yticks(ticks=range(len(unique_component)), labels=unique_component)
    plt.xlabel('Failure Time')
    plt.ylabel('Component ID')
    plt.title(i)
    plt.grid(True)
    plt.show()

# fig, ax = plt.subplots()
#plt.scatter(data_failure_time_distribution_POSTE_DE_CONTROLE, 295*np.ones(len(data_failure_time_distribution_POSTE_DE_CONTROLE)), color='blue', marker = 'x', s = 15, label = 'Failure time')

"""

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



# --------------------------------- POSTE 02 : ENTRÉE PLATEAUX PLEIN ---------------------------------
result_POSTE_02 = np.where(df1 == "POSTE 02 : ENTRÉE PLATEAUX PLEIN")
rows_POSTE_02, columns_POSTE_02 = result_POSTE_02
data_failure_time_distribution_POSTE_02 = df1.loc[rows_POSTE_02, "failure time distribution"]



# --------------------------------- POSTE 15 : CONTRÔLE HAUTE TENSION ---------------------------------
result_POSTE_15 = np.where(df1 == "POSTE 15 : CONTRÔLE HAUTE TENSION")
rows_POSTE_15, columns_POSTE_15 = result_POSTE_15
data_failure_time_distribution_POSTE_15 = df1.loc[rows_POSTE_15, "failure time distribution"]



# --------------------------------- MAGASIN PLATEAUX VIDES ---------------------------------
result_MAGASIN = np.where(df1 == "MAGASIN PLATEAUX VIDES")
rows_MAGASIN, columns_MAGASIN = result_MAGASIN
data_failure_time_distribution_MAGASIN = df1.loc[rows_MAGASIN, "failure time distribution"]




# --------------------------------- ASCENSEUR DE SORTIE ---------------------------------
result_ASCENSEUR_DE_SORTIE = np.where(df1 == "ASCENSEUR DE SORTIE")
rows_ASCENSEUR_DE_SORTIE, columns_ASCENSEUR_DE_SORTIE = result_ASCENSEUR_DE_SORTIE
data_failure_time_distribution_ASCENSEUR_DE_SORTIE = df1.loc[rows_ASCENSEUR_DE_SORTIE, "failure time distribution"]




# --------------------------------- MM-TAILLE1 ---------------------------------
result_MM = np.where(df1 == "MM-TAILLE1")
rows_MM, columns_MM = result_MM
data_failure_time_distribution_MM = df1.loc[rows_MM, "failure time distribution"]



# --------------------------------- ASCENSEUR ---------------------------------
result_ASCENSEUR = np.where(df1 == "ASCENSEUR")
rows_ASCENSEUR, columns_ASCENSEUR = result_ASCENSEUR
data_failure_time_distribution_ASCENSEUR = df1.loc[rows_ASCENSEUR, "failure time distribution"]



# --------------------------------- KTM6 ---------------------------------
result_KTM6 = np.where(df1 == "KTM6")
rows_KTM6, columns_KTM6 = result_KTM6
data_failure_time_distribution_KTM6 = df1.loc[rows_KTM6, "failure time distribution"]



# --------------------------------- PINCE ---------------------------------
result_PINCE = np.where(df1 == "PINCE")
rows_PINCE, columns_PINCE = result_PINCE
data_failure_time_distribution_PINCE = df1.loc[rows_PINCE, "failure time distribution"]



# --------------------------------- POSTE 05 : MONTAGE ENTRAINEURS ---------------------------------
result_POSTE_05 = np.where(df1 == "POSTE 05 : MONTAGE ENTRAINEURS")
rows_POSTE_05, columns_POSTE_05 = result_POSTE_05
data_failure_time_distribution_POSTE_05 = df1.loc[rows_POSTE_05, "failure time distribution"]



# --------------------------------- KTM5 ---------------------------------
result_KTM5 = np.where(df1 == "KTM5")
rows_KTM5, columns_KTM5 = result_KTM5
data_failure_time_distribution_KTM5 = df1.loc[rows_KTM5, "failure time distribution"]



# --------------------------------- EMMANCHEMENT ---------------------------------
result_EMMANCHEMENT = np.where(df1 == "EMMANCHEMENT")
rows_EMMANCHEMENT, columns_EMMANCHEMENT = result_EMMANCHEMENT
data_failure_time_distribution_EMMANCHEMENT = df1.loc[rows_EMMANCHEMENT, "failure time distribution"]



# --------------------------------- CHAUFFE VENTILATEURS ---------------------------------
result_CHAUFFE_VENTILATEURS = np.where(df1 == "CHAUFFE VENTILATEURS")
rows_CHAUFFE_VENTILATEURS, columns_CHAUFFE_VENTILATEURS = result_CHAUFFE_VENTILATEURS
data_failure_time_distribution_CHAUFFE_VENTILATEURS = df1.loc[rows_CHAUFFE_VENTILATEURS, "failure time distribution"]



# --------------------------------- ECRANS ---------------------------------
result_ECRANS = np.where(df1 == "ECRANS")
rows_ECRANS, columns_ECRANS = result_ECRANS
data_failure_time_distribution_ECRANS = df1.loc[rows_ECRANS, "failure time distribution"]



# --------------------------------- DIVERS ---------------------------------
result_DIVERS = np.where(df1 == "DIVERS")
rows_DIVERS, columns_DIVERS = result_DIVERS
data_failure_time_distribution_DIVERS = df1.loc[rows_DIVERS, "failure time distribution"]



# --------------------------------- EI7-BARRETTE ---------------------------------
result_EI7 = np.where(df1 == "EI7-BARRETTE")
rows_EI7, columns_EI7 = result_EI7
data_failure_time_distribution_EI7 = df1.loc[rows_EI7, "failure time distribution"]



# --------------------------------- POSTE 06A : MONTAGE FREINS + SERRAGE TIRANTS ---------------------------------
result_POSTE_06A = np.where(df1 == "POSTE 06A : MONTAGE FREINS + SERRAGE TIRANTS")
rows_POSTE_06A, columns_POSTE_06A = result_POSTE_06A
data_failure_time_distribution_POSTE_06A = df1.loc[rows_POSTE_06A, "failure time distribution"]



# --------------------------------- TRANSLATION ---------------------------------
result_TRANSLATION = np.where(df1 == "TRANSLATION")
rows_TRANSLATION, columns_TRANSLATION = result_TRANSLATION
data_failure_time_distribution_TRANSLATION = df1.loc[rows_TRANSLATION, "failure time distribution"]



# --------------------------------- CONVOYEUR CÔTÉ CONTRÔLE ---------------------------------
result_CONVOYEUR_COTE = np.where(df1 == "CONVOYEUR CÔTÉ CONTRÔLE")
rows_CONVOYEUR_COTE, columns_CONVOYEUR_COTE = result_CONVOYEUR_COTE
data_failure_time_distribution_CONVOYEUR_COTE = df1.loc[rows_CONVOYEUR_COTE, "failure time distribution"]



# --------------------------------- ASCENSEUR SORTIE ---------------------------------
result_ASCENSEUR_SORTIE = np.where(df1 == "ASCENSEUR SORTIE")
rows_ASCENSEUR_SORTIE, columns_ASCENSEUR_SORTIE = result_ASCENSEUR_SORTIE
data_failure_time_distribution_ASCENSEUR_SORTIE = df1.loc[rows_ASCENSEUR_SORTIE, "failure time distribution"]



# --------------------------------- VISSEUSES ÉLECTRIQUE ---------------------------------
result_VISSEUSES = np.where(df1 == "VISSEUSES ÉLECTRIQUE")
rows_VISSEUSES, columns_VISSEUSES = result_VISSEUSES
data_failure_time_distribution_VISSEUSES = df1.loc[rows_VISSEUSES, "failure time distribution"]



# --------------------------------- POSTE 07 : MONTAGE CAPOT + SOUPAPES ---------------------------------
result_POSTE_07 = np.where(df1 == "POSTE 07 : MONTAGE CAPOT + SOUPAPES")
rows_POSTE_07, columns_POSTE_07 = result_POSTE_07
data_failure_time_distribution_POSTE_07 = df1.loc[rows_POSTE_07, "failure time distribution"]


# --------------------------------- POSTE 14 : CONTRÔLE MISE Á LA TERRE ---------------------------------
result_POSTE_14 = np.where(df1 == "POSTE 14 : CONTRÔLE MISE Á LA TERRE")
rows_POSTE_14, columns_POSTE_14 = result_POSTE_14
data_failure_time_distribution_POSTE_14 = df1.loc[rows_POSTE_14, "failure time distribution"]







data_downtime_POSTE_DE_CONTROLE = df1.loc[rows_POSTE_DE_CONTROLE, "downtime"]
data_downtime_CONNECTEURS = df1.loc[rows_CONNECTEURS, "downtime"]  
data_downtime_POSTE_09 = df1.loc[rows_POSTE_09, "downtime"]
data_downtime_POSTE_04 = df1.loc[rows_POSTE_04, "downtime"]
data_downtime_CONVOYEURS = df1.loc[rows_CONVOYEURS, "downtime"] 
data_downtime_LIGNE_DE_MONTAGE_MOTG02 = df1.loc[rows_LIGNE_DE_MONTAGE_MOTG02, "downtime"]
data_downtime_POSTE_02 = df1.loc[rows_POSTE_02, "downtime"]
data_downtime_POSTE_15 = df1.loc[rows_POSTE_15, "downtime"]
data_downtime_MAGASIN = df1.loc[rows_MAGASIN, "downtime"]
data_downtime_ASCENSEUR_DE_SORTIE = df1.loc[rows_ASCENSEUR_DE_SORTIE, "downtime"]
data_downtime_MM = df1.loc[rows_MM, "downtime"]
data_downtime_ASCENSEUR = df1.loc[rows_MM, "downtime"]
data_downtime_KTM6 = df1.loc[rows_KTM6, "downtime"]
data_downtime_PINCE = df1.loc[rows_PINCE, "downtime"]
data_downtime_POSTE_05 = df1.loc[rows_POSTE_05, "downtime"]
data_downtime_KTM5 = df1.loc[rows_KTM5, "downtime"]
data_downtime_EMMANCHEMENT = df1.loc[rows_EMMANCHEMENT, "downtime"]
data_downtime_CHAUFFE_VENTILATEURS = df1.loc[rows_CHAUFFE_VENTILATEURS, "downtime"]
data_downtime_ECRANS = df1.loc[rows_ECRANS, "downtime"]
data_downtime_DIVERS = df1.loc[rows_DIVERS, "downtime"]
data_downtime_EI7 = df1.loc[rows_EI7, "downtime"]
data_downtime_POSTE_06A = df1.loc[rows_EI7, "downtime"]
data_downtime_TRANSLATION = df1.loc[rows_TRANSLATION, "downtime"]
data_downtime_CONVOYEUR_COTE = df1.loc[rows_CONVOYEUR_COTE, "downtime"]
data_downtime_ASCENSEUR_SORTIE = df1.loc[rows_ASCENSEUR_SORTIE, "downtime"]
data_downtime_VISSEUSES = df1.loc[rows_VISSEUSES, "downtime"]
data_downtime_POSTE_07 = df1.loc[rows_POSTE_07, "downtime"]
data_downtime_POSTE_14 = df1.loc[rows_POSTE_14, "downtime"]







data_POSTE_DE_CONTROLE = [(x, y) for x, y in zip(data_failure_time_distribution_POSTE_DE_CONTROLE, data_downtime_POSTE_DE_CONTROLE)]
data_CONNECTEURS = [(x, y) for x, y in zip(data_failure_time_distribution_CONNECTEURS, data_downtime_CONNECTEURS)]
data_POSTE_09 = [(x, y) for x, y in zip(data_failure_time_distribution_POSTE_09, data_downtime_POSTE_09)]
data_POSTE_04 = [(x, y) for x, y in zip(data_failure_time_distribution_POSTE_04, data_downtime_POSTE_04)]
data_CONVOYEURS = [(x, y) for x, y in zip(data_failure_time_distribution_CONVOYEURS, data_downtime_CONVOYEURS)]
data_LIGNE_DE_MONTAGE_MOTG02 = [(x, y) for x, y in zip(data_failure_time_distribution_LIGNE_DE_MONTAGE_MOTG02, data_downtime_LIGNE_DE_MONTAGE_MOTG02)]
data_POSTE_02 = [(x, y) for x, y in zip(data_failure_time_distribution_POSTE_02, data_downtime_POSTE_02)]
data_POSTE_15 = [(x, y) for x, y in zip(data_failure_time_distribution_POSTE_15, data_downtime_POSTE_15)]
data_MAGASIN = [(x, y) for x, y in zip(data_failure_time_distribution_MAGASIN, data_downtime_MAGASIN)]
data_ASCENSEUR_DE_SORTIE = [(x, y) for x, y in zip(data_failure_time_distribution_ASCENSEUR_DE_SORTIE, data_downtime_ASCENSEUR_DE_SORTIE)]
data_MM = [(x, y) for x, y in zip(data_failure_time_distribution_MM, data_downtime_MM)]
data_ASCENSEUR = [(x, y) for x, y in zip(data_failure_time_distribution_ASCENSEUR, data_downtime_ASCENSEUR)]
data_KTM6 = [(x, y) for x, y in zip(data_failure_time_distribution_KTM6, data_downtime_KTM6)]
data_PINCE = [(x, y) for x, y in zip(data_failure_time_distribution_PINCE, data_downtime_PINCE)]
data_POSTE_05 = [(x, y) for x, y in zip(data_failure_time_distribution_POSTE_05, data_downtime_POSTE_05)]
data_KTM5 = [(x, y) for x, y in zip(data_failure_time_distribution_KTM5, data_downtime_KTM5)]
data_EMMANCHEMENT = [(x, y) for x, y in zip(data_failure_time_distribution_EMMANCHEMENT, data_downtime_EMMANCHEMENT)]
data_CHAUFFE_VENTILATEURS = [(x, y) for x, y in zip(data_failure_time_distribution_CHAUFFE_VENTILATEURS, data_downtime_CHAUFFE_VENTILATEURS)]
data_ECRANS = [(x, y) for x, y in zip(data_failure_time_distribution_ECRANS, data_downtime_ECRANS)]
data_DIVERS = [(x, y) for x, y in zip(data_failure_time_distribution_DIVERS, data_downtime_DIVERS)]
data_EI7 = [(x, y) for x, y in zip(data_failure_time_distribution_EI7, data_downtime_EI7)]
data_POSTE_06A = [(x, y) for x, y in zip(data_failure_time_distribution_POSTE_06A, data_downtime_POSTE_06A)]
data_TRANSLATION = [(x, y) for x, y in zip(data_failure_time_distribution_TRANSLATION, data_downtime_TRANSLATION)]
data_CONVOYEUR_COTE = [(x, y) for x, y in zip(data_failure_time_distribution_CONVOYEUR_COTE, data_downtime_CONVOYEUR_COTE)]
data_ASCENSEUR_SORTIE = [(x, y) for x, y in zip(data_failure_time_distribution_ASCENSEUR_SORTIE, data_downtime_ASCENSEUR_SORTIE)]
data_VISSEUSES = [(x, y) for x, y in zip(data_failure_time_distribution_VISSEUSES, data_downtime_VISSEUSES)]
data_POSTE_07 = [(x, y) for x, y in zip(data_failure_time_distribution_POSTE_07, data_downtime_POSTE_07)]
data_POSTE_14 = [(x, y) for x, y in zip(data_failure_time_distribution_POSTE_14, data_downtime_POSTE_14)]
# print(data_POSTE_DE_CONTROLE)








MTBF_POSTE_DE_CONTROLE = df2.loc[np.where(df2 == "POSTE DE CONTRÔLE")[0], "80% MTBF"]
MTBF_CONNECTEURS = df2.loc[np.where(df2 == "CONNECTEURS")[0], "80% MTBF"]
MTBF_POSTE_09 = df2.loc[np.where(df2 == "POSTE 09 : MONTAGE CÔTÉ A (RETOURNEMENTS)")[0], "80% MTBF"]
MTBF_POSTE_04 = df2.loc[np.where(df2 == "POSTE 04  : EMMANCHEMENTS ROULEMENTS (PRESSE)")[0], "80% MTBF"]
MTBF_CONVOYEURS = df2.loc[np.where(df2 == "CONVOYEURS")[0], "80% MTBF"]
MTBF_LIGNE_DE_MONTAGE_MOTG02 = df2.loc[np.where(df2 == "LIGNE DE MONTAGE MOTG02")[0], "80% MTBF"]
MTBF_POSTE_02 = df2.loc[np.where(df2 == "POSTE 02 : ENTRÉE PLATEAUX PLEIN")[0], "80% MTBF"]
MTBF_POSTE_15 = df2.loc[np.where(df2 == "POSTE 15 : CONTRÔLE HAUTE TENSION")[0], "80% MTBF"]
MTBF_MAGASIN = df2.loc[np.where(df2 == "MAGASIN PLATEAUX VIDES")[0], "80% MTBF"]
MTBF_ASCENSEUR_DE_SORTIE = df2.loc[np.where(df2 == "ASCENSEUR DE SORTIE")[0], "80% MTBF"]
MTBF_MM = df2.loc[np.where(df2 == "MM-TAILLE1")[0], "80% MTBF"]
MTBF_ASCENSEUR = df2.loc[np.where(df2 == "ASCENSEUR")[0], "80% MTBF"]
MTBF_KTM6 = df2.loc[np.where(df2 == "KTM6")[0], "80% MTBF"]
MTBF_PINCE = df2.loc[np.where(df2 == "PINCE")[0], "80% MTBF"]
MTBF_POSTE_05 = df2.loc[np.where(df2 == "POSTE 05 : MONTAGE ENTRAINEURS")[0], "80% MTBF"]
MTBF_KTM5 = df2.loc[np.where(df2 == "KTM5")[0], "80% MTBF"]
MTBF_EMMANCHEMENT = df2.loc[np.where(df2 == "EMMANCHEMENT")[0], "80% MTBF"]
MTBF_CHAUFFE_VENTILATEURS = df2.loc[np.where(df2 == "CHAUFFE VENTILATEURS")[0], "80% MTBF"]
MTBF_ECRANS = df2.loc[np.where(df2 == "ECRANS")[0], "80% MTBF"]
MTBF_DIVERS = df2.loc[np.where(df2 == "DIVERS")[0], "80% MTBF"]
MTBF_EI7 = df2.loc[np.where(df2 == "EI7-BARRETTE")[0], "80% MTBF"]
MTBF_POSTE_06A = df2.loc[np.where(df2 == "POSTE 06A : MONTAGE FREINS + SERRAGE TIRANTS")[0], "80% MTBF"]
MTBF_TRANSLATION = df2.loc[np.where(df2 == "TRANSLATION")[0], "80% MTBF"]
MTBF_CONVOYEUR_COTE = df2.loc[np.where(df2 == "CONVOYEUR CÔTÉ CONTRÔLE")[0], "80% MTBF"]
MTBF_ASCENSEUR_SORTIE = df2.loc[np.where(df2 == "ASCENSEUR SORTIE")[0], "80% MTBF"]
MTBF_VISSEUSES = df2.loc[np.where(df2 == "VISSEUSES ÉLECTRIQUE")[0], "80% MTBF"]
MTBF_POSTE_07 = df2.loc[np.where(df2 == "POSTE 07 : MONTAGE CAPOT + SOUPAPES")[0], "80% MTBF"]
MTBF_POSTE_14 = df2.loc[np.where(df2 == "POSTE 14 : CONTRÔLE MISE Á LA TERRE")[0], "80% MTBF"]

print(MTBF_POSTE_DE_CONTROLE.iloc[0])







# Horizontal bar plot with gaps
fig, ax = plt.subplots()
# ax.broken_barh(data_POSTE_DE_CONTROLE, (63, 4), facecolors='blue')
# ax.broken_barh(data_CONNECTEURS, (53, 4), facecolors='blue')
# ax.broken_barh(data_POSTE_09, (43, 4), facecolors='blue')
# ax.broken_barh(data_POSTE_04, (33, 4), facecolors='blue')
# ax.broken_barh(data_CONVOYEURS, (23, 4), facecolors='blue')
# ax.broken_barh(data_LIGNE_DE_MONTAGE_MOTG02, (13, 4), facecolors='blue')
ax.set_xlim(-10, 5500)
ax.set_ylim(7, 340)
ax.set_xlabel('Time')
ax.set_ylabel('Component')
ax.set_yticks([295, 285, 275, 265, 255, 245, 235, 225, 215, 205, 195, 185, 175, 165, 155, 145, 135, 125, 115, 105, 95, 85, 75, 65, 55, 45, 35, 25], labels=['POSTE DE CONTRÔLE', 'CONNECTEURS', 'POSTE 09 : MONTAGE CÔTÉ A (RETOURNEMENTS)', 'POSTE 04  : EMMANCHEMENTS ROULEMENTS (PRESSE)', 'CONVOYEURS', 'LIGNE DE MONTAGE MOTG02', 'POSTE 02 : ENTRÉE PLATEAUX PLEIN', 'POSTE 15 : CONTRÔLE HAUTE TENSION', 'MAGASIN PLATEAUX VIDES', 'ASCENSEUR DE SORTIE', 'MM-TAILLE1', 'ASCENSEUR', 'KTM6', 'PINCE', 'POSTE 05 : MONTAGE ENTRAINEURS', 'KTM5', 'EMMANCHEMENT', 'CHAUFFE VENTILATEURS', 'ECRANS', 'DIVERS', 'EI7-BARRETTE', 'POSTE 06A : MONTAGE FREINS + SERRAGE TIRANTS', 'TRANSLATION', 'CONVOYEUR CÔTÉ CONTRÔLE', 'ASCENSEUR SORTIE', 'VISSEUSES ÉLECTRIQUE', 'POSTE 07 : MONTAGE CAPOT + SOUPAPES', 'POSTE 14 : CONTRÔLE MISE Á LA TERRE'])     # Modify y-axis tick labels

plt.scatter(data_failure_time_distribution_POSTE_DE_CONTROLE, 295*np.ones(len(data_failure_time_distribution_POSTE_DE_CONTROLE)), color='blue', marker = 'x', s = 15, label = 'Failure time')
plt.scatter(data_failure_time_distribution_CONNECTEURS, 285*np.ones(len(data_failure_time_distribution_CONNECTEURS)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_POSTE_09, 275*np.ones(len(data_failure_time_distribution_POSTE_09)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_POSTE_04, 265*np.ones(len(data_failure_time_distribution_POSTE_04)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_CONVOYEURS, 255*np.ones(len(data_failure_time_distribution_CONVOYEURS)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_LIGNE_DE_MONTAGE_MOTG02, 245*np.ones(len(data_failure_time_distribution_LIGNE_DE_MONTAGE_MOTG02)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_POSTE_02, 235*np.ones(len(data_failure_time_distribution_POSTE_02)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_POSTE_15, 225*np.ones(len(data_failure_time_distribution_POSTE_15)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_MAGASIN, 215*np.ones(len(data_failure_time_distribution_MAGASIN)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_ASCENSEUR_DE_SORTIE, 205*np.ones(len(data_failure_time_distribution_ASCENSEUR_DE_SORTIE)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_MM, 195*np.ones(len(data_failure_time_distribution_MM)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_ASCENSEUR, 185*np.ones(len(data_failure_time_distribution_ASCENSEUR)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_KTM6, 175*np.ones(len(data_failure_time_distribution_KTM6)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_PINCE, 165*np.ones(len(data_failure_time_distribution_PINCE)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_POSTE_05, 155*np.ones(len(data_failure_time_distribution_POSTE_05)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_KTM5, 145*np.ones(len(data_failure_time_distribution_KTM5)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_EMMANCHEMENT, 135*np.ones(len(data_failure_time_distribution_EMMANCHEMENT)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_CHAUFFE_VENTILATEURS, 125*np.ones(len(data_failure_time_distribution_CHAUFFE_VENTILATEURS)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_ECRANS, 115*np.ones(len(data_failure_time_distribution_ECRANS)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_DIVERS, 105*np.ones(len(data_failure_time_distribution_DIVERS)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_EI7, 95*np.ones(len(data_failure_time_distribution_EI7)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_POSTE_06A, 85*np.ones(len(data_failure_time_distribution_POSTE_06A)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_TRANSLATION, 75*np.ones(len(data_failure_time_distribution_TRANSLATION)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_CONVOYEUR_COTE, 65*np.ones(len(data_failure_time_distribution_CONVOYEUR_COTE)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_ASCENSEUR_SORTIE, 55*np.ones(len(data_failure_time_distribution_ASCENSEUR_SORTIE)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_VISSEUSES, 45*np.ones(len(data_failure_time_distribution_VISSEUSES)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_POSTE_07, 35*np.ones(len(data_failure_time_distribution_POSTE_07)), color='blue', marker = 'x', s = 15)
plt.scatter(data_failure_time_distribution_POSTE_14, 25*np.ones(len(data_failure_time_distribution_POSTE_14)), color='blue', marker = 'x', s = 15)






plt.scatter(MTBF_POSTE_DE_CONTROLE.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_POSTE_DE_CONTROLE.iloc[0]) + 1)]), 294*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_POSTE_DE_CONTROLE.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10, label = 'Nominal preventive maintenance time (80% MTBF)')
plt.scatter(MTBF_CONNECTEURS.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_CONNECTEURS.iloc[0]) + 1)]), 284*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_CONNECTEURS.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_POSTE_09.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_POSTE_09.iloc[0]) + 1)]), 274*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_POSTE_09.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_POSTE_04.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_POSTE_04.iloc[0]) + 1)]), 264*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_POSTE_04.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_CONVOYEURS.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_CONVOYEURS.iloc[0]) + 1)]), 254*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_CONVOYEURS.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_LIGNE_DE_MONTAGE_MOTG02.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_LIGNE_DE_MONTAGE_MOTG02.iloc[0]) + 1)]), 244*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_LIGNE_DE_MONTAGE_MOTG02.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_POSTE_02.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_POSTE_02.iloc[0]) + 1)]), 234*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_POSTE_02.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_POSTE_15.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_POSTE_15.iloc[0]) + 1)]), 224*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_POSTE_15.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_MAGASIN.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_MAGASIN.iloc[0]) + 1)]), 214*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_MAGASIN.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_ASCENSEUR_DE_SORTIE.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_ASCENSEUR_DE_SORTIE.iloc[0]) + 1)]), 204*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_ASCENSEUR_DE_SORTIE.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_MM.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_MM.iloc[0]) + 1)]), 194*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_MM.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_ASCENSEUR.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_ASCENSEUR.iloc[0]) + 1)]), 184*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_ASCENSEUR.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_KTM6.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_KTM6.iloc[0]) + 1)]), 174*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_KTM6.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_PINCE.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_PINCE.iloc[0]) + 1)]), 164*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_PINCE.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_POSTE_05.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_POSTE_05.iloc[0]) + 1)]), 154*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_POSTE_05.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_KTM5.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_KTM5.iloc[0]) + 1)]), 144*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_KTM5.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_EMMANCHEMENT.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_EMMANCHEMENT.iloc[0]) + 1)]), 134*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_EMMANCHEMENT.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_CHAUFFE_VENTILATEURS.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_CHAUFFE_VENTILATEURS.iloc[0]) + 1)]), 124*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_CHAUFFE_VENTILATEURS.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_ECRANS.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_ECRANS.iloc[0]) + 1)]), 114*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_ECRANS.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_DIVERS.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_DIVERS.iloc[0]) + 1)]), 104*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_DIVERS.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_EI7.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_EI7.iloc[0]) + 1)]), 94*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_EI7.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_POSTE_06A.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_POSTE_06A.iloc[0]) + 1)]), 84*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_POSTE_06A.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_TRANSLATION.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_TRANSLATION.iloc[0]) + 1)]), 74*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_TRANSLATION.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_CONVOYEUR_COTE.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_CONVOYEUR_COTE.iloc[0]) + 1)]), 64*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_CONVOYEUR_COTE.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_ASCENSEUR_SORTIE.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_ASCENSEUR_SORTIE.iloc[0]) + 1)]), 54*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_ASCENSEUR_SORTIE.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_VISSEUSES.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_VISSEUSES.iloc[0]) + 1)]), 44*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_VISSEUSES.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_POSTE_07.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_POSTE_07.iloc[0]) + 1)]), 34*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_POSTE_07.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)
plt.scatter(MTBF_POSTE_14.iloc[0]*np.array([i for i in range(1, int(5500/MTBF_POSTE_14.iloc[0]) + 1)]), 24*np.ones(len(np.array([i for i in range(1, int(5500/MTBF_POSTE_14.iloc[0]) + 1)]))), color='brown', marker = 'o', s = 10)



plt.title('Distribution of failure on each component')
ax.grid(True, linestyle=':')                                       # Make grid lines visible
plt.legend(loc='upper right')
plt.show()

"""