class Graphx(object):

    def __init__(self):
        self.nodes = []
        self.edges = []

    def __del__(self):
        del self.nodes
        del self.edges

    def add_edge(self, edge, fail_on_exist=False, add_new_nodes=True):
        self.add_edges([edge], fail_on_exist, add_new_nodes)

    def add_edges(self, edges, fail_on_exist=False, add_new_nodes=True):
        is_unique = True
        ex1, ex2 = 0, 0
        node_set = set()
        edge_set = set()

        for edge in edges:
            try:
                # len(edge) == 2:
                (e1, e2) = edge
                node_set.add(e1)
                node_set.add(e2)
            except Exception:
                raise Exception(f"Edge must be a tuple of 2: Found {edge}. Operation aborted!")
            if ((e2, e1) in self.edges) or (edge in self.edges) or ((e2, e1) in edge_set) or (edge in edge_set):
                is_unique = False
                ex1 = e1
                ex2 = e2
            else:
                edge_set.add((e1, e2))
        if is_unique or (not is_unique and not fail_on_exist):
            if not add_new_nodes:
                nodeseed = node_set - set(self.nodes)
                if len(nodeseed) > 0:
                    raise Exception(f"These nodes do not exist in graph: {nodeseed}. Operation aborted")
            try:
                self.add_nodes(list(node_set), False)
            except Exception:
                raise
            edges = list(edge_set)
            self.edges.extend(edges)
        elif fail_on_exist:
            raise Exception(f"This edge already exist {(ex1, ex2)} or is repeated in input. Operation aborted!")

    def add_node(self, node, fail_on_exist=True):
        self.add_nodes([node], fail_on_exist)

    def add_nodes(self, nodes, fail_on_exist=True):
        is_unique = True
        node_exist = []
        if fail_on_exist:
            for node in nodes:
                if node in self.nodes:
                    is_unique = False
                    node_exist += [node]
        else:
            nodes = list(set(nodes) - set(self.nodes))
        if is_unique:
            self.nodes.extend(nodes)
            self.nodes = list(set(self.nodes))
        else:
            raise Exception(f"The node(s) <<{node_exist}>> already exist. Operation aborted!")

    def get_edges(self):
        return self.edges

    def get_nodes(self):
        return self.nodes
