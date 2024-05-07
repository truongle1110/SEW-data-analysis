import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
    Nc -- number of component
    t_begin
    t_end
    C_iM -- preventive cost
    C_s -- setup cost
    C_iP -- specific cost
    C_iU -- unavailability cost
    C_d -- a positive constant representing downtime cost rate related to production loss
    d_i -- maintenance duration of component i
    t_i -- execution time of component i
    N_RM -- number of repairmem
    G -- group
    B_S -- setup cost saving
    B_U -- unavailability cost saving
    P -- penalty cost
    EB -- cost benefit = B_S + B_U + P
"""

# Load the Excel file
file_path_1 = 'data.xlsx'
file_path_2 = 'activity.xlsx'
df1 = pd.read_excel(file_path_1)
df2 = pd.read_excel(file_path_2)
# Load input
component = df1['Component']
alpha = df1['Alpha']
d = df1['Maintenance duration']
cost = df1['Replacement cost']
beta = df1['Beta']

t = df2['Replacement time']
ID_activity = df2['ID activity']
ID_component = df2['ID component']
map_activity_to_IDcomponent = list(zip(ID_activity, ID_component))    # list of tuple (ID_component, ID_activity)   

GENOME_LENGTH = 21                              # number of possible group
POPULATION_SIZE = 100
MUTATION_RATE = 0.01
CROSSOVER_RATE = 0.7
GENERATIONS = 2000

C_s = 500
C_d = 100

# initialize genome
def random_genome(length):
    return [random.randint(1, length) for _ in range(length)]
    
# initialize population
def init_population(population_size, genome_length):
    return [random_genome(genome_length) for _ in range(population_size)]

# evaluation
def decode(genome):
    # Dictionary to map original group to new group starting from 1
    group_mapping = {}
    new_group_number = 1

    # Create mapping from original group to new group numbers
    for group in genome:
        if group not in group_mapping:
            group_mapping[group] = new_group_number
            new_group_number += 1

    # Dictionary to store new groups and their respective activities
    group_activities = {}

    # Populate the dictionary using the new group numbers
    for activity, group in enumerate(genome, start=1):
        new_group = group_mapping[group]
        if new_group in group_activities:
            group_activities[new_group].append(activity)
        else:
            group_activities[new_group] = [activity]

    # items(): method to return the dictionary's key-value pairs
    # sorted: displaying the Keys in Sorted Order
    # for group, activities in sorted(group_activities.items()):
    #     print(f"Group {group}: Activities {activities}")

    number_of_groups = len(group_activities)
    G_activity = sorted(group_activities.items())                   # group and its activity
    return number_of_groups, G_activity

# setup cost saving
def saveup_cost_saving(G, C_s):
    B_S = []
    for group, activity in G:
        buffer = (len(activity) - 1) * C_s
        B_S.append(buffer)
    return B_S                                  # shape(B_S) = number of group

# mapping group of activity to group of component using list of tuple map_activity_to_IDcomponent defined above
def mapping_activity_to_componentID(map_activity_to_IDcomponent, G_activity):
    # Create a dictionary to map activities to ID components
    dict = {activity: id_component for activity, id_component in map_activity_to_IDcomponent}

    # Initialize the result list
    group_of_components = []

    # Process each group and its activities
    for group, activities in G_activity:
        # Find the ID components for each activity in the current group
        components = [dict[activity] for activity in activities if activity in dict]
        
        # Append the result as a tuple (group, list of components)
        group_of_components.append((group, components))
    return group_of_components


# unavailability cost saving
# def unavailability_cost_saving(G_k, C_d):
#     B_U = []
    
# get maintenance duration for each activity in a group
# def get_d_group():

# # Test main
genome = random_genome(GENOME_LENGTH)
N, G_activity = decode(genome)
print(f"Genome: {genome}")
print(f"Activities in group: {G_activity}")
print(f"Component ID and Activity ID: {map_activity_to_IDcomponent}")
G_component = mapping_activity_to_componentID(map_activity_to_IDcomponent, G_activity)
print(f"Components in group: {G_component}")

group_of duration = []
for group, id_component in G_component:
    print(f"Group: {group}, ID: {id_component}")
    for i in id_component:
        print(i)
        value = df1.loc[df1['ID'] == i, 'Maintenance duration'].iloc[0]
        print(value)
# value = df1.loc[df1['ID'] == 4, 'Maintenance duration'].iloc[0]
# print(value)

