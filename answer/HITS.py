import networkx as nx
import numpy as np

np.random.seed(1)
# Function to read the input from a text file and create a directed graph
def read_input(file_path):
    with open(file_path, 'r') as file:
        edges = [tuple(map(int, line.strip().split(','))) for line in file]
    return edges

# File path to the input text file
file_path = '../inputs/graph_1.txt'

edges = read_input(file_path)
graph = nx.DiGraph(edges)
hits_scores = nx.hits(graph)
print("Hub Scores:", hits_scores[0])
print("Authority Scores:", hits_scores[1])
