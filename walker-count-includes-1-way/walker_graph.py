import numpy as np
import pandas as pd
import networkx as nx
from matplotlib import pyplot as plt

def create_graph(list_of_includes):
    graph = nx.DiGraph()
    graph.add_edges_from(list_of_includes)
    return graph

def draw_graph(graph, filename):
    plt.figure(figsize=(22,22))
    plt.tight_layout()
    pos = nx.spring_layout(graph, 20)
    nx.draw(graph, pos, with_labels=True)
    if filename:
        plt.savefig("./images/" + filename + ".pdf", format="PDF")

def get_unique_node_list(graph):
    result = []
    aux = np.unique(np.array(graph.nodes()))
    for a in aux:
        result.append(a.strip())
    return result

def build_ds_from_graph(graph, unique_names, order_by_count = False, debug=False):
    node_main = []
    node_include = []
    node_include_count = []
    node_code = []
    include_code = []
    aux_name_dict = {}
    for node in nx.nodes(graph):
        counter = 0
        count_includes = 0
        if debug:
            print("for node:", node)
        for include in nx.neighbors(graph, node):
            if include.strip():
                node_main.append(node.strip())
                node_include.append(include.strip())
                count_includes += 1
            
        if count_includes == 0:
            if debug:
                print("no includes")
            node_main.append(node.strip())
            node_include.append("")
            if not str(node).strip() in aux_name_dict:
                aux_name_dict[str(node).strip()] = 0
        else:
            if debug:
                print(count_includes, "includes")
            aux_name_dict[str(node).strip()] = count_includes
        if debug:
            print("===========")
            
    full_ds = pd.DataFrame()
    full_ds['node_filename'] = node_main
    full_ds['include_filename'] = node_include
    
    for node in node_main:
        node_code.append(unique_names[node])
        node_include_count.append(aux_name_dict[node])  
    full_ds['node_code'] = node_code
        
    for node in node_include:
        if node:
            include_code.append(unique_names[node])
        else:
            include_code.append("")
    full_ds['include_code'] = include_code
    
    full_ds['total_includes'] = node_include_count
    
    if debug:
        print("Before false empty removal:", len(full_ds))
    full_ds = remove_false_empty(full_ds)
    if debug:
        print("After false empty removal:", len(full_ds))
    
    if order_by_count:
        return full_ds.sort_values(['total_includes', 'node_filename', 'include_filename'], ascending = [False, True, True])
    else:
        return full_ds

def remove_false_empty(ds, debug=False):
    ds2 = ds
    ds_filter_empy = ds[(ds.include_filename == "")]
    list_empty_include_index = ds_filter_empy.index
    list_empty_include = ds_filter_empy.values
    counter = 0
    for item in list_empty_include:
        ds_aux = ds[ds.node_filename == item[0]]
        if len(ds_aux) > 1:
            if debug:
                print("should delete:", item, len(ds_aux))
            ds2 = ds2.drop(index=list_empty_include_index[counter])
        counter += 1
    return ds2
