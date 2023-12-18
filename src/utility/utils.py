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

    # Check if the file is space-separated
    space_separated = any(" " in line for line in lines)

    # Populate the graph with parent-child relationships from the file
    for line in lines:
        if space_separated:
            # For space-separated files, split on whitespace
            # Split the line into words
            words = line.split()

            # Extract parent and child information
            parent = words[0]
            child = words[-1]
        else:
            # For comma-separated files, split on comma
            parent, child = line.strip().split(",")

        graph.add_edge(parent, child)

    # Sort the nodes within the graph
    graph.sort_nodes()

    return graph
