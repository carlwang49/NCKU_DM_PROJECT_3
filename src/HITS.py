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
    for iteration in range(num_iterations):
        # Perform one iteration of the HITS algorithm on the graph
        HITS_per_iter(graph)

        # Optionally display hub and authority values (commented out for brevity)
        # graph.display_hub_auth()

        # Optionally print iteration number (commented out for brevity)
        # print(f"Iteration {iteration + 1} complete")


if __name__ == "__main__":
    # Set the number of iterations for the HITS algorithm
    num_iterations = 100

    # Initialize the graph from a file
    graph = initialize_graph_from_file("./inputs/graph_4.txt")

    # Run the HITS algorithm on the graph
    run_hits_algorithm(graph, num_iterations)

    # Retrieve and print the authority and hub values
    auth_list, hub_list = graph.get_authority_hub_lists()
    print("Authority values:", auth_list)
    print("Hub values:", hub_list)
