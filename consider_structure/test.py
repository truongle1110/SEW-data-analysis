class Component:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.is_critical = False

class SeriesStructure:
    def __init__(self, components):
        self.components = components
    
    def determine_criticality(self):
        # In a series structure, all components are critical
        for component in self.components:
            component.is_critical = True

    def is_operational(self):
        # Series structure fails if any component fails
        return all(not component.is_critical for component in self.components)

class ParallelStructure:
    def __init__(self, components):
        self.components = components
    
    def determine_criticality(self):
        # In a parallel structure, no individual component is critical unless there is only one component
        if len(self.components) == 1:
            # If only one component exists, it is critical
            self.components[0].is_critical = True
        else:
            # Multiple components in parallel are not critical individually
            for component in self.components:
                component.is_critical = False

    def is_operational(self):
        # Parallel structure is operational as long as at least one component is operational
        return any(not component.is_critical for component in self.components)

class ComplexSystem:
    def __init__(self, structures):
        self.structures = structures
    
    def determine_system_criticality(self):
        """
        For a complex system that is a combination of series and parallel structures,
        determine the criticality of each component by assessing the role it plays in system failure.
        """
        for structure in self.structures:
            structure.determine_criticality()
    
    def list_critical_components(self):
        """
        List all critical components in the system.
        """
        criticals = []
        for structure in self.structures:
            for component in structure.components:
                if component.is_critical:
                    criticals.append(component.name)
        return criticals

# Example Usage:

# Define components with their capacities
component1 = Component("Component 1", 50)
component2 = Component("Component 2", 40)
component3 = Component("Component 3", 30)
component4 = Component("Component 4", 60)

# Define series structure for Component 1 and Component 2
series_structure_1_2 = SeriesStructure([component1, component2])

# Define parallel structure with the series structure (Component 1, Component 2) and Component 3, Component 4
parallel_structure_with_series = ParallelStructure([series_structure_1_2, component3, component4])

# Define the overall complex system
complex_system = ComplexSystem([parallel_structure_with_series])

# Determine the criticality of all components in the system
complex_system.determine_system_criticality()

# List critical components
critical_components = complex_system.list_critical_components()

# Display the critical components
print("Critical components in the system:")
for component in critical_components:
    print(component)