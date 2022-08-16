import walker_core
import walker_str
import walker_graph

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
    list_of_includes = walker_str.extract_includes(subsystem[1], subsystem_files[counter])
    counter += 1

    # create an include graph
    graph = walker_graph.create_graph(list_of_includes)

    # get a list of all nodes (without duplicates)
    unique_nodes = walker_graph.get_unique_node_list(graph)

    # generate unique IDs to be assigned to nodes
    unique_ids = walker_str.generate_unique_node_ids(unique_nodes)

    # generate a dataset with each node name, includes for each node and include count
    # this is an intermediate representation between graph and vector
    ds = walker_graph.build_ds_from_graph(graph, unique_ids)

    # generate text representation (vector) of graph
    vector = walker_str.get_vector_from_graph(ds)
    result_csv.append(subsystem[0] + ";" + subsystem[1] + ";" + str(vector))
    walker_core.save_vector_as_csv(result_csv, subsystem[0] + "_" + subsystem[1].lower())

    # generate visual representation (image) of graph
    #walker_graph.draw_graph(graph, subsystem[0] + "_" + subsystem[1].lower())

