
~/git/pc4covid19-rheiland-master/data$
cp PhysiCell_settings-v4-inherit2.xml PhysiCell_settings.xml
python flatten_covid19_cell_def_xml.py 
python create_cell_types.py flat.xml
cp flat.xml PhysiCell_settings.xml 
cp cell_types.py ../bin
