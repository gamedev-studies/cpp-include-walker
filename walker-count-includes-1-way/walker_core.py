import os
import pandas as pd

def load_subsystems_file(path, separator, engine="", debug=False):
    results = []
    ds_subs = pd.read_csv(path, sep=separator)
    if engine:
        ds_subs = ds_subs[(ds_subs.engine == engine)]
    for sub in ds_subs.values:
        subsystem_filenames = get_subsystem_filenames(sub[2], sub[3].split(","), False)
        results.append(subsystem_filenames)
        if debug:
            print("==========")
            print(subsystem_filenames)
            print("==========")
    return ds_subs.values, results

def do_walk(path):
    result = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            result.append(os.path.join(root, name))
    return result

def get_subsystem_filenames(base_path, folders, debug=False):
    result = []
    for folder in folders:
        if debug:
            print("=== Processing:", folder)
        full_path = base_path + "/" + folder
        files_in_folder = do_walk(full_path)
        if debug:
            print("=== files_in_folder:", full_path, files_in_folder)
        filtered_files = filter_cpp_files(files_in_folder)
        for file in filtered_files:
            result.append(file)
    return result

def filter_cpp_files(file_list):
    if file_list:
        return list(filter(is_cpp_file, file_list))
    return []

def is_cpp_file(filename, debug=False):
    extensions = get_cpp_extensions()
    for extension in extensions:
        if extension in filename:
            if debug:
                print(filename)
            return True
    return False

def get_cpp_extensions():
    return [".cpp", ".h"]

def get_strings_to_remove(prefix=None):
    base_list = ["#include", "\"", "../", "<", ">"]
    if prefix:
        base_list.append(prefix + "/")
    return base_list

def save_vector_as_csv(vector, name):
    if name:
        f = open("./vectors/" + name + ".csv", "w")
        if "dict" in str(type(vector)):
            for key, value in vector.items():
                f.write(value + "," + key + "\n")
        else:
            for item in vector:
                f.write(item + "\n")
        f.close()
    else:
        print("No filename informed.")