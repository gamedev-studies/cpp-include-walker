rm subsystem.dot
rm edge_count.csv
perl src/cinclude2dot.pl --src=$1 >> subsystem.dot
gvpr -f src/count_edges.gvpr subsystem.dot >> edge_count.csv
python3 src/order_edges.py