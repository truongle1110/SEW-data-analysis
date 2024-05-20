import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the Excel file
file_path_1 = 'failure time distribution.xlsx'
df1 = pd.read_excel(file_path_1)

# Components list
components = [
    "POSTE DE CONTRÔLE",
    "CONNECTEURS",
    "POSTE 09 : MONTAGE CÔTÉ A (RETOURNEMENTS)",
    "POSTE 04  : EMMANCHEMENTS ROULEMENTS",
    "CONVOYEURS",
    "LIGNE DE MONTAGE MOTG02"
]

# Plotting failure time distribution for each component
plt.figure(figsize=(10, 8))
for i, component in enumerate(components, start=1):
    data_failure_time_distribution = df1[df1['component'] == component]['failure time distribution']
    plt.scatter(
        data_failure_time_distribution, 
        np.full(len(data_failure_time_distribution), i * 10), 
        label=component, 
        marker='x'
    )

plt.title('Distribution of failure on each component')
plt.xlabel('Failure Time Distribution')
plt.ylabel('Component')
plt.yticks(ticks=[i * 10 for i in range(1, len(components) + 1)], labels=components)
plt.grid(True, linestyle=':')
plt.legend(loc='upper right')
plt.show()