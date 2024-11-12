import matplotlib.pyplot as plt
import numpy as np

# Sample data
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(5, 1, 1000)
data3 = np.random.normal(-3, 1.5, 1000)

# Define number of bins
bins = 30

# Plot multiple histograms in the same figure
plt.figure(figsize=(10, 6))

# First histogram
plt.hist(data1, bins=bins, alpha=0.5, label='Data 1')

# Second histogram
plt.hist(data2, bins=bins, alpha=0.5, label='Data 2')

# Third histogram
plt.hist(data3, bins=bins, alpha=0.5, label='Data 3')

# Adding titles and labels
plt.title('Multiple Histograms')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

# Display the plot
plt.show()