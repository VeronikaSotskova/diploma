from typing import Optional

from networkx import DiGraph

from core.service import DBTGraph


class DBTGraphService:
    graph = DBTGraph().get_graph()
    mapping = {
        "domain": "model",
        "table": "source"
    }

    def find_node_name(self, model_name: str, model_type: str) -> Optional[str]:
        node_name = None
        for node in self.graph.nodes():
            node_split = node.split(".")
            if node_split[0] == self.mapping[model_type] and node_split[-1] == model_name.lower():
                node_name = node
        return node_name

    def get_subgraph(self, node_name: str) -> Optional[DiGraph]:
        if node_name:
            neighbors = set(filter(lambda n: n.split('.')[0] in ["model", "source"],
                                   self.graph.to_undirected().neighbors(node_name)))
            neighbors.add(node_name)
        #     current_nodes = {node_name, }
        #     while current_nodes:
        #         print(current_nodes)
        #         cur_node = current_nodes.pop()
        #         nodes.add(cur_node)
        #         if cur_node not in selected_nodes:
        #             current_nodes.update(
        #                 list(filter(lambda n: n.split('.')[0] in ["model", "source"],
        #                             undirected_graph.neighbors(cur_node)))
        #             )
        #             selected_nodes.add(cur_node)

            return self.graph.subgraph(neighbors)
        return None
