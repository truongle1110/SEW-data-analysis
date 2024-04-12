import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Load the Excel file
file_path = 'failure time distribution.xlsx'  # Replace 'path_to_your_file.xlsx' with the actual path to your file
data = pd.read_excel(file_path)

component = data['component']
failure_time_distribution = data['failure time distribution']


result = np.where(data == "POSTE DE CONTRÔLE")
print(result)
rows, columns = result
print(rows)
print(columns)

print(data.iloc[result])
    



