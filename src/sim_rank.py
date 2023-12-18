import numpy as np
from utility.Graph import Graph
from typing import List


def initialize_similarity_matrix(num_nodes: int) -> np.ndarray:
    """
    Initialize the similarity matrix as an identity matrix.

    Parameters:
        num_nodes (int): The number of nodes in the graph.

    Returns:
        np.ndarray: The initialized similarity matrix.
    """
    return np.identity(num_nodes)


def update_similarity_matrix(sim: np.ndarray, nodes: List, c: float) -> np.ndarray:
    """
    Update the similarity matrix using SimRank algorithm.

    Parameters:
        sim (np.ndarray): The current similarity matrix.
        nodes (List): List of nodes in the graph.
        c (float): The decay factor.

    Returns:
        np.ndarray: The updated similarity matrix.
    """
    num_nodes = len(nodes)
    node_index = {node: idx for idx, node in enumerate(nodes)}
    new_sim = np.identity(num_nodes)

    for i, node_i in enumerate(nodes):
        for j, node_j in enumerate(nodes):
            if i != j:
                predecessors_i = [node_index[n] for n in node_i.parents]
                predecessors_j = [node_index[n] for n in node_j.parents]

                if predecessors_i and predecessors_j:
                    s_ij = sum(
                        sim[u][v] for u in predecessors_i for v in predecessors_j
                    )
                    new_sim[i][j] = round(
                        c * s_ij / (len(predecessors_i) * len(predecessors_j)), 3
                    )
    return new_sim


def sim_rank(graph: Graph, c: float = 0.8, iterations: int = 10) -> np.ndarray:
    """
    Calculate SimRank similarity matrix for nodes in a graph.

    Parameters:
        graph (Graph): The input graph.
        c (float): The decay factor (default is 0.8).
        iterations (int): The number of iterations to perform (default is 10).

    Returns:
        np.ndarray: The SimRank similarity matrix.

    Raises:
        ValueError: If the graph is empty.
    """
    nodes = graph.nodes
    num_nodes = len(nodes)

    if num_nodes == 0:
        raise ValueError("The graph is empty.")

    # Initialize the similarity matrix
    sim = initialize_similarity_matrix(num_nodes)

    # Perform SimRank iterations
    for _ in range(iterations):
        # Update the similarity matrix for the current iteration
        sim = update_similarity_matrix(sim, nodes, c)

    return sim
