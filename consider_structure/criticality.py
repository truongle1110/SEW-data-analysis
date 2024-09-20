class Component:
    def __init__(self, name):
        self.name = name
        self.is_critical = False

class SeriesStructure:
    def __init__(self, components):
        self.components = components
    
    def determine_criticality(self):
        # In a series structure, all components are critical
        for component in self.components:
            component.is_critical = True

class ParallelStructure:
    def __init__(self, components):
        self.components = components
    
    def determine_criticality(self):
        # In a parallel structure, no single component is critical unless it is the only one
        if len(self.components) == 1:
            self.components[0].is_critical = True
        else:
            for component in self.components:
                component.is_critical = False

class ComplexSystem:
    def __init__(self, structures):
        self.structures = structures
    
    def determine_system_criticality(self):
        # Iterate through all the structures and determine the criticality of components
        for structure in self.structures:
            structure.determine_criticality()
    
    def list_critical_components(self):
        criticals = []
        for structure in self.structures:
            for component in structure.components:
                if component.is_critical:
                    criticals.append(component.name)
        return criticals

# Defining the components in the system
component1 = Component("Component 1")
component2 = Component("Component 2")
component3 = Component("Component 3")
component4 = Component("Component 4")
component5 = Component("Component 5")
component6 = Component("Component 6")
component7 = Component("Component 7")
component8 = Component("Component 8")
component9 = Component("Component 9")
component10 = Component("Component 10")
component11 = Component("Component 11")
component12 = Component("Component 12")
component13 = Component("Component 13")
component14 = Component("Component 14")
component15 = Component("Component 15")
component16 = Component("Component 16")

# Building the system structure based on the image
series_1 = SeriesStructure([component1])

series_23 = SeriesStructure([component2, component3])

parallel_2345 = ParallelStructure([series_23, component4, component5])

parallel_78 = SeriesStructure([component7, component8])

series_678 = SeriesStructure([component6, parallel_78])

parallel_6789 = ParallelStructure([series_678, component9])

series_123456789 = SeriesStructure([series_1, parallel_2345, parallel_6789])

# series_10 = SeriesStructure([component10])
# parallel_1to10 = ParallelStructure([series_123456789, component10])

# Now, define the overall system combining all structures
complex_system = ComplexSystem([series_1, parallel_2345, parallel_6789])

# Determine the criticality of all components in the system
complex_system.determine_system_criticality()

# List critical components
critical_components = complex_system.list_critical_components()

# Display the critical components
print("Critical components in the system:")
for component in critical_components:
    print(component)
