class Node:
    def __init__(self, num):
        """
        Initialize a Node object with a unique identifier.

        Parameters:
            num (int): Unique identifier for the node.
        """
        self.num = num
        self.children = []  # List to store child nodes
        self.parents = []  # List to store parent nodes
        self.auth = 1.0  # Authority score for HITS algorithm
        self.hub = 1.0  # Hub score for HITS algorithm
        self.pagerank = 1.0  # PageRank score for PageRank algorithm

    def link_child(self, new_child):
        """
        Add a child node to the list of children.

        Parameters:
            new_child (Node): The node to be linked as a child.
        """
        if new_child not in self.children:
            self.children.append(new_child)

    def link_parent(self, new_parent):
        """
        Add a parent node to the list of parents.

        Parameters:
            new_parent (Node): The node to be linked as a parent.
        """
        if new_parent not in self.parents:
            self.parents.append(new_parent)

    def calculate_new_auth(self):
        """
        Calculate the new Authority value for the node.

        Returns:
            float: The calculated Authority value based on the Hub values of parent nodes.
        """
        return sum(node.hub for node in self.parents)

    def calculate_new_hub(self):
        """
        Calculate the new Hub value for the node.

        Returns:
            float: The calculated Hub value based on the Authority values of child nodes.
        """
        return sum(node.auth for node in self.children)

    def update_auth_hub(self, new_auth, new_hub):
        """
        Update the Authority and Hub values of the node.

        Args:
            new_auth (float): The new Authority value to set.
            new_hub (float): The new Hub value to set.
        """
        self.auth, self.hub = new_auth, new_hub
