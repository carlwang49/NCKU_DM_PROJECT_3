class Node:
    def __init__(self, num):
        self.num = num
        self.children = []
        self.parents = []
        self.auth = 1.0
        self.hub = 1.0
        self.pagerank = 1.0

    def link_child(self, new_child):
        if new_child not in self.children:
            self.children.append(new_child)

    def link_parent(self, new_parent):
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
