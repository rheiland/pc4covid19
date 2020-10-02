
~/git/pc4covid19-rheiland-master/data$
  729  cp PhysiCell_settings-v4-inherit.xml PhysiCell_settings.xml
  730  python flatten_covid19_cell_def_xml.py 
  731  python create_cell_types.py new_config.xml 
  732  cp new_config.xml PhysiCell_settings.xml 
  733  cp cell_types.py ../bin
