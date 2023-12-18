import numpy as np
from utility.Graph import Graph
from utility.utils import initialize_graph_from_file

def PageRank_one_iter(graph, d):
    num_nodes = len(graph.nodes)
    T = graph.transition_matrix()  # Transition matrix
    e = np.ones(num_nodes)  # Vector of ones

    # Current PageRank values
    r = np.array([node.pagerank for node in graph.nodes])
    
    # Calculate the new PageRank values
    new_r = (d / num_nodes) * e + (1 - d) * T.dot(r)

    # Update the PageRank values in the graph nodes
    for i, node in enumerate(graph.nodes):
        node.pagerank = new_r[i]

def PageRank(graph, d, iteration=100):
    for _ in range(iteration):
        PageRank_one_iter(graph, d)



if __name__ == '__main__':

    iteration = 30
    damping_factor = 0.1

    graph = initialize_graph_from_file('./inputs/graph_1.txt')

    PageRank(graph, damping_factor)
    print(graph.get_pagerank_list())