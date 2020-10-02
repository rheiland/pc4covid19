# flatten_covid19_cell_def_xml.py - convert a PhysiCell_settings.xml with inheritance of <cell_definitions>
#                                   into one without inheritance, i.e., verbose leaf <cell_definition>s.
#

import xml.etree.ElementTree as ET

tree = ET.parse("PhysiCell_settings.xml")  
xml_root = tree.getroot()
#uep = xml_root.find('.//cell_definitions')
#uep.items()
#xml_root.text
#xml_root.find('.//cell_definitions')

leaf_cell_types = ["lung epithelium", "CD8 Tcell", "macrophage", "neutrophil", "DC", "CD4 Tcell"]

f = open('new_config.xml', 'w')
with open('PhysiCell_settings.xml', 'r') as file:
    data = file.read()

default_start = data.index('<cell_definition ')
print('default_start = ',default_start)
default_end = data.index('</cell_definition>')
print('default_end = ',default_end)
default_str = data[default_start:default_end+19]

user_params_start = data.index('<user_parameters>')

f.write(data[:default_start])
f.write(default_str)  # default

idx = 1
for ctype in leaf_cell_types:
    f.write('\t\t<cell_definition name="' + ctype + '"  ID="' + str(idx) + '">\n')
    f.write(default_str[40:])
    idx += 1
f.write('\t</cell_definitions>\n\n')

f.write('\t' + data[user_params_start:])

f.close()