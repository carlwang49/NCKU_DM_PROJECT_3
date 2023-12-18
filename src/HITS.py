from utility.Graph import Graph
from utility.Node import Node
from utility.utils import initialize_graph_from_file


def HITS_per_iter(graph: Graph):
    """
    Perform one iteration of the HITS algorithm on the given graph.

    Args:
        graph (Graph): The graph on which the HITS algorithm is applied.
    """
    # Calculate new Authority and Hub values without updating
    new_auth_values: dict[Node, float] = {
        node: node.calculate_new_auth() for node in graph.nodes
    }
    new_hub_values: dict[Node, float] = {
        node: node.calculate_new_hub() for node in graph.nodes
    }

    # Update Authority and Hub values
    for node in graph.nodes:
        node.update_auth_hub(new_auth_values[node], new_hub_values[node])

    # Normalize Authority and Hub values
    graph.normalize_auth_hub()


def run_hits_algorithm(graph, num_iterations=100):
    """
    Execute the HITS (Hyperlink-Induced Topic Search) algorithm on the given graph.

    Args:
        graph (Graph): The graph on which the HITS algorithm is applied.
        num_iterations (int, optional): The number of iterations for the algorithm. Default is 100.

    Returns:
        None
    """
    for _ in range(num_iterations):
        # Perform one iteration of the HITS algorithm on the graph
        HITS_per_iter(graph)
