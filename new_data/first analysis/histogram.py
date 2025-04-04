import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# # Load the Excel file
# file_path = 'Failure distribution.xlsx'  # replace with your actual file path
# data = pd.read_excel(file_path)

# component = data['Libellé parc']

# result_POSTE_09 = np.where(data == "POSTE 09 : MONTAGE CÔTÉ A (RETOURNEMENTS)")
# rows_POSTE_09, columns_POSTE_09 = result_POSTE_09
# data_failure_time_distribution_POSTE_09 = data.loc[rows_POSTE_09, "Failure time point"]

# print(data_failure_time_distribution_POSTE_09)



# Load the Excel file
file_path = 'Failure distribution.xlsx'  # replace with your actual file path
all_sheets = pd.read_excel(file_path, sheet_name=None)
data = all_sheets['LIGNE DE MONTAGE MOTG01']
# print(data)
# Filter the rows where Column C has the specific value
filtered_data = data[data['Libellé parc'] == 'POSTE 04  : EMMANCHEMENTS ROULEMENTS (PRESSE)']

# Extract the corresponding values from Column E
failure_time_point = filtered_data['Failure time point']

# Display the extracted values
print(failure_time_point)

# Fit a normal distribution to the data
mu, std = norm.fit(failure_time_point)

# Plot the histogram and the PDF
plt.hist(failure_time_point, bins=10, density=True, alpha=0.7, color='g')
plt.title('POSTE 04  : EMMANCHEMENTS ROULEMENTS (PRESSE) histogram')
plt.show()

