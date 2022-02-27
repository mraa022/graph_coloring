
from chordal_graph_utilities import *
from six_coloring_algorithm import *
from greedy_coloring_algorithm import *


def color_graph(adjacency_matrix,verbose=0):
    if check_chordal(adjacency_matrix): # if it's chordal give it a min coloring
        print("GRAPH IS CORDAL")
        return color_chordal(adjacency_matrix,verbose)

    # else, check if it's planar, if it is color it with 6 colors, and compare that agains the result of the greedy algorithm
    # pick the better one
    greedy_coloring = color_greedy(adjacency_matrix,verbose)
    Graph_is_planar = check_planarity(adjacency_matrix)
    if Graph_is_planar:
        six_coloring = six_color(adjacency_matrix,0)
        if len(set(greedy_coloring.values()))< len(set(six_coloring.values())):
            print("GREEDY COLORING USED")
            return greedy_coloring
        else:
            print("SIX COLORING USED")
            if verbose:
                
                print(f"SIX COLORING E= {six_coloring} |E| = {len(set(six_coloring.values()))}")
            return six_coloring
    return greedy_coloring

A = [[0, 1, 1, 1, 1, 1, 0, 0, 0, 0], 
    [1, 0, 1, 1, 1, 0, 0, 1, 0, 0], 
    [1, 1, 0, 1, 0, 1, 1, 0, 0, 0], 
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 0], 
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 1, 1, 0, 0, 0, 0, 1, 0], 
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1], 
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]] 
color_graph(A,verbose=1)


