import os
import unittest
from src.DiGraph import DiGraph, NodeData
from src.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    # ========================== DiGraph & Node_Data ========================
    graph1 = DiGraph()
    for n in range(8):
        graph1.add_node(n)
        NodeData.SetWeight(graph1.get_all_v()[n], n + 2)
    graph1.add_edge(0, 1, 10)
    graph1.add_edge(1, 2, 11)
    graph1.add_edge(2, 0, 12)
    graph1.add_edge(3, 4, 13)
    graph1.add_edge(4, 5, 14)
    graph1.add_edge(5, 6, 15)
    graph1.add_edge(5, 0, 16)
    graph1.add_edge(6, 0, 17)
    graph1.add_edge(6, 2, 18)
    graph1.add_edge(6, 4, 19)
    graph1.add_edge(3, 7, 20)
    graph1.add_edge(7, 3, 21)
    graph1.add_edge(7, 5, 22)

    def test_0(self):
        graph0 = DiGraph()
        self.assertEqual(0, graph0.v_size(), msg="empty graph nodes")
        self.assertEqual(0, graph0.e_size(), msg="empty graph edges")
        self.assertEqual(0, graph0.get_mc(), msg="empty graph mc")
        self.assertEqual(False, graph0.remove_node(0), msg="empty graph remove node")
        self.assertEqual(False, graph0.remove_edge(2, 3), msg="empty graph remove edge")
        self.assertEqual(True, graph0.add_node(1), msg="graph0 add node")
        self.assertEqual(False, graph0.add_edge(1, 1, 11), msg="graph0 add edge")

    def test_1(self):
        self.assertEqual(8, self.graph1.v_size(), msg="node size test")
        self.assertEqual(13, self.graph1.e_size(), msg="edge size test")
        self.assertEqual({0: 17, 2: 18, 4: 19}, self.graph1.all_out_edges_of_node(6), msg="out edges test")
        self.assertEqual({2: 12, 5: 16, 6: 17}, self.graph1.all_in_edges_of_node(0), msg=" edges test")
        self.assertEqual(21, self.graph1.get_mc(), msg="mc test")

    def test_2(self):
        graph2 = DiGraph()
        for i in range(0, 10):
            graph2.add_node(i)
        for i in range(0, 9):
            graph2.add_edge(i, i + 1, i + 4)
        self.assertEqual(10, graph2.v_size(), msg="graph2 node size")
        self.assertEqual(9, graph2.e_size(), msg="graph2 edge size")
        self.assertEqual(19, graph2.get_mc(), msg="graph2 mc")
        self.assertEqual(True, graph2.remove_node(1), msg="graph2 remove node")
        self.assertEqual(False, graph2.remove_node(11), msg="graph2 remove not exist node")
        self.assertEqual(9, graph2.v_size(), msg="graph2 node size 2")
        self.assertEqual(7, graph2.e_size(), msg="graph2 edge size 2")
        self.assertEqual(20, graph2.get_mc(), msg="remove node get mc")
        graph2.remove_edge(8, 9)
        self.assertEqual(6, graph2.e_size(), msg="graph2 remove edge")

    # ========================== GraphAlgo ========================

    def test_3(self):
        graph3 = DiGraph()
        Galgo1 = GraphAlgo(graph3)
        self.assertEqual((float("inf"), []), Galgo1.shortest_path(1, 1), msg="empty graph algo shortest path")
        self.assertEqual([], Galgo1.connected_component(0), msg="empty graph connected_component")
        self.assertEqual([], Galgo1.connected_components(), msg="empty graph connected_components")

    def test_4(self):
        Galgo = GraphAlgo(self.graph1)
        self.assertEqual(self.graph1, Galgo.get_graph(), msg="get graph test")
        self.assertEqual((0, [1]), Galgo.shortest_path(1, 1), msg="shortest path to itself")
        self.assertEqual((float("inf"), []), Galgo.shortest_path(20, 50))
        self.assertEqual([], Galgo.connected_component(26))

    def test_5(self):
        try:
            Test1 = DiGraph()
            for i in range(0, 10):
                Test1.add_node(i)
            for i in range(0, 9):
                Test1.add_edge(i, i + 1, i + 4)
            GT = GraphAlgo(Test1)
            self.assertEqual(True, GT.save_to_json("../data/Test.json"))
            Test1_load = GraphAlgo()
            self.assertEqual(True, Test1_load.load_from_json('../data/Test.json'), msg="load graph")
            self.assertEqual(Test1, Test1_load.get_graph(), msg="load compare graph")
            Test1.remove_edge(0, 1)
            self.assertNotEqual(Test1, Test1_load.get_graph(), msg="load compare 2")
        finally:
            os.remove("../data/Test.json")

    def test_6(self):
        graph4 = DiGraph()
        for i in range(9):
            graph4.add_node(i)
        graph4.add_edge(0, 1, 2)
        graph4.add_edge(0, 4, 20)
        graph4.add_edge(1, 5, 3)
        graph4.add_edge(5, 2, 1)
        graph4.add_edge(5, 8, 4)
        graph4.add_edge(5, 7, 6)
        graph4.add_edge(2, 3, 7)
        graph4.add_edge(8, 5, 2)
        graph4.add_edge(8, 7, 1)
        graph4.add_edge(7, 4, 2)
        graph4.add_edge(3, 6, 5)
        graph4.add_edge(6, 2, 1)
        Galgo2 = GraphAlgo(graph4)
        self.assertEqual((18, [0, 1, 5, 2, 3, 6]), Galgo2.shortest_path(0, 6))

    def test_7(self):
        GraphAlgo1 = GraphAlgo(self.graph1)
        self.assertEqual([[0, 1, 2], [4, 5, 6], [3, 7]], GraphAlgo1.connected_components(), msg="connected components")
        self.assertEqual([0, 1, 2], GraphAlgo1.connected_component(0), msg="connected components")

    def test_8(self):
        Galgo0 = GraphAlgo()
        Galgo0.load_from_json('../data/A0')
        Galgo0.plot_graph()

        Galgo1 = GraphAlgo()
        Galgo1.load_from_json('../data/A1')
        Galgo1.plot_graph()

        Galgo2 = GraphAlgo()
        Galgo2.load_from_json('../data/A2')
        Galgo2.plot_graph()

        Galgo3 = GraphAlgo()
        Galgo3.load_from_json('../data/A3')
        Galgo3.plot_graph()

        Galgo4 = GraphAlgo()
        Galgo4.load_from_json('../data/A4')
        Galgo4.plot_graph()

        Galgo5 = GraphAlgo()
        Galgo5.load_from_json('../data/A5')
        Galgo5.plot_graph()

        Galgo5 = GraphAlgo()
        Galgo5.load_from_json('../data/G_10_80_1.json')
        Galgo5.plot_graph()

