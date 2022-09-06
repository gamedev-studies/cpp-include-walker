# cpp-include-walker
This program iterates over all files in a program and counts the number of includes through different methods. By Gabriel C. Ullmann, 2022.

# 1-way-includes
It takes each file, check which files it includes, but DOES NOT check which files include it.

## How to use it?
- In the "filepaths" folder, place a CSV file separated by semicolon containing: engine  name, subsystem prefix (name), base/root folder for the subsystem, subfolders of the subsystem. You can use "subsystems.csv" as an example.
- Execute "main.py" to generate a text representation (vector) of the include graph.
- Vectors are saved in CSV format in the "vectors" folder.
- If you want to generate a visual representation (image) of the graph, use the draw_graph function in walker_graph.py.
- Images will be saved in the "images" folder in PDF format.

# 2-way-includes
It takes each file, check which files it includes, and which files include it.

## How to use it?
You can see a step-by-step below. You can also see examples in the "filepaths" folder.

- Enter the "2-way-includes" folder
- Execute cpp-walker.sh passing the following parameters:
    1. Engine root folder (absolute path)
    2. Search for includes in these folders (can be the same as 1 if there are no external/third party folders to include in the search)
    3. Engine name
    4. Subsystem name
    5. List of subsystem folders separated by comma (path relative to the engine's root)
- The graphviz include graph and data that is reused on every run for every subsystem will be generated and saved to the "graphs" folder
- The resulting vector and name map can be found in the "results" folder