def dijkstras_algorithm(G, start_vertex, end_vertex):
    D = {v: float('inf') for v in G}
    D[start_vertex] = 0

    unvisited = list(G)
    previous_vertices = {v: None for v in G}

    while unvisited:
        current_vertex = min((D[vertex], vertex) for vertex in unvisited)[1]
        if current_vertex == end_vertex:
            break
        unvisited.remove(current_vertex)

        for neighbour, cost in G[current_vertex].items():
            new_cost = D[current_vertex] + cost['weight']  # Adjusted line
            if new_cost < D[neighbour]:
                D[neighbour] = new_cost
                previous_vertices[neighbour] = current_vertex

    path, current_vertex = [], end_vertex
    while previous_vertices[current_vertex] is not None:
        path.insert(0, current_vertex)
        current_vertex = previous_vertices[current_vertex]
    path.insert(0, current_vertex)

    return D[end_vertex], path