# cpp-include-walker
Script to extract include graph from any C++ code. Currently used to create include graphs for game engines.

## Author
Gabriel C. Ullmann, 2022

## How to use
- In the "filepaths" folder, place a CSV file separated by semicolon containing: engine  name, subsystem prefix (name), base/root folder for the subsystem, subfolders of the subsystem. You can use "subsystems.csv" as an example.
- Execute "main.py" to generate a text representation (vector) of the include graph.
- Vectors are saved in CSV format in the "vectors" folder.
- If you want to generate a visual representation (image) of the graph, use the draw_graph function in walker_graph.py.
- Images will be saved in the "images" folder in PDF format.