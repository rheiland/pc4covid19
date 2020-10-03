# flatten_covid19_cell_def_xml.py - convert a PhysiCell_settings.xml with inheritance of <cell_definitions>
#                                   into one without inheritance, i.e., verbose leaf <cell_definition>s.
#
# Note: leaf cell defs are hard-coded in this script for now.
#
# Author: Randy Heiland
#

import xml.etree.ElementTree as ET

tree = ET.parse("PhysiCell_settings.xml")  
xml_root = tree.getroot()
#uep = xml_root.find('.//cell_definitions')
#uep.items()
#xml_root.text
#xml_root.find('.//cell_definitions')

#leaf_cell_defs = ["lung epithelium", "CD8 Tcell", "macrophage", "neutrophil", "DC", "CD4 Tcell"]
leaf_cell_defs = {"lung epithelium":"1", "CD8 Tcell":"3", "macrophage":"4", "neutrophil":"5", "DC":"6", "CD4 Tcell":"7"}

#--------------------------------------------------
print("--- Phase 1: create a new .xml containing 6 copies of 'default' cell_definition, with desired names.")

# output file: new, flattened config file
new_xml_file = 'new_config.xml'
f = open(new_xml_file, 'w')

# read the original config file into a string
with open('PhysiCell_settings.xml', 'r') as file:
    data = file.read()

default_start = data.index('<cell_definition ')  # find the start of the 'default' cell_def
#print('default_start = ',default_start)
default_end = data.index('</cell_definition>')   # find the end of the 'default' cell_def
#print('default_end = ',default_end)
default_str = data[default_start:default_end+19]   # put entire 'default' cell_def into a string

user_params_start = data.index('<user_parameters>')

f.write(data[:default_start])   # copy over everything up to the start of the 'default' cell_def
f.write(default_str)  # copy the 'default'

idx = 1
# copy the 'default', but substitute the name and ID to be the leaf cell_defs
for ctype in leaf_cell_defs.keys():
    # f.write('\t\t<cell_definition name="' + ctype + '"  ID="' + str(idx) + '">\n')
    # f.write('\t\t<cell_definition name="' + ctype + '" parent_type="default"  ID="' + str(idx) + '">\n')
    f.write('\t\t<cell_definition name="' + ctype + '" parent_type="default"  ID="' + leaf_cell_defs[ctype] + '">\n')
    f.write(default_str[40:])
    idx += 1
f.write('\t</cell_definitions>\n\n')

# append the <user_parameters> block, plus the terminating '</PhysiCell_settings>'
f.write('\t' + data[user_params_start:])

f.close()
print("\nDone.")

#--------------------------------------------------
print("--- Phase 2: edit the new .xml so each immune cell type has its parent's params.")
		# <cell_definition name="immune" parent_type="default" ID="2">
		# 	<phenotype>
		# 		<mechanics> 
		# 			<cell_cell_adhesion_strength units="micron/min">0</cell_cell_adhesion_strength>
		# 			<cell_cell_repulsion_strength units="micron/min">10</cell_cell_repulsion_strength>
print("\nDone.")

#--------------------------------------------------
print("--- Phase 3: edit the new .xml so each immune cell type has its specific params.")

print("\nDone. Please check the output file: " + new_xml_file + "\n")
print("--- Phase 1: create a new .xml containing 6 copies of 'default' cell_definition, with desired names.")