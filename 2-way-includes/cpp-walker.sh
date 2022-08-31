# 1 path to folder with all subsystems
# 2 path to necessary includes
# 3 engine_subsystem name (to be used as result file name)
# 4 subsystem folders

rm subsystem.dot
rm edge_count.csv
perl src/cinclude2dot.pl --src=$1 --include=$2 --paths >> subsystem.dot
python3 src/remove_linebreaks.py
gvpr -f src/count_edges.gvpr subsystem.dot >> edge_count.csv
python3 src/order_edges.py $3 $4

