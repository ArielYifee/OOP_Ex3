# OPP_Ex3 - Directed Weighted Graph in Python

Ex2 is the fourth exercise in the OPP course of Ariel university. this exercise will allow you to create a directed and weighted graph and to get information such as the shortest path between nodes, strongly connected components of the graph copy the graph, remove nodes, or edges, adding nodes, connection node, save and load graph and more.

# Installation

to use this exercise you need to import the .java files to your IDE and now you can use this.

# Usage

we have two classes: DiGraph, this class included NodeData class and GraphAlgo. there is an interface to each class that elaborates on each function. in the implementation of each function, some comments will explain how the function works. download and put in your favorite IDE (:


# Class Method

## class: DiGraph implements GraphInterfac

function:

* v_size
* e_size
* get_all_v
* all_in_edges_of_node
* all_out_edges_of_node
* get_mc
* add_edge
* add_node
* remove_node
* remove_edge

## class: NodeData

function:

* getId
* SetEIn
* GetEIn
* SetEOut
* GetEOut
* SetPos
* GetPos
* SetWeight
* GetWeight
* getInfo
* setInfo
* getTag
* setTag

## class: GraphAlgo implements GraphAlgoInterface

function: 

 * get_graph
 * load_from_json
 * save_to_json
 * shortest_path
 * connected_component
 * connected_components
 * plot_graph
 * SetVal 
	
# Links
	
[Shortest path problem](https://en.wikipedia.org/wiki/Shortest_path_problem)

[Tarjan's algorithm](https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm)
	
# Tests 

Ex3_Test (unittest)

## License

this exercise was made by Ariel Yifee and Moriya Bitton.
