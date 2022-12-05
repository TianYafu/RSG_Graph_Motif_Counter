import math

import networkx as nx
import numpy as np
from itertools import combinations

import pickle
from matplotlib import pyplot as plt

def common_graph_motifs_undirected(n_nodes, ignore_unconnected_graph=True):
    '''
    Return lists of all common graph motifs which have <n_nodes> nodes.
    Label of node will be like 0, 1, 2, 3, 4
    :return: dict: { n_edges: list( nx.Graph() )}
    '''

    assert n_nodes != 0
    if(n_nodes == 1):
        G = nx.Graph()
        G.add_node(1)
        return {0:[G]}

    ret_dict = {}

    node_label_list = list(range(n_nodes))
    print("node_label_list", node_label_list)

    node_combination = list(combinations(node_label_list, 2))
    print(f"got {len(node_combination)} node_combinations = ", node_combination)

    min_n_edges, max_n_edges = n_nodes-1, int(n_nodes * (n_nodes-1) / 2)
    for n_edge in range(min_n_edges, max_n_edges+1):
        _temp_graph_list = []
        print(f"[info] generating motif with n_edge {n_edge} / {max_n_edges}")  # generating motif with n_edge 4 / 10
        edge_configuration = list(combinations(node_combination, n_edge))
        print(f"    got {len(edge_configuration)} graphs with n_edge = {n_edge}")
        # print("edge_configuration", edge_configuration)
        for i in edge_configuration:
            G = nx.Graph()
            G.add_nodes_from(node_label_list)
            G.add_edges_from(i)
            if(ignore_unconnected_graph==True and nx.is_connected(G) == False):
                continue
            for _g in _temp_graph_list:
                if(nx.is_isomorphic(G, _g)):
                    break
            else:
                _temp_graph_list.append(G)

        print(f"[info] Add {len(_temp_graph_list)} graphs from n_edge = {n_edge}")
        ret_dict[n_edge] = _temp_graph_list

    print(f"[info] End generating common graph motif, size={n_nodes}, n_graphs={len(ret_dict)}")
    return ret_dict


def visualize_graph_motifs(graphs_dict):
    '''

    :param graphs_dict: dict: { n_edges: list( nx.Graph() )}
    :return:
    '''
    flattened_graphs_dict = []
    for key in graphs_dict:
        for g in graphs_dict[key]:
            flattened_graphs_dict.append(g)

    n_graphs = len(flattened_graphs_dict)
    print("[info] amount of graphs: ", n_graphs)
    column = 8 # (8 graphs in a line)
    if(n_graphs >= 100):
        column = 20
    row = math.ceil(n_graphs/column)
    print(f"[info] will provide a {column} x {row} figure")

    n_nodes = flattened_graphs_dict[0].number_of_nodes()

    figsize = (column*0.5, row*0.6+2)
    fig = plt.figure(figsize=figsize)
    for index, g in enumerate(flattened_graphs_dict):
        _col, _row = index%column, int(index/column)
        print(f"    img position: {_col}, {_row}")
        ax = fig.add_subplot(row, column, index+1)
        nx.draw(g, ax=ax, node_size=10)
        ax.set_title(f"G{index}", fontsize=8)
    fig.suptitle(f'All graph motifs with {n_nodes} nodes', fontsize=16)
    plt.tight_layout()

    plt.show()

def save_graph_dict(n_nodes, graphs_dict):
    flattened_graphs_dict = []
    for key in graphs_dict:
        for g in graphs_dict[key]:
            flattened_graphs_dict.append(g)

    file_name = f"data/M_{n_nodes}.pkl"
    file_name_flattened = f"data/M_{n_nodes}_flattened.pkl"

    with open(file_name, "wb") as fh:
        pickle.dump(graphs_dict, fh)
    with open(file_name_flattened, "wb") as fh:
        pickle.dump(flattened_graphs_dict, fh)



if(__name__ == "__main__"):
    N_NODES = 7
    graphs_dict = common_graph_motifs_undirected(n_nodes=N_NODES, ignore_unconnected_graph=True)
    visualize_graph_motifs(graphs_dict)
    save_graph_dict(n_nodes=N_NODES, graphs_dict=graphs_dict)