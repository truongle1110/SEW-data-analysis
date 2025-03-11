import matplotlib.pyplot as plt

def plot_replacement_times_both_plans(individual_plan, estimate_plan):
    """Plot replacement times from both plans on a single horizontal scatter plot,
    using 'o' markers for the Individual Plan and 'x' markers for the Estimate Plan."""
    
    # We'll assume both plans have the same set of component names
    components = list(individual_plan.keys())
    
    plt.figure()
    
    for i, comp in enumerate(components):
        # Extract replacement times for both plans
        times_indiv = individual_plan[comp]['replacement_time']
        times_est = estimate_plan[comp]['replacement_time']
        
        # For the legend, we only set the label on the first component’s plots
        if i == 0:
            plt.scatter(times_indiv, [i]*len(times_indiv),
                        marker='o', label='Individual Plan')
            plt.scatter(times_est, [i]*len(times_est),
                        marker='x', label='Estimate Plan')
        else:
            plt.scatter(times_indiv, [i]*len(times_indiv), marker='o')
            plt.scatter(times_est, [i]*len(times_est), marker='x')
    
    # Label axes
    plt.xlabel('Replacement Time')
    plt.ylabel('Component')
    
    # Replace numeric y-ticks with component labels
    plt.yticks(range(len(components)), components)
    
    # Add a legend so we can distinguish the two plans
    plt.legend()
    
    # Add a title (optional)
    plt.title('Replacement Times: Individual vs. Estimate Plans')
    
    # Show the figure
    plt.show()


# Example usage with your dictionaries:
individual_plan = {
    'POSTE DE CONTRÔLE': {
        'duration': [1.108, 1.108, 1.108, 1.108, 1.108],
        'replacement_time': [173.298, 346.596, 519.895, 693.193, 866.491]
    },
    'CONNECTEURS': {
        'duration': [3.849, 3.849, 3.849, 3.849, 3.849],
        'replacement_time': [538.635, 718.179, 179.545, 359.09, 897.724]
    },
    'POSTE 09 : MONTAGE CÔTÉ A (RETOURNEMENTS)': {
        'duration': [0.726, 0.726, 0.726, 0.726],
        'replacement_time': [208.829, 417.658, 626.487, 835.316]
    },
    'POSTE 04  : EMMANCHEMENTS ROULEMENTS (PRESSE)': {
        'duration': [1.925],
        'replacement_time': [548.357]
    },
    'CONVOYEURS': {
        'duration': [0.492],
        'replacement_time': [627.938]
    },
    'LIGNE DE MONTAGE MOTG02': {
        'duration': [0.89],
        'replacement_time': [732.33]
    }
}

estimate_plan = {
    'POSTE DE CONTRÔLE': {
        'duration': [1.108, 1.108, 1.108, 1.108, 8.806],
        'replacement_time': [173.298, 346.596, 519.895, 693.193, 697.198]
    },
    'CONNECTEURS': {
        'duration': [8.806, 8.806, 3.849, 3.849, 3.849],
        'replacement_time': [697.198, 697.198, 179.545, 359.09, 897.724]
    },
    'POSTE 09 : MONTAGE CÔTÉ A (RETOURNEMENTS)': {
        'duration': [0.726, 0.726, 0.726, 0.726],
        'replacement_time': [208.829, 417.658, 626.487, 835.316]
    },
    'POSTE 04  : EMMANCHEMENTS ROULEMENTS (PRESSE)': {
        'duration': [1.925],
        'replacement_time': [548.357]
    },
    'CONVOYEURS': {
        'duration': [0.492],
        'replacement_time': [627.938]
    },
    'LIGNE DE MONTAGE MOTG02': {
        'duration': [0.89],
        'replacement_time': [732.33]
    }
}

plot_replacement_times_both_plans(individual_plan, estimate_plan)
