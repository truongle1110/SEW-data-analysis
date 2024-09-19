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
component6 = Component(50)
component7 = Component(40)
component8 = Component(30)
component9 = Component(60)
component10 = Component(70)

# Define series and parallel structures
series_12 = SeriesStructure([component1, component2])
parallel_1234 = ParallelStructure([series_12, component3, component4])
parallel_67 = ParallelStructure([component6, component7])
series_567 = SeriesStructure([component5, parallel_67])
parallel_5678 = ParallelStructure([series_567, component8])

# Define the overall series-parallel system
system = SeriesParallelSystem([parallel_1234])

# Calculate the maximum capacity of the system
max_capacity = system.max_capacity()
print(f"The maximum capacity of the series-parallel system is: {max_capacity}")