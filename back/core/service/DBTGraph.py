import networkx as nx

from src.settings import DBT_PROJECT_PATH


class DBTGraph:
    graph = None

    def get_graph(self):
        if self.graph is None:
            self.graph = nx.read_gpickle(f"{DBT_PROJECT_PATH}/target/graph.gpickle")
        return self.graph
