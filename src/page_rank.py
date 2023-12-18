import numpy as np
from utility.Graph import Graph
from utility.utils import initialize_graph_from_file

def PageRank_one_iter(graph, d, is_init_page_rank):
    num_nodes = len(graph.nodes)
    T = graph.transition_matrix()  # Transition matrix
    e = np.ones(num_nodes)  # Vector of ones

    if is_init_page_rank:
        r = np.array([node.pagerank / num_nodes for node in graph.nodes])
    
    r = np.array([node.pagerank for node in graph.nodes])
    # Calculate the new PageRank values
    new_r = (d / num_nodes) * e + (1 - d) * T.dot(r)

    # Update the PageRank values in the graph nodes
    for i, node in enumerate(graph.nodes):
        node.pagerank = new_r[i]

def PageRank(graph, d, iteration=100):
    for i in range(iteration):
        is_init_page_rank = False
        if i == 0:
            is_init_page_rank = True
        PageRank_one_iter(graph, d, is_init_page_rank)



if __name__ == '__main__':

    iteration = 30
    damping_factor = 0.1

    graph = initialize_graph_from_file('./inputs/graph_2.txt')

    PageRank(graph, damping_factor)
    print(graph.get_pagerank_list())