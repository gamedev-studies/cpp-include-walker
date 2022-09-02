# remove weird line breaks from .dot file
# this allows to look for filenames more easily
# remove first
dot_file = open("subsystem.dot", "r")
new_file = ""
for line in dot_file:
    new_file += line.replace("\\n", "")
dot_file.close()

# write to file after
dot_file = open("subsystem.dot", "w")
dot_file.write(new_file)
dot_file.close()

# 2
dot_file = open("edge_count.csv", "r")
new_file = ""
for line in dot_file:
    new_file += line.replace("\\n", "")
dot_file.close()

# 2
dot_file = open("edge_count.csv", "w")
dot_file.write(new_file)
dot_file.close()