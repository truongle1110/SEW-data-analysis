class Component:
    def __init__(self, name, capacity):
        """
        Initialize a component with a name and capacity.
        :param name: Name of the component.
        :param capacity: Capacity of the component.
        """
        self.name = name
        self.capacity = capacity
        self.is_critical = False

class SeriesStructure:
    def __init__(self, components):
        """
        Initialize a series structure with components.
        :param components: List of Component or Structure objects.
        """
        self.components = components
    
    def determine_criticality(self):
        """
        In a series structure, all components are critical, unless nested in a parallel structure.
        """
        for component in self.components:
            component.is_critical = True
    
    def max_capacity(self):
        """
        In a series structure, the maximum capacity is limited by the component with the smallest capacity.
        :return: Maximum capacity of the series structure.
        """
        return min(component.max_capacity() if isinstance(component, (SeriesStructure, ParallelStructure)) else component.capacity for component in self.components)

class ParallelStructure:
    def __init__(self, components):
        """
        Initialize a parallel structure with components.
        :param components: List of Component or Structure objects.
        """
        self.components = components
    
    def determine_criticality(self):
        """
        In a parallel structure, no single component is critical unless it is the only one.
        """
        if len(self.components) == 1:
            self.components[0].is_critical = True
        else:
            for component in self.components:
                component.is_critical = False
    
    def max_capacity(self):
        """
        In a parallel structure, the maximum capacity is the sum of the capacities of all components.
        :return: Maximum capacity of the parallel structure.
        """
        return min(component.max_capacity() if isinstance(component, (SeriesStructure, ParallelStructure)) else component.capacity for component in self.components)

class ComplexSystem:
    def __init__(self, structures):
        """
        Initialize a complex system consisting of multiple structures.
        :param structures: List of SeriesStructure or ParallelStructure objects.
        """
        self.structures = structures
    
    def determine_system_criticality(self):
        """
        Determine the criticality of each component in the system.
        """
        for structure in self.structures:
            structure.determine_criticality()
    
    def list_critical_components(self):
        """
        List all critical components in the system.
        :return: List of names of critical components.
        """
        criticals = []
        for structure in self.structures:
            for component in structure.components:
                if component.is_critical:
                    criticals.append(component.name)
        return criticals
    
    def max_capacity(self):
        """
        Calculate the maximum capacity of the entire system.
        The system's maximum capacity is limited by the weakest series structure.
        :return: Maximum capacity of the system.
        """
        return min(structure.max_capacity() for structure in self.structures)

# Example usage:

# Define components with their capacities
component1 = Component("Component 1", 50)
component2 = Component("Component 2", 40)
component3 = Component("Component 3", 60)
component4 = Component("Component 4", 80)
component5 = Component("Component 5", 70)

# Step 1: Series of component 2 and 3
series_2_3 = SeriesStructure([component2, component3])

# Step 2: Parallel of (series 2 3) with component 4 and component 5
parallel_4_5 = ParallelStructure([component4, component5])
parallel_2_3_4_5 = ParallelStructure([series_2_3, parallel_4_5])

# Step 3: Series of component 1 with the whole subsystem (2, 3, 4, 5)
series_1 = SeriesStructure([component1])

# Now, define the overall system
complex_system = ComplexSystem([series_1, parallel_2_3_4_5])

# Determine the criticality of all components in the system
complex_system.determine_system_criticality()

# List critical components
critical_components = complex_system.list_critical_components()

# Find the maximum capacity of the system
max_capacity = complex_system.max_capacity()

# Display results
print("Critical components in the system:")
for component in critical_components:
    print(component)

print(f"\nThe maximum capacity of the system is: {max_capacity}")
