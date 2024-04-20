import networkx as nx
import city_graph
from dijkstras_algorithm import dijkstras_algorithm

# Convert NetworkX graph into a dict of dicts
G_dict = nx.to_dict_of_dicts(city_graph.G)

start_vertex = "NY"
end_vertex = "CA2"

import time

def main():
    # Your Implementation
    start_time = time.perf_counter()
    distance, path = dijkstras_algorithm(G_dict, start_vertex, end_vertex)
    end_time = time.perf_counter()
    print("Execution time (Own Implementation):", end_time - start_time, "seconds")
    print("Shortest distance (Own Implementation):", distance)
    print("Shortest path (Own Implementation):", path)

    # NetworkX Implementation
    start_time = time.perf_counter()
    nx_distance = nx.shortest_path_length(city_graph.G, start_vertex, end_vertex, weight='weight')
    nx_path = nx.shortest_path(city_graph.G, start_vertex, end_vertex, weight='weight')
    end_time = time.perf_counter()
    print("Execution time (NetworkX):", end_time - start_time, "seconds")
    print("Shortest distance (NetworkX):", nx_distance)
    print("Shortest path (NetworkX):", nx_path)


if __name__ == "__main__":
    main()