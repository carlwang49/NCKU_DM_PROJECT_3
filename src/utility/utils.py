from utility.Graph import Graph


def initialize_graph_from_file(file_path):
    """
    Initialize a graph from a file containing parent-child relationships.

    Args:
        file_path (str): The path to the file containing parent-child relationships.

    Returns:
        Graph: A graph object representing the relationships.
    """
    # Read lines from the file
    with open(file_path) as file:
        lines = file.readlines()

    # Create a new Graph object
    graph = Graph()

    # Populate the graph with parent-child relationships from the file
    for line in lines:
        # Extract parent and child information from each line
        parent, child = line.strip().split(",")
        graph.add_edge(parent, child)

    # Sort the nodes within the graph
    graph.sort_nodes()

    return graph
