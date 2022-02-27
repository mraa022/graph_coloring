import numpy as np
from copy import deepcopy


def find_largest_clique(adjacency_matrix,v_to_right,v):
    # gets a larger clique than the current one when coloring a cordal graph
    if len(v_to_right) == 1:
        return v_to_right+[v]
    neighbor_set = []
    for vertex in range(len(adjacency_matrix[0])):
       
        if adjacency_matrix[v][vertex]==1 and vertex in v_to_right:
            neighbor_set.append(vertex)
    if v == 7:
        print("FML")
    return neighbor_set+[v]
def get_color_neigbors(adjacency_matrix,coloring,v):
    # gets the colors of the neighbors of a vertex (if any)
    neighbors = [x for x in get_neighbor_set(adjacency_matrix,v,[]) if x in coloring] # get only neighbors that were colored
    colors =  [coloring[i] for i in neighbors]
    return colors
def get_neighbor_set(adjacency_matrix,v,removed_vs):
    # gets the set of neighbors of a vertex
    neighbor_set = []
    for vertex in range(len(adjacency_matrix[0])):
        if vertex not in removed_vs:
            if adjacency_matrix[v][vertex]==1:
                neighbor_set.append(vertex)
        
    return neighbor_set

def check_clique(adjacency_matrix,vertex_set):
    # checks if a list of vertices form a clique
    if len(vertex_set)<=1:
        
        return True
    for v in vertex_set:
        for other_v in vertex_set:
            if adjacency_matrix[v][other_v] == 0 and other_v != v:
                return False
    return True

def find_simplicial(adjacency_matrix,removed_vs):
    # finds a simplicial vertex or returns False if it can't be found
    for v in range(len(adjacency_matrix[0])):
        if v not in removed_vs:
           
            neigbor_v = get_neighbor_set(adjacency_matrix,v,removed_vs)
            # if removed_vs == {9:True}:
            #     print(v+1, [x+1 for x in neigbor_v])
            if check_clique(adjacency_matrix,neigbor_v)==True:
                
                return v
    return 'False' # no simplicial vertex. this means G is not chordal
def check_chordal(adjacency_matrix):
    # checks if a graph is chordal or not
    simplicial_ordering = []
    removed_vertex  = {}
    for _ in range(len(adjacency_matrix[0])):
        v_simplicial = find_simplicial(adjacency_matrix,removed_vertex)
        
        if v_simplicial != 'False':
            
            simplicial_ordering.append(v_simplicial)
            removed_vertex[v_simplicial] = True
            
        else:
            print(f"THE GRAPH IS NOT CHORDAL SINCE THE SUB GRAPH INDUCED BY DELETING {[x+1 for x in removed_vertex.keys()]} has no simplicial vertex")
            return False
    return [x for x in simplicial_ordering]


def color_chordal(adjacency_matrix,verbose = 0):
    # colors a chordal graph using a min coloring by applying the greedy coloring algorithm to the reverse of the simplicial ordering
    simplicial_ordering = check_chordal(adjacency_matrix)
    largest_clique = [simplicial_ordering[-1]]
    coloring = {simplicial_ordering[-1]:1}

    vertex = len(simplicial_ordering)-2
    while vertex >-1:
        v = simplicial_ordering[vertex]
        neighbor_colors = get_color_neigbors(adjacency_matrix,coloring,v)
        available_colors = [x for x in coloring.values() if x not in neighbor_colors]

        if not available_colors: 
            coloring[v] = max(coloring.values())+1
            # find all of the neighbors of vi to the right to get a bigger clique (after adding vi to it)
            largest_clique = find_largest_clique(adjacency_matrix,simplicial_ordering[vertex+1:],v)
        else:
            coloring[v] = min(available_colors)
        vertex-=1
    user_coloring = dict([ (x+1,coloring[x]) for x in coloring.keys()])
    if verbose:
        print(f"CLIQUE K = {[x+1 for x in largest_clique]} |K| = {len(largest_clique)}")
        print(f"COLORING E= {user_coloring} |E| = {len(set(coloring.values()))}") 
    return user_coloring,[x+1 for x in largest_clique]