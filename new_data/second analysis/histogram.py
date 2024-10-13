import matplotlib.pyplot as plt

# Example data points
data = [1.0, 1.5, 2.1, 2.5, 3.0, 4.2, 5.0, 5.5, 6.0]

# Create a normalized histogram
plt.hist(data, bins=10, density=True, alpha=0.6, color='g')

# Show the plot
plt.show()