class Component:
    def __init__(self, name):
        """
        Initialize a component with a name.
        :param name: Name of the component.
        """
        self.name = name

class SeriesStructure:
    def __init__(self, components):
        """
        Initialize a series structure with components.
        :param components: List of Component or Structure objects.
        """
        self.components = components
    
    def get_minimal_cut_sets(self):
        """
        In a series structure, all components must work, so all form a single minimal cut set.
        :return: List of minimal cut sets for the series structure.
        """
        cut_sets = []
        for component in self.components:
            if isinstance(component, Component):
                cut_sets.append([component.name])
            elif isinstance(component, (SeriesStructure, ParallelStructure)):
                nested_cut_sets = component.get_minimal_cut_sets()
                cut_sets.append(nested_cut_sets)
        
        # In a series, the minimal cut set is the combination of all cut sets
        # Combine the cut sets from nested components (flatten the lists)
        combined_cut_sets = []
        for nested_set in cut_sets:
            if isinstance(nested_set[0], list):
                combined_cut_sets.extend(nested_set)
            else:
                combined_cut_sets.append(nested_set)
        return [combined_cut_sets]

class ParallelStructure:
    def __init__(self, components):
        """
        Initialize a parallel structure with components.
        :param components: List of Component or Structure objects.
        """
        self.components = components
    
    def get_minimal_cut_sets(self):
        """
        In a parallel structure, the system fails only if all paths fail,
        so each component or substructure forms a separate minimal cut set.
        :return: List of minimal cut sets for the parallel structure.
        """
        cut_sets = []
        for component in self.components:
            if isinstance(component, Component):
                cut_sets.append([component.name])
            elif isinstance(component, (SeriesStructure, ParallelStructure)):
                nested_cut_sets = component.get_minimal_cut_sets()
                cut_sets.extend(nested_cut_sets)  # Each branch is its own cut set
        return cut_sets

class ComplexSystem:
    def __init__(self, structures):
        """
        Initialize a complex system consisting of multiple structures.
        :param structures: List of SeriesStructure or ParallelStructure objects.
        """
        self.structures = structures
    
    def get_minimal_cut_sets(self):
        """
        Get minimal cut sets for the entire system.
        :return: List of minimal cut sets for the entire system.
        """
        cut_sets = []
        for structure in self.structures:
            cut_sets.extend(structure.get_minimal_cut_sets())
        return cut_sets

# Example usage:

# Define components
component1 = Component("Component 1")
component2 = Component("Component 2")
component3 = Component("Component 3")
component4 = Component("Component 4")
component5 = Component("Component 5")

# Step 1: Series of component 2 and 3
series_2_3 = SeriesStructure([component2, component3])

# Step 2: Parallel of (series 2 3) with component 4 and component 5
parallel_4_5 = ParallelStructure([component4, component5])
parallel_2_3_4_5 = ParallelStructure([series_2_3, parallel_4_5])

# Step 3: Series of component 1 with the whole subsystem (2, 3, 4, 5)
series_1 = SeriesStructure([component1, parallel_2_3_4_5])

# Now, define the overall system
complex_system = ComplexSystem([series_1])

# Get minimal cut sets
minimal_cut_sets = complex_system.get_minimal_cut_sets()

# Display results
print("Minimal cut sets:")
for cut_set in minimal_cut_sets:
    print(cut_set)
print(minimal_cut_sets)