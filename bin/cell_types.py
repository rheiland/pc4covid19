 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box,Dropdown
    
class CellTypesTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        widget_layout_long = {'width': '20%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}
        divider_button_layout={'width':'60%'}
        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')

        self.cell_type_dropdown = Dropdown(description='Cell type:',)
        self.cell_type_dropdown.style = {'description_width': '%sch' % str(len(self.cell_type_dropdown.description) + 1)}

        cell_type_names_layout={'width':'30%'}
        cell_type_names_style={'description_width':'initial'}
#        self.parent_name = Text(value='None',description='inherits properties from parent type:',disabled=True, style=cell_type_names_style, layout=cell_type_names_layout)

#        explain_inheritance = Label(value='    This cell line inherits its properties from its parent type. Any settings below override those inherited properties.')  # , style=cell_type_names_style, layout=cell_type_names_layout)

#        self.cell_type_parent_row = HBox([self.cell_type_dropdown, self.parent_name])
        self.cell_type_parent_row = HBox([self.cell_type_dropdown])
#        self.cell_type_parent_dict = {}

        self.cell_type_dict = {}
        self.cell_type_dict['lung epithelium'] = 'lung epithelium'
        self.cell_type_dict['CD8 Tcell'] = 'CD8 Tcell'
        self.cell_type_dict['macrophage'] = 'macrophage'
        self.cell_type_dict['neutrophil'] = 'neutrophil'
        self.cell_type_dict['DC'] = 'DC'
        self.cell_type_dict['CD4 Tcell'] = 'CD4 Tcell'
        self.cell_type_dict['fibroblast'] = 'fibroblast'
        self.cell_type_dropdown.options = self.cell_type_dict

        self.cell_type_dropdown.observe(self.cell_type_cb)

        self.cell_def_vboxes = []
        #  >>>>>>>>>>>>>>>>> <cell_definition> = default
        #  ------------------------- 
        div_row1 = Button(description='phenotype:cycle (model: flow_cytometry_separated_cycle_model; code=6)', disabled=True, layout=divider_button_layout)
        div_row1.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 1 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float0 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float0, units_btn, ]
        box0 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 1 -> Phase 2 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float1 = FloatText(value='0.00208333', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float1, units_btn, ]
        box1 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 2 -> Phase 3 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float2 = FloatText(value='0.00416667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float2, units_btn, ]
        box2 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 3 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float3 = FloatText(value='0.0166667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float3, units_btn, ]
        box3 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row2 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row2.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float4 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float4, units_btn, ]
        box4 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float5 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float5, units_btn, ]
        box5 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float6 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float6, units_btn, ]
        box6 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float7 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float7, units_btn, ]
        box7 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float8 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float8, units_btn, ]
        box8 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float9 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float9, units_btn, ]
        box9 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float10 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float10, units_btn, ]
        box10 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float11 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float11, units_btn, ]
        box11 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float12 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float12, units_btn, ]
        box12 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float13 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float13, units_btn, ]
        box13 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float14 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float14, units_btn, ]
        box14 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float15 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float15, units_btn, ]
        box15 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float16 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float16, units_btn, ]
        box16 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float17 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float17, units_btn, ]
        box17 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row3 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row3.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float18 = FloatText(value='2494', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float18, units_btn, ]
        box18 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float19 = FloatText(value='0.75', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float19, units_btn, ]
        box19 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float20 = FloatText(value='540', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float20, units_btn, ]
        box20 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float21 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float21, units_btn, ]
        box21 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float22 = FloatText(value='0.0045', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float22, units_btn, ]
        box22 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float23 = FloatText(value='0.0055', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float23, units_btn, ]
        box23 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcified_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float24 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float24, units_btn, ]
        box24 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float25 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float25, units_btn, ]
        box25 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float26 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float26, units_btn, ]
        box26 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row4 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row4.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float27 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float27, units_btn, ]
        box27 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float28 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float28, units_btn, ]
        box28 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float29 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float29, units_btn, ]
        box29 = Box(children=row, layout=box_layout)

        self.bool0 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float30 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool0, name_btn, self.float30, units_btn, ]
        box30 = Box(children=row, layout=box_layout)

        self.bool1 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float31 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool1, name_btn, self.float31, units_btn, ]
        box31 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row5 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row5.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float32 = FloatText(value='4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float32, units_btn]
        box32 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float33 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float33, units_btn]
        box33 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float34 = FloatText(value='0.7', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float34, units_btn]
        box34 = Box(children=row, layout=box_layout)
        self.bool2 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        self.bool3 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool4 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate1 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate1]
        box35 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction1 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction1]
        box36 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row6 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row6.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text0 = Text(value='interferon 1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text0]
        box37 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float35 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float35, units_btn]
        box38 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float36 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float36, units_btn]
        box39 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text1 = Text(value='pro-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text1]
        box40 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float37 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float37, units_btn]
        box41 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float38 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float38, units_btn]
        box42 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text2 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text2]
        box43 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float39 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float39, units_btn]
        box44 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float40 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float40, units_btn]
        box45 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text3 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text3]
        box46 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float41 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float41, units_btn]
        box47 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float42 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float42, units_btn]
        box48 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text4 = Text(value='anti-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text4]
        box49 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float43 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float43, units_btn]
        box50 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float44 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float44, units_btn]
        box51 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text5 = Text(value='collagen', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text5]
        box52 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float45 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float45, units_btn]
        box53 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float46 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float46, units_btn]
        box54 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row7 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row7.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        div_row8 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row8.style.button_color = 'cyan'
        name_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float47 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float47, units_btn, description_btn] 

        box55 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float48 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='uncoated endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float48, units_btn, description_btn] 

        box56 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_RNA', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float49 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='RNA', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total (functional) viral RNA copies', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float49, units_btn, description_btn] 

        box57 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_protein', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float50 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='protein', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='total assembled sets of viral protein', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float50, units_btn, description_btn] 

        box58 = Box(children=row, layout=box_layout)
        name_btn = Button(description='assembled_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float51 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total assembled virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float51, units_btn, description_btn] 

        box59 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_uncoating_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float52 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which an internalized virion is uncoated', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float52, units_btn, description_btn] 

        box60 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_to_RNA_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float53 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which uncoated virion makes its mRNA available', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float53, units_btn, description_btn] 

        box61 = Box(children=row, layout=box_layout)
        name_btn = Button(description='protein_synthesis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float54 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at mRNA creates complete set of proteins', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float54, units_btn, description_btn] 

        box62 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_assembly_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float55 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which viral proteins are assembled into complete virion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float55, units_btn, description_btn] 

        box63 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_export_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float56 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which a virion is exported from a live cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float56, units_btn, description_btn] 

        box64 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float57 = FloatText(value='1000', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of unbound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float57, units_btn, description_btn] 

        box65 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float58 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of bound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float58, units_btn, description_btn] 

        box66 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float59 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of internalized unbound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float59, units_btn, description_btn] 

        box67 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float60 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of internalized bound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float60, units_btn, description_btn] 

        box68 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float61 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float61, units_btn, description_btn] 

        box69 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_endocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float62 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor-virus endocytosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float62, units_btn, description_btn] 

        box70 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_cargo_release_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float63 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus cargo release rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float63, units_btn, description_btn] 

        box71 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_recycling_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float64 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor recycling rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float64, units_btn, description_btn] 

        box72 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_infected_apoptosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float65 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='maximum rate of cell apoptosis due to viral infection', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float65, units_btn, description_btn] 

        box73 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_apoptosis_half_max', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float66 = FloatText(value='250', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='viral load at which cells reach half max apoptosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float66, units_btn, description_btn] 

        box74 = Box(children=row, layout=box_layout)
        name_btn = Button(description='apoptosis_hill_power', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float67 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Hill power for viral load apoptosis response', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float67, units_btn, description_btn] 

        box75 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virus_fraction_released_at_death', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float68 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='fraction of internal virus released at cell death', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float68, units_btn, description_btn] 

        box76 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float69 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='max rate that infected cells secrete chemokine', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float69, units_btn, description_btn] 

        box77 = Box(children=row, layout=box_layout)
        name_btn = Button(description='debris_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float70 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate that dead cells release debris', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float70, units_btn, description_btn] 

        box78 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_activated', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float71 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='used internally to track activation of chemokine secretion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float71, units_btn, description_btn] 

        box79 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_secretion_rate_via_infection', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float72 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Type-1 interferon secretion rate for infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float72, units_btn, description_btn] 

        box80 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_interferon_secretion_rate_via_paracrine', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float73 = FloatText(value='0.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Type-1 interferon secretion rate after activation by Type-1 interferon', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float73, units_btn, description_btn] 

        box81 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_response_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float74 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Interferon response scales linearly until Int-1 exceeds this threshold', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float74, units_btn, description_btn] 

        box82 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_activation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float75 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Current interferon signaling activation state (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float75, units_btn, description_btn] 

        box83 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_virus_inhibition', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float76 = FloatText(value='0.9', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='At max interferon activation, max inhibition of viral replication (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float76, units_btn, description_btn] 

        box84 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_viral_RNA_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float77 = FloatText(value='2', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='infected cell interferon secretion saturates at this viral RNA level', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float77, units_btn, description_btn] 

        box85 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float78 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='tracks total contact time with CD8 T cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float78, units_btn, description_btn] 

        box86 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float79 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the rate at which the cell attaches to cells in contact', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float79, units_btn, description_btn] 

        box87 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_lifetime', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float80 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='the mean duration of a cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float80, units_btn, description_btn] 

        box88 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_death_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float81 = FloatText(value='50', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='threshold CD8 T cell contact time to trigger apoptosis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float81, units_btn, description_btn] 

        box89 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_attachment_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float82 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float82, units_btn, description_btn] 

        box90 = Box(children=row, layout=box_layout)
        name_btn = Button(description='elastic_attachment_coefficient', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float83 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='elastic coefficient for cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float83, units_btn, description_btn] 

        box91 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_to_next_phagocytosis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float84 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='time it takes for the apoptotic material to be phagocytosed', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float84, units_btn, description_btn] 

        box92 = Box(children=row, layout=box_layout)
        name_btn = Button(description='material_internalisation_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float85 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float85, units_btn, description_btn] 

        box93 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_macrophage_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float86 = FloatText(value='6500', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float86, units_btn, description_btn] 

        box94 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_neutrophil_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float87 = FloatText(value='1581', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float87, units_btn, description_btn] 

        box95 = Box(children=row, layout=box_layout)
        name_btn = Button(description='exhausted_macrophage_death_rat', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float88 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float88, units_btn, description_btn] 

        box96 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ability_to_phagocytose_infected_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float89 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Boolean for whether macrophages can phagocytose infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float89, units_btn, description_btn] 

        box97 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_of_DC_departure', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float90 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Time DC leaves tissue after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float90, units_btn, description_btn] 

        box98 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float91 = FloatText(value='0.167', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float91, units_btn, description_btn] 

        box99 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float92 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float92, units_btn, description_btn] 

        box100 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_chemokine_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float93 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to chemokine in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float93, units_btn, description_btn] 

        box101 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float94 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float94, units_btn, description_btn] 

        box102 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float95 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float95, units_btn, description_btn] 

        box103 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_immune_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float96 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='used internally to track activation state', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float96, units_btn, description_btn] 

        box104 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antiinflammatory_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float97 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='secretion rate of anti-inflammatory from infected epithelium cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float97, units_btn, description_btn] 

        box105 = Box(children=row, layout=box_layout)
        name_btn = Button(description='collagen_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float98 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='secretion rate of collagen from fibroblast', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float98, units_btn, description_btn] 

        box106 = Box(children=row, layout=box_layout)

        self.cell_def_vbox0 = VBox([
          div_row1, box0, box1, box2, box3, div_row2, death_model1,box4, box5, box6, box7, box8, box9, box10, death_model2,box11, box12, box13, box14, box15, box16, box17, div_row3, box18, box19, box20, box21, box22, box23, box24, box25, box26, div_row4, box27, box28, box29, box30, box31, div_row5, box32,box33,box34,self.bool2,self.bool3,chemotaxis_btn,self.bool4,box35,box36,div_row6, box37,box38,box39,box40,box41,box42,box43,box44,box45,box46,box47,box48,box49,box50,box51,box52,box53,box54,div_row7, div_row8,          box55,
          box56,
          box57,
          box58,
          box59,
          box60,
          box61,
          box62,
          box63,
          box64,
          box65,
          box66,
          box67,
          box68,
          box69,
          box70,
          box71,
          box72,
          box73,
          box74,
          box75,
          box76,
          box77,
          box78,
          box79,
          box80,
          box81,
          box82,
          box83,
          box84,
          box85,
          box86,
          box87,
          box88,
          box89,
          box90,
          box91,
          box92,
          box93,
          box94,
          box95,
          box96,
          box97,
          box98,
          box99,
          box100,
          box101,
          box102,
          box103,
          box104,
          box105,
          box106,
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox0)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = lung epithelium
        #  ------------------------- 
        div_row9 = Button(description='phenotype:cycle (model: flow_cytometry_separated_cycle_model; code=6)', disabled=True, layout=divider_button_layout)
        div_row9.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 1 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float99 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float99, units_btn, ]
        box107 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 1 -> Phase 2 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float100 = FloatText(value='0.00208333', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float100, units_btn, ]
        box108 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 2 -> Phase 3 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float101 = FloatText(value='0.00416667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float101, units_btn, ]
        box109 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 3 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float102 = FloatText(value='0.0166667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float102, units_btn, ]
        box110 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row10 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row10.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float103 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float103, units_btn, ]
        box111 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float104 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float104, units_btn, ]
        box112 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float105 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float105, units_btn, ]
        box113 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float106 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float106, units_btn, ]
        box114 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float107 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float107, units_btn, ]
        box115 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float108 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float108, units_btn, ]
        box116 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float109 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float109, units_btn, ]
        box117 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float110 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float110, units_btn, ]
        box118 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float111 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float111, units_btn, ]
        box119 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float112 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float112, units_btn, ]
        box120 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float113 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float113, units_btn, ]
        box121 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float114 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float114, units_btn, ]
        box122 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float115 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float115, units_btn, ]
        box123 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float116 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float116, units_btn, ]
        box124 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row11 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row11.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float117 = FloatText(value='2494', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float117, units_btn, ]
        box125 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float118 = FloatText(value='0.75', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float118, units_btn, ]
        box126 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float119 = FloatText(value='540', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float119, units_btn, ]
        box127 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float120 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float120, units_btn, ]
        box128 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float121 = FloatText(value='0.0045', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float121, units_btn, ]
        box129 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float122 = FloatText(value='0.0055', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float122, units_btn, ]
        box130 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcified_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float123 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float123, units_btn, ]
        box131 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float124 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float124, units_btn, ]
        box132 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float125 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float125, units_btn, ]
        box133 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row12 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row12.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float126 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float126, units_btn, ]
        box134 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float127 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float127, units_btn, ]
        box135 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float128 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float128, units_btn, ]
        box136 = Box(children=row, layout=box_layout)

        self.bool5 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float129 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool5, name_btn, self.float129, units_btn, ]
        box137 = Box(children=row, layout=box_layout)

        self.bool6 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float130 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool6, name_btn, self.float130, units_btn, ]
        box138 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row13 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row13.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float131 = FloatText(value='4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float131, units_btn]
        box139 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float132 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float132, units_btn]
        box140 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float133 = FloatText(value='0.7', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float133, units_btn]
        box141 = Box(children=row, layout=box_layout)
        self.bool7 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        self.bool8 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool9 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate2 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate2]
        box142 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction2 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction2]
        box143 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row14 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row14.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text6 = Text(value='interferon 1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text6]
        box144 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float134 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float134, units_btn]
        box145 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float135 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float135, units_btn]
        box146 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text7 = Text(value='pro-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text7]
        box147 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float136 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float136, units_btn]
        box148 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float137 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float137, units_btn]
        box149 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text8 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text8]
        box150 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float138 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float138, units_btn]
        box151 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float139 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float139, units_btn]
        box152 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text9 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text9]
        box153 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float140 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float140, units_btn]
        box154 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float141 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float141, units_btn]
        box155 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text10 = Text(value='anti-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text10]
        box156 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float142 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float142, units_btn]
        box157 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float143 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float143, units_btn]
        box158 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text11 = Text(value='collagen', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text11]
        box159 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float144 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float144, units_btn]
        box160 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float145 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float145, units_btn]
        box161 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row15 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row15.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        div_row16 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row16.style.button_color = 'cyan'
        name_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float146 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float146, units_btn, description_btn] 

        box162 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float147 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='uncoated endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float147, units_btn, description_btn] 

        box163 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_RNA', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float148 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='RNA', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total (functional) viral RNA copies', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float148, units_btn, description_btn] 

        box164 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_protein', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float149 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='protein', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='total assembled sets of viral protein', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float149, units_btn, description_btn] 

        box165 = Box(children=row, layout=box_layout)
        name_btn = Button(description='assembled_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float150 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total assembled virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float150, units_btn, description_btn] 

        box166 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_uncoating_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float151 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which an internalized virion is uncoated', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float151, units_btn, description_btn] 

        box167 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_to_RNA_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float152 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which uncoated virion makes its mRNA available', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float152, units_btn, description_btn] 

        box168 = Box(children=row, layout=box_layout)
        name_btn = Button(description='protein_synthesis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float153 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at mRNA creates complete set of proteins', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float153, units_btn, description_btn] 

        box169 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_assembly_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float154 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which viral proteins are assembled into complete virion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float154, units_btn, description_btn] 

        box170 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_export_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float155 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which a virion is exported from a live cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float155, units_btn, description_btn] 

        box171 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float156 = FloatText(value='1000', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of unbound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float156, units_btn, description_btn] 

        box172 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float157 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of bound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float157, units_btn, description_btn] 

        box173 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float158 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of internalized unbound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float158, units_btn, description_btn] 

        box174 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float159 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of internalized bound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float159, units_btn, description_btn] 

        box175 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float160 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float160, units_btn, description_btn] 

        box176 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_endocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float161 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor-virus endocytosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float161, units_btn, description_btn] 

        box177 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_cargo_release_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float162 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus cargo release rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float162, units_btn, description_btn] 

        box178 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_recycling_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float163 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor recycling rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float163, units_btn, description_btn] 

        box179 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_infected_apoptosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float164 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='maximum rate of cell apoptosis due to viral infection', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float164, units_btn, description_btn] 

        box180 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_apoptosis_half_max', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float165 = FloatText(value='250', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='viral load at which cells reach half max apoptosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float165, units_btn, description_btn] 

        box181 = Box(children=row, layout=box_layout)
        name_btn = Button(description='apoptosis_hill_power', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float166 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Hill power for viral load apoptosis response', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float166, units_btn, description_btn] 

        box182 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virus_fraction_released_at_death', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float167 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='fraction of internal virus released at cell death', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float167, units_btn, description_btn] 

        box183 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float168 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='max rate that infected cells secrete chemokine', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float168, units_btn, description_btn] 

        box184 = Box(children=row, layout=box_layout)
        name_btn = Button(description='debris_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float169 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate that dead cells release debris', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float169, units_btn, description_btn] 

        box185 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_activated', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float170 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='used internally to track activation of chemokine secretion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float170, units_btn, description_btn] 

        box186 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_secretion_rate_via_infection', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float171 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Type-1 interferon secretion rate for infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float171, units_btn, description_btn] 

        box187 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_interferon_secretion_rate_via_paracrine', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float172 = FloatText(value='0.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Type-1 interferon secretion rate after activation by Type-1 interferon', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float172, units_btn, description_btn] 

        box188 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_response_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float173 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Interferon response scales linearly until Int-1 exceeds this threshold', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float173, units_btn, description_btn] 

        box189 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_activation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float174 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Current interferon signaling activation state (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float174, units_btn, description_btn] 

        box190 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_virus_inhibition', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float175 = FloatText(value='0.9', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='At max interferon activation, max inhibition of viral replication (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float175, units_btn, description_btn] 

        box191 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_viral_RNA_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float176 = FloatText(value='2', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='infected cell interferon secretion saturates at this viral RNA level', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float176, units_btn, description_btn] 

        box192 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float177 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='tracks total contact time with CD8 T cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float177, units_btn, description_btn] 

        box193 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float178 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the rate at which the cell attaches to cells in contact', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float178, units_btn, description_btn] 

        box194 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_lifetime', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float179 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='the mean duration of a cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float179, units_btn, description_btn] 

        box195 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_death_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float180 = FloatText(value='50', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='threshold CD8 T cell contact time to trigger apoptosis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float180, units_btn, description_btn] 

        box196 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_attachment_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float181 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float181, units_btn, description_btn] 

        box197 = Box(children=row, layout=box_layout)
        name_btn = Button(description='elastic_attachment_coefficient', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float182 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='elastic coefficient for cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float182, units_btn, description_btn] 

        box198 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_to_next_phagocytosis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float183 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='time it takes for the apoptotic material to be phagocytosed', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float183, units_btn, description_btn] 

        box199 = Box(children=row, layout=box_layout)
        name_btn = Button(description='material_internalisation_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float184 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float184, units_btn, description_btn] 

        box200 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_macrophage_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float185 = FloatText(value='6500', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float185, units_btn, description_btn] 

        box201 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_neutrophil_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float186 = FloatText(value='1581', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float186, units_btn, description_btn] 

        box202 = Box(children=row, layout=box_layout)
        name_btn = Button(description='exhausted_macrophage_death_rat', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float187 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float187, units_btn, description_btn] 

        box203 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ability_to_phagocytose_infected_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float188 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Boolean for whether macrophages can phagocytose infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float188, units_btn, description_btn] 

        box204 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_of_DC_departure', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float189 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Time DC leaves tissue after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float189, units_btn, description_btn] 

        box205 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float190 = FloatText(value='0.167', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float190, units_btn, description_btn] 

        box206 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float191 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float191, units_btn, description_btn] 

        box207 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_chemokine_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float192 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to chemokine in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float192, units_btn, description_btn] 

        box208 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float193 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float193, units_btn, description_btn] 

        box209 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float194 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float194, units_btn, description_btn] 

        box210 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_immune_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float195 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='used internally to track activation state', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float195, units_btn, description_btn] 

        box211 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antiinflammatory_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float196 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='secretion rate of anti-inflammatory from infected epithelium cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float196, units_btn, description_btn] 

        box212 = Box(children=row, layout=box_layout)
        name_btn = Button(description='collagen_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float197 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='secretion rate of collagen from fibroblast', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float197, units_btn, description_btn] 

        box213 = Box(children=row, layout=box_layout)

        self.cell_def_vbox1 = VBox([
          div_row9, box107, box108, box109, box110, div_row10, death_model1,box111, box112, box113, box114, box115, box116, box117, death_model2,box118, box119, box120, box121, box122, box123, box124, div_row11, box125, box126, box127, box128, box129, box130, box131, box132, box133, div_row12, box134, box135, box136, box137, box138, div_row13, box139,box140,box141,self.bool7,self.bool8,chemotaxis_btn,self.bool9,box142,box143,div_row14, box144,box145,box146,box147,box148,box149,box150,box151,box152,box153,box154,box155,box156,box157,box158,box159,box160,box161,div_row15, div_row16,          box162,
          box163,
          box164,
          box165,
          box166,
          box167,
          box168,
          box169,
          box170,
          box171,
          box172,
          box173,
          box174,
          box175,
          box176,
          box177,
          box178,
          box179,
          box180,
          box181,
          box182,
          box183,
          box184,
          box185,
          box186,
          box187,
          box188,
          box189,
          box190,
          box191,
          box192,
          box193,
          box194,
          box195,
          box196,
          box197,
          box198,
          box199,
          box200,
          box201,
          box202,
          box203,
          box204,
          box205,
          box206,
          box207,
          box208,
          box209,
          box210,
          box211,
          box212,
          box213,
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox1)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = CD8 Tcell
        #  ------------------------- 
        div_row17 = Button(description='phenotype:cycle (model: flow_cytometry_separated_cycle_model; code=6)', disabled=True, layout=divider_button_layout)
        div_row17.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 1 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float198 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float198, units_btn, ]
        box214 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 1 -> Phase 2 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float199 = FloatText(value='0.00208333', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float199, units_btn, ]
        box215 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 2 -> Phase 3 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float200 = FloatText(value='0.00416667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float200, units_btn, ]
        box216 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 3 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float201 = FloatText(value='0.0166667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float201, units_btn, ]
        box217 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row18 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row18.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float202 = FloatText(value='2.8e-4', step='1e-05', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float202, units_btn, ]
        box218 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float203 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float203, units_btn, ]
        box219 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float204 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float204, units_btn, ]
        box220 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float205 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float205, units_btn, ]
        box221 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float206 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float206, units_btn, ]
        box222 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float207 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float207, units_btn, ]
        box223 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float208 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float208, units_btn, ]
        box224 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float209 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float209, units_btn, ]
        box225 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float210 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float210, units_btn, ]
        box226 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float211 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float211, units_btn, ]
        box227 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float212 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float212, units_btn, ]
        box228 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float213 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float213, units_btn, ]
        box229 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float214 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float214, units_btn, ]
        box230 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float215 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float215, units_btn, ]
        box231 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row19 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row19.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float216 = FloatText(value='478', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float216, units_btn, ]
        box232 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float217 = FloatText(value='0.75', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float217, units_btn, ]
        box233 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float218 = FloatText(value='47.8', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float218, units_btn, ]
        box234 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float219 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float219, units_btn, ]
        box235 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float220 = FloatText(value='0.0045', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float220, units_btn, ]
        box236 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float221 = FloatText(value='0.0055', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float221, units_btn, ]
        box237 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcified_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float222 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float222, units_btn, ]
        box238 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float223 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float223, units_btn, ]
        box239 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float224 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float224, units_btn, ]
        box240 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row20 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row20.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float225 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float225, units_btn, ]
        box241 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float226 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float226, units_btn, ]
        box242 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float227 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float227, units_btn, ]
        box243 = Box(children=row, layout=box_layout)

        self.bool10 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float228 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool10, name_btn, self.float228, units_btn, ]
        box244 = Box(children=row, layout=box_layout)

        self.bool11 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float229 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool11, name_btn, self.float229, units_btn, ]
        box245 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row21 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row21.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float230 = FloatText(value='4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float230, units_btn]
        box246 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float231 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float231, units_btn]
        box247 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float232 = FloatText(value='0.70', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float232, units_btn]
        box248 = Box(children=row, layout=box_layout)
        self.bool12 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        self.bool13 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool14 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate3 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate3]
        box249 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction3 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction3]
        box250 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row22 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row22.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text12 = Text(value='interferon 1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text12]
        box251 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float233 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float233, units_btn]
        box252 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float234 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float234, units_btn]
        box253 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text13 = Text(value='pro-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text13]
        box254 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float235 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float235, units_btn]
        box255 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float236 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float236, units_btn]
        box256 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text14 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text14]
        box257 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float237 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float237, units_btn]
        box258 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float238 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float238, units_btn]
        box259 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text15 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text15]
        box260 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float239 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float239, units_btn]
        box261 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float240 = FloatText(value='0.1', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float240, units_btn]
        box262 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text16 = Text(value='anti-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text16]
        box263 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float241 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float241, units_btn]
        box264 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float242 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float242, units_btn]
        box265 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text17 = Text(value='collagen', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text17]
        box266 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float243 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float243, units_btn]
        box267 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float244 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float244, units_btn]
        box268 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row23 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row23.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        div_row24 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row24.style.button_color = 'cyan'
        name_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float245 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float245, units_btn, description_btn] 

        box269 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float246 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='uncoated endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float246, units_btn, description_btn] 

        box270 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_RNA', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float247 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='RNA', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total (functional) viral RNA copies', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float247, units_btn, description_btn] 

        box271 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_protein', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float248 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='protein', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='total assembled sets of viral protein', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float248, units_btn, description_btn] 

        box272 = Box(children=row, layout=box_layout)
        name_btn = Button(description='assembled_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float249 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total assembled virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float249, units_btn, description_btn] 

        box273 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_uncoating_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float250 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which an internalized virion is uncoated', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float250, units_btn, description_btn] 

        box274 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_to_RNA_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float251 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which uncoated virion makes its mRNA available', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float251, units_btn, description_btn] 

        box275 = Box(children=row, layout=box_layout)
        name_btn = Button(description='protein_synthesis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float252 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at mRNA creates complete set of proteins', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float252, units_btn, description_btn] 

        box276 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_assembly_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float253 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which viral proteins are assembled into complete virion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float253, units_btn, description_btn] 

        box277 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_export_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float254 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which a virion is exported from a live cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float254, units_btn, description_btn] 

        box278 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float255 = FloatText(value='1000', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of unbound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float255, units_btn, description_btn] 

        box279 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float256 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of bound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float256, units_btn, description_btn] 

        box280 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float257 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of internalized unbound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float257, units_btn, description_btn] 

        box281 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float258 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of internalized bound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float258, units_btn, description_btn] 

        box282 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float259 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float259, units_btn, description_btn] 

        box283 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_endocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float260 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor-virus endocytosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float260, units_btn, description_btn] 

        box284 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_cargo_release_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float261 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus cargo release rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float261, units_btn, description_btn] 

        box285 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_recycling_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float262 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor recycling rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float262, units_btn, description_btn] 

        box286 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_infected_apoptosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float263 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='maximum rate of cell apoptosis due to viral infection', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float263, units_btn, description_btn] 

        box287 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_apoptosis_half_max', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float264 = FloatText(value='250', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='viral load at which cells reach half max apoptosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float264, units_btn, description_btn] 

        box288 = Box(children=row, layout=box_layout)
        name_btn = Button(description='apoptosis_hill_power', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float265 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Hill power for viral load apoptosis response', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float265, units_btn, description_btn] 

        box289 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virus_fraction_released_at_death', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float266 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='fraction of internal virus released at cell death', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float266, units_btn, description_btn] 

        box290 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float267 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='max rate that infected cells secrete chemokine', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float267, units_btn, description_btn] 

        box291 = Box(children=row, layout=box_layout)
        name_btn = Button(description='debris_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float268 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate that dead cells release debris', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float268, units_btn, description_btn] 

        box292 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_activated', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float269 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='used internally to track activation of chemokine secretion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float269, units_btn, description_btn] 

        box293 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_secretion_rate_via_infection', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float270 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Type-1 interferon secretion rate for infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float270, units_btn, description_btn] 

        box294 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_interferon_secretion_rate_via_paracrine', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float271 = FloatText(value='0.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Type-1 interferon secretion rate after activation by Type-1 interferon', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float271, units_btn, description_btn] 

        box295 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_response_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float272 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Interferon response scales linearly until Int-1 exceeds this threshold', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float272, units_btn, description_btn] 

        box296 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_activation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float273 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Current interferon signaling activation state (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float273, units_btn, description_btn] 

        box297 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_virus_inhibition', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float274 = FloatText(value='0.9', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='At max interferon activation, max inhibition of viral replication (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float274, units_btn, description_btn] 

        box298 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_viral_RNA_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float275 = FloatText(value='2', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='infected cell interferon secretion saturates at this viral RNA level', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float275, units_btn, description_btn] 

        box299 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float276 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='tracks total contact time with CD8 T cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float276, units_btn, description_btn] 

        box300 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float277 = FloatText(value='0.2', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the rate at which the cell attaches to cells in contact', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float277, units_btn, description_btn] 

        box301 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_lifetime', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float278 = FloatText(value='8.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='the mean duration of a cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float278, units_btn, description_btn] 

        box302 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_death_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float279 = FloatText(value='50', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='threshold CD8 T cell contact time to trigger apoptosis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float279, units_btn, description_btn] 

        box303 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_attachment_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float280 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float280, units_btn, description_btn] 

        box304 = Box(children=row, layout=box_layout)
        name_btn = Button(description='elastic_attachment_coefficient', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float281 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='elastic coefficient for cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float281, units_btn, description_btn] 

        box305 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_to_next_phagocytosis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float282 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='time it takes for the apoptotic material to be phagocytosed', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float282, units_btn, description_btn] 

        box306 = Box(children=row, layout=box_layout)
        name_btn = Button(description='material_internalisation_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float283 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float283, units_btn, description_btn] 

        box307 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_macrophage_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float284 = FloatText(value='6500', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float284, units_btn, description_btn] 

        box308 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_neutrophil_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float285 = FloatText(value='1581', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float285, units_btn, description_btn] 

        box309 = Box(children=row, layout=box_layout)
        name_btn = Button(description='exhausted_macrophage_death_rat', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float286 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float286, units_btn, description_btn] 

        box310 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ability_to_phagocytose_infected_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float287 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Boolean for whether macrophages can phagocytose infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float287, units_btn, description_btn] 

        box311 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_of_DC_departure', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float288 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Time DC leaves tissue after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float288, units_btn, description_btn] 

        box312 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float289 = FloatText(value='0.167', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float289, units_btn, description_btn] 

        box313 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float290 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float290, units_btn, description_btn] 

        box314 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_chemokine_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float291 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to chemokine in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float291, units_btn, description_btn] 

        box315 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float292 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float292, units_btn, description_btn] 

        box316 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float293 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float293, units_btn, description_btn] 

        box317 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_immune_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float294 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='used internally to track activation state', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float294, units_btn, description_btn] 

        box318 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antiinflammatory_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float295 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='secretion rate of anti-inflammatory from infected epithelium cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float295, units_btn, description_btn] 

        box319 = Box(children=row, layout=box_layout)
        name_btn = Button(description='collagen_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float296 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='secretion rate of collagen from fibroblast', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float296, units_btn, description_btn] 

        box320 = Box(children=row, layout=box_layout)

        self.cell_def_vbox2 = VBox([
          div_row17, box214, box215, box216, box217, div_row18, death_model1,box218, box219, box220, box221, box222, box223, box224, death_model2,box225, box226, box227, box228, box229, box230, box231, div_row19, box232, box233, box234, box235, box236, box237, box238, box239, box240, div_row20, box241, box242, box243, box244, box245, div_row21, box246,box247,box248,self.bool12,self.bool13,chemotaxis_btn,self.bool14,box249,box250,div_row22, box251,box252,box253,box254,box255,box256,box257,box258,box259,box260,box261,box262,box263,box264,box265,box266,box267,box268,div_row23, div_row24,          box269,
          box270,
          box271,
          box272,
          box273,
          box274,
          box275,
          box276,
          box277,
          box278,
          box279,
          box280,
          box281,
          box282,
          box283,
          box284,
          box285,
          box286,
          box287,
          box288,
          box289,
          box290,
          box291,
          box292,
          box293,
          box294,
          box295,
          box296,
          box297,
          box298,
          box299,
          box300,
          box301,
          box302,
          box303,
          box304,
          box305,
          box306,
          box307,
          box308,
          box309,
          box310,
          box311,
          box312,
          box313,
          box314,
          box315,
          box316,
          box317,
          box318,
          box319,
          box320,
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox2)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = macrophage
        #  ------------------------- 
        div_row25 = Button(description='phenotype:cycle (model: flow_cytometry_separated_cycle_model; code=6)', disabled=True, layout=divider_button_layout)
        div_row25.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 1 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float297 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float297, units_btn, ]
        box321 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 1 -> Phase 2 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float298 = FloatText(value='0.00208333', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float298, units_btn, ]
        box322 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 2 -> Phase 3 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float299 = FloatText(value='0.00416667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float299, units_btn, ]
        box323 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 3 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float300 = FloatText(value='0.0166667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float300, units_btn, ]
        box324 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row26 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row26.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float301 = FloatText(value='2.1e-4', step='1e-05', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float301, units_btn, ]
        box325 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float302 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float302, units_btn, ]
        box326 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float303 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float303, units_btn, ]
        box327 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float304 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float304, units_btn, ]
        box328 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float305 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float305, units_btn, ]
        box329 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float306 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float306, units_btn, ]
        box330 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float307 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float307, units_btn, ]
        box331 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float308 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float308, units_btn, ]
        box332 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float309 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float309, units_btn, ]
        box333 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float310 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float310, units_btn, ]
        box334 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float311 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float311, units_btn, ]
        box335 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float312 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float312, units_btn, ]
        box336 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float313 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float313, units_btn, ]
        box337 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float314 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float314, units_btn, ]
        box338 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row27 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row27.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float315 = FloatText(value='4849', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float315, units_btn, ]
        box339 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float316 = FloatText(value='0.75', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float316, units_btn, ]
        box340 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float317 = FloatText(value='485', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float317, units_btn, ]
        box341 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float318 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float318, units_btn, ]
        box342 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float319 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float319, units_btn, ]
        box343 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float320 = FloatText(value='0.0055', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float320, units_btn, ]
        box344 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcified_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float321 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float321, units_btn, ]
        box345 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float322 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float322, units_btn, ]
        box346 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float323 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float323, units_btn, ]
        box347 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row28 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row28.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float324 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float324, units_btn, ]
        box348 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float325 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float325, units_btn, ]
        box349 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float326 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float326, units_btn, ]
        box350 = Box(children=row, layout=box_layout)

        self.bool15 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float327 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool15, name_btn, self.float327, units_btn, ]
        box351 = Box(children=row, layout=box_layout)

        self.bool16 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float328 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool16, name_btn, self.float328, units_btn, ]
        box352 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row29 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row29.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float329 = FloatText(value='4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float329, units_btn]
        box353 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float330 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float330, units_btn]
        box354 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float331 = FloatText(value='0.7', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float331, units_btn]
        box355 = Box(children=row, layout=box_layout)
        self.bool17 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        self.bool18 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool19 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate4 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate4]
        box356 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction4 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction4]
        box357 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row30 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row30.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text18 = Text(value='interferon 1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text18]
        box358 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float332 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float332, units_btn]
        box359 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float333 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float333, units_btn]
        box360 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text19 = Text(value='pro-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text19]
        box361 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float334 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float334, units_btn]
        box362 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float335 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float335, units_btn]
        box363 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text20 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text20]
        box364 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float336 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float336, units_btn]
        box365 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float337 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float337, units_btn]
        box366 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text21 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text21]
        box367 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float338 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float338, units_btn]
        box368 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float339 = FloatText(value='0.1', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float339, units_btn]
        box369 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text22 = Text(value='anti-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text22]
        box370 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float340 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float340, units_btn]
        box371 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float341 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float341, units_btn]
        box372 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text23 = Text(value='collagen', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text23]
        box373 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float342 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float342, units_btn]
        box374 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float343 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float343, units_btn]
        box375 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row31 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row31.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        div_row32 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row32.style.button_color = 'cyan'
        name_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float344 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float344, units_btn, description_btn] 

        box376 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float345 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='uncoated endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float345, units_btn, description_btn] 

        box377 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_RNA', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float346 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='RNA', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total (functional) viral RNA copies', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float346, units_btn, description_btn] 

        box378 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_protein', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float347 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='protein', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='total assembled sets of viral protein', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float347, units_btn, description_btn] 

        box379 = Box(children=row, layout=box_layout)
        name_btn = Button(description='assembled_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float348 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total assembled virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float348, units_btn, description_btn] 

        box380 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_uncoating_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float349 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which an internalized virion is uncoated', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float349, units_btn, description_btn] 

        box381 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_to_RNA_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float350 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which uncoated virion makes its mRNA available', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float350, units_btn, description_btn] 

        box382 = Box(children=row, layout=box_layout)
        name_btn = Button(description='protein_synthesis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float351 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at mRNA creates complete set of proteins', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float351, units_btn, description_btn] 

        box383 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_assembly_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float352 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which viral proteins are assembled into complete virion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float352, units_btn, description_btn] 

        box384 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_export_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float353 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which a virion is exported from a live cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float353, units_btn, description_btn] 

        box385 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float354 = FloatText(value='1000', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of unbound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float354, units_btn, description_btn] 

        box386 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float355 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of bound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float355, units_btn, description_btn] 

        box387 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float356 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of internalized unbound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float356, units_btn, description_btn] 

        box388 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float357 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of internalized bound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float357, units_btn, description_btn] 

        box389 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float358 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float358, units_btn, description_btn] 

        box390 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_endocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float359 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor-virus endocytosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float359, units_btn, description_btn] 

        box391 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_cargo_release_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float360 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus cargo release rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float360, units_btn, description_btn] 

        box392 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_recycling_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float361 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor recycling rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float361, units_btn, description_btn] 

        box393 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_infected_apoptosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float362 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='maximum rate of cell apoptosis due to viral infection', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float362, units_btn, description_btn] 

        box394 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_apoptosis_half_max', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float363 = FloatText(value='250', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='viral load at which cells reach half max apoptosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float363, units_btn, description_btn] 

        box395 = Box(children=row, layout=box_layout)
        name_btn = Button(description='apoptosis_hill_power', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float364 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Hill power for viral load apoptosis response', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float364, units_btn, description_btn] 

        box396 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virus_fraction_released_at_death', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float365 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='fraction of internal virus released at cell death', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float365, units_btn, description_btn] 

        box397 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float366 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='max rate that infected cells secrete chemokine', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float366, units_btn, description_btn] 

        box398 = Box(children=row, layout=box_layout)
        name_btn = Button(description='debris_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float367 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate that dead cells release debris', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float367, units_btn, description_btn] 

        box399 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_activated', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float368 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='used internally to track activation of chemokine secretion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float368, units_btn, description_btn] 

        box400 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_secretion_rate_via_infection', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float369 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Type-1 interferon secretion rate for infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float369, units_btn, description_btn] 

        box401 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_interferon_secretion_rate_via_paracrine', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float370 = FloatText(value='0.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Type-1 interferon secretion rate after activation by Type-1 interferon', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float370, units_btn, description_btn] 

        box402 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_response_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float371 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Interferon response scales linearly until Int-1 exceeds this threshold', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float371, units_btn, description_btn] 

        box403 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_activation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float372 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Current interferon signaling activation state (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float372, units_btn, description_btn] 

        box404 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_virus_inhibition', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float373 = FloatText(value='0.9', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='At max interferon activation, max inhibition of viral replication (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float373, units_btn, description_btn] 

        box405 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_viral_RNA_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float374 = FloatText(value='2', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='infected cell interferon secretion saturates at this viral RNA level', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float374, units_btn, description_btn] 

        box406 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float375 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='tracks total contact time with CD8 T cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float375, units_btn, description_btn] 

        box407 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float376 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the rate at which the cell attaches to cells in contact', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float376, units_btn, description_btn] 

        box408 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_lifetime', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float377 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='the mean duration of a cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float377, units_btn, description_btn] 

        box409 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_death_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float378 = FloatText(value='50', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='threshold CD8 T cell contact time to trigger apoptosis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float378, units_btn, description_btn] 

        box410 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_attachment_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float379 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float379, units_btn, description_btn] 

        box411 = Box(children=row, layout=box_layout)
        name_btn = Button(description='elastic_attachment_coefficient', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float380 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='elastic coefficient for cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float380, units_btn, description_btn] 

        box412 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_to_next_phagocytosis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float381 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='time it takes for the apoptotic material to be phagocytosed', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float381, units_btn, description_btn] 

        box413 = Box(children=row, layout=box_layout)
        name_btn = Button(description='material_internalisation_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float382 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float382, units_btn, description_btn] 

        box414 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_macrophage_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float383 = FloatText(value='6500', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float383, units_btn, description_btn] 

        box415 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_neutrophil_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float384 = FloatText(value='1581', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float384, units_btn, description_btn] 

        box416 = Box(children=row, layout=box_layout)
        name_btn = Button(description='exhausted_macrophage_death_rat', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float385 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float385, units_btn, description_btn] 

        box417 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ability_to_phagocytose_infected_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float386 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Boolean for whether macrophages can phagocytose infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float386, units_btn, description_btn] 

        box418 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_of_DC_departure', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float387 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Time DC leaves tissue after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float387, units_btn, description_btn] 

        box419 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float388 = FloatText(value='0.167', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float388, units_btn, description_btn] 

        box420 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float389 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float389, units_btn, description_btn] 

        box421 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_chemokine_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float390 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to chemokine in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float390, units_btn, description_btn] 

        box422 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float391 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float391, units_btn, description_btn] 

        box423 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float392 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float392, units_btn, description_btn] 

        box424 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_immune_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float393 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='used internally to track activation state', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float393, units_btn, description_btn] 

        box425 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antiinflammatory_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float394 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='secretion rate of anti-inflammatory from infected epithelium cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float394, units_btn, description_btn] 

        box426 = Box(children=row, layout=box_layout)
        name_btn = Button(description='collagen_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float395 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='secretion rate of collagen from fibroblast', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float395, units_btn, description_btn] 

        box427 = Box(children=row, layout=box_layout)

        self.cell_def_vbox3 = VBox([
          div_row25, box321, box322, box323, box324, div_row26, death_model1,box325, box326, box327, box328, box329, box330, box331, death_model2,box332, box333, box334, box335, box336, box337, box338, div_row27, box339, box340, box341, box342, box343, box344, box345, box346, box347, div_row28, box348, box349, box350, box351, box352, div_row29, box353,box354,box355,self.bool17,self.bool18,chemotaxis_btn,self.bool19,box356,box357,div_row30, box358,box359,box360,box361,box362,box363,box364,box365,box366,box367,box368,box369,box370,box371,box372,box373,box374,box375,div_row31, div_row32,          box376,
          box377,
          box378,
          box379,
          box380,
          box381,
          box382,
          box383,
          box384,
          box385,
          box386,
          box387,
          box388,
          box389,
          box390,
          box391,
          box392,
          box393,
          box394,
          box395,
          box396,
          box397,
          box398,
          box399,
          box400,
          box401,
          box402,
          box403,
          box404,
          box405,
          box406,
          box407,
          box408,
          box409,
          box410,
          box411,
          box412,
          box413,
          box414,
          box415,
          box416,
          box417,
          box418,
          box419,
          box420,
          box421,
          box422,
          box423,
          box424,
          box425,
          box426,
          box427,
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox3)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = neutrophil
        #  ------------------------- 
        div_row33 = Button(description='phenotype:cycle (model: flow_cytometry_separated_cycle_model; code=6)', disabled=True, layout=divider_button_layout)
        div_row33.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 1 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float396 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float396, units_btn, ]
        box428 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 1 -> Phase 2 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float397 = FloatText(value='0.00208333', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float397, units_btn, ]
        box429 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 2 -> Phase 3 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float398 = FloatText(value='0.00416667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float398, units_btn, ]
        box430 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 3 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float399 = FloatText(value='0.0166667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float399, units_btn, ]
        box431 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row34 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row34.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float400 = FloatText(value='8.9e-4', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float400, units_btn, ]
        box432 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float401 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float401, units_btn, ]
        box433 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float402 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float402, units_btn, ]
        box434 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float403 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float403, units_btn, ]
        box435 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float404 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float404, units_btn, ]
        box436 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float405 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float405, units_btn, ]
        box437 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float406 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float406, units_btn, ]
        box438 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float407 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float407, units_btn, ]
        box439 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float408 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float408, units_btn, ]
        box440 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float409 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float409, units_btn, ]
        box441 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float410 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float410, units_btn, ]
        box442 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float411 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float411, units_btn, ]
        box443 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float412 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float412, units_btn, ]
        box444 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float413 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float413, units_btn, ]
        box445 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row35 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row35.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float414 = FloatText(value='1437', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float414, units_btn, ]
        box446 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float415 = FloatText(value='0.75', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float415, units_btn, ]
        box447 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float416 = FloatText(value='143.7', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float416, units_btn, ]
        box448 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float417 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float417, units_btn, ]
        box449 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float418 = FloatText(value='0.045', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float418, units_btn, ]
        box450 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float419 = FloatText(value='0.0055', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float419, units_btn, ]
        box451 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcified_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float420 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float420, units_btn, ]
        box452 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float421 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float421, units_btn, ]
        box453 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float422 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float422, units_btn, ]
        box454 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row36 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row36.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float423 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float423, units_btn, ]
        box455 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float424 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float424, units_btn, ]
        box456 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float425 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float425, units_btn, ]
        box457 = Box(children=row, layout=box_layout)

        self.bool20 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float426 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool20, name_btn, self.float426, units_btn, ]
        box458 = Box(children=row, layout=box_layout)

        self.bool21 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float427 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool21, name_btn, self.float427, units_btn, ]
        box459 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row37 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row37.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float428 = FloatText(value='19', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float428, units_btn]
        box460 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float429 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float429, units_btn]
        box461 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float430 = FloatText(value='0.91', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float430, units_btn]
        box462 = Box(children=row, layout=box_layout)
        self.bool22 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        self.bool23 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool24 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate5 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate5]
        box463 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction5 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction5]
        box464 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row38 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row38.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text24 = Text(value='interferon 1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text24]
        box465 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float431 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float431, units_btn]
        box466 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float432 = FloatText(value='0.1', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float432, units_btn]
        box467 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text25 = Text(value='pro-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text25]
        box468 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float433 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float433, units_btn]
        box469 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float434 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float434, units_btn]
        box470 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text26 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text26]
        box471 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float435 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float435, units_btn]
        box472 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float436 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float436, units_btn]
        box473 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text27 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text27]
        box474 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float437 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float437, units_btn]
        box475 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float438 = FloatText(value='0.1', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float438, units_btn]
        box476 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text28 = Text(value='anti-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text28]
        box477 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float439 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float439, units_btn]
        box478 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float440 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float440, units_btn]
        box479 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text29 = Text(value='collagen', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text29]
        box480 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float441 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float441, units_btn]
        box481 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float442 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float442, units_btn]
        box482 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row39 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row39.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        div_row40 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row40.style.button_color = 'cyan'
        name_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float443 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float443, units_btn, description_btn] 

        box483 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float444 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='uncoated endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float444, units_btn, description_btn] 

        box484 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_RNA', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float445 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='RNA', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total (functional) viral RNA copies', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float445, units_btn, description_btn] 

        box485 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_protein', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float446 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='protein', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='total assembled sets of viral protein', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float446, units_btn, description_btn] 

        box486 = Box(children=row, layout=box_layout)
        name_btn = Button(description='assembled_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float447 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total assembled virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float447, units_btn, description_btn] 

        box487 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_uncoating_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float448 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which an internalized virion is uncoated', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float448, units_btn, description_btn] 

        box488 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_to_RNA_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float449 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which uncoated virion makes its mRNA available', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float449, units_btn, description_btn] 

        box489 = Box(children=row, layout=box_layout)
        name_btn = Button(description='protein_synthesis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float450 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at mRNA creates complete set of proteins', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float450, units_btn, description_btn] 

        box490 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_assembly_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float451 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which viral proteins are assembled into complete virion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float451, units_btn, description_btn] 

        box491 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_export_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float452 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which a virion is exported from a live cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float452, units_btn, description_btn] 

        box492 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float453 = FloatText(value='1000', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of unbound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float453, units_btn, description_btn] 

        box493 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float454 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of bound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float454, units_btn, description_btn] 

        box494 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float455 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of internalized unbound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float455, units_btn, description_btn] 

        box495 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float456 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of internalized bound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float456, units_btn, description_btn] 

        box496 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float457 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float457, units_btn, description_btn] 

        box497 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_endocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float458 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor-virus endocytosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float458, units_btn, description_btn] 

        box498 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_cargo_release_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float459 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus cargo release rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float459, units_btn, description_btn] 

        box499 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_recycling_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float460 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor recycling rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float460, units_btn, description_btn] 

        box500 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_infected_apoptosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float461 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='maximum rate of cell apoptosis due to viral infection', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float461, units_btn, description_btn] 

        box501 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_apoptosis_half_max', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float462 = FloatText(value='250', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='viral load at which cells reach half max apoptosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float462, units_btn, description_btn] 

        box502 = Box(children=row, layout=box_layout)
        name_btn = Button(description='apoptosis_hill_power', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float463 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Hill power for viral load apoptosis response', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float463, units_btn, description_btn] 

        box503 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virus_fraction_released_at_death', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float464 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='fraction of internal virus released at cell death', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float464, units_btn, description_btn] 

        box504 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float465 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='max rate that infected cells secrete chemokine', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float465, units_btn, description_btn] 

        box505 = Box(children=row, layout=box_layout)
        name_btn = Button(description='debris_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float466 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate that dead cells release debris', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float466, units_btn, description_btn] 

        box506 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_activated', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float467 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='used internally to track activation of chemokine secretion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float467, units_btn, description_btn] 

        box507 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_secretion_rate_via_infection', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float468 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Type-1 interferon secretion rate for infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float468, units_btn, description_btn] 

        box508 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_interferon_secretion_rate_via_paracrine', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float469 = FloatText(value='0.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Type-1 interferon secretion rate after activation by Type-1 interferon', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float469, units_btn, description_btn] 

        box509 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_response_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float470 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Interferon response scales linearly until Int-1 exceeds this threshold', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float470, units_btn, description_btn] 

        box510 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_activation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float471 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Current interferon signaling activation state (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float471, units_btn, description_btn] 

        box511 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_virus_inhibition', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float472 = FloatText(value='0.9', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='At max interferon activation, max inhibition of viral replication (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float472, units_btn, description_btn] 

        box512 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_viral_RNA_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float473 = FloatText(value='2', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='infected cell interferon secretion saturates at this viral RNA level', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float473, units_btn, description_btn] 

        box513 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float474 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='tracks total contact time with CD8 T cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float474, units_btn, description_btn] 

        box514 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float475 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the rate at which the cell attaches to cells in contact', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float475, units_btn, description_btn] 

        box515 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_lifetime', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float476 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='the mean duration of a cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float476, units_btn, description_btn] 

        box516 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_death_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float477 = FloatText(value='50', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='threshold CD8 T cell contact time to trigger apoptosis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float477, units_btn, description_btn] 

        box517 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_attachment_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float478 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float478, units_btn, description_btn] 

        box518 = Box(children=row, layout=box_layout)
        name_btn = Button(description='elastic_attachment_coefficient', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float479 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='elastic coefficient for cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float479, units_btn, description_btn] 

        box519 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_to_next_phagocytosis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float480 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='time it takes for the apoptotic material to be phagocytosed', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float480, units_btn, description_btn] 

        box520 = Box(children=row, layout=box_layout)
        name_btn = Button(description='material_internalisation_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float481 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float481, units_btn, description_btn] 

        box521 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_macrophage_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float482 = FloatText(value='6500', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float482, units_btn, description_btn] 

        box522 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_neutrophil_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float483 = FloatText(value='1581', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float483, units_btn, description_btn] 

        box523 = Box(children=row, layout=box_layout)
        name_btn = Button(description='exhausted_macrophage_death_rat', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float484 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float484, units_btn, description_btn] 

        box524 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ability_to_phagocytose_infected_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float485 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Boolean for whether macrophages can phagocytose infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float485, units_btn, description_btn] 

        box525 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_of_DC_departure', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float486 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Time DC leaves tissue after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float486, units_btn, description_btn] 

        box526 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float487 = FloatText(value='0.117', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float487, units_btn, description_btn] 

        box527 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float488 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float488, units_btn, description_btn] 

        box528 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_chemokine_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float489 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to chemokine in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float489, units_btn, description_btn] 

        box529 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float490 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float490, units_btn, description_btn] 

        box530 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float491 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float491, units_btn, description_btn] 

        box531 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_immune_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float492 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='used internally to track activation state', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float492, units_btn, description_btn] 

        box532 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antiinflammatory_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float493 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='secretion rate of anti-inflammatory from infected epithelium cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float493, units_btn, description_btn] 

        box533 = Box(children=row, layout=box_layout)
        name_btn = Button(description='collagen_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float494 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='secretion rate of collagen from fibroblast', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float494, units_btn, description_btn] 

        box534 = Box(children=row, layout=box_layout)

        self.cell_def_vbox4 = VBox([
          div_row33, box428, box429, box430, box431, div_row34, death_model1,box432, box433, box434, box435, box436, box437, box438, death_model2,box439, box440, box441, box442, box443, box444, box445, div_row35, box446, box447, box448, box449, box450, box451, box452, box453, box454, div_row36, box455, box456, box457, box458, box459, div_row37, box460,box461,box462,self.bool22,self.bool23,chemotaxis_btn,self.bool24,box463,box464,div_row38, box465,box466,box467,box468,box469,box470,box471,box472,box473,box474,box475,box476,box477,box478,box479,box480,box481,box482,div_row39, div_row40,          box483,
          box484,
          box485,
          box486,
          box487,
          box488,
          box489,
          box490,
          box491,
          box492,
          box493,
          box494,
          box495,
          box496,
          box497,
          box498,
          box499,
          box500,
          box501,
          box502,
          box503,
          box504,
          box505,
          box506,
          box507,
          box508,
          box509,
          box510,
          box511,
          box512,
          box513,
          box514,
          box515,
          box516,
          box517,
          box518,
          box519,
          box520,
          box521,
          box522,
          box523,
          box524,
          box525,
          box526,
          box527,
          box528,
          box529,
          box530,
          box531,
          box532,
          box533,
          box534,
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox4)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = DC
        #  ------------------------- 
        div_row41 = Button(description='phenotype:cycle (model: flow_cytometry_separated_cycle_model; code=6)', disabled=True, layout=divider_button_layout)
        div_row41.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 1 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float495 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float495, units_btn, ]
        box535 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 1 -> Phase 2 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float496 = FloatText(value='0.00208333', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float496, units_btn, ]
        box536 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 2 -> Phase 3 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float497 = FloatText(value='0.00416667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float497, units_btn, ]
        box537 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 3 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float498 = FloatText(value='0.0166667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float498, units_btn, ]
        box538 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row42 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row42.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float499 = FloatText(value='8.9e-4', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float499, units_btn, ]
        box539 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float500 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float500, units_btn, ]
        box540 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float501 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float501, units_btn, ]
        box541 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float502 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float502, units_btn, ]
        box542 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float503 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float503, units_btn, ]
        box543 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float504 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float504, units_btn, ]
        box544 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float505 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float505, units_btn, ]
        box545 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float506 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float506, units_btn, ]
        box546 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float507 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float507, units_btn, ]
        box547 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float508 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float508, units_btn, ]
        box548 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float509 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float509, units_btn, ]
        box549 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float510 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float510, units_btn, ]
        box550 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float511 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float511, units_btn, ]
        box551 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float512 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float512, units_btn, ]
        box552 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row43 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row43.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float513 = FloatText(value='1767', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float513, units_btn, ]
        box553 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float514 = FloatText(value='0.75', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float514, units_btn, ]
        box554 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float515 = FloatText(value='176.7', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float515, units_btn, ]
        box555 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float516 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float516, units_btn, ]
        box556 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float517 = FloatText(value='0.045', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float517, units_btn, ]
        box557 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float518 = FloatText(value='0.0055', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float518, units_btn, ]
        box558 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcified_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float519 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float519, units_btn, ]
        box559 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float520 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float520, units_btn, ]
        box560 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float521 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float521, units_btn, ]
        box561 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row44 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row44.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float522 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float522, units_btn, ]
        box562 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float523 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float523, units_btn, ]
        box563 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float524 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float524, units_btn, ]
        box564 = Box(children=row, layout=box_layout)

        self.bool25 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float525 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool25, name_btn, self.float525, units_btn, ]
        box565 = Box(children=row, layout=box_layout)

        self.bool26 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float526 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool26, name_btn, self.float526, units_btn, ]
        box566 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row45 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row45.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float527 = FloatText(value='2', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float527, units_btn]
        box567 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float528 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float528, units_btn]
        box568 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float529 = FloatText(value='0.7', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float529, units_btn]
        box569 = Box(children=row, layout=box_layout)
        self.bool27 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        self.bool28 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool29 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate6 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate6]
        box570 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction6 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction6]
        box571 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row46 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row46.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text30 = Text(value='interferon 1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text30]
        box572 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float530 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float530, units_btn]
        box573 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float531 = FloatText(value='0.1', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float531, units_btn]
        box574 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text31 = Text(value='pro-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text31]
        box575 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float532 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float532, units_btn]
        box576 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float533 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float533, units_btn]
        box577 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text32 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text32]
        box578 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float534 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float534, units_btn]
        box579 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float535 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float535, units_btn]
        box580 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text33 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text33]
        box581 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float536 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float536, units_btn]
        box582 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float537 = FloatText(value='0.1', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float537, units_btn]
        box583 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text34 = Text(value='anti-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text34]
        box584 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float538 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float538, units_btn]
        box585 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float539 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float539, units_btn]
        box586 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text35 = Text(value='collagen', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text35]
        box587 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float540 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float540, units_btn]
        box588 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float541 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float541, units_btn]
        box589 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row47 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row47.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        div_row48 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row48.style.button_color = 'cyan'
        name_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float542 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float542, units_btn, description_btn] 

        box590 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float543 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='uncoated endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float543, units_btn, description_btn] 

        box591 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_RNA', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float544 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='RNA', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total (functional) viral RNA copies', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float544, units_btn, description_btn] 

        box592 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_protein', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float545 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='protein', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='total assembled sets of viral protein', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float545, units_btn, description_btn] 

        box593 = Box(children=row, layout=box_layout)
        name_btn = Button(description='assembled_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float546 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total assembled virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float546, units_btn, description_btn] 

        box594 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_uncoating_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float547 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which an internalized virion is uncoated', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float547, units_btn, description_btn] 

        box595 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_to_RNA_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float548 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which uncoated virion makes its mRNA available', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float548, units_btn, description_btn] 

        box596 = Box(children=row, layout=box_layout)
        name_btn = Button(description='protein_synthesis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float549 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at mRNA creates complete set of proteins', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float549, units_btn, description_btn] 

        box597 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_assembly_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float550 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which viral proteins are assembled into complete virion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float550, units_btn, description_btn] 

        box598 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_export_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float551 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which a virion is exported from a live cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float551, units_btn, description_btn] 

        box599 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float552 = FloatText(value='1000', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of unbound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float552, units_btn, description_btn] 

        box600 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float553 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of bound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float553, units_btn, description_btn] 

        box601 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float554 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of internalized unbound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float554, units_btn, description_btn] 

        box602 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float555 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of internalized bound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float555, units_btn, description_btn] 

        box603 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float556 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float556, units_btn, description_btn] 

        box604 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_endocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float557 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor-virus endocytosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float557, units_btn, description_btn] 

        box605 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_cargo_release_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float558 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus cargo release rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float558, units_btn, description_btn] 

        box606 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_recycling_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float559 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor recycling rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float559, units_btn, description_btn] 

        box607 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_infected_apoptosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float560 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='maximum rate of cell apoptosis due to viral infection', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float560, units_btn, description_btn] 

        box608 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_apoptosis_half_max', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float561 = FloatText(value='250', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='viral load at which cells reach half max apoptosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float561, units_btn, description_btn] 

        box609 = Box(children=row, layout=box_layout)
        name_btn = Button(description='apoptosis_hill_power', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float562 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Hill power for viral load apoptosis response', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float562, units_btn, description_btn] 

        box610 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virus_fraction_released_at_death', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float563 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='fraction of internal virus released at cell death', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float563, units_btn, description_btn] 

        box611 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float564 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='max rate that infected cells secrete chemokine', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float564, units_btn, description_btn] 

        box612 = Box(children=row, layout=box_layout)
        name_btn = Button(description='debris_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float565 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate that dead cells release debris', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float565, units_btn, description_btn] 

        box613 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_activated', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float566 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='used internally to track activation of chemokine secretion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float566, units_btn, description_btn] 

        box614 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_secretion_rate_via_infection', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float567 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Type-1 interferon secretion rate for infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float567, units_btn, description_btn] 

        box615 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_interferon_secretion_rate_via_paracrine', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float568 = FloatText(value='0.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Type-1 interferon secretion rate after activation by Type-1 interferon', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float568, units_btn, description_btn] 

        box616 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_response_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float569 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Interferon response scales linearly until Int-1 exceeds this threshold', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float569, units_btn, description_btn] 

        box617 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_activation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float570 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Current interferon signaling activation state (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float570, units_btn, description_btn] 

        box618 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_virus_inhibition', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float571 = FloatText(value='0.9', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='At max interferon activation, max inhibition of viral replication (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float571, units_btn, description_btn] 

        box619 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_viral_RNA_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float572 = FloatText(value='2', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='infected cell interferon secretion saturates at this viral RNA level', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float572, units_btn, description_btn] 

        box620 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float573 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='tracks total contact time with CD8 T cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float573, units_btn, description_btn] 

        box621 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float574 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the rate at which the cell attaches to cells in contact', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float574, units_btn, description_btn] 

        box622 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_lifetime', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float575 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='the mean duration of a cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float575, units_btn, description_btn] 

        box623 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_death_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float576 = FloatText(value='50', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='threshold CD8 T cell contact time to trigger apoptosis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float576, units_btn, description_btn] 

        box624 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_attachment_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float577 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float577, units_btn, description_btn] 

        box625 = Box(children=row, layout=box_layout)
        name_btn = Button(description='elastic_attachment_coefficient', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float578 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='elastic coefficient for cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float578, units_btn, description_btn] 

        box626 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_to_next_phagocytosis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float579 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='time it takes for the apoptotic material to be phagocytosed', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float579, units_btn, description_btn] 

        box627 = Box(children=row, layout=box_layout)
        name_btn = Button(description='material_internalisation_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float580 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float580, units_btn, description_btn] 

        box628 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_macrophage_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float581 = FloatText(value='6500', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float581, units_btn, description_btn] 

        box629 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_neutrophil_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float582 = FloatText(value='1581', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float582, units_btn, description_btn] 

        box630 = Box(children=row, layout=box_layout)
        name_btn = Button(description='exhausted_macrophage_death_rat', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float583 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float583, units_btn, description_btn] 

        box631 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ability_to_phagocytose_infected_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float584 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Boolean for whether macrophages can phagocytose infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float584, units_btn, description_btn] 

        box632 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_of_DC_departure', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float585 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Time DC leaves tissue after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float585, units_btn, description_btn] 

        box633 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float586 = FloatText(value='0.167', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float586, units_btn, description_btn] 

        box634 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float587 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float587, units_btn, description_btn] 

        box635 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_chemokine_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float588 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to chemokine in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float588, units_btn, description_btn] 

        box636 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float589 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float589, units_btn, description_btn] 

        box637 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float590 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float590, units_btn, description_btn] 

        box638 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_immune_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float591 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='used internally to track activation state', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float591, units_btn, description_btn] 

        box639 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antiinflammatory_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float592 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='secretion rate of anti-inflammatory from infected epithelium cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float592, units_btn, description_btn] 

        box640 = Box(children=row, layout=box_layout)
        name_btn = Button(description='collagen_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float593 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='secretion rate of collagen from fibroblast', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float593, units_btn, description_btn] 

        box641 = Box(children=row, layout=box_layout)

        self.cell_def_vbox5 = VBox([
          div_row41, box535, box536, box537, box538, div_row42, death_model1,box539, box540, box541, box542, box543, box544, box545, death_model2,box546, box547, box548, box549, box550, box551, box552, div_row43, box553, box554, box555, box556, box557, box558, box559, box560, box561, div_row44, box562, box563, box564, box565, box566, div_row45, box567,box568,box569,self.bool27,self.bool28,chemotaxis_btn,self.bool29,box570,box571,div_row46, box572,box573,box574,box575,box576,box577,box578,box579,box580,box581,box582,box583,box584,box585,box586,box587,box588,box589,div_row47, div_row48,          box590,
          box591,
          box592,
          box593,
          box594,
          box595,
          box596,
          box597,
          box598,
          box599,
          box600,
          box601,
          box602,
          box603,
          box604,
          box605,
          box606,
          box607,
          box608,
          box609,
          box610,
          box611,
          box612,
          box613,
          box614,
          box615,
          box616,
          box617,
          box618,
          box619,
          box620,
          box621,
          box622,
          box623,
          box624,
          box625,
          box626,
          box627,
          box628,
          box629,
          box630,
          box631,
          box632,
          box633,
          box634,
          box635,
          box636,
          box637,
          box638,
          box639,
          box640,
          box641,
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox5)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = CD4 Tcell
        #  ------------------------- 
        div_row49 = Button(description='phenotype:cycle (model: flow_cytometry_separated_cycle_model; code=6)', disabled=True, layout=divider_button_layout)
        div_row49.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 1 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float594 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float594, units_btn, ]
        box642 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 1 -> Phase 2 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float595 = FloatText(value='0.00208333', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float595, units_btn, ]
        box643 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 2 -> Phase 3 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float596 = FloatText(value='0.00416667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float596, units_btn, ]
        box644 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 3 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float597 = FloatText(value='0.0166667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float597, units_btn, ]
        box645 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row50 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row50.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float598 = FloatText(value='2.8e-4', step='1e-05', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float598, units_btn, ]
        box646 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float599 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float599, units_btn, ]
        box647 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float600 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float600, units_btn, ]
        box648 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float601 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float601, units_btn, ]
        box649 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float602 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float602, units_btn, ]
        box650 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float603 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float603, units_btn, ]
        box651 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float604 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float604, units_btn, ]
        box652 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float605 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float605, units_btn, ]
        box653 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float606 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float606, units_btn, ]
        box654 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float607 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float607, units_btn, ]
        box655 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float608 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float608, units_btn, ]
        box656 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float609 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float609, units_btn, ]
        box657 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float610 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float610, units_btn, ]
        box658 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float611 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float611, units_btn, ]
        box659 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row51 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row51.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float612 = FloatText(value='478', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float612, units_btn, ]
        box660 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float613 = FloatText(value='0.75', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float613, units_btn, ]
        box661 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float614 = FloatText(value='47.8', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float614, units_btn, ]
        box662 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float615 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float615, units_btn, ]
        box663 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float616 = FloatText(value='0.0045', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float616, units_btn, ]
        box664 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float617 = FloatText(value='0.0055', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float617, units_btn, ]
        box665 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcified_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float618 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float618, units_btn, ]
        box666 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float619 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float619, units_btn, ]
        box667 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float620 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float620, units_btn, ]
        box668 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row52 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row52.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float621 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float621, units_btn, ]
        box669 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float622 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float622, units_btn, ]
        box670 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float623 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float623, units_btn, ]
        box671 = Box(children=row, layout=box_layout)

        self.bool30 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float624 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool30, name_btn, self.float624, units_btn, ]
        box672 = Box(children=row, layout=box_layout)

        self.bool31 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float625 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool31, name_btn, self.float625, units_btn, ]
        box673 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row53 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row53.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float626 = FloatText(value='4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float626, units_btn]
        box674 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float627 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float627, units_btn]
        box675 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float628 = FloatText(value='0.70', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float628, units_btn]
        box676 = Box(children=row, layout=box_layout)
        self.bool32 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        self.bool33 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool34 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate7 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate7]
        box677 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction7 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction7]
        box678 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row54 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row54.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text36 = Text(value='interferon 1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text36]
        box679 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float629 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float629, units_btn]
        box680 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float630 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float630, units_btn]
        box681 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text37 = Text(value='pro-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text37]
        box682 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float631 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float631, units_btn]
        box683 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float632 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float632, units_btn]
        box684 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text38 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text38]
        box685 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float633 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float633, units_btn]
        box686 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float634 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float634, units_btn]
        box687 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text39 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text39]
        box688 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float635 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float635, units_btn]
        box689 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float636 = FloatText(value='0.1', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float636, units_btn]
        box690 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text40 = Text(value='anti-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text40]
        box691 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float637 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float637, units_btn]
        box692 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float638 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float638, units_btn]
        box693 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text41 = Text(value='collagen', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text41]
        box694 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float639 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float639, units_btn]
        box695 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float640 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float640, units_btn]
        box696 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row55 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row55.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        div_row56 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row56.style.button_color = 'cyan'
        name_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float641 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float641, units_btn, description_btn] 

        box697 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float642 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='uncoated endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float642, units_btn, description_btn] 

        box698 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_RNA', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float643 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='RNA', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total (functional) viral RNA copies', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float643, units_btn, description_btn] 

        box699 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_protein', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float644 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='protein', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='total assembled sets of viral protein', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float644, units_btn, description_btn] 

        box700 = Box(children=row, layout=box_layout)
        name_btn = Button(description='assembled_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float645 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total assembled virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float645, units_btn, description_btn] 

        box701 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_uncoating_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float646 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which an internalized virion is uncoated', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float646, units_btn, description_btn] 

        box702 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_to_RNA_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float647 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which uncoated virion makes its mRNA available', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float647, units_btn, description_btn] 

        box703 = Box(children=row, layout=box_layout)
        name_btn = Button(description='protein_synthesis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float648 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at mRNA creates complete set of proteins', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float648, units_btn, description_btn] 

        box704 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_assembly_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float649 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which viral proteins are assembled into complete virion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float649, units_btn, description_btn] 

        box705 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_export_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float650 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which a virion is exported from a live cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float650, units_btn, description_btn] 

        box706 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float651 = FloatText(value='1000', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of unbound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float651, units_btn, description_btn] 

        box707 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float652 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of bound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float652, units_btn, description_btn] 

        box708 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float653 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of internalized unbound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float653, units_btn, description_btn] 

        box709 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float654 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of internalized bound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float654, units_btn, description_btn] 

        box710 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float655 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float655, units_btn, description_btn] 

        box711 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_endocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float656 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor-virus endocytosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float656, units_btn, description_btn] 

        box712 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_cargo_release_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float657 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus cargo release rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float657, units_btn, description_btn] 

        box713 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_recycling_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float658 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor recycling rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float658, units_btn, description_btn] 

        box714 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_infected_apoptosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float659 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='maximum rate of cell apoptosis due to viral infection', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float659, units_btn, description_btn] 

        box715 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_apoptosis_half_max', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float660 = FloatText(value='250', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='viral load at which cells reach half max apoptosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float660, units_btn, description_btn] 

        box716 = Box(children=row, layout=box_layout)
        name_btn = Button(description='apoptosis_hill_power', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float661 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Hill power for viral load apoptosis response', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float661, units_btn, description_btn] 

        box717 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virus_fraction_released_at_death', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float662 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='fraction of internal virus released at cell death', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float662, units_btn, description_btn] 

        box718 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float663 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='max rate that infected cells secrete chemokine', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float663, units_btn, description_btn] 

        box719 = Box(children=row, layout=box_layout)
        name_btn = Button(description='debris_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float664 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate that dead cells release debris', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float664, units_btn, description_btn] 

        box720 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_activated', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float665 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='used internally to track activation of chemokine secretion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float665, units_btn, description_btn] 

        box721 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_secretion_rate_via_infection', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float666 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Type-1 interferon secretion rate for infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float666, units_btn, description_btn] 

        box722 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_interferon_secretion_rate_via_paracrine', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float667 = FloatText(value='0.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Type-1 interferon secretion rate after activation by Type-1 interferon', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float667, units_btn, description_btn] 

        box723 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_response_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float668 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Interferon response scales linearly until Int-1 exceeds this threshold', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float668, units_btn, description_btn] 

        box724 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_activation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float669 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Current interferon signaling activation state (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float669, units_btn, description_btn] 

        box725 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_virus_inhibition', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float670 = FloatText(value='0.9', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='At max interferon activation, max inhibition of viral replication (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float670, units_btn, description_btn] 

        box726 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_viral_RNA_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float671 = FloatText(value='2', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='infected cell interferon secretion saturates at this viral RNA level', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float671, units_btn, description_btn] 

        box727 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float672 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='tracks total contact time with CD8 T cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float672, units_btn, description_btn] 

        box728 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float673 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the rate at which the cell attaches to cells in contact', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float673, units_btn, description_btn] 

        box729 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_lifetime', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float674 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='the mean duration of a cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float674, units_btn, description_btn] 

        box730 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_death_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float675 = FloatText(value='50', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='threshold CD8 T cell contact time to trigger apoptosis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float675, units_btn, description_btn] 

        box731 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_attachment_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float676 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float676, units_btn, description_btn] 

        box732 = Box(children=row, layout=box_layout)
        name_btn = Button(description='elastic_attachment_coefficient', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float677 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='elastic coefficient for cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float677, units_btn, description_btn] 

        box733 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_to_next_phagocytosis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float678 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='time it takes for the apoptotic material to be phagocytosed', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float678, units_btn, description_btn] 

        box734 = Box(children=row, layout=box_layout)
        name_btn = Button(description='material_internalisation_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float679 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float679, units_btn, description_btn] 

        box735 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_macrophage_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float680 = FloatText(value='6500', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float680, units_btn, description_btn] 

        box736 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_neutrophil_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float681 = FloatText(value='1581', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float681, units_btn, description_btn] 

        box737 = Box(children=row, layout=box_layout)
        name_btn = Button(description='exhausted_macrophage_death_rat', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float682 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float682, units_btn, description_btn] 

        box738 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ability_to_phagocytose_infected_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float683 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Boolean for whether macrophages can phagocytose infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float683, units_btn, description_btn] 

        box739 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_of_DC_departure', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float684 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Time DC leaves tissue after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float684, units_btn, description_btn] 

        box740 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float685 = FloatText(value='0.167', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float685, units_btn, description_btn] 

        box741 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float686 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float686, units_btn, description_btn] 

        box742 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_chemokine_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float687 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to chemokine in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float687, units_btn, description_btn] 

        box743 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float688 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float688, units_btn, description_btn] 

        box744 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float689 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float689, units_btn, description_btn] 

        box745 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_immune_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float690 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='used internally to track activation state', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float690, units_btn, description_btn] 

        box746 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antiinflammatory_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float691 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='secretion rate of anti-inflammatory from infected epithelium cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float691, units_btn, description_btn] 

        box747 = Box(children=row, layout=box_layout)
        name_btn = Button(description='collagen_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float692 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='secretion rate of collagen from fibroblast', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float692, units_btn, description_btn] 

        box748 = Box(children=row, layout=box_layout)

        self.cell_def_vbox6 = VBox([
          div_row49, box642, box643, box644, box645, div_row50, death_model1,box646, box647, box648, box649, box650, box651, box652, death_model2,box653, box654, box655, box656, box657, box658, box659, div_row51, box660, box661, box662, box663, box664, box665, box666, box667, box668, div_row52, box669, box670, box671, box672, box673, div_row53, box674,box675,box676,self.bool32,self.bool33,chemotaxis_btn,self.bool34,box677,box678,div_row54, box679,box680,box681,box682,box683,box684,box685,box686,box687,box688,box689,box690,box691,box692,box693,box694,box695,box696,div_row55, div_row56,          box697,
          box698,
          box699,
          box700,
          box701,
          box702,
          box703,
          box704,
          box705,
          box706,
          box707,
          box708,
          box709,
          box710,
          box711,
          box712,
          box713,
          box714,
          box715,
          box716,
          box717,
          box718,
          box719,
          box720,
          box721,
          box722,
          box723,
          box724,
          box725,
          box726,
          box727,
          box728,
          box729,
          box730,
          box731,
          box732,
          box733,
          box734,
          box735,
          box736,
          box737,
          box738,
          box739,
          box740,
          box741,
          box742,
          box743,
          box744,
          box745,
          box746,
          box747,
          box748,
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox6)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = fibroblast
        #  ------------------------- 
        div_row57 = Button(description='phenotype:cycle (model: flow_cytometry_separated_cycle_model; code=6)', disabled=True, layout=divider_button_layout)
        div_row57.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 1 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float693 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float693, units_btn, ]
        box749 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 1 -> Phase 2 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float694 = FloatText(value='0.00208333', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float694, units_btn, ]
        box750 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 2 -> Phase 3 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float695 = FloatText(value='0.00416667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float695, units_btn, ]
        box751 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 3 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float696 = FloatText(value='0.0166667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float696, units_btn, ]
        box752 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row58 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row58.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float697 = FloatText(value='2.8e-4', step='1e-05', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float697, units_btn, ]
        box753 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float698 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float698, units_btn, ]
        box754 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float699 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float699, units_btn, ]
        box755 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float700 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float700, units_btn, ]
        box756 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float701 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float701, units_btn, ]
        box757 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float702 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float702, units_btn, ]
        box758 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float703 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float703, units_btn, ]
        box759 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float704 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float704, units_btn, ]
        box760 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float705 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float705, units_btn, ]
        box761 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float706 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float706, units_btn, ]
        box762 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float707 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float707, units_btn, ]
        box763 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float708 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float708, units_btn, ]
        box764 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float709 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float709, units_btn, ]
        box765 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float710 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float710, units_btn, ]
        box766 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row59 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row59.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float711 = FloatText(value='2494', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float711, units_btn, ]
        box767 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float712 = FloatText(value='0.75', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float712, units_btn, ]
        box768 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float713 = FloatText(value='540', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float713, units_btn, ]
        box769 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float714 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float714, units_btn, ]
        box770 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float715 = FloatText(value='0.0045', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float715, units_btn, ]
        box771 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float716 = FloatText(value='0.0055', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float716, units_btn, ]
        box772 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcified_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float717 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float717, units_btn, ]
        box773 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float718 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float718, units_btn, ]
        box774 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float719 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float719, units_btn, ]
        box775 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row60 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row60.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float720 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float720, units_btn, ]
        box776 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float721 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float721, units_btn, ]
        box777 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float722 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float722, units_btn, ]
        box778 = Box(children=row, layout=box_layout)

        self.bool35 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float723 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool35, name_btn, self.float723, units_btn, ]
        box779 = Box(children=row, layout=box_layout)

        self.bool36 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float724 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool36, name_btn, self.float724, units_btn, ]
        box780 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row61 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row61.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float725 = FloatText(value='4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float725, units_btn]
        box781 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float726 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float726, units_btn]
        box782 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float727 = FloatText(value='0.70', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float727, units_btn]
        box783 = Box(children=row, layout=box_layout)
        self.bool37 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        self.bool38 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool39 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate8 = Text(value='anti-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate8]
        box784 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction8 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction8]
        box785 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row62 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row62.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text42 = Text(value='interferon 1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text42]
        box786 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float728 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float728, units_btn]
        box787 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float729 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float729, units_btn]
        box788 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text43 = Text(value='pro-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text43]
        box789 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float730 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float730, units_btn]
        box790 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float731 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float731, units_btn]
        box791 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text44 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text44]
        box792 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float732 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float732, units_btn]
        box793 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float733 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float733, units_btn]
        box794 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text45 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text45]
        box795 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float734 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float734, units_btn]
        box796 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float735 = FloatText(value='0.1', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float735, units_btn]
        box797 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text46 = Text(value='anti-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text46]
        box798 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float736 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float736, units_btn]
        box799 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float737 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float737, units_btn]
        box800 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text47 = Text(value='collagen', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text47]
        box801 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float738 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float738, units_btn]
        box802 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float739 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float739, units_btn]
        box803 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row63 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row63.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        div_row64 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row64.style.button_color = 'cyan'
        name_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float740 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float740, units_btn, description_btn] 

        box804 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float741 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='uncoated endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float741, units_btn, description_btn] 

        box805 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_RNA', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float742 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='RNA', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total (functional) viral RNA copies', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float742, units_btn, description_btn] 

        box806 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_protein', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float743 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='protein', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='total assembled sets of viral protein', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float743, units_btn, description_btn] 

        box807 = Box(children=row, layout=box_layout)
        name_btn = Button(description='assembled_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float744 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total assembled virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float744, units_btn, description_btn] 

        box808 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_uncoating_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float745 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which an internalized virion is uncoated', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float745, units_btn, description_btn] 

        box809 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_to_RNA_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float746 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which uncoated virion makes its mRNA available', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float746, units_btn, description_btn] 

        box810 = Box(children=row, layout=box_layout)
        name_btn = Button(description='protein_synthesis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float747 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at mRNA creates complete set of proteins', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float747, units_btn, description_btn] 

        box811 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_assembly_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float748 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which viral proteins are assembled into complete virion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float748, units_btn, description_btn] 

        box812 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_export_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float749 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which a virion is exported from a live cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float749, units_btn, description_btn] 

        box813 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float750 = FloatText(value='1000', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of unbound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float750, units_btn, description_btn] 

        box814 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float751 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of bound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float751, units_btn, description_btn] 

        box815 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float752 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of internalized unbound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float752, units_btn, description_btn] 

        box816 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float753 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of internalized bound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float753, units_btn, description_btn] 

        box817 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float754 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float754, units_btn, description_btn] 

        box818 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_endocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float755 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor-virus endocytosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float755, units_btn, description_btn] 

        box819 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_cargo_release_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float756 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus cargo release rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float756, units_btn, description_btn] 

        box820 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_recycling_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float757 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor recycling rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float757, units_btn, description_btn] 

        box821 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_infected_apoptosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float758 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='maximum rate of cell apoptosis due to viral infection', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float758, units_btn, description_btn] 

        box822 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_apoptosis_half_max', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float759 = FloatText(value='250', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='viral load at which cells reach half max apoptosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float759, units_btn, description_btn] 

        box823 = Box(children=row, layout=box_layout)
        name_btn = Button(description='apoptosis_hill_power', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float760 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Hill power for viral load apoptosis response', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float760, units_btn, description_btn] 

        box824 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virus_fraction_released_at_death', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float761 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='fraction of internal virus released at cell death', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float761, units_btn, description_btn] 

        box825 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float762 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='max rate that infected cells secrete chemokine', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float762, units_btn, description_btn] 

        box826 = Box(children=row, layout=box_layout)
        name_btn = Button(description='debris_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float763 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate that dead cells release debris', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float763, units_btn, description_btn] 

        box827 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_activated', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float764 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='used internally to track activation of chemokine secretion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float764, units_btn, description_btn] 

        box828 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_secretion_rate_via_infection', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float765 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Type-1 interferon secretion rate for infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float765, units_btn, description_btn] 

        box829 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_interferon_secretion_rate_via_paracrine', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float766 = FloatText(value='0.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Type-1 interferon secretion rate after activation by Type-1 interferon', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float766, units_btn, description_btn] 

        box830 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_response_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float767 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Interferon response scales linearly until Int-1 exceeds this threshold', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float767, units_btn, description_btn] 

        box831 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_activation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float768 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Current interferon signaling activation state (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float768, units_btn, description_btn] 

        box832 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_virus_inhibition', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float769 = FloatText(value='0.9', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='At max interferon activation, max inhibition of viral replication (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float769, units_btn, description_btn] 

        box833 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_viral_RNA_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float770 = FloatText(value='2', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='infected cell interferon secretion saturates at this viral RNA level', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float770, units_btn, description_btn] 

        box834 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float771 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='tracks total contact time with CD8 T cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float771, units_btn, description_btn] 

        box835 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float772 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the rate at which the cell attaches to cells in contact', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float772, units_btn, description_btn] 

        box836 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_lifetime', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float773 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='the mean duration of a cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float773, units_btn, description_btn] 

        box837 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_death_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float774 = FloatText(value='50', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='threshold CD8 T cell contact time to trigger apoptosis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float774, units_btn, description_btn] 

        box838 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_attachment_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float775 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float775, units_btn, description_btn] 

        box839 = Box(children=row, layout=box_layout)
        name_btn = Button(description='elastic_attachment_coefficient', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float776 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='elastic coefficient for cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float776, units_btn, description_btn] 

        box840 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_to_next_phagocytosis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float777 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='time it takes for the apoptotic material to be phagocytosed', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float777, units_btn, description_btn] 

        box841 = Box(children=row, layout=box_layout)
        name_btn = Button(description='material_internalisation_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float778 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float778, units_btn, description_btn] 

        box842 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_macrophage_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float779 = FloatText(value='6500', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float779, units_btn, description_btn] 

        box843 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_neutrophil_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float780 = FloatText(value='1581', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float780, units_btn, description_btn] 

        box844 = Box(children=row, layout=box_layout)
        name_btn = Button(description='exhausted_macrophage_death_rat', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float781 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float781, units_btn, description_btn] 

        box845 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ability_to_phagocytose_infected_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float782 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Boolean for whether macrophages can phagocytose infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float782, units_btn, description_btn] 

        box846 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_of_DC_departure', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float783 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Time DC leaves tissue after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float783, units_btn, description_btn] 

        box847 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float784 = FloatText(value='0.167', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float784, units_btn, description_btn] 

        box848 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float785 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float785, units_btn, description_btn] 

        box849 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_chemokine_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float786 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to chemokine in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float786, units_btn, description_btn] 

        box850 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float787 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float787, units_btn, description_btn] 

        box851 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float788 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float788, units_btn, description_btn] 

        box852 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_immune_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float789 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='used internally to track activation state', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float789, units_btn, description_btn] 

        box853 = Box(children=row, layout=box_layout)
        name_btn = Button(description='antiinflammatory_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float790 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='secretion rate of anti-inflammatory from infected epithelium cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float790, units_btn, description_btn] 

        box854 = Box(children=row, layout=box_layout)
        name_btn = Button(description='collagen_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float791 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='secretion rate of collagen from fibroblast', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float791, units_btn, description_btn] 

        box855 = Box(children=row, layout=box_layout)

        self.cell_def_vbox7 = VBox([
          div_row57, box749, box750, box751, box752, div_row58, death_model1,box753, box754, box755, box756, box757, box758, box759, death_model2,box760, box761, box762, box763, box764, box765, box766, div_row59, box767, box768, box769, box770, box771, box772, box773, box774, box775, div_row60, box776, box777, box778, box779, box780, div_row61, box781,box782,box783,self.bool37,self.bool38,chemotaxis_btn,self.bool39,box784,box785,div_row62, box786,box787,box788,box789,box790,box791,box792,box793,box794,box795,box796,box797,box798,box799,box800,box801,box802,box803,div_row63, div_row64,          box804,
          box805,
          box806,
          box807,
          box808,
          box809,
          box810,
          box811,
          box812,
          box813,
          box814,
          box815,
          box816,
          box817,
          box818,
          box819,
          box820,
          box821,
          box822,
          box823,
          box824,
          box825,
          box826,
          box827,
          box828,
          box829,
          box830,
          box831,
          box832,
          box833,
          box834,
          box835,
          box836,
          box837,
          box838,
          box839,
          box840,
          box841,
          box842,
          box843,
          box844,
          box845,
          box846,
          box847,
          box848,
          box849,
          box850,
          box851,
          box852,
          box853,
          box854,
          box855,
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox7)



        row = [name_btn, self.float791, units_btn, description_btn] 
        box803 = Box(children=row, layout=box_layout)

        self.tab = VBox([
          self.cell_type_parent_row,  
self.cell_def_vbox0, self.cell_def_vbox1, self.cell_def_vbox2, self.cell_def_vbox3, self.cell_def_vbox4, self.cell_def_vbox5, self.cell_def_vbox6, self.cell_def_vbox7,         ])
    #------------------------------
    def cell_type_cb(self, change):
        if change['type'] == 'change' and change['name'] == 'value':
            # print("changed to %s" % change['new'])
            # self.parent_name.value = self.cell_type_parent_dict[change['new']]
            # idx_selected = list(self.cell_type_parent_dict.keys()).index(change['new'])
            idx_selected = list(self.cell_type_dict.keys()).index(change['new'])
            # print('index=',idx_selected)
            # self.vbox1.layout.visibility = 'hidden'  # vs. visible
            # self.vbox1.layout.visibility = None 

            # There's probably a better way to do this, but for now,
            # we hide all vboxes containing the widgets for the different cell defs
            # and only display the contents of the selected one.
            for vb in self.cell_def_vboxes:
                vb.layout.display = 'none'   # vs. 'contents'
            self.cell_def_vboxes[idx_selected+1].layout.display = 'contents'   # vs. 'contents'  (added "+1" to idx_selected for version 4)


    #------------------------------
    def display_cell_type_default(self):
        # print("display_cell_type_default():")
        #print("    self.cell_type_parent_dict = ",self.cell_type_parent_dict)

        # There's probably a better way to do this, but for now,
        # we hide all vboxes containing the widgets for the different cell defs
        # and only display the contents of 'default'
        for vb in self.cell_def_vboxes:
            vb.layout.display = 'none'   # vs. 'contents'
        self.cell_def_vboxes[1].layout.display = 'contents'


    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//cell_definitions')  # find unique entry point

        # ------------------ cell_definition: default
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        self.float0.value = float(uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        self.float1.value = float(uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[2]').text)
        self.float2.value = float(uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[3]').text)
        self.float3.value = float(uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[4]').text)
        # ---------  death 
        self.float4.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//death_rate').text)
        self.float5.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text)
        self.float6.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text)
        self.float7.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float8.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text)
        self.float9.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//calcification_rate').text)
        self.float10.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//relative_rupture_volume').text)
        self.float11.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//death_rate').text)
        self.float12.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        self.float13.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        self.float14.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float15.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        self.float16.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//calcification_rate').text)
        self.float17.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)
        # ---------  volume 
        self.float18.value = float(uep.find('.//cell_definition[1]//phenotype//volume//total').text)
        self.float19.value = float(uep.find('.//cell_definition[1]//phenotype//volume//fluid_fraction').text)
        self.float20.value = float(uep.find('.//cell_definition[1]//phenotype//volume//nuclear').text)
        self.float21.value = float(uep.find('.//cell_definition[1]//phenotype//volume//fluid_change_rate').text)
        self.float22.value = float(uep.find('.//cell_definition[1]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        self.float23.value = float(uep.find('.//cell_definition[1]//phenotype//volume//nuclear_biomass_change_rate').text)
        self.float24.value = float(uep.find('.//cell_definition[1]//phenotype//volume//calcified_fraction').text)
        self.float25.value = float(uep.find('.//cell_definition[1]//phenotype//volume//calcification_rate').text)
        self.float26.value = float(uep.find('.//cell_definition[1]//phenotype//volume//relative_rupture_volume').text)
        # ---------  mechanics 
        self.float27.value = float(uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float28.value = float(uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float29.value = float(uep.find('.//cell_definition[1]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool0.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool1.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float32.value = float(uep.find('.//cell_definition[1]//phenotype//motility//speed').text)
        self.float33.value = float(uep.find('.//cell_definition[1]//phenotype//motility//persistence_time').text)
        self.float34.value = float(uep.find('.//cell_definition[1]//phenotype//motility//migration_bias').text)
        self.bool2.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//motility//options//enabled').text.lower()))
        self.bool3.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//motility//options//use_2D').text.lower()))
        self.bool4.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate1.value = uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction1.value = uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text0.value = uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]').attrib['name']
        self.float35.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]//secretion_target').text)
        self.float36.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]//uptake_rate').text)
        self.text1.value = uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]').attrib['name']
        self.float37.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]//secretion_target').text)
        self.float38.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]//uptake_rate').text)
        self.text2.value = uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]').attrib['name']
        self.float39.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]//secretion_target').text)
        self.float40.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]//uptake_rate').text)
        self.text3.value = uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]').attrib['name']
        self.float41.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]//secretion_target').text)
        self.float42.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]//uptake_rate').text)
        self.text4.value = uep.find('.//cell_definition[1]//phenotype//secretion//substrate[5]').attrib['name']
        self.float43.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[5]//secretion_target').text)
        self.float44.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[5]//uptake_rate').text)
        self.text5.value = uep.find('.//cell_definition[1]//phenotype//secretion//substrate[6]').attrib['name']
        self.float45.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[6]//secretion_target').text)
        self.float46.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[6]//uptake_rate').text)
        # ---------  molecular
        # ------------------ cell_definition: lung epithelium
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        self.float99.value = float(uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        self.float100.value = float(uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[2]').text)
        self.float101.value = float(uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[3]').text)
        self.float102.value = float(uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[4]').text)
        # ---------  death 
        self.float103.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[1]//death_rate').text)
        self.float104.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text)
        self.float105.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text)
        self.float106.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float107.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text)
        self.float108.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//calcification_rate').text)
        self.float109.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//relative_rupture_volume').text)
        self.float110.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[2]//death_rate').text)
        self.float111.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        self.float112.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        self.float113.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float114.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        self.float115.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//calcification_rate').text)
        self.float116.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)
        # ---------  volume 
        self.float117.value = float(uep.find('.//cell_definition[2]//phenotype//volume//total').text)
        self.float118.value = float(uep.find('.//cell_definition[2]//phenotype//volume//fluid_fraction').text)
        self.float119.value = float(uep.find('.//cell_definition[2]//phenotype//volume//nuclear').text)
        self.float120.value = float(uep.find('.//cell_definition[2]//phenotype//volume//fluid_change_rate').text)
        self.float121.value = float(uep.find('.//cell_definition[2]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        self.float122.value = float(uep.find('.//cell_definition[2]//phenotype//volume//nuclear_biomass_change_rate').text)
        self.float123.value = float(uep.find('.//cell_definition[2]//phenotype//volume//calcified_fraction').text)
        self.float124.value = float(uep.find('.//cell_definition[2]//phenotype//volume//calcification_rate').text)
        self.float125.value = float(uep.find('.//cell_definition[2]//phenotype//volume//relative_rupture_volume').text)
        # ---------  mechanics 
        self.float126.value = float(uep.find('.//cell_definition[2]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float127.value = float(uep.find('.//cell_definition[2]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float128.value = float(uep.find('.//cell_definition[2]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool5.value = ('true' == (uep.find('.//cell_definition[2]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool6.value = ('true' == (uep.find('.//cell_definition[2]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float131.value = float(uep.find('.//cell_definition[2]//phenotype//motility//speed').text)
        self.float132.value = float(uep.find('.//cell_definition[2]//phenotype//motility//persistence_time').text)
        self.float133.value = float(uep.find('.//cell_definition[2]//phenotype//motility//migration_bias').text)
        self.bool7.value = ('true' == (uep.find('.//cell_definition[2]//phenotype//motility//options//enabled').text.lower()))
        self.bool8.value = ('true' == (uep.find('.//cell_definition[2]//phenotype//motility//options//use_2D').text.lower()))
        self.bool9.value = ('true' == (uep.find('.//cell_definition[2]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate2.value = uep.find('.//cell_definition[2]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction2.value = uep.find('.//cell_definition[2]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text6.value = uep.find('.//cell_definition[2]//phenotype//secretion//substrate[1]').attrib['name']
        self.float134.value = float(uep.find('.//cell_definition[2]//phenotype//secretion//substrate[1]//secretion_target').text)
        self.float135.value = float(uep.find('.//cell_definition[2]//phenotype//secretion//substrate[1]//uptake_rate').text)
        self.text7.value = uep.find('.//cell_definition[2]//phenotype//secretion//substrate[2]').attrib['name']
        self.float136.value = float(uep.find('.//cell_definition[2]//phenotype//secretion//substrate[2]//secretion_target').text)
        self.float137.value = float(uep.find('.//cell_definition[2]//phenotype//secretion//substrate[2]//uptake_rate').text)
        self.text8.value = uep.find('.//cell_definition[2]//phenotype//secretion//substrate[3]').attrib['name']
        self.float138.value = float(uep.find('.//cell_definition[2]//phenotype//secretion//substrate[3]//secretion_target').text)
        self.float139.value = float(uep.find('.//cell_definition[2]//phenotype//secretion//substrate[3]//uptake_rate').text)
        self.text9.value = uep.find('.//cell_definition[2]//phenotype//secretion//substrate[4]').attrib['name']
        self.float140.value = float(uep.find('.//cell_definition[2]//phenotype//secretion//substrate[4]//secretion_target').text)
        self.float141.value = float(uep.find('.//cell_definition[2]//phenotype//secretion//substrate[4]//uptake_rate').text)
        self.text10.value = uep.find('.//cell_definition[2]//phenotype//secretion//substrate[5]').attrib['name']
        self.float142.value = float(uep.find('.//cell_definition[2]//phenotype//secretion//substrate[5]//secretion_target').text)
        self.float143.value = float(uep.find('.//cell_definition[2]//phenotype//secretion//substrate[5]//uptake_rate').text)
        self.text11.value = uep.find('.//cell_definition[2]//phenotype//secretion//substrate[6]').attrib['name']
        self.float144.value = float(uep.find('.//cell_definition[2]//phenotype//secretion//substrate[6]//secretion_target').text)
        self.float145.value = float(uep.find('.//cell_definition[2]//phenotype//secretion//substrate[6]//uptake_rate').text)
        # ---------  molecular
        # ------------------ cell_definition: CD8 Tcell
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        self.float198.value = float(uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        self.float199.value = float(uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[2]').text)
        self.float200.value = float(uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[3]').text)
        self.float201.value = float(uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[4]').text)
        # ---------  death 
        self.float202.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[1]//death_rate').text)
        self.float203.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text)
        self.float204.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text)
        self.float205.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float206.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text)
        self.float207.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//calcification_rate').text)
        self.float208.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//relative_rupture_volume').text)
        self.float209.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[2]//death_rate').text)
        self.float210.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        self.float211.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        self.float212.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float213.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        self.float214.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//calcification_rate').text)
        self.float215.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)
        # ---------  volume 
        self.float216.value = float(uep.find('.//cell_definition[3]//phenotype//volume//total').text)
        self.float217.value = float(uep.find('.//cell_definition[3]//phenotype//volume//fluid_fraction').text)
        self.float218.value = float(uep.find('.//cell_definition[3]//phenotype//volume//nuclear').text)
        self.float219.value = float(uep.find('.//cell_definition[3]//phenotype//volume//fluid_change_rate').text)
        self.float220.value = float(uep.find('.//cell_definition[3]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        self.float221.value = float(uep.find('.//cell_definition[3]//phenotype//volume//nuclear_biomass_change_rate').text)
        self.float222.value = float(uep.find('.//cell_definition[3]//phenotype//volume//calcified_fraction').text)
        self.float223.value = float(uep.find('.//cell_definition[3]//phenotype//volume//calcification_rate').text)
        self.float224.value = float(uep.find('.//cell_definition[3]//phenotype//volume//relative_rupture_volume').text)
        # ---------  mechanics 
        self.float225.value = float(uep.find('.//cell_definition[3]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float226.value = float(uep.find('.//cell_definition[3]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float227.value = float(uep.find('.//cell_definition[3]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool10.value = ('true' == (uep.find('.//cell_definition[3]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool11.value = ('true' == (uep.find('.//cell_definition[3]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float230.value = float(uep.find('.//cell_definition[3]//phenotype//motility//speed').text)
        self.float231.value = float(uep.find('.//cell_definition[3]//phenotype//motility//persistence_time').text)
        self.float232.value = float(uep.find('.//cell_definition[3]//phenotype//motility//migration_bias').text)
        self.bool12.value = ('true' == (uep.find('.//cell_definition[3]//phenotype//motility//options//enabled').text.lower()))
        self.bool13.value = ('true' == (uep.find('.//cell_definition[3]//phenotype//motility//options//use_2D').text.lower()))
        self.bool14.value = ('true' == (uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate3.value = uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction3.value = uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text12.value = uep.find('.//cell_definition[3]//phenotype//secretion//substrate[1]').attrib['name']
        self.float233.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[1]//secretion_target').text)
        self.float234.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[1]//uptake_rate').text)
        self.text13.value = uep.find('.//cell_definition[3]//phenotype//secretion//substrate[2]').attrib['name']
        self.float235.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[2]//secretion_target').text)
        self.float236.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[2]//uptake_rate').text)
        self.text14.value = uep.find('.//cell_definition[3]//phenotype//secretion//substrate[3]').attrib['name']
        self.float237.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[3]//secretion_target').text)
        self.float238.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[3]//uptake_rate').text)
        self.text15.value = uep.find('.//cell_definition[3]//phenotype//secretion//substrate[4]').attrib['name']
        self.float239.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[4]//secretion_target').text)
        self.float240.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[4]//uptake_rate').text)
        self.text16.value = uep.find('.//cell_definition[3]//phenotype//secretion//substrate[5]').attrib['name']
        self.float241.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[5]//secretion_target').text)
        self.float242.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[5]//uptake_rate').text)
        self.text17.value = uep.find('.//cell_definition[3]//phenotype//secretion//substrate[6]').attrib['name']
        self.float243.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[6]//secretion_target').text)
        self.float244.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[6]//uptake_rate').text)
        # ---------  molecular
        # ------------------ cell_definition: macrophage
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        self.float297.value = float(uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        self.float298.value = float(uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[2]').text)
        self.float299.value = float(uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[3]').text)
        self.float300.value = float(uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[4]').text)
        # ---------  death 
        self.float301.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[1]//death_rate').text)
        self.float302.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text)
        self.float303.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text)
        self.float304.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float305.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text)
        self.float306.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//calcification_rate').text)
        self.float307.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//relative_rupture_volume').text)
        self.float308.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[2]//death_rate').text)
        self.float309.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        self.float310.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        self.float311.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float312.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        self.float313.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//calcification_rate').text)
        self.float314.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)
        # ---------  volume 
        self.float315.value = float(uep.find('.//cell_definition[4]//phenotype//volume//total').text)
        self.float316.value = float(uep.find('.//cell_definition[4]//phenotype//volume//fluid_fraction').text)
        self.float317.value = float(uep.find('.//cell_definition[4]//phenotype//volume//nuclear').text)
        self.float318.value = float(uep.find('.//cell_definition[4]//phenotype//volume//fluid_change_rate').text)
        self.float319.value = float(uep.find('.//cell_definition[4]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        self.float320.value = float(uep.find('.//cell_definition[4]//phenotype//volume//nuclear_biomass_change_rate').text)
        self.float321.value = float(uep.find('.//cell_definition[4]//phenotype//volume//calcified_fraction').text)
        self.float322.value = float(uep.find('.//cell_definition[4]//phenotype//volume//calcification_rate').text)
        self.float323.value = float(uep.find('.//cell_definition[4]//phenotype//volume//relative_rupture_volume').text)
        # ---------  mechanics 
        self.float324.value = float(uep.find('.//cell_definition[4]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float325.value = float(uep.find('.//cell_definition[4]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float326.value = float(uep.find('.//cell_definition[4]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool15.value = ('true' == (uep.find('.//cell_definition[4]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool16.value = ('true' == (uep.find('.//cell_definition[4]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float329.value = float(uep.find('.//cell_definition[4]//phenotype//motility//speed').text)
        self.float330.value = float(uep.find('.//cell_definition[4]//phenotype//motility//persistence_time').text)
        self.float331.value = float(uep.find('.//cell_definition[4]//phenotype//motility//migration_bias').text)
        self.bool17.value = ('true' == (uep.find('.//cell_definition[4]//phenotype//motility//options//enabled').text.lower()))
        self.bool18.value = ('true' == (uep.find('.//cell_definition[4]//phenotype//motility//options//use_2D').text.lower()))
        self.bool19.value = ('true' == (uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate4.value = uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction4.value = uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text18.value = uep.find('.//cell_definition[4]//phenotype//secretion//substrate[1]').attrib['name']
        self.float332.value = float(uep.find('.//cell_definition[4]//phenotype//secretion//substrate[1]//secretion_target').text)
        self.float333.value = float(uep.find('.//cell_definition[4]//phenotype//secretion//substrate[1]//uptake_rate').text)
        self.text19.value = uep.find('.//cell_definition[4]//phenotype//secretion//substrate[2]').attrib['name']
        self.float334.value = float(uep.find('.//cell_definition[4]//phenotype//secretion//substrate[2]//secretion_target').text)
        self.float335.value = float(uep.find('.//cell_definition[4]//phenotype//secretion//substrate[2]//uptake_rate').text)
        self.text20.value = uep.find('.//cell_definition[4]//phenotype//secretion//substrate[3]').attrib['name']
        self.float336.value = float(uep.find('.//cell_definition[4]//phenotype//secretion//substrate[3]//secretion_target').text)
        self.float337.value = float(uep.find('.//cell_definition[4]//phenotype//secretion//substrate[3]//uptake_rate').text)
        self.text21.value = uep.find('.//cell_definition[4]//phenotype//secretion//substrate[4]').attrib['name']
        self.float338.value = float(uep.find('.//cell_definition[4]//phenotype//secretion//substrate[4]//secretion_target').text)
        self.float339.value = float(uep.find('.//cell_definition[4]//phenotype//secretion//substrate[4]//uptake_rate').text)
        self.text22.value = uep.find('.//cell_definition[4]//phenotype//secretion//substrate[5]').attrib['name']
        self.float340.value = float(uep.find('.//cell_definition[4]//phenotype//secretion//substrate[5]//secretion_target').text)
        self.float341.value = float(uep.find('.//cell_definition[4]//phenotype//secretion//substrate[5]//uptake_rate').text)
        self.text23.value = uep.find('.//cell_definition[4]//phenotype//secretion//substrate[6]').attrib['name']
        self.float342.value = float(uep.find('.//cell_definition[4]//phenotype//secretion//substrate[6]//secretion_target').text)
        self.float343.value = float(uep.find('.//cell_definition[4]//phenotype//secretion//substrate[6]//uptake_rate').text)
        # ---------  molecular
        # ------------------ cell_definition: neutrophil
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        self.float396.value = float(uep.find('.//cell_definition[5]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        self.float397.value = float(uep.find('.//cell_definition[5]//phenotype//cycle//phase_transition_rates//rate[2]').text)
        self.float398.value = float(uep.find('.//cell_definition[5]//phenotype//cycle//phase_transition_rates//rate[3]').text)
        self.float399.value = float(uep.find('.//cell_definition[5]//phenotype//cycle//phase_transition_rates//rate[4]').text)
        # ---------  death 
        self.float400.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[1]//death_rate').text)
        self.float401.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text)
        self.float402.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text)
        self.float403.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float404.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text)
        self.float405.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//calcification_rate').text)
        self.float406.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//relative_rupture_volume').text)
        self.float407.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[2]//death_rate').text)
        self.float408.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        self.float409.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        self.float410.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float411.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        self.float412.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//calcification_rate').text)
        self.float413.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)
        # ---------  volume 
        self.float414.value = float(uep.find('.//cell_definition[5]//phenotype//volume//total').text)
        self.float415.value = float(uep.find('.//cell_definition[5]//phenotype//volume//fluid_fraction').text)
        self.float416.value = float(uep.find('.//cell_definition[5]//phenotype//volume//nuclear').text)
        self.float417.value = float(uep.find('.//cell_definition[5]//phenotype//volume//fluid_change_rate').text)
        self.float418.value = float(uep.find('.//cell_definition[5]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        self.float419.value = float(uep.find('.//cell_definition[5]//phenotype//volume//nuclear_biomass_change_rate').text)
        self.float420.value = float(uep.find('.//cell_definition[5]//phenotype//volume//calcified_fraction').text)
        self.float421.value = float(uep.find('.//cell_definition[5]//phenotype//volume//calcification_rate').text)
        self.float422.value = float(uep.find('.//cell_definition[5]//phenotype//volume//relative_rupture_volume').text)
        # ---------  mechanics 
        self.float423.value = float(uep.find('.//cell_definition[5]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float424.value = float(uep.find('.//cell_definition[5]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float425.value = float(uep.find('.//cell_definition[5]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool20.value = ('true' == (uep.find('.//cell_definition[5]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool21.value = ('true' == (uep.find('.//cell_definition[5]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float428.value = float(uep.find('.//cell_definition[5]//phenotype//motility//speed').text)
        self.float429.value = float(uep.find('.//cell_definition[5]//phenotype//motility//persistence_time').text)
        self.float430.value = float(uep.find('.//cell_definition[5]//phenotype//motility//migration_bias').text)
        self.bool22.value = ('true' == (uep.find('.//cell_definition[5]//phenotype//motility//options//enabled').text.lower()))
        self.bool23.value = ('true' == (uep.find('.//cell_definition[5]//phenotype//motility//options//use_2D').text.lower()))
        self.bool24.value = ('true' == (uep.find('.//cell_definition[5]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate5.value = uep.find('.//cell_definition[5]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction5.value = uep.find('.//cell_definition[5]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text24.value = uep.find('.//cell_definition[5]//phenotype//secretion//substrate[1]').attrib['name']
        self.float431.value = float(uep.find('.//cell_definition[5]//phenotype//secretion//substrate[1]//secretion_target').text)
        self.float432.value = float(uep.find('.//cell_definition[5]//phenotype//secretion//substrate[1]//uptake_rate').text)
        self.text25.value = uep.find('.//cell_definition[5]//phenotype//secretion//substrate[2]').attrib['name']
        self.float433.value = float(uep.find('.//cell_definition[5]//phenotype//secretion//substrate[2]//secretion_target').text)
        self.float434.value = float(uep.find('.//cell_definition[5]//phenotype//secretion//substrate[2]//uptake_rate').text)
        self.text26.value = uep.find('.//cell_definition[5]//phenotype//secretion//substrate[3]').attrib['name']
        self.float435.value = float(uep.find('.//cell_definition[5]//phenotype//secretion//substrate[3]//secretion_target').text)
        self.float436.value = float(uep.find('.//cell_definition[5]//phenotype//secretion//substrate[3]//uptake_rate').text)
        self.text27.value = uep.find('.//cell_definition[5]//phenotype//secretion//substrate[4]').attrib['name']
        self.float437.value = float(uep.find('.//cell_definition[5]//phenotype//secretion//substrate[4]//secretion_target').text)
        self.float438.value = float(uep.find('.//cell_definition[5]//phenotype//secretion//substrate[4]//uptake_rate').text)
        self.text28.value = uep.find('.//cell_definition[5]//phenotype//secretion//substrate[5]').attrib['name']
        self.float439.value = float(uep.find('.//cell_definition[5]//phenotype//secretion//substrate[5]//secretion_target').text)
        self.float440.value = float(uep.find('.//cell_definition[5]//phenotype//secretion//substrate[5]//uptake_rate').text)
        self.text29.value = uep.find('.//cell_definition[5]//phenotype//secretion//substrate[6]').attrib['name']
        self.float441.value = float(uep.find('.//cell_definition[5]//phenotype//secretion//substrate[6]//secretion_target').text)
        self.float442.value = float(uep.find('.//cell_definition[5]//phenotype//secretion//substrate[6]//uptake_rate').text)
        # ---------  molecular
        # ------------------ cell_definition: DC
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        self.float495.value = float(uep.find('.//cell_definition[6]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        self.float496.value = float(uep.find('.//cell_definition[6]//phenotype//cycle//phase_transition_rates//rate[2]').text)
        self.float497.value = float(uep.find('.//cell_definition[6]//phenotype//cycle//phase_transition_rates//rate[3]').text)
        self.float498.value = float(uep.find('.//cell_definition[6]//phenotype//cycle//phase_transition_rates//rate[4]').text)
        # ---------  death 
        self.float499.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[1]//death_rate').text)
        self.float500.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text)
        self.float501.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text)
        self.float502.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float503.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text)
        self.float504.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//calcification_rate').text)
        self.float505.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//relative_rupture_volume').text)
        self.float506.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[2]//death_rate').text)
        self.float507.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        self.float508.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        self.float509.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float510.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        self.float511.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//calcification_rate').text)
        self.float512.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)
        # ---------  volume 
        self.float513.value = float(uep.find('.//cell_definition[6]//phenotype//volume//total').text)
        self.float514.value = float(uep.find('.//cell_definition[6]//phenotype//volume//fluid_fraction').text)
        self.float515.value = float(uep.find('.//cell_definition[6]//phenotype//volume//nuclear').text)
        self.float516.value = float(uep.find('.//cell_definition[6]//phenotype//volume//fluid_change_rate').text)
        self.float517.value = float(uep.find('.//cell_definition[6]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        self.float518.value = float(uep.find('.//cell_definition[6]//phenotype//volume//nuclear_biomass_change_rate').text)
        self.float519.value = float(uep.find('.//cell_definition[6]//phenotype//volume//calcified_fraction').text)
        self.float520.value = float(uep.find('.//cell_definition[6]//phenotype//volume//calcification_rate').text)
        self.float521.value = float(uep.find('.//cell_definition[6]//phenotype//volume//relative_rupture_volume').text)
        # ---------  mechanics 
        self.float522.value = float(uep.find('.//cell_definition[6]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float523.value = float(uep.find('.//cell_definition[6]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float524.value = float(uep.find('.//cell_definition[6]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool25.value = ('true' == (uep.find('.//cell_definition[6]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool26.value = ('true' == (uep.find('.//cell_definition[6]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float527.value = float(uep.find('.//cell_definition[6]//phenotype//motility//speed').text)
        self.float528.value = float(uep.find('.//cell_definition[6]//phenotype//motility//persistence_time').text)
        self.float529.value = float(uep.find('.//cell_definition[6]//phenotype//motility//migration_bias').text)
        self.bool27.value = ('true' == (uep.find('.//cell_definition[6]//phenotype//motility//options//enabled').text.lower()))
        self.bool28.value = ('true' == (uep.find('.//cell_definition[6]//phenotype//motility//options//use_2D').text.lower()))
        self.bool29.value = ('true' == (uep.find('.//cell_definition[6]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate6.value = uep.find('.//cell_definition[6]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction6.value = uep.find('.//cell_definition[6]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text30.value = uep.find('.//cell_definition[6]//phenotype//secretion//substrate[1]').attrib['name']
        self.float530.value = float(uep.find('.//cell_definition[6]//phenotype//secretion//substrate[1]//secretion_target').text)
        self.float531.value = float(uep.find('.//cell_definition[6]//phenotype//secretion//substrate[1]//uptake_rate').text)
        self.text31.value = uep.find('.//cell_definition[6]//phenotype//secretion//substrate[2]').attrib['name']
        self.float532.value = float(uep.find('.//cell_definition[6]//phenotype//secretion//substrate[2]//secretion_target').text)
        self.float533.value = float(uep.find('.//cell_definition[6]//phenotype//secretion//substrate[2]//uptake_rate').text)
        self.text32.value = uep.find('.//cell_definition[6]//phenotype//secretion//substrate[3]').attrib['name']
        self.float534.value = float(uep.find('.//cell_definition[6]//phenotype//secretion//substrate[3]//secretion_target').text)
        self.float535.value = float(uep.find('.//cell_definition[6]//phenotype//secretion//substrate[3]//uptake_rate').text)
        self.text33.value = uep.find('.//cell_definition[6]//phenotype//secretion//substrate[4]').attrib['name']
        self.float536.value = float(uep.find('.//cell_definition[6]//phenotype//secretion//substrate[4]//secretion_target').text)
        self.float537.value = float(uep.find('.//cell_definition[6]//phenotype//secretion//substrate[4]//uptake_rate').text)
        self.text34.value = uep.find('.//cell_definition[6]//phenotype//secretion//substrate[5]').attrib['name']
        self.float538.value = float(uep.find('.//cell_definition[6]//phenotype//secretion//substrate[5]//secretion_target').text)
        self.float539.value = float(uep.find('.//cell_definition[6]//phenotype//secretion//substrate[5]//uptake_rate').text)
        self.text35.value = uep.find('.//cell_definition[6]//phenotype//secretion//substrate[6]').attrib['name']
        self.float540.value = float(uep.find('.//cell_definition[6]//phenotype//secretion//substrate[6]//secretion_target').text)
        self.float541.value = float(uep.find('.//cell_definition[6]//phenotype//secretion//substrate[6]//uptake_rate').text)
        # ---------  molecular
        # ------------------ cell_definition: CD4 Tcell
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        self.float594.value = float(uep.find('.//cell_definition[7]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        self.float595.value = float(uep.find('.//cell_definition[7]//phenotype//cycle//phase_transition_rates//rate[2]').text)
        self.float596.value = float(uep.find('.//cell_definition[7]//phenotype//cycle//phase_transition_rates//rate[3]').text)
        self.float597.value = float(uep.find('.//cell_definition[7]//phenotype//cycle//phase_transition_rates//rate[4]').text)
        # ---------  death 
        self.float598.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[1]//death_rate').text)
        self.float599.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text)
        self.float600.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text)
        self.float601.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float602.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text)
        self.float603.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//calcification_rate').text)
        self.float604.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//relative_rupture_volume').text)
        self.float605.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[2]//death_rate').text)
        self.float606.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        self.float607.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        self.float608.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float609.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        self.float610.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//calcification_rate').text)
        self.float611.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)
        # ---------  volume 
        self.float612.value = float(uep.find('.//cell_definition[7]//phenotype//volume//total').text)
        self.float613.value = float(uep.find('.//cell_definition[7]//phenotype//volume//fluid_fraction').text)
        self.float614.value = float(uep.find('.//cell_definition[7]//phenotype//volume//nuclear').text)
        self.float615.value = float(uep.find('.//cell_definition[7]//phenotype//volume//fluid_change_rate').text)
        self.float616.value = float(uep.find('.//cell_definition[7]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        self.float617.value = float(uep.find('.//cell_definition[7]//phenotype//volume//nuclear_biomass_change_rate').text)
        self.float618.value = float(uep.find('.//cell_definition[7]//phenotype//volume//calcified_fraction').text)
        self.float619.value = float(uep.find('.//cell_definition[7]//phenotype//volume//calcification_rate').text)
        self.float620.value = float(uep.find('.//cell_definition[7]//phenotype//volume//relative_rupture_volume').text)
        # ---------  mechanics 
        self.float621.value = float(uep.find('.//cell_definition[7]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float622.value = float(uep.find('.//cell_definition[7]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float623.value = float(uep.find('.//cell_definition[7]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool30.value = ('true' == (uep.find('.//cell_definition[7]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool31.value = ('true' == (uep.find('.//cell_definition[7]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float626.value = float(uep.find('.//cell_definition[7]//phenotype//motility//speed').text)
        self.float627.value = float(uep.find('.//cell_definition[7]//phenotype//motility//persistence_time').text)
        self.float628.value = float(uep.find('.//cell_definition[7]//phenotype//motility//migration_bias').text)
        self.bool32.value = ('true' == (uep.find('.//cell_definition[7]//phenotype//motility//options//enabled').text.lower()))
        self.bool33.value = ('true' == (uep.find('.//cell_definition[7]//phenotype//motility//options//use_2D').text.lower()))
        self.bool34.value = ('true' == (uep.find('.//cell_definition[7]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate7.value = uep.find('.//cell_definition[7]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction7.value = uep.find('.//cell_definition[7]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text36.value = uep.find('.//cell_definition[7]//phenotype//secretion//substrate[1]').attrib['name']
        self.float629.value = float(uep.find('.//cell_definition[7]//phenotype//secretion//substrate[1]//secretion_target').text)
        self.float630.value = float(uep.find('.//cell_definition[7]//phenotype//secretion//substrate[1]//uptake_rate').text)
        self.text37.value = uep.find('.//cell_definition[7]//phenotype//secretion//substrate[2]').attrib['name']
        self.float631.value = float(uep.find('.//cell_definition[7]//phenotype//secretion//substrate[2]//secretion_target').text)
        self.float632.value = float(uep.find('.//cell_definition[7]//phenotype//secretion//substrate[2]//uptake_rate').text)
        self.text38.value = uep.find('.//cell_definition[7]//phenotype//secretion//substrate[3]').attrib['name']
        self.float633.value = float(uep.find('.//cell_definition[7]//phenotype//secretion//substrate[3]//secretion_target').text)
        self.float634.value = float(uep.find('.//cell_definition[7]//phenotype//secretion//substrate[3]//uptake_rate').text)
        self.text39.value = uep.find('.//cell_definition[7]//phenotype//secretion//substrate[4]').attrib['name']
        self.float635.value = float(uep.find('.//cell_definition[7]//phenotype//secretion//substrate[4]//secretion_target').text)
        self.float636.value = float(uep.find('.//cell_definition[7]//phenotype//secretion//substrate[4]//uptake_rate').text)
        self.text40.value = uep.find('.//cell_definition[7]//phenotype//secretion//substrate[5]').attrib['name']
        self.float637.value = float(uep.find('.//cell_definition[7]//phenotype//secretion//substrate[5]//secretion_target').text)
        self.float638.value = float(uep.find('.//cell_definition[7]//phenotype//secretion//substrate[5]//uptake_rate').text)
        self.text41.value = uep.find('.//cell_definition[7]//phenotype//secretion//substrate[6]').attrib['name']
        self.float639.value = float(uep.find('.//cell_definition[7]//phenotype//secretion//substrate[6]//secretion_target').text)
        self.float640.value = float(uep.find('.//cell_definition[7]//phenotype//secretion//substrate[6]//uptake_rate').text)
        # ---------  molecular
        # ------------------ cell_definition: fibroblast
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        self.float693.value = float(uep.find('.//cell_definition[8]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        self.float694.value = float(uep.find('.//cell_definition[8]//phenotype//cycle//phase_transition_rates//rate[2]').text)
        self.float695.value = float(uep.find('.//cell_definition[8]//phenotype//cycle//phase_transition_rates//rate[3]').text)
        self.float696.value = float(uep.find('.//cell_definition[8]//phenotype//cycle//phase_transition_rates//rate[4]').text)
        # ---------  death 
        self.float697.value = float(uep.find('.//cell_definition[8]//phenotype//death//model[1]//death_rate').text)
        self.float698.value = float(uep.find('.//cell_definition[8]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text)
        self.float699.value = float(uep.find('.//cell_definition[8]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text)
        self.float700.value = float(uep.find('.//cell_definition[8]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float701.value = float(uep.find('.//cell_definition[8]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text)
        self.float702.value = float(uep.find('.//cell_definition[8]//phenotype//death//model[1]//parameters//calcification_rate').text)
        self.float703.value = float(uep.find('.//cell_definition[8]//phenotype//death//model[1]//parameters//relative_rupture_volume').text)
        self.float704.value = float(uep.find('.//cell_definition[8]//phenotype//death//model[2]//death_rate').text)
        self.float705.value = float(uep.find('.//cell_definition[8]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        self.float706.value = float(uep.find('.//cell_definition[8]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        self.float707.value = float(uep.find('.//cell_definition[8]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float708.value = float(uep.find('.//cell_definition[8]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        self.float709.value = float(uep.find('.//cell_definition[8]//phenotype//death//model[2]//parameters//calcification_rate').text)
        self.float710.value = float(uep.find('.//cell_definition[8]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)
        # ---------  volume 
        self.float711.value = float(uep.find('.//cell_definition[8]//phenotype//volume//total').text)
        self.float712.value = float(uep.find('.//cell_definition[8]//phenotype//volume//fluid_fraction').text)
        self.float713.value = float(uep.find('.//cell_definition[8]//phenotype//volume//nuclear').text)
        self.float714.value = float(uep.find('.//cell_definition[8]//phenotype//volume//fluid_change_rate').text)
        self.float715.value = float(uep.find('.//cell_definition[8]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        self.float716.value = float(uep.find('.//cell_definition[8]//phenotype//volume//nuclear_biomass_change_rate').text)
        self.float717.value = float(uep.find('.//cell_definition[8]//phenotype//volume//calcified_fraction').text)
        self.float718.value = float(uep.find('.//cell_definition[8]//phenotype//volume//calcification_rate').text)
        self.float719.value = float(uep.find('.//cell_definition[8]//phenotype//volume//relative_rupture_volume').text)
        # ---------  mechanics 
        self.float720.value = float(uep.find('.//cell_definition[8]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float721.value = float(uep.find('.//cell_definition[8]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float722.value = float(uep.find('.//cell_definition[8]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool35.value = ('true' == (uep.find('.//cell_definition[8]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool36.value = ('true' == (uep.find('.//cell_definition[8]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float725.value = float(uep.find('.//cell_definition[8]//phenotype//motility//speed').text)
        self.float726.value = float(uep.find('.//cell_definition[8]//phenotype//motility//persistence_time').text)
        self.float727.value = float(uep.find('.//cell_definition[8]//phenotype//motility//migration_bias').text)
        self.bool37.value = ('true' == (uep.find('.//cell_definition[8]//phenotype//motility//options//enabled').text.lower()))
        self.bool38.value = ('true' == (uep.find('.//cell_definition[8]//phenotype//motility//options//use_2D').text.lower()))
        self.bool39.value = ('true' == (uep.find('.//cell_definition[8]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate8.value = uep.find('.//cell_definition[8]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction8.value = uep.find('.//cell_definition[8]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text42.value = uep.find('.//cell_definition[8]//phenotype//secretion//substrate[1]').attrib['name']
        self.float728.value = float(uep.find('.//cell_definition[8]//phenotype//secretion//substrate[1]//secretion_target').text)
        self.float729.value = float(uep.find('.//cell_definition[8]//phenotype//secretion//substrate[1]//uptake_rate').text)
        self.text43.value = uep.find('.//cell_definition[8]//phenotype//secretion//substrate[2]').attrib['name']
        self.float730.value = float(uep.find('.//cell_definition[8]//phenotype//secretion//substrate[2]//secretion_target').text)
        self.float731.value = float(uep.find('.//cell_definition[8]//phenotype//secretion//substrate[2]//uptake_rate').text)
        self.text44.value = uep.find('.//cell_definition[8]//phenotype//secretion//substrate[3]').attrib['name']
        self.float732.value = float(uep.find('.//cell_definition[8]//phenotype//secretion//substrate[3]//secretion_target').text)
        self.float733.value = float(uep.find('.//cell_definition[8]//phenotype//secretion//substrate[3]//uptake_rate').text)
        self.text45.value = uep.find('.//cell_definition[8]//phenotype//secretion//substrate[4]').attrib['name']
        self.float734.value = float(uep.find('.//cell_definition[8]//phenotype//secretion//substrate[4]//secretion_target').text)
        self.float735.value = float(uep.find('.//cell_definition[8]//phenotype//secretion//substrate[4]//uptake_rate').text)
        self.text46.value = uep.find('.//cell_definition[8]//phenotype//secretion//substrate[5]').attrib['name']
        self.float736.value = float(uep.find('.//cell_definition[8]//phenotype//secretion//substrate[5]//secretion_target').text)
        self.float737.value = float(uep.find('.//cell_definition[8]//phenotype//secretion//substrate[5]//uptake_rate').text)
        self.text47.value = uep.find('.//cell_definition[8]//phenotype//secretion//substrate[6]').attrib['name']
        self.float738.value = float(uep.find('.//cell_definition[8]//phenotype//secretion//substrate[6]//secretion_target').text)
        self.float739.value = float(uep.find('.//cell_definition[8]//phenotype//secretion//substrate[6]//uptake_rate').text)
        # ---------  molecular


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//cell_definitions')  # find unique entry point

        # ------------------ cell_definition: default
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float0.value)
        uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[2]').text = str(self.float1.value)
        uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[3]').text = str(self.float2.value)
        uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[4]').text = str(self.float3.value)
        # ---------  death 
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//death_rate').text = str(self.float4.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text = str(self.float5.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text = str(self.float6.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float7.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text = str(self.float8.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//calcification_rate').text = str(self.float9.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//relative_rupture_volume').text = str(self.float10.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//death_rate').text = str(self.float11.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text = str(self.float12.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text = str(self.float13.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float14.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text = str(self.float15.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//calcification_rate').text = str(self.float16.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//relative_rupture_volume').text = str(self.float17.value)
        # ---------  volume 
        uep.find('.//cell_definition[1]//phenotype//volume//total').text = str(self.float18.value)
        uep.find('.//cell_definition[1]//phenotype//volume//fluid_fraction').text = str(self.float19.value)
        uep.find('.//cell_definition[1]//phenotype//volume//nuclear').text = str(self.float20.value)
        uep.find('.//cell_definition[1]//phenotype//volume//fluid_change_rate').text = str(self.float21.value)
        uep.find('.//cell_definition[1]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float22.value)
        uep.find('.//cell_definition[1]//phenotype//volume//nuclear_biomass_change_rate').text = str(self.float23.value)
        uep.find('.//cell_definition[1]//phenotype//volume//calcified_fraction').text = str(self.float24.value)
        uep.find('.//cell_definition[1]//phenotype//volume//calcification_rate').text = str(self.float25.value)
        uep.find('.//cell_definition[1]//phenotype//volume//relative_rupture_volume').text = str(self.float26.value)
        # ---------  mechanics 
        uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float27.value)
        uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float28.value)
        uep.find('.//cell_definition[1]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float29.value)
        uep.find('.//cell_definition[1]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool0.value)
        uep.find('.//cell_definition[1]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool1.value)
        # ---------  motility 
        uep.find('.//cell_definition[1]//phenotype//motility//speed').text = str(self.float32.value)
        uep.find('.//cell_definition[1]//phenotype//motility//persistence_time').text = str(self.float33.value)
        uep.find('.//cell_definition[1]//phenotype//motility//migration_bias').text = str(self.float34.value)
        uep.find('.//cell_definition[1]//phenotype//motility//options//enabled').text = str(self.bool2.value)
        uep.find('.//cell_definition[1]//phenotype//motility//options//use_2D').text = str(self.bool3.value)
        uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool4.value)
        uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate1.value)
        uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction1.value)
        # ---------  secretion 
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text0.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]//secretion_target').text = str(self.float35.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]//uptake_rate').text = str(self.float36.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text1.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]//secretion_target').text = str(self.float37.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]//uptake_rate').text = str(self.float38.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text2.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]//secretion_target').text = str(self.float39.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]//uptake_rate').text = str(self.float40.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]').attrib['name'] = str(self.text3.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]//secretion_target').text = str(self.float41.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]//uptake_rate').text = str(self.float42.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[5]').attrib['name'] = str(self.text4.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[5]//secretion_target').text = str(self.float43.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[5]//uptake_rate').text = str(self.float44.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[6]').attrib['name'] = str(self.text5.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[6]//secretion_target').text = str(self.float45.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[6]//uptake_rate').text = str(self.float46.value)
        # ---------  molecular
        # ------------------ cell_definition: lung epithelium
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float99.value)
        uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[2]').text = str(self.float100.value)
        uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[3]').text = str(self.float101.value)
        uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[4]').text = str(self.float102.value)
        # ---------  death 
        uep.find('.//cell_definition[2]//phenotype//death//model[1]//death_rate').text = str(self.float103.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text = str(self.float104.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text = str(self.float105.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float106.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text = str(self.float107.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//calcification_rate').text = str(self.float108.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//relative_rupture_volume').text = str(self.float109.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[2]//death_rate').text = str(self.float110.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text = str(self.float111.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text = str(self.float112.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float113.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text = str(self.float114.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//calcification_rate').text = str(self.float115.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//relative_rupture_volume').text = str(self.float116.value)
        # ---------  volume 
        uep.find('.//cell_definition[2]//phenotype//volume//total').text = str(self.float117.value)
        uep.find('.//cell_definition[2]//phenotype//volume//fluid_fraction').text = str(self.float118.value)
        uep.find('.//cell_definition[2]//phenotype//volume//nuclear').text = str(self.float119.value)
        uep.find('.//cell_definition[2]//phenotype//volume//fluid_change_rate').text = str(self.float120.value)
        uep.find('.//cell_definition[2]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float121.value)
        uep.find('.//cell_definition[2]//phenotype//volume//nuclear_biomass_change_rate').text = str(self.float122.value)
        uep.find('.//cell_definition[2]//phenotype//volume//calcified_fraction').text = str(self.float123.value)
        uep.find('.//cell_definition[2]//phenotype//volume//calcification_rate').text = str(self.float124.value)
        uep.find('.//cell_definition[2]//phenotype//volume//relative_rupture_volume').text = str(self.float125.value)
        # ---------  mechanics 
        uep.find('.//cell_definition[2]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float126.value)
        uep.find('.//cell_definition[2]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float127.value)
        uep.find('.//cell_definition[2]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float128.value)
        uep.find('.//cell_definition[2]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool5.value)
        uep.find('.//cell_definition[2]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool6.value)
        # ---------  motility 
        uep.find('.//cell_definition[2]//phenotype//motility//speed').text = str(self.float131.value)
        uep.find('.//cell_definition[2]//phenotype//motility//persistence_time').text = str(self.float132.value)
        uep.find('.//cell_definition[2]//phenotype//motility//migration_bias').text = str(self.float133.value)
        uep.find('.//cell_definition[2]//phenotype//motility//options//enabled').text = str(self.bool7.value)
        uep.find('.//cell_definition[2]//phenotype//motility//options//use_2D').text = str(self.bool8.value)
        uep.find('.//cell_definition[2]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool9.value)
        uep.find('.//cell_definition[2]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate2.value)
        uep.find('.//cell_definition[2]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction2.value)
        # ---------  secretion 
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text6.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[1]//secretion_target').text = str(self.float134.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[1]//uptake_rate').text = str(self.float135.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text7.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[2]//secretion_target').text = str(self.float136.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[2]//uptake_rate').text = str(self.float137.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text8.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[3]//secretion_target').text = str(self.float138.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[3]//uptake_rate').text = str(self.float139.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[4]').attrib['name'] = str(self.text9.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[4]//secretion_target').text = str(self.float140.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[4]//uptake_rate').text = str(self.float141.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[5]').attrib['name'] = str(self.text10.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[5]//secretion_target').text = str(self.float142.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[5]//uptake_rate').text = str(self.float143.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[6]').attrib['name'] = str(self.text11.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[6]//secretion_target').text = str(self.float144.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[6]//uptake_rate').text = str(self.float145.value)
        # ---------  molecular
        # ------------------ cell_definition: CD8 Tcell
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float198.value)
        uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[2]').text = str(self.float199.value)
        uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[3]').text = str(self.float200.value)
        uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[4]').text = str(self.float201.value)
        # ---------  death 
        uep.find('.//cell_definition[3]//phenotype//death//model[1]//death_rate').text = str(self.float202.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text = str(self.float203.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text = str(self.float204.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float205.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text = str(self.float206.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//calcification_rate').text = str(self.float207.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//relative_rupture_volume').text = str(self.float208.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[2]//death_rate').text = str(self.float209.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text = str(self.float210.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text = str(self.float211.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float212.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text = str(self.float213.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//calcification_rate').text = str(self.float214.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//relative_rupture_volume').text = str(self.float215.value)
        # ---------  volume 
        uep.find('.//cell_definition[3]//phenotype//volume//total').text = str(self.float216.value)
        uep.find('.//cell_definition[3]//phenotype//volume//fluid_fraction').text = str(self.float217.value)
        uep.find('.//cell_definition[3]//phenotype//volume//nuclear').text = str(self.float218.value)
        uep.find('.//cell_definition[3]//phenotype//volume//fluid_change_rate').text = str(self.float219.value)
        uep.find('.//cell_definition[3]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float220.value)
        uep.find('.//cell_definition[3]//phenotype//volume//nuclear_biomass_change_rate').text = str(self.float221.value)
        uep.find('.//cell_definition[3]//phenotype//volume//calcified_fraction').text = str(self.float222.value)
        uep.find('.//cell_definition[3]//phenotype//volume//calcification_rate').text = str(self.float223.value)
        uep.find('.//cell_definition[3]//phenotype//volume//relative_rupture_volume').text = str(self.float224.value)
        # ---------  mechanics 
        uep.find('.//cell_definition[3]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float225.value)
        uep.find('.//cell_definition[3]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float226.value)
        uep.find('.//cell_definition[3]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float227.value)
        uep.find('.//cell_definition[3]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool10.value)
        uep.find('.//cell_definition[3]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool11.value)
        # ---------  motility 
        uep.find('.//cell_definition[3]//phenotype//motility//speed').text = str(self.float230.value)
        uep.find('.//cell_definition[3]//phenotype//motility//persistence_time').text = str(self.float231.value)
        uep.find('.//cell_definition[3]//phenotype//motility//migration_bias').text = str(self.float232.value)
        uep.find('.//cell_definition[3]//phenotype//motility//options//enabled').text = str(self.bool12.value)
        uep.find('.//cell_definition[3]//phenotype//motility//options//use_2D').text = str(self.bool13.value)
        uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool14.value)
        uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate3.value)
        uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction3.value)
        # ---------  secretion 
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text12.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[1]//secretion_target').text = str(self.float233.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[1]//uptake_rate').text = str(self.float234.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text13.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[2]//secretion_target').text = str(self.float235.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[2]//uptake_rate').text = str(self.float236.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text14.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[3]//secretion_target').text = str(self.float237.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[3]//uptake_rate').text = str(self.float238.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[4]').attrib['name'] = str(self.text15.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[4]//secretion_target').text = str(self.float239.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[4]//uptake_rate').text = str(self.float240.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[5]').attrib['name'] = str(self.text16.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[5]//secretion_target').text = str(self.float241.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[5]//uptake_rate').text = str(self.float242.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[6]').attrib['name'] = str(self.text17.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[6]//secretion_target').text = str(self.float243.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[6]//uptake_rate').text = str(self.float244.value)
        # ---------  molecular
        # ------------------ cell_definition: macrophage
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float297.value)
        uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[2]').text = str(self.float298.value)
        uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[3]').text = str(self.float299.value)
        uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[4]').text = str(self.float300.value)
        # ---------  death 
        uep.find('.//cell_definition[4]//phenotype//death//model[1]//death_rate').text = str(self.float301.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text = str(self.float302.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text = str(self.float303.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float304.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text = str(self.float305.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//calcification_rate').text = str(self.float306.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//relative_rupture_volume').text = str(self.float307.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[2]//death_rate').text = str(self.float308.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text = str(self.float309.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text = str(self.float310.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float311.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text = str(self.float312.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//calcification_rate').text = str(self.float313.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//relative_rupture_volume').text = str(self.float314.value)
        # ---------  volume 
        uep.find('.//cell_definition[4]//phenotype//volume//total').text = str(self.float315.value)
        uep.find('.//cell_definition[4]//phenotype//volume//fluid_fraction').text = str(self.float316.value)
        uep.find('.//cell_definition[4]//phenotype//volume//nuclear').text = str(self.float317.value)
        uep.find('.//cell_definition[4]//phenotype//volume//fluid_change_rate').text = str(self.float318.value)
        uep.find('.//cell_definition[4]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float319.value)
        uep.find('.//cell_definition[4]//phenotype//volume//nuclear_biomass_change_rate').text = str(self.float320.value)
        uep.find('.//cell_definition[4]//phenotype//volume//calcified_fraction').text = str(self.float321.value)
        uep.find('.//cell_definition[4]//phenotype//volume//calcification_rate').text = str(self.float322.value)
        uep.find('.//cell_definition[4]//phenotype//volume//relative_rupture_volume').text = str(self.float323.value)
        # ---------  mechanics 
        uep.find('.//cell_definition[4]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float324.value)
        uep.find('.//cell_definition[4]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float325.value)
        uep.find('.//cell_definition[4]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float326.value)
        uep.find('.//cell_definition[4]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool15.value)
        uep.find('.//cell_definition[4]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool16.value)
        # ---------  motility 
        uep.find('.//cell_definition[4]//phenotype//motility//speed').text = str(self.float329.value)
        uep.find('.//cell_definition[4]//phenotype//motility//persistence_time').text = str(self.float330.value)
        uep.find('.//cell_definition[4]//phenotype//motility//migration_bias').text = str(self.float331.value)
        uep.find('.//cell_definition[4]//phenotype//motility//options//enabled').text = str(self.bool17.value)
        uep.find('.//cell_definition[4]//phenotype//motility//options//use_2D').text = str(self.bool18.value)
        uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool19.value)
        uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate4.value)
        uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction4.value)
        # ---------  secretion 
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text18.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[1]//secretion_target').text = str(self.float332.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[1]//uptake_rate').text = str(self.float333.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text19.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[2]//secretion_target').text = str(self.float334.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[2]//uptake_rate').text = str(self.float335.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text20.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[3]//secretion_target').text = str(self.float336.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[3]//uptake_rate').text = str(self.float337.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[4]').attrib['name'] = str(self.text21.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[4]//secretion_target').text = str(self.float338.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[4]//uptake_rate').text = str(self.float339.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[5]').attrib['name'] = str(self.text22.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[5]//secretion_target').text = str(self.float340.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[5]//uptake_rate').text = str(self.float341.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[6]').attrib['name'] = str(self.text23.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[6]//secretion_target').text = str(self.float342.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[6]//uptake_rate').text = str(self.float343.value)
        # ---------  molecular
        # ------------------ cell_definition: neutrophil
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        uep.find('.//cell_definition[5]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float396.value)
        uep.find('.//cell_definition[5]//phenotype//cycle//phase_transition_rates//rate[2]').text = str(self.float397.value)
        uep.find('.//cell_definition[5]//phenotype//cycle//phase_transition_rates//rate[3]').text = str(self.float398.value)
        uep.find('.//cell_definition[5]//phenotype//cycle//phase_transition_rates//rate[4]').text = str(self.float399.value)
        # ---------  death 
        uep.find('.//cell_definition[5]//phenotype//death//model[1]//death_rate').text = str(self.float400.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text = str(self.float401.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text = str(self.float402.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float403.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text = str(self.float404.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//calcification_rate').text = str(self.float405.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//relative_rupture_volume').text = str(self.float406.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[2]//death_rate').text = str(self.float407.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text = str(self.float408.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text = str(self.float409.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float410.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text = str(self.float411.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//calcification_rate').text = str(self.float412.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//relative_rupture_volume').text = str(self.float413.value)
        # ---------  volume 
        uep.find('.//cell_definition[5]//phenotype//volume//total').text = str(self.float414.value)
        uep.find('.//cell_definition[5]//phenotype//volume//fluid_fraction').text = str(self.float415.value)
        uep.find('.//cell_definition[5]//phenotype//volume//nuclear').text = str(self.float416.value)
        uep.find('.//cell_definition[5]//phenotype//volume//fluid_change_rate').text = str(self.float417.value)
        uep.find('.//cell_definition[5]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float418.value)
        uep.find('.//cell_definition[5]//phenotype//volume//nuclear_biomass_change_rate').text = str(self.float419.value)
        uep.find('.//cell_definition[5]//phenotype//volume//calcified_fraction').text = str(self.float420.value)
        uep.find('.//cell_definition[5]//phenotype//volume//calcification_rate').text = str(self.float421.value)
        uep.find('.//cell_definition[5]//phenotype//volume//relative_rupture_volume').text = str(self.float422.value)
        # ---------  mechanics 
        uep.find('.//cell_definition[5]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float423.value)
        uep.find('.//cell_definition[5]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float424.value)
        uep.find('.//cell_definition[5]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float425.value)
        uep.find('.//cell_definition[5]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool20.value)
        uep.find('.//cell_definition[5]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool21.value)
        # ---------  motility 
        uep.find('.//cell_definition[5]//phenotype//motility//speed').text = str(self.float428.value)
        uep.find('.//cell_definition[5]//phenotype//motility//persistence_time').text = str(self.float429.value)
        uep.find('.//cell_definition[5]//phenotype//motility//migration_bias').text = str(self.float430.value)
        uep.find('.//cell_definition[5]//phenotype//motility//options//enabled').text = str(self.bool22.value)
        uep.find('.//cell_definition[5]//phenotype//motility//options//use_2D').text = str(self.bool23.value)
        uep.find('.//cell_definition[5]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool24.value)
        uep.find('.//cell_definition[5]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate5.value)
        uep.find('.//cell_definition[5]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction5.value)
        # ---------  secretion 
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text24.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[1]//secretion_target').text = str(self.float431.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[1]//uptake_rate').text = str(self.float432.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text25.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[2]//secretion_target').text = str(self.float433.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[2]//uptake_rate').text = str(self.float434.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text26.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[3]//secretion_target').text = str(self.float435.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[3]//uptake_rate').text = str(self.float436.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[4]').attrib['name'] = str(self.text27.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[4]//secretion_target').text = str(self.float437.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[4]//uptake_rate').text = str(self.float438.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[5]').attrib['name'] = str(self.text28.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[5]//secretion_target').text = str(self.float439.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[5]//uptake_rate').text = str(self.float440.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[6]').attrib['name'] = str(self.text29.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[6]//secretion_target').text = str(self.float441.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[6]//uptake_rate').text = str(self.float442.value)
        # ---------  molecular
        # ------------------ cell_definition: DC
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        uep.find('.//cell_definition[6]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float495.value)
        uep.find('.//cell_definition[6]//phenotype//cycle//phase_transition_rates//rate[2]').text = str(self.float496.value)
        uep.find('.//cell_definition[6]//phenotype//cycle//phase_transition_rates//rate[3]').text = str(self.float497.value)
        uep.find('.//cell_definition[6]//phenotype//cycle//phase_transition_rates//rate[4]').text = str(self.float498.value)
        # ---------  death 
        uep.find('.//cell_definition[6]//phenotype//death//model[1]//death_rate').text = str(self.float499.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text = str(self.float500.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text = str(self.float501.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float502.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text = str(self.float503.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//calcification_rate').text = str(self.float504.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//relative_rupture_volume').text = str(self.float505.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[2]//death_rate').text = str(self.float506.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text = str(self.float507.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text = str(self.float508.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float509.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text = str(self.float510.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//calcification_rate').text = str(self.float511.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//relative_rupture_volume').text = str(self.float512.value)
        # ---------  volume 
        uep.find('.//cell_definition[6]//phenotype//volume//total').text = str(self.float513.value)
        uep.find('.//cell_definition[6]//phenotype//volume//fluid_fraction').text = str(self.float514.value)
        uep.find('.//cell_definition[6]//phenotype//volume//nuclear').text = str(self.float515.value)
        uep.find('.//cell_definition[6]//phenotype//volume//fluid_change_rate').text = str(self.float516.value)
        uep.find('.//cell_definition[6]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float517.value)
        uep.find('.//cell_definition[6]//phenotype//volume//nuclear_biomass_change_rate').text = str(self.float518.value)
        uep.find('.//cell_definition[6]//phenotype//volume//calcified_fraction').text = str(self.float519.value)
        uep.find('.//cell_definition[6]//phenotype//volume//calcification_rate').text = str(self.float520.value)
        uep.find('.//cell_definition[6]//phenotype//volume//relative_rupture_volume').text = str(self.float521.value)
        # ---------  mechanics 
        uep.find('.//cell_definition[6]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float522.value)
        uep.find('.//cell_definition[6]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float523.value)
        uep.find('.//cell_definition[6]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float524.value)
        uep.find('.//cell_definition[6]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool25.value)
        uep.find('.//cell_definition[6]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool26.value)
        # ---------  motility 
        uep.find('.//cell_definition[6]//phenotype//motility//speed').text = str(self.float527.value)
        uep.find('.//cell_definition[6]//phenotype//motility//persistence_time').text = str(self.float528.value)
        uep.find('.//cell_definition[6]//phenotype//motility//migration_bias').text = str(self.float529.value)
        uep.find('.//cell_definition[6]//phenotype//motility//options//enabled').text = str(self.bool27.value)
        uep.find('.//cell_definition[6]//phenotype//motility//options//use_2D').text = str(self.bool28.value)
        uep.find('.//cell_definition[6]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool29.value)
        uep.find('.//cell_definition[6]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate6.value)
        uep.find('.//cell_definition[6]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction6.value)
        # ---------  secretion 
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text30.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[1]//secretion_target').text = str(self.float530.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[1]//uptake_rate').text = str(self.float531.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text31.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[2]//secretion_target').text = str(self.float532.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[2]//uptake_rate').text = str(self.float533.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text32.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[3]//secretion_target').text = str(self.float534.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[3]//uptake_rate').text = str(self.float535.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[4]').attrib['name'] = str(self.text33.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[4]//secretion_target').text = str(self.float536.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[4]//uptake_rate').text = str(self.float537.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[5]').attrib['name'] = str(self.text34.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[5]//secretion_target').text = str(self.float538.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[5]//uptake_rate').text = str(self.float539.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[6]').attrib['name'] = str(self.text35.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[6]//secretion_target').text = str(self.float540.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[6]//uptake_rate').text = str(self.float541.value)
        # ---------  molecular
        # ------------------ cell_definition: CD4 Tcell
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        uep.find('.//cell_definition[7]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float594.value)
        uep.find('.//cell_definition[7]//phenotype//cycle//phase_transition_rates//rate[2]').text = str(self.float595.value)
        uep.find('.//cell_definition[7]//phenotype//cycle//phase_transition_rates//rate[3]').text = str(self.float596.value)
        uep.find('.//cell_definition[7]//phenotype//cycle//phase_transition_rates//rate[4]').text = str(self.float597.value)
        # ---------  death 
        uep.find('.//cell_definition[7]//phenotype//death//model[1]//death_rate').text = str(self.float598.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text = str(self.float599.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text = str(self.float600.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float601.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text = str(self.float602.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//calcification_rate').text = str(self.float603.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//relative_rupture_volume').text = str(self.float604.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[2]//death_rate').text = str(self.float605.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text = str(self.float606.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text = str(self.float607.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float608.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text = str(self.float609.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//calcification_rate').text = str(self.float610.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//relative_rupture_volume').text = str(self.float611.value)
        # ---------  volume 
        uep.find('.//cell_definition[7]//phenotype//volume//total').text = str(self.float612.value)
        uep.find('.//cell_definition[7]//phenotype//volume//fluid_fraction').text = str(self.float613.value)
        uep.find('.//cell_definition[7]//phenotype//volume//nuclear').text = str(self.float614.value)
        uep.find('.//cell_definition[7]//phenotype//volume//fluid_change_rate').text = str(self.float615.value)
        uep.find('.//cell_definition[7]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float616.value)
        uep.find('.//cell_definition[7]//phenotype//volume//nuclear_biomass_change_rate').text = str(self.float617.value)
        uep.find('.//cell_definition[7]//phenotype//volume//calcified_fraction').text = str(self.float618.value)
        uep.find('.//cell_definition[7]//phenotype//volume//calcification_rate').text = str(self.float619.value)
        uep.find('.//cell_definition[7]//phenotype//volume//relative_rupture_volume').text = str(self.float620.value)
        # ---------  mechanics 
        uep.find('.//cell_definition[7]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float621.value)
        uep.find('.//cell_definition[7]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float622.value)
        uep.find('.//cell_definition[7]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float623.value)
        uep.find('.//cell_definition[7]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool30.value)
        uep.find('.//cell_definition[7]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool31.value)
        # ---------  motility 
        uep.find('.//cell_definition[7]//phenotype//motility//speed').text = str(self.float626.value)
        uep.find('.//cell_definition[7]//phenotype//motility//persistence_time').text = str(self.float627.value)
        uep.find('.//cell_definition[7]//phenotype//motility//migration_bias').text = str(self.float628.value)
        uep.find('.//cell_definition[7]//phenotype//motility//options//enabled').text = str(self.bool32.value)
        uep.find('.//cell_definition[7]//phenotype//motility//options//use_2D').text = str(self.bool33.value)
        uep.find('.//cell_definition[7]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool34.value)
        uep.find('.//cell_definition[7]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate7.value)
        uep.find('.//cell_definition[7]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction7.value)
        # ---------  secretion 
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text36.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[1]//secretion_target').text = str(self.float629.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[1]//uptake_rate').text = str(self.float630.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text37.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[2]//secretion_target').text = str(self.float631.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[2]//uptake_rate').text = str(self.float632.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text38.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[3]//secretion_target').text = str(self.float633.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[3]//uptake_rate').text = str(self.float634.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[4]').attrib['name'] = str(self.text39.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[4]//secretion_target').text = str(self.float635.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[4]//uptake_rate').text = str(self.float636.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[5]').attrib['name'] = str(self.text40.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[5]//secretion_target').text = str(self.float637.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[5]//uptake_rate').text = str(self.float638.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[6]').attrib['name'] = str(self.text41.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[6]//secretion_target').text = str(self.float639.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[6]//uptake_rate').text = str(self.float640.value)
        # ---------  molecular
        # ------------------ cell_definition: fibroblast
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        uep.find('.//cell_definition[8]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float693.value)
        uep.find('.//cell_definition[8]//phenotype//cycle//phase_transition_rates//rate[2]').text = str(self.float694.value)
        uep.find('.//cell_definition[8]//phenotype//cycle//phase_transition_rates//rate[3]').text = str(self.float695.value)
        uep.find('.//cell_definition[8]//phenotype//cycle//phase_transition_rates//rate[4]').text = str(self.float696.value)
        # ---------  death 
        uep.find('.//cell_definition[8]//phenotype//death//model[1]//death_rate').text = str(self.float697.value)
        uep.find('.//cell_definition[8]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text = str(self.float698.value)
        uep.find('.//cell_definition[8]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text = str(self.float699.value)
        uep.find('.//cell_definition[8]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float700.value)
        uep.find('.//cell_definition[8]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text = str(self.float701.value)
        uep.find('.//cell_definition[8]//phenotype//death//model[1]//parameters//calcification_rate').text = str(self.float702.value)
        uep.find('.//cell_definition[8]//phenotype//death//model[1]//parameters//relative_rupture_volume').text = str(self.float703.value)
        uep.find('.//cell_definition[8]//phenotype//death//model[2]//death_rate').text = str(self.float704.value)
        uep.find('.//cell_definition[8]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text = str(self.float705.value)
        uep.find('.//cell_definition[8]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text = str(self.float706.value)
        uep.find('.//cell_definition[8]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float707.value)
        uep.find('.//cell_definition[8]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text = str(self.float708.value)
        uep.find('.//cell_definition[8]//phenotype//death//model[2]//parameters//calcification_rate').text = str(self.float709.value)
        uep.find('.//cell_definition[8]//phenotype//death//model[2]//parameters//relative_rupture_volume').text = str(self.float710.value)
        # ---------  volume 
        uep.find('.//cell_definition[8]//phenotype//volume//total').text = str(self.float711.value)
        uep.find('.//cell_definition[8]//phenotype//volume//fluid_fraction').text = str(self.float712.value)
        uep.find('.//cell_definition[8]//phenotype//volume//nuclear').text = str(self.float713.value)
        uep.find('.//cell_definition[8]//phenotype//volume//fluid_change_rate').text = str(self.float714.value)
        uep.find('.//cell_definition[8]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float715.value)
        uep.find('.//cell_definition[8]//phenotype//volume//nuclear_biomass_change_rate').text = str(self.float716.value)
        uep.find('.//cell_definition[8]//phenotype//volume//calcified_fraction').text = str(self.float717.value)
        uep.find('.//cell_definition[8]//phenotype//volume//calcification_rate').text = str(self.float718.value)
        uep.find('.//cell_definition[8]//phenotype//volume//relative_rupture_volume').text = str(self.float719.value)
        # ---------  mechanics 
        uep.find('.//cell_definition[8]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float720.value)
        uep.find('.//cell_definition[8]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float721.value)
        uep.find('.//cell_definition[8]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float722.value)
        uep.find('.//cell_definition[8]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool35.value)
        uep.find('.//cell_definition[8]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool36.value)
        # ---------  motility 
        uep.find('.//cell_definition[8]//phenotype//motility//speed').text = str(self.float725.value)
        uep.find('.//cell_definition[8]//phenotype//motility//persistence_time').text = str(self.float726.value)
        uep.find('.//cell_definition[8]//phenotype//motility//migration_bias').text = str(self.float727.value)
        uep.find('.//cell_definition[8]//phenotype//motility//options//enabled').text = str(self.bool37.value)
        uep.find('.//cell_definition[8]//phenotype//motility//options//use_2D').text = str(self.bool38.value)
        uep.find('.//cell_definition[8]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool39.value)
        uep.find('.//cell_definition[8]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate8.value)
        uep.find('.//cell_definition[8]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction8.value)
        # ---------  secretion 
        uep.find('.//cell_definition[8]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text42.value)
        uep.find('.//cell_definition[8]//phenotype//secretion//substrate[1]//secretion_target').text = str(self.float728.value)
        uep.find('.//cell_definition[8]//phenotype//secretion//substrate[1]//uptake_rate').text = str(self.float729.value)
        uep.find('.//cell_definition[8]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text43.value)
        uep.find('.//cell_definition[8]//phenotype//secretion//substrate[2]//secretion_target').text = str(self.float730.value)
        uep.find('.//cell_definition[8]//phenotype//secretion//substrate[2]//uptake_rate').text = str(self.float731.value)
        uep.find('.//cell_definition[8]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text44.value)
        uep.find('.//cell_definition[8]//phenotype//secretion//substrate[3]//secretion_target').text = str(self.float732.value)
        uep.find('.//cell_definition[8]//phenotype//secretion//substrate[3]//uptake_rate').text = str(self.float733.value)
        uep.find('.//cell_definition[8]//phenotype//secretion//substrate[4]').attrib['name'] = str(self.text45.value)
        uep.find('.//cell_definition[8]//phenotype//secretion//substrate[4]//secretion_target').text = str(self.float734.value)
        uep.find('.//cell_definition[8]//phenotype//secretion//substrate[4]//uptake_rate').text = str(self.float735.value)
        uep.find('.//cell_definition[8]//phenotype//secretion//substrate[5]').attrib['name'] = str(self.text46.value)
        uep.find('.//cell_definition[8]//phenotype//secretion//substrate[5]//secretion_target').text = str(self.float736.value)
        uep.find('.//cell_definition[8]//phenotype//secretion//substrate[5]//uptake_rate').text = str(self.float737.value)
        uep.find('.//cell_definition[8]//phenotype//secretion//substrate[6]').attrib['name'] = str(self.text47.value)
        uep.find('.//cell_definition[8]//phenotype//secretion//substrate[6]//secretion_target').text = str(self.float738.value)
        uep.find('.//cell_definition[8]//phenotype//secretion//substrate[6]//uptake_rate').text = str(self.float739.value)
        # ---------  molecular
