cp PhysiCell_settings-v4-inherit2.xml PhysiCell_settings.xml
python flatten_covid19_cell_def_xml.py 
python create_cell_types.py new_flat_config.xml
cp new_flat_config.xml PhysiCell_settings.xml 
cp cell_types.py ../bin
