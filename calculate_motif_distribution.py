import networkx as nx
import numpy as np
import time

from load_graph_motifs import load_motif_list

from matplotlib import pyplot as plt

def calc_motif_distribution(G, graph_motif_list):
    '''
    :param G:
    :param graph_motif_list: list( nx.Graph )
    :return: hist: np.array(int) represents the occurrence of graph motifs in param graph_motif_list
    '''

    hist = np.zeros(len(graph_motif_list), dtype=int)
    print(f"[info] calc_motif_distribution: {len(graph_motif_list)} graphs to go ")
    for index, motif in enumerate(graph_motif_list):
        if(motif.number_of_nodes() == 1):
            hist[index] = G.number_of_nodes()
            continue
        if(motif.number_of_nodes() == 2):
            hist[index] = G.number_of_edges()
            continue

        if(index % 10 == 0):
            pass

        t0 = time.perf_counter()
        GM = nx.algorithms.isomorphism.GraphMatcher(G, motif)
        for subgraph in GM.subgraph_isomorphisms_iter():
            hist[index] += 1
        t1 = time.perf_counter()
        print(f"    progress: {index}/{len(graph_motif_list)} usint time {t1-t0}")
    return hist

def render_motif_hist(hist, graph_motif_list):
    '''
    Render distribution using pyplot
    :param hist:
    :param graph_motif_list:
    :return:
    '''
    X = [index for index, i in enumerate(hist)]
    Y = hist

    fig = plt.figure(figsize=(10, 5))
    # creating the bar plot
    plt.bar(X, Y, color='maroon', width=0.4)

    plt.xlabel("Graph motif number")
    plt.ylabel("occurrence")
    plt.title("Graph motif distribution")
    plt.show()


if(__name__ == "__main__"):
    motif_list = load_motif_list([1,2,3,4,5,6])
    # G = load_motif_list([7])[100]  # use M7(100) as a sample
    G = nx.gnp_random_graph(50, 0.3)
    nx.draw(G)
    hist = calc_motif_distribution(G, motif_list)
    print(hist)
    render_motif_hist(hist, motif_list)