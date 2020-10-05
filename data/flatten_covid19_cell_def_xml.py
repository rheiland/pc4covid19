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
new_xml_file = 'new_flat_config.xml'
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

tree_flat = ET.parse(new_xml_file)  
xml_flat_root = tree_flat.getroot()

#--------------------------------------------------
print("--- Phase 2: edit the new .xml so each immune cell type has its parent's params.")

#immune_cell_defs = ["immune"]
#immune_cell_defs = ["CD8 Tcell"]
immune_cell_defs = ["CD8 Tcell", "macrophage", "neutrophil", "DC", "CD4 Tcell"]
		# <cell_definition name="immune" parent_type="default" ID="2">
		# 	<phenotype>
		# 		<mechanics> 
		# 			<cell_cell_adhesion_strength units="micron/min">0</cell_cell_adhesion_strength>
		# 			<cell_cell_repulsion_strength units="micron/min">10</cell_cell_repulsion_strength>
def update_all_immune_cell_def_params(xmlpath, save_param_val):
    for cell_def in immune_cell_defs:
        for cd in xml_flat_root.findall('cell_definitions//cell_definition'):  # find *this* cell_def in flattened XML
            if cd.attrib['name'] == cell_def:
                print('-- update ',cell_def, ', xmlpath=',xmlpath, " = ",save_param_val)
                cd.find('.'+xmlpath).text = save_param_val
                # cd.'.//cell_definition[1]//phenotype//mechanics//cell_cell_adhesion_strength').text = save_param_val

def recurse_node(root,xmlpath):
    global save_param_val
    xmlpath = xmlpath + "//" + root.tag[root.tag.rfind('}')+1:]
    param_val = ''
    for child in root:
        param_val = ' '.join(child.text.split())
        if param_val != '':
            # print('param value=',param_val, ' for ',end='')
            save_param_val = param_val
            # uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float27.value)
        recurse_node(child,xmlpath)
    if len(list(root)) == 0:
        # print(xmlpath)
        print(xmlpath,' = ',save_param_val)
        update_all_immune_cell_def_params(xmlpath, save_param_val)

idx = -1
uep = None
# for requested cell_def param values in the original (inheritance) XML, copy them into the new (flattened) XML
for cd in xml_root.findall('cell_definitions//cell_definition'):
    idx += 1
    if cd.attrib["name"] == "immune":
        uep = cd
        print("---------------- processing immune cell_def at idx= ",idx)   # 2  (0=default, 1=lung epi)
        # immune_uep = root.find('.//cell_definitions')
        for child in cd:
            print("------- calling recurse_node on child=",child)
            recurse_node(child,"")
#print(uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//enabled').text
#/phenotype/mechanicscell_cell_adhesion_strength/
#fullpath = ".//cell_definition[" + str(idx) + "]//phenotype//motility//options//chemotaxis//enabled"
#fullpath = "cell_definitions//cell_definition[" + str(idx) + "]//phenotype//mechanics//cell_cell_adhesion_strength"
#print(uep.find('.//cell_definition[2]//phenotype//mechanics//cell_cell_adhesion_strength').text)

# cell_adhesion = uep.find('.//phenotype//mechanics//cell_cell_adhesion_strength').text
# cell_repulsion = uep.find('.//phenotype//mechanics//cell_cell_repulsion_strength').text
# print("------ cell_adhesion = ",cell_adhesion)
# print("------ cell_repulsion = ",cell_repulsion)

# in fill_xml method of GUI tabs:
        # uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float27.value)

#print(cd.find(fullpath).text)
#uep = xml_root.find('.//cell_definitions')
#print(uep.find(fullpath).text)

# for cell_def in immune_cell_defs:
#     print("------ immune cell = ",cell_def)
#     xml_root = tree.getroot()
#     for cd in xml_root.findall('cell_definitions//cell_definition'):
#         # print(cd)
#         if cd.attrib["name"] == cell_def:
#             print("found ",cd.attrib["name"])
print("\nDone.")

#tree_flat.write("new_flat_config2.xml")
#tree_flat = ET.parse(new_xml_file)  
#f.close()
#--------------------------------------------------
print("--- Phase 3: edit the new .xml so each immune cell type has its specific params.")

def update_this_immune_cell_def_params(xmlpath, save_param_val, cell_def_name):
#    for cell_def in immune_cell_defs:
    for cd in xml_flat_root.findall('cell_definitions//cell_definition'):  # find *this* cell_def in flattened XML
        if cd.attrib['name'] == cell_def_name:
            print('-- update ',cell_def_name, ', xmlpath=',xmlpath, " = ",save_param_val)
            cd.find('.'+xmlpath).text = save_param_val

def recurse_node2(root,xmlpath, cell_def_name):
    global save_param_val
    xmlpath = xmlpath + "//" + root.tag[root.tag.rfind('}')+1:]
    param_val = ''
    for child in root:
        param_val = ' '.join(child.text.split())
        if param_val != '':
            # print('param value=',param_val, ' for ',end='')
            save_param_val = param_val
            # uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float27.value)
        recurse_node2(child,xmlpath,cell_def_name)
    if len(list(root)) == 0:
        # print(xmlpath)
        print(xmlpath,' = ',save_param_val)
        update_this_immune_cell_def_params(xmlpath, save_param_val, cell_def_name)


immune_cell_defs = ["CD8 Tcell", "macrophage", "neutrophil", "DC", "CD4 Tcell"]
for cd in xml_root.findall('cell_definitions//cell_definition'):
    idx += 1
    if cd.attrib["name"] in immune_cell_defs:
        uep = cd
        # print("---------------- processing immune cell_def at idx= ",idx)   # 2  (0=default, 1=lung epi)
        print("---------------- processing ",cd.attrib["name"])   # 2  (0=default, 1=lung epi)
        # immune_uep = root.find('.//cell_definitions')
        for child in cd:
            print("------- calling recurse_node on child=",child)
            recurse_node2(child,"",cd.attrib["name"])

print("\nDone.")
tree_flat.write("new_flat_config.xml")
#--------------------------------------------------
#tree_flat = ET.parse(new_xml_file)  
#xml_root = tree.getroot()
#tree_flat.write("new_flat_config2.xml")

#print("\nDone. Please check the output file: " + new_xml_file + "\n")
print("\nDone. Please check the output file: new_flat_config.xml\n")