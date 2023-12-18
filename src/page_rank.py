import numpy as np
from utility.Graph import Graph


def page_rank_one_iteration(graph: Graph, d, is_init_page_rank):
    """
    Perform one iteration of the PageRank algorithm.

    Args:
        graph (Graph): The graph object.
        d (float): The damping factor.
        is_init_page_rank (bool): Whether it's the first iteration for initializing PageRank.

    Returns:
        np.ndarray: The updated PageRank values after one iteration.
    """
    num_nodes = len(graph.nodes)
    transition_matrix = graph.transition_matrix()
    e = np.ones(num_nodes)  # Vector of ones

    if is_init_page_rank:
        current_page_rank = np.array(
            [node.pagerank / num_nodes for node in graph.nodes]
        )
    else:
        current_page_rank = np.array([node.pagerank for node in graph.nodes])

    # Calculate the new PageRank values
    new_page_rank = (d / num_nodes) * e + (1 - d) * transition_matrix.dot(
        current_page_rank
    )

    # Update the PageRank values in the graph nodes
    for i, node in enumerate(graph.nodes):
        node.pagerank = new_page_rank[i]


def page_rank(graph: Graph, d, iterations=100):
    """
    Run the PageRank algorithm on the graph.

    Args:
        graph (Graph): The graph object.
        d (float): The damping factor.
        iterations (int): The number of iterations.

    Returns:
        np.ndarray: The final PageRank values.
    """
    for i in range(iterations):
        is_init_page_rank = i == 0
        page_rank_one_iteration(graph, d, is_init_page_rank)
