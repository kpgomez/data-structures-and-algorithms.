class Vertex:
    """
    Essentially a node with a different name
    """
    # What does a vertex know about itself? It knows about its value and its neighbors.
    def __init__(self, value=None):
        self.value = value


class Graph:
    """
    Graphs are represented as an adjacency list.
    """

    def __init__(self, start=None, vertices=None, edges=None):
        # initialization here
        self.start = start
        self.vertices = []  # adjacency list
        self.edges = {}

    # def add_vertex(self):
    #     # method body here
    #     pass

    def add_node(self, value) -> Vertex:
        """
        Adds a vertex to the graph.
        :param value:
        :type value: any
        :return: vertex node
        :rtype: Vertex
        """
        # create a new node
        new_vertex = Vertex(value)

        # add new node to graph's adjacency list
        self.vertices.append(new_vertex)

        # return the added vertex
        return new_vertex

    def add_edge(self, first_vertex, second_vertex, weight=None) -> None:
        """
        Adds a new edge between two vertices in the graph.
        :param first_vertex:
        :type first_vertex:
        :param second_vertex:
        :type second_vertex:
        :param weight:
        :type weight:
        :return:
        :rtype:
        """
        edges = {}

        # confirm both vertices are in the graph
        if first_vertex in self.vertices and second_vertex in self.vertices:
            self.edges[first_vertex.value] = edges[second_vertex.value]
            edges[second_vertex.value]["weight"] = weight
            self.edges[second_vertex.value] = edges[first_vertex.value]
            edges[first_vertex.value]["weight"] = weight

    def get_vertices(self):
        """
        Returns all vertices in the graph as a collection.
        :return:
        :rtype:
        """
        return self.vertices

    def get_neighbors(self, vertex):
        """
        Returns a collection of edges connected to the given vertex.
        :param vertex:
        :type vertex:
        :return:
        :rtype:
        """

        # could potentially implement edges as a dictionary of dictionaries
        return self.edges[vertex]

    def size(self):
        """
        Returns the total number of vertices in the graph.
        :return:
        :rtype:
        """
        return len(self.vertices)





