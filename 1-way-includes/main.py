import walker_core
import walker_str
import walker_graph

def start_by_entrypoints(engine_base_path, list_of_entrypoints, itr = 0, max_itr = 5, arr_result = []):
    # get all includes for each file
    try:
        print("Generating for", len(list_of_entrypoints), "file(s)")
        list_of_includes = walker_str.extract_includes(list_of_entrypoints)
    except UnicodeDecodeError:
        print("UnicodeDecodeError")
    
    arr_tmp = []
    for include in list_of_includes:
        arr_result.append(include)
        include_name = include[1].strip()
        if not "/" in include_name:
            include_parent = include[0].split("/")
            include_name = "/".join(include_parent[0:len(include_parent)-1])
            include_name = include_name.strip()
        arr_tmp.append(engine_base_path + "/" + include_name)

    if itr < max_itr:
        itr += 1
        start_by_entrypoints(engine_base_path, arr_tmp, itr, max_itr, arr_result)

    return arr_result

def start_by_most_includes():
    # resulting .csv will be stored here
    # separated by semicolon
    result_csv = ["engine;subsystem;vector"]
    subsystems_path = "./filepaths/subsystems.csv"
    separator = ";"

    # get all paths to subsystems of all engines
    subsystem_ds, subsystem_files = walker_core.load_subsystems_file(subsystems_path, separator)

    # for each subsystem
    counter = 0
    for subsystem in subsystem_ds:

        # get all includes for each file
        try:
            print("Generating:", subsystem[0] + "_" + subsystem[1])
            list_of_includes = walker_str.extract_includes(subsystem_files[counter], subsystem[1])
            counter += 1
        except UnicodeDecodeError:
            counter += 1
            print("UnicodeDecodeError")

        # create an include graph
        graph = walker_graph.create_graph(list_of_includes)

        # get a list of all nodes (without duplicates)
        unique_nodes = walker_graph.get_unique_node_list(graph)

        # generate unique IDs to be assigned to nodes
        unique_ids = walker_str.generate_unique_node_ids(unique_nodes)

        # generate a dataset with each node name, includes for each node and include count
        # this is an intermediate representation between graph and vector
        ds = walker_graph.build_ds_from_graph(graph, unique_ids, True)

        # generate text representation (vector) of graph
        vector = walker_str.get_vector_from_graph(ds)
        result_csv.append(subsystem[0] + ";" + subsystem[1] + ";" + str(vector))
        walker_core.save_vector_as_csv(result_csv, subsystem[0] + "_" + subsystem[1].lower())
        result_csv = ["engine;subsystem;vector"]

        # generate visual representation (image) of graph
        #walker_graph.draw_graph(graph, subsystem[0] + "_" + subsystem[1].lower())

def start_by_include_order():
    # resulting .csv will be stored here
    # separated by semicolon
    result_csv = ["engine;subsystem;vector"]
    subsystems_path = "./filepaths/subsystems2.csv"
    separator = ";"
    filename = "z1"

    # get all paths to subsystems of all engines
    subsystem_ds, subsystem_files = walker_core.load_subsystems_file(subsystems_path, separator, "", False)

    # get all includes for each file
    include_list = []
    for subsystem in subsystem_ds:
        try:
            #print("Generating:", subsystem[0] + "_" + subsystem[1])
            parts_to_remove = walker_core.get_strings_to_remove(subsystem[1])
            all_subsystem_folders = subsystem[3].split(",")
            for subsystem_file in subsystem_files[0]:
                if walker_core.is_cpp_file(subsystem_file):
                    #print("For file:", subsystem_file)
                    current_file = open(subsystem_file, "r")
                    for line in current_file:
                        if line.strip().startswith("#include"):
                            clean_name = line.strip()
                            for folder in all_subsystem_folders:
                                if folder in clean_name:
                                    for part in parts_to_remove:
                                        clean_name = clean_name.replace(part, "")
                                    clean_name = walker_str.remove_comments(clean_name)
                                    include_list.append((subsystem_file, clean_name))
                #print("Includes are:", include_list)
        except UnicodeDecodeError:
            print("UnicodeDecodeError")

        # create an include graph
        graph = walker_graph.create_graph(include_list)

        # get a list of all nodes (without duplicates)
        unique_nodes = walker_graph.get_unique_node_list(graph)

        # generate unique IDs to be assigned to nodes
        unique_ids = walker_str.generate_unique_node_ids(unique_nodes)
        
        # generate a dataset with each node name, includes for each node and include count
        # this is an intermediate representation between graph and vector
        ds = walker_graph.build_ds_from_graph(graph, unique_ids, True)

        # generate text representation (vector) of graph
        vector = walker_str.get_vector_from_graph(ds)
        result_csv.append(subsystem[0] + ";" + subsystem[1] + ";" + str(vector))
        walker_core.save_vector_as_csv(result_csv, filename)
        walker_core.save_vector_as_csv(unique_ids, filename + "-ref")
        result_csv = ["engine;subsystem;vector"]

def main_start_by_entrypoints():
    depth = 4
    filename = "z1"
    engine_base = '/media/ullmann/Portable Drive/engines/godot'
    subsystem_entrypoint = ['/media/ullmann/Portable Drive/engines/godot/servers/audio_server.cpp']
    list_of_includes = start_by_entrypoints(engine_base, subsystem_entrypoint, 0, depth, [])

    # create an include graph
    graph = walker_graph.create_graph(list_of_includes)

    # get a list of all nodes (without duplicates)
    unique_nodes = walker_graph.get_unique_node_list(graph)

    # generate unique IDs to be assigned to nodes
    unique_ids = walker_str.generate_unique_node_ids(unique_nodes)

    # generate a dataset with each node name, includes for each node and include count
    # this is an intermediate representation between graph and vector
    ds = walker_graph.build_ds_from_graph(graph, unique_ids, False)

    # generate text representation (vector) of graph
    vector = walker_str.get_vector_from_graph(ds)
    result_csv = ["engine;subsystem;vector"]
    result_csv.append(engine_base + ";" + str(subsystem_entrypoint) + ";" + str(vector))
    walker_core.save_vector_as_csv(result_csv, filename)
    walker_core.save_vector_as_csv(unique_ids, filename + "-ref")

def main():
    start_by_include_order()

main()