python3 1.generate_temp_xml.py
python3 2.icg.py 
dot -Tpng -o graph.png ICG.dot
rm temp_xml_generated
python3 3.query_xml_tree.py
