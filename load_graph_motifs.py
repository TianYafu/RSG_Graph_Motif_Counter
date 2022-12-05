import pickle
import networkx as nx
import os

def load_motif_list(n_nodes_list):
    '''

    :param n_nodes_list: list(int) lists of graph motif to be returned
                         E.g. n_nodes_list = [1, 2, 3]
                              will return every graph motif with nodes amount 1, 2, and 3
    :return: list( nx.Graph )
    '''
    ret_list = []
    for i in n_nodes_list:
        file_name = f"data/M_{i}_flattened.pkl"
        assert os.path.isfile(file_name)
        with open(file_name, "rb") as fh:
            graph_list = pickle.load(fh)
            ret_list = ret_list + graph_list
    print(f"[info] Loads {len(ret_list)} graphs with nodes {n_nodes_list}")
    return ret_list


if(__name__ == "__main__"):
    graph_list = load_motif_list([1,2,3,4,5,6,6])
    # print(graph_list)