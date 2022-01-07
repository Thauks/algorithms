import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

class path_cache:
    def __init__(self):
        self.path = []
        self.distance = np.inf
    
    def update(self, path, distance):
        self.path = path
        self.distance = distance
    
    def reset(self):
        self.path = []
        self.distance = np.inf

PATH_CACHE = path_cache()

def dijkstra_rec(G:nx.Graph, start:int, end:int, distance=0, path=[], visited=[]):   # Returns the shortest path from start to end
    if start == end:
        global PATH_CACHE
        if PATH_CACHE.distance > distance:
            PATH_CACHE.update(path, distance)
        elif PATH_CACHE.distance == distance:
            if len(PATH_CACHE.path) > len(path):
                PATH_CACHE.update(path, distance)
    else:
        for n1, n2, w in G.edges(start, data=True):   
            if n2 not in visited:
                # print(n1, n2, end, w['weight'], distance, path, visited)
                dijkstra_rec(G, n2, end, distance+w['weight'], path + [n1], visited + [n1])


def graph_generator() -> nx.Graph:
    # Generates a graph and sets random weights to each edge
    G = nx.dorogovtsev_goltsev_mendes_graph(3)

    for n1, n2, data in G.edges(data=True):
        # get random weight between each node
        r_weight = round(random.uniform(0, 1)*10, 0)
        data['weight'] = int(r_weight)
    return G

def plot_graph(G:nx.Graph) -> None:
    # Plots the given nx.graph
    pos=nx.spring_layout(G) 
    nx.draw_networkx(G,pos)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    plt.show()
    

if __name__ == '__main__':
    shortest_paths = {}
    G = graph_generator()
    plot_graph(G)
    for i in G.nodes():
        for j in G.nodes():
            key = '-'.join(sorted([str(i), str(j)]))
            if key not in shortest_paths and i != j:
                dijkstra_rec(G, i, j)
                shortest_paths[key] = (PATH_CACHE.distance, PATH_CACHE.path)
                PATH_CACHE.reset()
            
    print(shortest_paths)