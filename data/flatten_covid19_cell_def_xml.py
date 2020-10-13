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
leaf_cell_defs = {"lung epithelium":"1", "CD8 Tcell":"3", "macrophage":"4", "neutrophil":"5", "DC":"6", "CD4 Tcell":"7"}

#--------------------------------------------------
print("--- Phase 1: create a new .xml containing 6 copies of 'default' cell_definition, with desired names.")

#tree0 = tree
#flat_root = xml_root
# default_cell_def = xml_root.find("cell_definitions//cell_definition[@name='default']")
cell_defs = tree.find('cell_definitions')
# root_node = cell_defs.getroot()
#--------------------------------------------------
print("--- Remove all but default cell_defs")
for cell_def in list(cell_defs):
    # print(cell_def.tag, cell_def.attrib['name'])
    if (cell_def.attrib['name'] != 'default'):
        print("removing ", cell_def.attrib['name'])
        cell_defs.remove(cell_def)
        # ET.SubElement(root_node,default_cell_def)
        # cell_defs.insert(0,default_cell_def)

#--------------------------------------------------
# Get a copy of the "default"
default_cell_def = xml_root.find("cell_definitions//cell_definition[@name='default']")
print("--- Insert duplicate default cell_def for each leaf")
for leaf in leaf_cell_defs:
    # print('-- ',leaf)
#    print(cell_def.tag, cell_def.attrib['name'])
    # print("insert default for ", leaf.attrib['name'])
    # print("insert default for ", leaf)
    # default_cell_def.attrib['name'] = leaf
    # tmp_cd.attrib['name'] = leaf
    # cell_defs.insert(0,default_cell_def)
    cell_defs.insert(0,default_cell_def)

new_xml_file = "new_flat_config1.xml"
# new_xml_file = "flat.xml"
tree.write(new_xml_file)

#--------------------------------------------------
tree = ET.parse("new_flat_config1.xml")  
# tree = ET.parse(new_xml_file)  
cell_defs = tree.find('cell_definitions')
xml_root = tree.getroot()

print("--- Change cell_def name for each leaf")
idx = -1
leaf_name = list(leaf_cell_defs.keys())
for cell_def in list(cell_defs):
# for leaf in leaf_cell_defs:
    if idx >= 0:
        cell_def.attrib['name'] = leaf_name[idx]
        cell_def.attrib['ID'] = leaf_cell_defs[leaf_name[idx]]
        # insert parent = "default" attribute
        cell_def.set("parent","default")

        print(cell_def.attrib['name'])
    idx += 1
    # cell_def.attrib['name'] = leaf

#tree = tree0
# default_cell_def = xml_root.find("cell_definitions//cell_definition[@name='default']")
# ET.SubElement(cell_defs, default_cell_def)

new_xml_file = "new_flat_config1.xml"
tree.write(new_xml_file)

print("\nDone. Please check the output file: " + new_xml_file + "\n")

#--------------------------------------------------
print("--- Phase 2: edit the new .xml so each immune cell type has its parent's params (<cell_definition name='immune' parent_type='default' ...>)")

tree_flat = ET.parse("new_flat_config1.xml")  
# tree_flat = ET.parse(new_xml_file)  
# tree = ET.parse("PhysiCell_settings.xml")  
xml_flat_root = tree_flat.getroot()

immune_cell_defs = ["CD8 Tcell", "macrophage", "neutrophil", "DC", "CD4 Tcell"]
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
# tree = ET.parse("PhysiCell_settings.xml")  
tree = ET.parse("new_flat_config1.xml")  
xml_root = tree.getroot()
uep = None
# for requested cell_def param values in the original (inheritance) XML, copy them into the new (flattened) XML
for cd in xml_root.findall('cell_definitions//cell_definition'):
    idx += 1
    if cd.attrib["name"] == "immune":
        uep = cd
        print("---------------- processing immune cell_def at idx= ",idx)   # 2  (0=default, 1=lung epi)
        # immune_uep = root.find('.//cell_definitions')
        for child in cd:
            if child.tag != 'custom_data':
                print("------- calling recurse_node on child=",child)
                recurse_node(child,"")
print("\nDone.")

new_xml_file = "new_flat_config2.xml"
tree_flat.write(new_xml_file)
print("\nDone. Please check the output file: " + new_xml_file + "\n")

#--------------------------------------------------
print("--- Phase 3: edit the new .xml so each immune cell type has its specific params (from the ORIGINAL .xml).")

tree_orig = ET.parse("PhysiCell_settings.xml")  
xml_orig = tree_orig.getroot()

tree_flat = ET.parse("new_flat_config2.xml")  
# tree_flat = ET.parse(new_xml_file)  
xml_flat_root = tree_flat.getroot()  # we'll update xml_flat_root (and write to a new output file)

def update_this_immune_cell_def_params(xmlpath, save_param_val, cell_def_name):
#    for cell_def in immune_cell_defs:
    for cd in xml_flat_root.findall('cell_definitions//cell_definition'):  # find *this* cell_def in flattened XML
        if cd.attrib['name'] == cell_def_name:
            if len(xmlpath) > 13:  # i.e., not equal to just "//custom_data" (with no param name)
                print('-- update ',cell_def_name, ', xmlpath=',xmlpath, " = ",save_param_val)
                cd.find('.'+xmlpath).text = save_param_val

def recurse_node2(root,xmlpath, cell_def_name):
    global save_param_val
    xmlpath = xmlpath + "//" + root.tag[root.tag.rfind('}')+1:]
    param_val = ''
    for child in root:
        if child.text == None:
            print(">>>> ", child, ".text is None")
            continue
        param_val = ' '.join(child.text.split())
        if param_val != '':
            # print('param value=',param_val, ' for ',end='')
            save_param_val = param_val
        recurse_node2(child,xmlpath,cell_def_name)
    if len(list(root)) == 0:
        # print(xmlpath)
        print(xmlpath,' = ',save_param_val)
        update_this_immune_cell_def_params(xmlpath, save_param_val, cell_def_name)
        save_param_val = None


immune_cell_defs = ["CD8 Tcell", "macrophage", "neutrophil", "DC", "CD4 Tcell"]
for cd in xml_orig.findall('cell_definitions//cell_definition'):
    idx += 1
    if cd.attrib["name"] in immune_cell_defs:
        uep = cd
        print("\n---------------- processing ",cd.attrib["name"])   # 2  (0=default, 1=lung epi)
        # immune_uep = root.find('.//cell_definitions')
        for child in cd:
            print("------- calling recurse_node2 on child=",child)
            recurse_node2(child,"",cd.attrib["name"])

print("\nDone.")

#new_xml_file = "new_flat_config3.xml"
new_xml_file = "flat.xml"
tree_flat.write(new_xml_file)

print("---> wrote ",new_xml_file, "(copy it to PhysiCell_settings.xml if desirable)\n")