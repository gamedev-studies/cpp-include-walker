import numpy as np
import walker_core

def extract_includes(prefix, subsystem_files):
    include_list = []
    parts_to_remove = walker_core.get_strings_to_remove(prefix)
    for subsystem_file in subsystem_files:
        if walker_core.is_cpp_file(subsystem_file):
            current_file = open(subsystem_file, "r")
            for line in current_file:
                if line.strip().startswith("#include"):
                    clean_name = line.strip()
                    for part in parts_to_remove:
                        clean_name = clean_name.replace(part, "")
                    include_list.append((subsystem_file, clean_name))
    return include_list

def generate_unique_node_ids(node_list):
    ascii_begin = 65
    ascii_end = 91
    ascii_limit = ascii_end - ascii_begin
    alphabet = np.arange(ascii_begin, ascii_end)
    all_node_names = np.array([])
    for node in node_list:
        all_node_names = np.append(all_node_names, str(node).strip())
    unique_names = np.unique(all_node_names)
    name_map = {}
    counter = 0
    cycle = 1
    for name in unique_names:
        name_map[name] = chr(alphabet[counter]) + str(cycle)
        counter += 1
        if counter == ascii_limit:
            counter = 0
            cycle += 1
    return name_map

def get_vector_from_graph(ds):
    result = ""
    for item in ds.values:
        str_to_add = item[2] + "inc" + ("NULL" if (item[3] == "") else item[3])
        if result == "":
            result += str_to_add
        else:
            result += "," + str_to_add
    return result