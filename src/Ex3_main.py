from queue import PriorityQueue

from src.DiGraph import DiGraph, NodeData
from src.GraphAlgo import GraphAlgo
import time


def check():
    """
    Graph: |V|=4 , |E|=5
    {0: 0: |edges out| 1 |edges in| 1, 1: 1: |edges out| 3 |edges in| 1, 2: 2: |edges out| 1 |edges in| 1, 3: 3: |edges out| 0 |edges in| 2}
    {0: 1}
    {0: 1.1, 2: 1.3, 3: 10}
    (3.4, [0, 1, 2, 3])
    [[0, 1], [2], [3]]
    (2.8, [0, 1, 3])
    (inf, [])
    2.062180280059253 [1, 10, 7]
    17.693921758901507 [47, 46, 44, 43, 42, 41, 40, 39, 15, 16, 17, 18, 19]
    11.51061380461898 [20, 21, 32, 31, 30, 29, 14, 13, 3, 2]
    inf []
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]]
    """
    check0()
    check1()
    check2()


def check0():
    """
    This function tests the naming (main methods of the DiGraph class, as defined in GraphInterface.
    :return:
    """
    g = DiGraph()  # creates an empty directed graph
    for n in range(4):
        g.add_node(n)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 0, 1.1)
    g.add_edge(1, 2, 1.3)
    g.add_edge(2, 3, 1.1)
    g.add_edge(1, 3, 1.9)
    g.remove_edge(1, 3)
    g.add_edge(1, 3, 10)
    print(g)  # prints the __repr__ (func output)
    print(g.get_all_v())  # prints a dict with all the graph's vertices.
    print(g.all_in_edges_of_node(1))
    print(g.all_out_edges_of_node(1))
    g_algo = GraphAlgo(g)
    print(g_algo.shortest_path(0, 3))
    g_algo.plot_graph()


def check1():
    """
       This function tests the naming (main methods of the GraphAlgo class, as defined in GraphAlgoInterface.
    :return:
    """
    g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
    file = "../data/T0.json"
    g_algo.load_from_json(file)  # init a GraphAlgo from a json file
    print(g_algo.connected_components())
    print(g_algo.shortest_path(0, 3))
    print(g_algo.shortest_path(3, 1))
    g_algo.save_to_json(file + '_saved')
    g_algo.plot_graph()


def check2():
    """ This function tests the naming, basic testing over A5 json file.
      :return:
      """
    g_algo = GraphAlgo()
    file = '../data/A5'
    g_algo.load_from_json(file)
    g_algo.get_graph().remove_edge(13, 14)
    g_algo.save_to_json(file + "_edited")
    dist, path = g_algo.shortest_path(1, 7)
    print(dist, path)
    dist, path = g_algo.shortest_path(47, 19)
    print(dist, path)
    dist, path = g_algo.shortest_path(20, 2)
    print(dist, path)
    dist, path = g_algo.shortest_path(2, 20)
    print(dist, path)
    print(g_algo.connected_component(0))
    print(g_algo.connected_components())
    g_algo.plot_graph()


if __name__ == '__main__':
    # g = DiGraph()
    # queue = PriorityQueue()
    # for n in range(8):
    #     g.add_node(n)
    #     NodeData.SetWeight(g.get_all_v()[n], n+2)
    #     queue.put(g.get_all_v()[n])
    # while queue:
    #     print(queue.get())
    # g.add_edge(0, 1, 2)
    # g.add_edge(1, 2, 2)
    # g.add_edge(2, 0, 2)
    # g.add_edge(3, 4, 2)
    # g.add_edge(4, 5, 2)
    # g.add_edge(5, 6, 2)
    # g.add_edge(5, 0, 2)
    # g.add_edge(6, 0, 2)
    # g.add_edge(6, 2, 2)
    # g.add_edge(6, 4, 2)
    # g.add_edge(3, 7, 2)
    # g.add_edge(7, 3, 2)
    # g.add_edge(7, 5, 2)
    # galgo = GraphAlgo()
    # file = '../data/G_30000_240000_0.json'
    # start1 = time.time()
    # galgo.load_from_json(file)
    # end1 = time.time()
    # print(end1 - start1)
    # start = time.time()
    # s = galgo.connected_components()
    # print(s)
    # end = time.time()
    # print(s, "\n", end-start)
    check()
    # g = DiGraph()  # creates an empty directed graph
    # for n in range(3):
    #     g.add_node(n)
    # g.add_edge(0, 1, 2)
    # g.add_edge(1, 2, 2)
    # g.add_edge(2, 0, 2)
    # g_al = GraphAlgo(g)
    # g_al.plot_graph()
# from DiGraph import DiGraph, NodeData
# from GraphAlgo import GraphAlgo
#
#
# def check():
#     """
#     Graph: |V|=4 , |E|=5
#     {0: 0: |edges out| 1 |edges in| 1, 1: 1: |edges out| 3 |edges in| 1, 2: 2: |edges out| 1 |edges in| 1, 3: 3: |edges out| 0 |edges in| 2}
#     {0: 1}
#     {0: 1.1, 2: 1.3, 3: 10}
#     (3.4, [0, 1, 2, 3])
#     [[0, 1], [2], [3]]
#     (2.8, [0, 1, 3])
#     (inf, [])
#     2.062180280059253 [1, 10, 7]
#     17.693921758901507 [47, 46, 44, 43, 42, 41, 40, 39, 15, 16, 17, 18, 19]
#     11.51061380461898 [20, 21, 32, 31, 30, 29, 14, 13, 3, 2]
#     inf []
#     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#     [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]]
#     """
#     check0()
#     check1()
#     check2()
#
#
# def check0():
#     """
#     This function tests the naming (main methods of the DiGraph class, as defined in GraphInterface.
#     :return:
#     """
#     g = DiGraph()  # creates an empty directed graph
#     for n in range(4):
#         g.add_node(n)
#     g.add_edge(0, 1, 1)
#     # g.add_edge(1, 0, 1.1)
#     g.add_edge(1, 2, 1.3)
#     g.add_edge(2, 3, 1.1)
#     g.add_edge(1, 3, 1.9)
#     g.remove_edge(1, 3)
#     g.add_edge(3, 1, 10)
#     print(1, g)  # prints the __repr__ (func output)
#     print(2, g.get_all_v())  # prints a dict with all the graph's vertices.
#     print(3, g.all_in_edges_of_node(1))
#     print(4, g.all_out_edges_of_node(1))
#     g_algo = GraphAlgo(g)
#     l = g_algo.connected_components()
#     print(l)
#     print(g_algo.connected_component(2))
#     g_algo.plot_graph()
#     # print(5, g_algo.shortest_path(0, 3))
#     # g_algo.save_to_json("../data/Graph.json")
#     # g0 = GraphAlgo()
#     # g0.load_from_json("../data/Graph.json")
#     # g1 = g0.get_graph()
#     # print(g1.get_all_v())
#     # g_algo.plot_graph()
#
#
# def check1():
#     """
#        This function tests the naming (main methods of the GraphAlgo class, as defined in GraphAlgoInterface.
#     :return:
#     """
#     g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
#     file = "../data/T0.json"
#     g_algo.load_from_json(file)  # init a GraphAlgo from a json file
#     print(g_algo.connected_components())
#     print(g_algo.shortest_path(0, 3))
#     print(g_algo.shortest_path(3, 1))
#     g_algo.save_to_json(file + '_saved')
#     g_algo.plot_graph()
#
#
# def check2():
#     """ This function tests the naming, basic testing over A5 json file.
#       :return:
#       """
#     g_algo = GraphAlgo()
#     file = '../data/A5'
#     g_algo.load_from_json(file)
#     g_algo.get_graph().remove_edge(13, 14)
#     g_algo.save_to_json(file + "_edited")
#     dist, path = g_algo.shortest_path(1, 7)
#     print(dist, path)
#     dist, path = g_algo.shortest_path(47, 19)
#     print(dist, path)
#     dist, path = g_algo.shortest_path(20, 2)
#     print(dist, path)
#     dist, path = g_algo.shortest_path(2, 20)
#     print(dist, path)
#     print(g_algo.connected_component(0))
#     print(g_algo.connected_components())
#     g_algo.plot_graph()
#
#
# if __name__ == '__main__':
#     check0()
#     # n1 = NodeData(1)
#     # print(n1)
#     # n2 = NodeData(2)
#     # n3 = NodeData(3)
#     # n1.SetWeight(11)
#     # n2.SetWeight(22)
#     # n3.SetWeight(33)
#     # arr = [n3, n1, n2]
#     # print(arr)
#     # arr.sort()
#     # print(arr)
#     # n4 = arr.pop(0)
#     # print(n4)
#     # print(arr)