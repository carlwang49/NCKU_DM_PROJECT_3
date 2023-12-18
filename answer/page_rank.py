import networkx as nx

# Function to read the input from a text file and create a directed graph
def read_input(file_path):
    with open(file_path, 'r') as file:
        edges = [tuple(map(int, line.strip().split(','))) for line in file]
    return edges

# Function to perform PageRank algorithm on a directed graph
def pagerank_algorithm(graph):
    pagerank_scores = nx.pagerank(graph, alpha=0.85, max_iter=100)
    # Round the scores to two decimal places
    rounded_scores = {node: round(score, 3) for node, score in pagerank_scores.items()}
    return rounded_scores

# File path to the input text file
file_path = '../inputs/graph_1.txt'

# Read input and create a directed graph
edges = read_input(file_path)
graph = nx.DiGraph(edges)

# Perform PageRank algorithm
pagerank_scores = pagerank_algorithm(graph)

# Display PageRank scores
print("PageRank Scores:", pagerank_scores)
