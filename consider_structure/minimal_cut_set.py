import networkx as nx
from itertools import combinations

# Function to compute minimal cut sets
def minimal_cut_sets(G, source, target):
    # List to store all minimal cut sets
    minimal_cuts = []
    
    # Get all the nodes excluding source and target
    components = list(G.nodes())
    components.remove(source)
    components.remove(target)
    
    # Iterate over different sizes of combinations
    for r in range(1, len(components) + 1):
        for combo in combinations(components, r):
            # Create a copy of the graph
            G_copy = G.copy()
            # Remove the selected components from the graph (simulate failure)
            G_copy.remove_nodes_from(combo)
            
            # Check if source and target are disconnected
            if not nx.has_path(G_copy, source, target):
                # If they are disconnected, this set is a cut set
                # Check if it's minimal by making sure no subset of this is already a minimal cut set
                is_minimal = True
                for other_cut in minimal_cuts:
                    if set(other_cut).issubset(combo):
                        is_minimal = False
                        break
                if is_minimal:
                    minimal_cuts.append(combo)
                    
    return minimal_cuts

# Example: Create a graph for a simple system with components A, B, C, D
# Define the reliability block diagram as a directed graph
G = nx.DiGraph()
G.add_edges_from([
    ('source', 'E1'),
    ('source', 'E4'),
    ('E1', 'E2'),
    ('E2', 'E3'),
    ('E4', 'E5'),
    ('E3', 'E6'),
    ('E5', 'E6'),
    ('E6', 'E7'),
    ('E7', 'target')
])

# Define the source and target nodes representing system input and output
source = 'source'
target = 'target'

# Calculate minimal cut sets
minimal_cuts = minimal_cut_sets(G, source, target)

# Display the result
for idx, cut in enumerate(minimal_cuts, start=1):
    print(f"Minimal Cut Set {idx}: {set(cut)}")

