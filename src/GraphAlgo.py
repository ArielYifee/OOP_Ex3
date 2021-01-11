import json
import matplotlib.pyplot as plt
from typing import List
from numpy import random
from queue import PriorityQueue
from src.GraphAlgoInterface import GraphAlgoInterface
from src import GraphInterface
from src.DiGraph import DiGraph, NodeData


class GraphAlgo(GraphAlgoInterface, DiGraph):

    def __init__(self, graph: DiGraph = None):
        self._graph = graph

    def get_graph(self) -> GraphInterface:
        return self._graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            graph = DiGraph()
            with open(file_name) as fl:
                json_graph = json.load(fl)
                fl.close()
            nodes = json_graph["Nodes"]
            for node in nodes:
                graph.add_node(node["id"])
                nd = graph.get_all_v()
                if "pos" in node:
                    if isinstance(node["pos"], str):
                        f = [tuple(float(x) for x in node["pos"].split(","))]
                        NodeData.SetPos(nd[node["id"]], f[0])
                    else:
                        NodeData.SetPos(nd[node["id"]], node["pos"])
            edges = json_graph["Edges"]
            for edge in edges:
                graph.add_edge(edge["src"], edge["dest"], edge["w"])
            self._graph = graph
            return True
        except Exception as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            edges = []
            nodes = []
            graph_nodes = self._graph.get_all_v()
            for key in graph_nodes:
                if NodeData.GetPos(graph_nodes[key]) is not None:
                    temp_node = {"pos": NodeData.GetPos(graph_nodes[key]), "id": key}
                else:
                    temp_node = {"id": key}
                node_edges = self._graph.all_out_edges_of_node(key)
                for dest in node_edges:
                    temp_edge = {"src": key, "dest": dest, "w": node_edges[dest]}
                    edges.append(temp_edge)
                nodes.append(temp_node)
            graph = {"Nodes": nodes, "Edges": edges}
            with open(file_name, "w") as json_file:
                json.dump(graph, json_file)
            return True
        except Exception as e:
            print(e)
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        path = []
        queue = PriorityQueue()
        nodes = self._graph.get_all_v()
        if (id1 not in nodes) or (id2 not in nodes):
            ans = float("inf"), []
            return ans
        if id1 == id2:
            path.append(id1)
            ans = 0, path
            return ans
        self.setVal()
        NodeData.SetInfo(nodes[id1], "")
        NodeData.SetWeight(nodes[id1], 0)
        path.append(nodes[id1])
        queue.put((NodeData.GetWeight(nodes[id1]), id1))
        while queue.empty() is False:
            node = queue.get()[1]
            if node is None:
                ans = float("inf"), []
                return ans
            if NodeData.GetId(nodes[node]) is id2:
                i = NodeData.GetInfo(nodes[node])
                i += "," + str(NodeData.GetId(nodes[node]))
                int_l = list(map(int, i.split(",")))
                tup = NodeData.GetWeight(nodes[node]), int_l
                return tup
            edges = self._graph.all_out_edges_of_node(NodeData.GetId(nodes[node]))
            for key in edges:
                NodeData.GetWeight(nodes[key])
                r = NodeData.GetWeight(nodes[key])
                s = NodeData.GetWeight(nodes[node]) + edges[key]
                if NodeData.GetWeight(nodes[key]) > NodeData.GetWeight(nodes[node]) + edges[key]:
                    NodeData.SetWeight(nodes[key], NodeData.GetWeight(nodes[node]) + edges[key])
                    s = NodeData.GetInfo(nodes[node])
                    if NodeData.GetId(nodes[node]) is id1:
                        s += str(NodeData.GetId(nodes[node]))
                    else:
                        s += "," + str(NodeData.GetId(nodes[node]))
                    NodeData.SetInfo(nodes[key], s)
                    queue.put((NodeData.GetWeight(nodes[key]), key))
        return float("inf"), []

    def connected_component(self, id1: int) -> list:
        if id1 in self._graph.get_all_v():
            L = self.connected_components()
            for list in L:
                if id1 in list:
                    return list
        return []

    def connected_components(self) -> List[list]:
        if self._graph is None:
            return []
        result = []  # list of lists that will contain the result
        preorder = {}  # dict that marks the nodes and give them their get in number
        parent_path = {}  # dict that contain the nodes and their parent get in number
        visited = {}  # dict that contains all the visited nodes
        scc_queue = []  # list of the components
        i = 0  # Preorder counter
        g = self._graph.get_all_v()
        for node in g:  # go through all the nodes in the graph
            if node not in visited:  # check if the node is already visited
                queue = [node]  # if not visited put into a temporary queue
                while queue:  # while the queue is not empty
                    v = queue[-1]  # get the last node from the queue
                    if v not in preorder:  # check if the node not in the preorder marks
                        i = i + 1  # new get in number
                        preorder[v] = i  # put the node with its get in number
                    done = 1  # if done is 1 it's mean that the there isn't another components
                    n_neighbors = self._graph.all_out_edges_of_node(v)
                    for w in n_neighbors:  # go throw the nodes neighbors
                        if w not in preorder:  # check if the node not in the preorder marks
                            queue.append(w)  # add the neighbor to the temporary queue
                            done = 0  # if done is 0 it's mean that we need to search for another components
                            break  # add only one neighbor to the queue
                    if done == 1:  # if done is 1 it's mean that the there isn't another components
                        parent_path[v] = preorder[v]  # put the node into the parent path
                        for w in n_neighbors:  # go throw the node's neighbors
                            if w not in visited:  # if the neighbor isn't visited
                                if preorder[w] > preorder[v]:  # if the neighbor get in after the node
                                    parent_path[v] = min([parent_path[v], parent_path[
                                        w]])  # set the node the number of his neighbor parent
                                else:  # the node get in before the neighbor
                                    parent_path[v] = min(
                                        [parent_path[v], preorder[w]])  # set the node parent to the min get in number
                        queue.pop()  # get out the node from the temporary queue
                        if parent_path[v] == preorder[
                            v]:  # if the node parent is same as his get in number (mean that he's the root)
                            visited[v] = True  # set the node as visited
                            scc = [v]  # add the node to the components group
                            while scc_queue and preorder[scc_queue[-1]] > preorder[
                                v]:  # while the queue isn't empty and the last node in the queue get in the preorder after the node
                                k = scc_queue.pop()  # pop the next node
                                visited[k] = True  # set it as visited
                                scc.append(k)  # add it to the component group
                            result.append(scc)  # add the list to the result list
                        else:  # we haven't get to the root yet
                            scc_queue.append(v)  # put the node to the components queue
        return result

    def plot_graph(self) -> None:
        nodes = self._graph.get_all_v()
        ls = list()
        for node in nodes:
            p = NodeData.GetPos(nodes[node])
            if p is None:
                p = (random.uniform(0, 50), random.uniform(0, 50))
                NodeData.SetPos(nodes[node], p)
        for node in nodes:
            src_pos = NodeData.GetPos(nodes[node])
            px = src_pos[0]
            py = src_pos[1]
            plt.text(px, py, str(node), color="red")
            for neighbors in self._graph.all_out_edges_of_node(node):
                dst_pos = NodeData.GetPos(nodes[neighbors])
                srcval = [src_pos[0], src_pos[1]]
                ls.append(srcval)
                destval = [dst_pos[0], dst_pos[1]]
                ls.append(destval)
        ls1 = iter(ls)
        xsum = 0
        ysum = 0
        for p1, p2 in zip(ls1, ls1):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            if dx < 0:
                dx = dx * -1
            if dy < 0:
                dy = dy * -1
            xsum += dx
            ysum += dy
        scale = max(xsum, ysum) / len(ls)
        if scale < 0.09:
            scale *= 3
        lst = iter(ls)
        for p1, p2 in zip(lst, lst):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            plt.arrow(p2[0], p2[1], dx, dy, length_includes_head=True, width=(scale * 0.001), head_width=(scale * 0.07))
        plt.ylabel("Y")
        plt.xlabel("X")
        plt.title("We Love Shai (Sason, Yehuda) Aharon ;)")
        plt.show()

    def setVal(self):
        nodes = self._graph.get_all_v()
        for values in nodes.values():
            NodeData.SetInfo(values, "")
            NodeData.SetWeight(values, float('inf'))
            NodeData.SetTag(values, 0)
