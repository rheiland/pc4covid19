
# Manually insert missing params into "default" cell_definition, e.g. multiple <uptake_rate>, then:

~/git/pc4covid19-rheiland-master/data$
cp PhysiCell_settings-insert-default-update_rates.xml PhysiCell_settings.xml
python flatten_covid19_cell_def_xml.py 
#   Run the output file thru a XML validator!!
python create_cell_types.py flat.xml
cp flat.xml PhysiCell_settings.xml 
cp cell_types.py ../bin

# may need to re-run xml2jupyter to create new user_params.py
# may need to update data/initial.xml

