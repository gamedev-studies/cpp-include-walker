dot_file = open("subsystem.dot", "r")
new_file = ""
for line in dot_file:
    new_file += line.replace("\\n", "")
dot_file.close()
print("====================")

dot_file = open("subsystem.dot", "w")
dot_file.write(new_file)
dot_file.close()