from utility.Node import Node
import numpy as np

class Graph:
    def __init__(self):
        self.nodes = []

    def contains(self, num):
        return any(node.num == num for node in self.nodes)

    def normalize_auth_hub(self):
        auth_sum = sum(node.auth for node in self.nodes)
        hub_sum = sum(node.hub for node in self.nodes)

        for node in self.nodes:
            node.auth /= auth_sum
            node.hub /= hub_sum

    def find(self, num):
        """
        Retrieve the node with the given num, or create a new node if not found.

        Args:
            num (str): The num of the node to find or create.

        Returns:
            Node: The existing node with the specified num or the newly created node.
        """

        # If the node is not present in the graph, create a new node and add it
        if not self.contains(num):
            new_node = Node(num)
            self.nodes.append(new_node)
            return new_node
        # If the node already exists, return the matching node
        return next(node for node in self.nodes if node.num == num)

    def add_edge(self, parent: Node, child: Node):
        """
        Add an edge between the parent and child nodes in the graph.

        Args:
            parent (Node): The parent node to establish an edge from.
            child (Node): The child node to establish an edge to.

        Notes:
            The method ensures that both the parent and child nodes are present in the graph.
            If the nodes are not found, they will be created and added to the graph.
            The edge is bidirectional, linking the child node as a child of the parent
            and the parent node as a parent of the child.

        Returns:
            None
        """
        # Ensure the presence of the parent and child nodes in the graph
        parent_node = self.find(parent)
        child_node = self.find(child)

        # Establish a bidirectional edge between the parent and child nodes
        parent_node.link_child(child_node)
        child_node.link_parent(parent_node)

    def sort_nodes(self):
        """
        Sort the nodes in the graph based on their number in ascending numerical order.

        Notes:
            The sorting is performed using the integer values obtained from the number of the nodes.
            This method directly modifies the order of nodes within the graph.

        Returns:
            None
        """
        # Sort nodes based on their names converted to integers
        self.nodes.sort(key=lambda node: int(node.num))

    def get_authority_hub_lists(self):
        """
        Retrieve lists of authority and hub values for nodes in the graph.

        Returns:
            tuple: A tuple containing two lists representing authority and hub values.
        """
        # Create lists for authority and hub values
        authority_list = [node.auth for node in self.nodes]
        hub_list = [node.hub for node in self.nodes]

        # Round values to three decimal places for clarity
        rounded_authority = [round(value, 3) for value in authority_list]
        rounded_hub = [round(value, 3) for value in hub_list]

        return rounded_authority, rounded_hub
    
    def get_pagerank_list(self):
        pagerank_list = np.asarray([node.pagerank for node in self.nodes], dtype='float32')
        return np.round(pagerank_list, 3)
    
    def transition_matrix(self):
        size = len(self.nodes)
        B = np.zeros((size, size))
        E = np.zeros((size, size))
        node_index = {node: i for i, node in enumerate(self.nodes)}

        # Build the transition matrix B and the escape matrix E
        for node in self.nodes:
            idx = node_index[node]
            if node.children:  # If the node has outgoing links
                children_indices = [node_index[child] for child in node.children]
                B[children_indices, idx] = 1.0 / len(node.children)
            else:  # If the node is a dangling node (no outgoing links)
                E[:, idx] = 1.0 / size  # Add escape probability to all nodes
        
        # Combine B and E to form the stochastic matrix M
        M = B + E  # M will be used in the PageRank calculation
        return M
