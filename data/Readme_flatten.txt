
# Manually insert missing params into "default" cell_definition, e.g. multiple <uptake_rate>, then:

~/git/pc4covid19-rheiland-master/data$
cp PhysiCell_settings-insert-default-uptake_rates.xml PhysiCell_settings.xml
python flatten_covid19_cell_def_xml.py 
#   Run the output file thru a XML validator!!
python create_cell_types.py flat.xml
cp flat.xml PhysiCell_settings.xml 
# Make sure it has: <folder>.</folder> AND <omp_num_threads>=4
cp cell_types.py ../bin

# may need to re-run xml2jupyter:
#   python xml2jupyter.py PhysiCell_settings.xml
#   cp user_params.py ../bin
#   cp microenv_params.py ../bin

# may need to update data/initial.xml

