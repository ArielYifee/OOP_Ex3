from src.GraphInterface import GraphInterface


class NodeData:

    def __init__(self, node_id: int, pos: tuple = None):
        self._id = node_id
        self._pos = pos
        self._weight = float('inf')
        self._tag = 0
        self._info = ""
        self._edgesIn = 0
        self._edgesOut = 0
        self._visited = True

    def SetEIn(self, Enum: int):
        self._edgesIn = Enum

    def GetEIn(self):
        return self._edgesIn

    def SetEOut(self, Enum: int):
        self._edgesIn = Enum

    def GetEOut(self):
        return self._edgesIn

    def GetId(self):
        return self._id

    def SetPos(self, pos: tuple):
        self._pos = pos

    def GetPos(self):
        return self._pos

    def SetWeight(self, weight: float):
        self._weight = weight

    def GetWeight(self):
        return self._weight

    def SetTag(self, tag: float):
        self._tag = tag

    def GetTag(self):
        return self._tag

    def SetInfo(self, info: str):
        self._info = info

    def GetInfo(self):
        return self._info

    def SetVisited(self, visited: bool):
        self._visited = visited

    def IsVisited(self):
        return self._visited

    def __lt__(self, other):
        return self._weight < other._weight

    def __str__(self):
        return str(self._id) + ": |edges out| " + str(self._edgesOut) + " |edges in| " + str(self._edgesIn)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self._id is other._id


class DiGraph(GraphInterface, NodeData):

    def __init__(self):
        self._Nodes = dict()
        self._Edges = dict()
        self._ReversEdges = dict()
        self._MC = 0
        self._EdgesNum = 0

    def __str__(self):
        return "Graph: |V|=" + str(len(self._Nodes)) + " , |E|=" + str(self._EdgesNum)

    def __eq__(self, other):
        if not (isinstance(other, DiGraph)) or (other is None):
            return False
        else:
            if (self.e_size() != other.e_size()) or (len(self._Nodes) != len(other._Nodes)):
                return False
            else:
                for i in self._Nodes.keys():
                    if i not in other.get_all_v():
                        return False
                    else:
                        for k, v in self.all_out_edges_of_node(i).items():
                            if k not in other.all_out_edges_of_node(i) and other.all_out_edges_of_node(i)[k] is not v:
                                return False
        return True

    def v_size(self) -> int:
        return len(self._Nodes)

    def e_size(self) -> int:
        return self._EdgesNum

    def get_all_v(self) -> dict:
        return self._Nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        in_edges = dict()
        for key in self._ReversEdges[id1]:
            in_edges[key] = self._ReversEdges[id1][key]
        return in_edges

    def all_out_edges_of_node(self, id1: int) -> dict:
        out_edges = dict()
        for key in self._Edges[id1]:
            out_edges[key] = self._Edges[id1][key]
        return out_edges

    def get_mc(self) -> int:
        return self._MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        # check if both of the node are in the graph
        if (id1 not in self._Nodes) or (id2 not in self._Nodes):
            return False
        if id1 is id2:
            return False
        if id2 not in self._Edges[id1]:
            self._Edges[id1][id2] = weight
            self._ReversEdges[id2][id1] = weight
            self._MC += 1
            self._EdgesNum += 1
            NodeData.SetEIn(self._Nodes[id2], (NodeData.GetEIn(self._Nodes[id2]) + 1))
            NodeData.SetEOut(self._Nodes[id1], (NodeData.GetEOut(self._Nodes[id1]) + 1))
            return True
        else:  # if the edge exist do nothing.
            return False
            # if self._Edges[id1][id] == weight:
            #     return False
            # self._Edges[id1][id2] = weight
            # self._ReversEdges[id2][id1] = weight
            # self._MC += 1
            # NodeData.SetEIn(self._Nodes[id2], (NodeData.GetEIn(self._Nodes[id2]) + 1))
            # NodeData.SetEOut(self._Nodes[id1], (NodeData.GetEOut(self._Nodes[id1]) + 1))

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self._Nodes:
            node = NodeData(node_id, pos)
            self._Nodes[node_id] = node
            self._Edges[node_id] = dict()
            self._ReversEdges[node_id] = dict()
            self._MC += 1
            return True
        else:  # if the node exist do nothing
            return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self._Nodes:
            edgNum = len(self._Edges[node_id])
            self._Nodes.pop(node_id, None)
            self._Edges.pop(node_id, None)
            for key in self._Edges:
                if node_id in self._Edges[key]:
                    self._Edges[key].pop(node_id)
                    edgNum += 1
            for key in self._ReversEdges:
                if node_id in self._ReversEdges[key]:
                    self._ReversEdges[key].pop(node_id)
            self._EdgesNum -= edgNum
            self._MC += 1
            return True
        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self._Edges:
            if node_id2 in self._Edges[node_id1]:
                self._Edges[node_id1].pop(node_id2)
                self._ReversEdges[node_id2].pop(node_id1)
                self._EdgesNum -= 1
                self._MC += 1
                return True
            else:
                return False
        else:
            return False
