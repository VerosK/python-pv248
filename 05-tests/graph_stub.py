
class GraphException(Exception):
    pass


class Graph:
    def __init__(self):
        "Create empty oriented graph"
        self._nodes = {}

    def add_node(self, node_id):
        """Create new_node in the graph. Raises GraphException
        when duplicate node_id already exists"""
        if node_id in self._nodes:
            raise GraphException("Duplicate node_id used")

    def add_edge(self, node_from, node_to):
        """Add edge to the graph.
        Raises GraphException when duplicate edge exists
        """
        pass

    def has_edge(self, node_from, node_to):
        """
        Checks is edge exists.

        Raises GraphException is node_from and node_to doesn't exists.
        Returns True if edge exists
        Retrun False if edge doesn't exist.
        """
        return True

    def has_path(self, node_from, node_to):
        """
        Checks is path exists.

        Raises GraphException is node_from and node_to doesn't exists.
        Returns True if path exists
        Retrun False if path doesn't exist.
        """
        pass

    def nodes(self):
        "Return list on nodes ids"
        return self._nodes.keys()

    def node_count(self):
        "Return count of nodes"
        return len(self._nodes)
