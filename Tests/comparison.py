import time

from src.GraphAlgo import GraphAlgo
import networkx as nx


def test_my_code10(Galgo: GraphAlgo):
    start1 = time.time()
    Galgo.connected_components()
    end1 = time.time()
    start2 = time.time()
    Galgo.connected_component(5)
    end2 = time.time()
    start3 = time.time()
    Galgo.shortest_path(1, 8)
    end3 = time.time()
    print("G_10 - connected components: ", end1 - start1,
          "\nG_10 - connected component (5): ", end2 - start2,
          "\nG_10 - shortest path (1,8): ", end3 - start3)


def test_my_code100(Galgo: GraphAlgo):
    start1 = time.time()
    Galgo.connected_components()
    end1 = time.time()
    start2 = time.time()
    Galgo.connected_component(50)
    end2 = time.time()
    start3 = time.time()
    Galgo.shortest_path(10, 80)
    end3 = time.time()
    print("G_100 - connected components: ", end1 - start1,
          "\nG_100 - connected component (50): ", end2 - start2,
          "\nG_100 - shortest path (10,80): ", end3 - start3)


def test_my_code1000(Galgo: GraphAlgo):
    start1 = time.time()
    Galgo.connected_components()
    end1 = time.time()
    start2 = time.time()
    Galgo.connected_component(500)
    end2 = time.time()
    start3 = time.time()
    Galgo.shortest_path(100, 800)
    end3 = time.time()
    print("G_1000 - connected components: ", end1 - start1,
          "\nG_1000 - connected component (500): ", end2 - start2,
          "\nG_1000 - shortest path (100,800): ", end3 - start3)


def test_my_code10000(Galgo: GraphAlgo):
    start1 = time.time()
    Galgo.connected_components()
    end1 = time.time()
    start2 = time.time()
    Galgo.connected_component(5000)
    end2 = time.time()
    start3 = time.time()
    Galgo.shortest_path(1000, 8000)
    end3 = time.time()
    print("G_10000 - connected components: ", end1 - start1,
          "\nG_10000 - connected component (5000): ", end2 - start2,
          "\nG_10000 - shortest path (100,8000): ", end3 - start3)


def test_my_code20000(Galgo: GraphAlgo):
    start1 = time.time()
    Galgo.connected_components()
    end1 = time.time()
    start2 = time.time()
    Galgo.connected_component(10000)
    end2 = time.time()
    start3 = time.time()
    Galgo.shortest_path(1000, 2000)
    end3 = time.time()
    print("G_20000 - connected components: ", end1 - start1,
          "\nG_20000 - connected component (10000): ", end2 - start2,
          "\nG_20000 - shortest path (1000,12000): ", end3 - start3)


def test_my_code30000(Galgo: GraphAlgo):
    start1 = time.time()
    Galgo.connected_components()
    end1 = time.time()
    start2 = time.time()
    Galgo.connected_component(20000)
    end2 = time.time()
    start3 = time.time()
    Galgo.shortest_path(11000, 12000)
    end3 = time.time()
    print("G_30000 - connected components: ", end1 - start1,
          "\nG_30000 - connected component (20000): ", end2 - start2,
          "\nG_30000 - shortest path (1000,20000): ", end3 - start3)


def test_Networkx10(Galgo: GraphAlgo):
    G = nx.DiGraph()
    for i in Galgo.get_graph().get_all_v().keys():
        G.add_node(i)
    for src in Galgo.get_graph().get_all_v().keys():
        for dest, weight in Galgo.get_graph().all_out_edges_of_node(src).items():
            G.add_edge(src, dest, weight=weight)
    start1 = time.time()
    nx.strongly_connected_components(G)
    end1 = time.time()
    start2 = time.time()
    nx.dijkstra_path(G=G, source=1, target=8)
    end2 = time.time()
    print("G_10 - connected components: ", end1 - start1,
          "\nG_10 - shortest path (1,8): ", end2 - start2)


def test_Networkx100(Galgo: GraphAlgo):
    G = nx.DiGraph()
    for i in Galgo.get_graph().get_all_v().keys():
        G.add_node(i)
    for src in Galgo.get_graph().get_all_v().keys():
        for dest, weight in Galgo.get_graph().all_out_edges_of_node(src).items():
            G.add_edge(src, dest, weight=weight)
    start1 = time.time()
    nx.strongly_connected_components(G)
    end1 = time.time()
    start2 = time.time()
    nx.dijkstra_path(G=G, source=10, target=80)
    end2 = time.time()
    print("G_100 - connected components: ", end1 - start1,
          "\nG_100 - shortest path (10,80): ", end2 - start2)


def test_Networkx1000(Galgo: GraphAlgo):
    G = nx.DiGraph()
    for i in Galgo.get_graph().get_all_v().keys():
        G.add_node(i)
    for src in Galgo.get_graph().get_all_v().keys():
        for dest, weight in Galgo.get_graph().all_out_edges_of_node(src).items():
            G.add_edge(src, dest, weight=weight)
    start1 = time.time()
    nx.strongly_connected_components(G)
    end1 = time.time()
    start2 = time.time()
    nx.dijkstra_path(G=G, source=100, target=800)
    end2 = time.time()
    print("G_1000 - connected components: ", end1 - start1,
          "\nG_1000 - shortest path (100,800): ", end2 - start2)


def test_Networkx10000(Galgo: GraphAlgo):
    G = nx.DiGraph()
    for i in Galgo.get_graph().get_all_v().keys():
        G.add_node(i)
    for src in Galgo.get_graph().get_all_v().keys():
        for dest, weight in Galgo.get_graph().all_out_edges_of_node(src).items():
            G.add_edge(src, dest, weight=weight)
    start1 = time.time()
    nx.strongly_connected_components(G)
    end1 = time.time()
    start2 = time.time()
    nx.dijkstra_path(G=G, source=5000, target=8000)
    end2 = time.time()
    print("G_10000 - connected components: ", end1 - start1,
          "\nG_10000 - shortest path (5000,8000): ", end2 - start2)


def test_Networkx20000(Galgo: GraphAlgo):
    G = nx.DiGraph()
    for i in Galgo.get_graph().get_all_v().keys():
        G.add_node(i)
    for src in Galgo.get_graph().get_all_v().keys():
        for dest, weight in Galgo.get_graph().all_out_edges_of_node(src).items():
            G.add_edge(src, dest, weight=weight)
    start1 = time.time()
    nx.strongly_connected_components(G)
    end1 = time.time()
    start2 = time.time()
    nx.dijkstra_path(G=G, source=5000, target=6000)
    end2 = time.time()
    print("G_20000 - connected components: ", end1 - start1,
          "\nG_20000 - shortest path (11000,12000): ", end2 - start2)


def test_Networkx30000(Galgo: GraphAlgo):
    G = nx.DiGraph()
    for i in Galgo.get_graph().get_all_v().keys():
        G.add_node(i)
    for src in Galgo.get_graph().get_all_v().keys():
        for dest, weight in Galgo.get_graph().all_out_edges_of_node(src).items():
            G.add_edge(src, dest, weight=weight)
    start1 = time.time()
    r = nx.strongly_connected_components(G)
    end1 = time.time()
    print(r)
    start2 = time.time()
    nx.dijkstra_path(G=G, source=11000, target=12000)
    end2 = time.time()
    print("G_30000 - connected components: ", end1 - start1,
          "\nG_30000 - shortest path (11000,12000): ", end2 - start2)


if __name__ == '__main__':
    Galgo10 = GraphAlgo()
    file = '../data/G_10_80_0.json'
    Galgo10.load_from_json(file)
    test_my_code10(Galgo10)

    Galgo100 = GraphAlgo()
    file = '../data/G_100_800_0.json'
    Galgo100.load_from_json(file)
    test_my_code100(Galgo100)

    Galgo1000 = GraphAlgo()
    file = '../data/G_1000_8000_0.json'
    Galgo1000.load_from_json(file)
    test_my_code1000(Galgo1000)

    Galgo10000 = GraphAlgo()
    file = '../data/G_10000_80000_0.json'
    Galgo10000.load_from_json(file)
    test_my_code10000(Galgo10000)

    Galgo20000 = GraphAlgo()
    file = '../data/G_20000_160000_0.json'
    Galgo20000.load_from_json(file)
    test_my_code20000(Galgo20000)

    Galgo30000 = GraphAlgo()
    file = '../data/G_30000_240000_0.json'
    Galgo30000.load_from_json(file)
    test_my_code30000(Galgo30000)

    print("NetworkX:")

    test_Networkx10(Galgo10)
    test_Networkx100(Galgo100)
    test_Networkx1000(Galgo1000)
    test_Networkx10000(Galgo10000)
    test_Networkx20000(Galgo20000)
    test_Networkx30000(Galgo30000)
