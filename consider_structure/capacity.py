class Component:
    def __init__(self, capacity):
        self.capacity = capacity

class SeriesStructure:
    def __init__(self, components):
        self.components = components
    
    def max_capacity(self):
        # In a series structure, the system capacity is limited by the weakest component
        return min(component.capacity for component in self.components)

class ParallelStructure:
    def __init__(self, components):
        self.components = components
    
    def max_capacity(self):
        # In a parallel structure, the system capacity is the sum of the components' capacities
        return sum(component.capacity for component in self.components)

class SeriesParallelSystem:
    def __init__(self, structures):
        self.structures = structures
    
    def max_capacity(self):
        # For a series-parallel system, the system capacity is limited by the weakest series part
        return min(structure.max_capacity() for structure in self.structures)

# Example usage:

# Define components with their capacities
component1 = Component(50)
component2 = Component(40)
component3 = Component(30)
component4 = Component(60)
component5 = Component(70)

# Define series and parallel structures
# Example: A series structure made up of components 1 and 2
series1 = SeriesStructure([component1, component2])

# Example: A parallel structure made up of components 3, 4, and 5
parallel1 = ParallelStructure([component3, component4, component5])

# Define the overall series-parallel system
# For example, combining series1 and parallel1 in series
system = SeriesParallelSystem([series1, parallel1])

# Calculate the maximum capacity of the system
max_capacity = system.max_capacity()
print(f"The maximum capacity of the series-parallel system is: {max_capacity}")
