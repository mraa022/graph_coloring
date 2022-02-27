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



def color_greedy(adjacency_matrix,verbose = 0):
    # colors a chordal graph using a min coloring by applying the greedy coloring algorithm to the reverse of the simplicial ordering
    ordering = list(range(len(adjacency_matrix[0])))
    
    coloring = {ordering[0]:1}

    vertex = 0
    while vertex < len(adjacency_matrix[0]):
        v = ordering[vertex]
        neighbor_colors = get_color_neigbors(adjacency_matrix,coloring,v)
        available_colors = [x for x in coloring.values() if x not in neighbor_colors]

        if not available_colors: 
            coloring[v] = max(coloring.values())+1   
        else:
            coloring[v] = min(available_colors)
        vertex+=1
    user_coloring = dict([ (x+1,coloring[x]) for x in coloring.keys()])
    if verbose:
        print(f"COLORING E= {user_coloring} |E| = {len(set(coloring.values()))}") 
    return user_coloring