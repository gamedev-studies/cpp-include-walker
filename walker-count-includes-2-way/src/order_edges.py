import pandas as pd
import numpy as np

def get_vector_format(line):
    result = line.strip().replace("\"", "").split("->")
    return list(map(lambda item: item.strip(), result)) 

def generate_unique_node_ids(node_list, id_type):
    name_map = {}
    all_node_names = np.array([])

    if id_type == "string":
        ascii_begin = 65
        ascii_end = 91
        ascii_limit = ascii_end - ascii_begin
        alphabet = np.arange(ascii_begin, ascii_end)
    elif id_type == "number":
        starting_number = 1

    #get unique names
    for node in node_list:
        all_node_names = np.append(all_node_names, str(node).strip())
    unique_names = np.unique(all_node_names)

    counter = 0
    if id_type == "string":
        cycle = 1
        for name in unique_names:
            name_map[name] = chr(alphabet[counter]) + str(cycle)
            counter += 1
            if counter == ascii_limit:
                counter = 0
                cycle += 1
    elif id_type == "number":
        counter = starting_number
        for name in unique_names:
            name_map[name] = str(counter)
            counter += 1
    else:
        print("Error: unknown ID type. Types allowed: string, number.")

    return name_map

def concat_vector_items(id_type, ordered_dot_ids):
    result_vector = ""
    first_item = True
    if id_type == "string":
        for file_id in ordered_dot_ids:
            if first_item:
                result_vector += "inc".join(file_id)
                first_item = False
            else:
                result_vector += "," + ("inc".join(file_id))
    elif id_type == "number":
        for file_id in ordered_dot_ids:
            pair = ",".join(file_id)
            if first_item:
                result_vector += "(" + pair + ",1)"
                first_item = False
            else:
                result_vector += ",(" + pair + ",1)"
    return result_vector

def gen_vector(id_type="string", save_to_file=True):
    # order and save
    ds = pd.read_csv('edge_count.csv')
    ds = ds.sort_values(by="sum", ascending=False)
    ds = ds[(ds.includes != "includes")]
    ds.to_csv('edges_ordered.csv')

    # use the ordered ds
    dot_file = open("subsystem.dot", "r")
    dot_file_lines = []
    for line in dot_file:
        dot_file_lines.append(line)
    ordered_file_names = ds['edge'].values #[0:2]
    name_map = generate_unique_node_ids(ordered_file_names, id_type)
    ordered_dot = []
    for file_name in ordered_file_names:
        for line in dot_file_lines:
            if file_name + "\" ->" in line:
                ordered_dot.append(get_vector_format(line))
    ordered_dot_ids = []
    for line in ordered_dot:
        node = ""
        include = ""
        try:
            node = name_map[line[0]]
            include = name_map[line[1]]
        except KeyError:
            #print("err")
            pass
        ordered_dot_ids.append([node, include])

    result_vector = concat_vector_items(id_type, ordered_dot_ids)

    if not save_to_file:
        print(result_vector)
        print(name_map)
    else:
        vector_file = open("vector.csv", "w")
        vector_file.write(result_vector)
        vector_file.close()

        map_file = open("vector_map.json", "w")
        map_file.write(str(name_map))
        map_file.close()

gen_vector("number")