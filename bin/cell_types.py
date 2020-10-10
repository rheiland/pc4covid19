 
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
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text1 = Text(value='pro-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text1]
        box39 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float36 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float36, units_btn]
        box40 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float37 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float37, units_btn]
        box41 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text2 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text2]
        box42 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float38 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float38, units_btn]
        box43 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float39 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float39, units_btn]
        box44 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text3 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text3]
        box45 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float40 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float40, units_btn]
        box46 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float41 = FloatText(value='0.1', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float41, units_btn]
        box47 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row7 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row7.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        div_row8 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row8.style.button_color = 'cyan'
        name_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float42 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float42, units_btn, description_btn] 

        box48 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float43 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='uncoated endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float43, units_btn, description_btn] 

        box49 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_RNA', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float44 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='RNA', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='total (functional) viral RNA copies', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float44, units_btn, description_btn] 

        box50 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_protein', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float45 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='protein', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total assembled sets of viral protein', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float45, units_btn, description_btn] 

        box51 = Box(children=row, layout=box_layout)
        name_btn = Button(description='assembled_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float46 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='total assembled virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float46, units_btn, description_btn] 

        box52 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_uncoating_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float47 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which an internalized virion is uncoated', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float47, units_btn, description_btn] 

        box53 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_to_RNA_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float48 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which uncoated virion makes its mRNA available', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float48, units_btn, description_btn] 

        box54 = Box(children=row, layout=box_layout)
        name_btn = Button(description='protein_synthesis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float49 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at mRNA creates complete set of proteins', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float49, units_btn, description_btn] 

        box55 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_assembly_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float50 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which viral proteins are assembled into complete virion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float50, units_btn, description_btn] 

        box56 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_export_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float51 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which a virion is exported from a live cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float51, units_btn, description_btn] 

        box57 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float52 = FloatText(value='1000', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of unbound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float52, units_btn, description_btn] 

        box58 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float53 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of bound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float53, units_btn, description_btn] 

        box59 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float54 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of internalized unbound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float54, units_btn, description_btn] 

        box60 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float55 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of internalized bound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float55, units_btn, description_btn] 

        box61 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float56 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor-virus binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float56, units_btn, description_btn] 

        box62 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_endocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float57 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus endocytosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float57, units_btn, description_btn] 

        box63 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_cargo_release_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float58 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor-virus cargo release rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float58, units_btn, description_btn] 

        box64 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_recycling_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float59 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor recycling rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float59, units_btn, description_btn] 

        box65 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_infected_apoptosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float60 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='maximum rate of cell apoptosis due to viral infection', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float60, units_btn, description_btn] 

        box66 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_apoptosis_half_max', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float61 = FloatText(value='250', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='viral load at which cells reach half max apoptosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float61, units_btn, description_btn] 

        box67 = Box(children=row, layout=box_layout)
        name_btn = Button(description='apoptosis_hill_power', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float62 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Hill power for viral load apoptosis response', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float62, units_btn, description_btn] 

        box68 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virus_fraction_released_at_death', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float63 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='fraction of internal virus released at cell death', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float63, units_btn, description_btn] 

        box69 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float64 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='max rate that infected cells secrete chemokine', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float64, units_btn, description_btn] 

        box70 = Box(children=row, layout=box_layout)
        name_btn = Button(description='debris_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float65 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate that dead cells release debris', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float65, units_btn, description_btn] 

        box71 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_activated', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float66 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='used internally to track activation of chemokine secretion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float66, units_btn, description_btn] 

        box72 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_secretion_rate_via_infection', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float67 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Type-1 interferon secretion rate for infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float67, units_btn, description_btn] 

        box73 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_interferon_secretion_rate_via_paracrine', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float68 = FloatText(value='0.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Type-1 interferon secretion rate after activation by Type-1 interferon', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float68, units_btn, description_btn] 

        box74 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_response_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float69 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Interferon response scales linearly until Int-1 exceeds this threshold', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float69, units_btn, description_btn] 

        box75 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_activation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float70 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Current interferon signaling activation state (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float70, units_btn, description_btn] 

        box76 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_virus_inhibition', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float71 = FloatText(value='0.9', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='At max interferon activation, max inhibition of viral replication (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float71, units_btn, description_btn] 

        box77 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_viral_RNA_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float72 = FloatText(value='2', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='infected cell interferon secretion saturates at this viral RNA level', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float72, units_btn, description_btn] 

        box78 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float73 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='tracks total contact time with CD8 T cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float73, units_btn, description_btn] 

        box79 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float74 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='the rate at which the cell attaches to cells in contact', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float74, units_btn, description_btn] 

        box80 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_lifetime', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float75 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the mean duration of a cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float75, units_btn, description_btn] 

        box81 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_death_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float76 = FloatText(value='50', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='threshold CD8 T cell contact time to trigger apoptosis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float76, units_btn, description_btn] 

        box82 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_attachment_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float77 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float77, units_btn, description_btn] 

        box83 = Box(children=row, layout=box_layout)
        name_btn = Button(description='elastic_attachment_coefficient', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float78 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='elastic coefficient for cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float78, units_btn, description_btn] 

        box84 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_to_next_phagocytosis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float79 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='time it takes for the apoptotic material to be phagocytosed', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float79, units_btn, description_btn] 

        box85 = Box(children=row, layout=box_layout)
        name_btn = Button(description='material_internalisation_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float80 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float80, units_btn, description_btn] 

        box86 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_macrophage_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float81 = FloatText(value='6500', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float81, units_btn, description_btn] 

        box87 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_neutrophil_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float82 = FloatText(value='1581', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float82, units_btn, description_btn] 

        box88 = Box(children=row, layout=box_layout)
        name_btn = Button(description='exhausted_macrophage_death_rat', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float83 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float83, units_btn, description_btn] 

        box89 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ability_to_phagocytose_infected_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float84 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Boolean for whether macrophages can phagocytose infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float84, units_btn, description_btn] 

        box90 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_of_DC_departure', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float85 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Time DC leaves tissue after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float85, units_btn, description_btn] 

        box91 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float86 = FloatText(value='0.167', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float86, units_btn, description_btn] 

        box92 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float87 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float87, units_btn, description_btn] 

        box93 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_chemokine_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float88 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to chemokine in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float88, units_btn, description_btn] 

        box94 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float89 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float89, units_btn, description_btn] 

        box95 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float90 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float90, units_btn, description_btn] 

        box96 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_immune_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float91 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='used internally to track activation state', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float91, units_btn, description_btn] 

        box97 = Box(children=row, layout=box_layout)

        self.cell_def_vbox0 = VBox([
          div_row1, box0, box1, box2, box3, div_row2, death_model1,box4, box5, box6, box7, box8, box9, box10, death_model2,box11, box12, box13, box14, box15, box16, box17, div_row3, box18, box19, box20, box21, box22, box23, box24, box25, box26, div_row4, box27, box28, box29, box30, box31, div_row5, box32,box33,box34,self.bool2,self.bool3,chemotaxis_btn,self.bool4,box35,box36,div_row6, box37,box38,box39,box40,box41,box42,box43,box44,box45,box46,box47,div_row7, div_row8,          box48,
          box49,
          box50,
          box51,
          box52,
          box53,
          box54,
          box55,
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
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox0)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = lung epithelium
        #  ------------------------- 
        div_row9 = Button(description='phenotype:cycle (model: flow_cytometry_separated_cycle_model; code=6)', disabled=True, layout=divider_button_layout)
        div_row9.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 1 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float92 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float92, units_btn, ]
        box98 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 1 -> Phase 2 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float93 = FloatText(value='0.00208333', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float93, units_btn, ]
        box99 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 2 -> Phase 3 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float94 = FloatText(value='0.00416667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float94, units_btn, ]
        box100 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 3 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float95 = FloatText(value='0.0166667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float95, units_btn, ]
        box101 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row10 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row10.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float96 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float96, units_btn, ]
        box102 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float97 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float97, units_btn, ]
        box103 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float98 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float98, units_btn, ]
        box104 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float99 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float99, units_btn, ]
        box105 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float100 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float100, units_btn, ]
        box106 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float101 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float101, units_btn, ]
        box107 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float102 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float102, units_btn, ]
        box108 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float103 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float103, units_btn, ]
        box109 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float104 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float104, units_btn, ]
        box110 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float105 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float105, units_btn, ]
        box111 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float106 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float106, units_btn, ]
        box112 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float107 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float107, units_btn, ]
        box113 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float108 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float108, units_btn, ]
        box114 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float109 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float109, units_btn, ]
        box115 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row11 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row11.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float110 = FloatText(value='2494', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float110, units_btn, ]
        box116 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float111 = FloatText(value='0.75', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float111, units_btn, ]
        box117 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float112 = FloatText(value='540', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float112, units_btn, ]
        box118 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float113 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float113, units_btn, ]
        box119 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float114 = FloatText(value='0.0045', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float114, units_btn, ]
        box120 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float115 = FloatText(value='0.0055', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float115, units_btn, ]
        box121 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcified_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float116 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float116, units_btn, ]
        box122 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float117 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float117, units_btn, ]
        box123 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float118 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float118, units_btn, ]
        box124 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row12 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row12.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float119 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float119, units_btn, ]
        box125 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float120 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float120, units_btn, ]
        box126 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float121 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float121, units_btn, ]
        box127 = Box(children=row, layout=box_layout)

        self.bool5 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float122 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool5, name_btn, self.float122, units_btn, ]
        box128 = Box(children=row, layout=box_layout)

        self.bool6 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float123 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool6, name_btn, self.float123, units_btn, ]
        box129 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row13 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row13.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float124 = FloatText(value='4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float124, units_btn]
        box130 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float125 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float125, units_btn]
        box131 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float126 = FloatText(value='0.7', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float126, units_btn]
        box132 = Box(children=row, layout=box_layout)
        self.bool7 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        self.bool8 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool9 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate2 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate2]
        box133 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction2 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction2]
        box134 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row14 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row14.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text4 = Text(value='interferon 1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text4]
        box135 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float127 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float127, units_btn]
        box136 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text5 = Text(value='pro-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text5]
        box137 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float128 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float128, units_btn]
        box138 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float129 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float129, units_btn]
        box139 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text6 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text6]
        box140 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float130 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float130, units_btn]
        box141 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float131 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float131, units_btn]
        box142 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text7 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text7]
        box143 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float132 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float132, units_btn]
        box144 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float133 = FloatText(value='0.1', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float133, units_btn]
        box145 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row15 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row15.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        div_row16 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row16.style.button_color = 'cyan'
        name_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float134 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float134, units_btn, description_btn] 

        box146 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float135 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='uncoated endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float135, units_btn, description_btn] 

        box147 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_RNA', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float136 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='RNA', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='total (functional) viral RNA copies', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float136, units_btn, description_btn] 

        box148 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_protein', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float137 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='protein', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total assembled sets of viral protein', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float137, units_btn, description_btn] 

        box149 = Box(children=row, layout=box_layout)
        name_btn = Button(description='assembled_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float138 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='total assembled virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float138, units_btn, description_btn] 

        box150 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_uncoating_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float139 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which an internalized virion is uncoated', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float139, units_btn, description_btn] 

        box151 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_to_RNA_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float140 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which uncoated virion makes its mRNA available', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float140, units_btn, description_btn] 

        box152 = Box(children=row, layout=box_layout)
        name_btn = Button(description='protein_synthesis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float141 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at mRNA creates complete set of proteins', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float141, units_btn, description_btn] 

        box153 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_assembly_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float142 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which viral proteins are assembled into complete virion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float142, units_btn, description_btn] 

        box154 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_export_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float143 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which a virion is exported from a live cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float143, units_btn, description_btn] 

        box155 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float144 = FloatText(value='1000', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of unbound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float144, units_btn, description_btn] 

        box156 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float145 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of bound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float145, units_btn, description_btn] 

        box157 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float146 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of internalized unbound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float146, units_btn, description_btn] 

        box158 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float147 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of internalized bound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float147, units_btn, description_btn] 

        box159 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float148 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor-virus binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float148, units_btn, description_btn] 

        box160 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_endocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float149 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus endocytosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float149, units_btn, description_btn] 

        box161 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_cargo_release_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float150 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor-virus cargo release rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float150, units_btn, description_btn] 

        box162 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_recycling_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float151 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor recycling rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float151, units_btn, description_btn] 

        box163 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_infected_apoptosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float152 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='maximum rate of cell apoptosis due to viral infection', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float152, units_btn, description_btn] 

        box164 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_apoptosis_half_max', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float153 = FloatText(value='250', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='viral load at which cells reach half max apoptosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float153, units_btn, description_btn] 

        box165 = Box(children=row, layout=box_layout)
        name_btn = Button(description='apoptosis_hill_power', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float154 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Hill power for viral load apoptosis response', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float154, units_btn, description_btn] 

        box166 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virus_fraction_released_at_death', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float155 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='fraction of internal virus released at cell death', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float155, units_btn, description_btn] 

        box167 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float156 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='max rate that infected cells secrete chemokine', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float156, units_btn, description_btn] 

        box168 = Box(children=row, layout=box_layout)
        name_btn = Button(description='debris_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float157 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate that dead cells release debris', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float157, units_btn, description_btn] 

        box169 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_activated', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float158 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='used internally to track activation of chemokine secretion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float158, units_btn, description_btn] 

        box170 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_secretion_rate_via_infection', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float159 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Type-1 interferon secretion rate for infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float159, units_btn, description_btn] 

        box171 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_interferon_secretion_rate_via_paracrine', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float160 = FloatText(value='0.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Type-1 interferon secretion rate after activation by Type-1 interferon', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float160, units_btn, description_btn] 

        box172 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_response_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float161 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Interferon response scales linearly until Int-1 exceeds this threshold', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float161, units_btn, description_btn] 

        box173 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_activation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float162 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Current interferon signaling activation state (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float162, units_btn, description_btn] 

        box174 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_virus_inhibition', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float163 = FloatText(value='0.9', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='At max interferon activation, max inhibition of viral replication (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float163, units_btn, description_btn] 

        box175 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_viral_RNA_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float164 = FloatText(value='2', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='infected cell interferon secretion saturates at this viral RNA level', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float164, units_btn, description_btn] 

        box176 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float165 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='tracks total contact time with CD8 T cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float165, units_btn, description_btn] 

        box177 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float166 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='the rate at which the cell attaches to cells in contact', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float166, units_btn, description_btn] 

        box178 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_lifetime', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float167 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the mean duration of a cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float167, units_btn, description_btn] 

        box179 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_death_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float168 = FloatText(value='50', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='threshold CD8 T cell contact time to trigger apoptosis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float168, units_btn, description_btn] 

        box180 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_attachment_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float169 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float169, units_btn, description_btn] 

        box181 = Box(children=row, layout=box_layout)
        name_btn = Button(description='elastic_attachment_coefficient', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float170 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='elastic coefficient for cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float170, units_btn, description_btn] 

        box182 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_to_next_phagocytosis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float171 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='time it takes for the apoptotic material to be phagocytosed', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float171, units_btn, description_btn] 

        box183 = Box(children=row, layout=box_layout)
        name_btn = Button(description='material_internalisation_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float172 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float172, units_btn, description_btn] 

        box184 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_macrophage_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float173 = FloatText(value='6500', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float173, units_btn, description_btn] 

        box185 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_neutrophil_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float174 = FloatText(value='1581', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float174, units_btn, description_btn] 

        box186 = Box(children=row, layout=box_layout)
        name_btn = Button(description='exhausted_macrophage_death_rat', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float175 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float175, units_btn, description_btn] 

        box187 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ability_to_phagocytose_infected_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float176 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Boolean for whether macrophages can phagocytose infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float176, units_btn, description_btn] 

        box188 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_of_DC_departure', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float177 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Time DC leaves tissue after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float177, units_btn, description_btn] 

        box189 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float178 = FloatText(value='0.167', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float178, units_btn, description_btn] 

        box190 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float179 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float179, units_btn, description_btn] 

        box191 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_chemokine_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float180 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to chemokine in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float180, units_btn, description_btn] 

        box192 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float181 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float181, units_btn, description_btn] 

        box193 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float182 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float182, units_btn, description_btn] 

        box194 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_immune_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float183 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='used internally to track activation state', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float183, units_btn, description_btn] 

        box195 = Box(children=row, layout=box_layout)

        self.cell_def_vbox1 = VBox([
          div_row9, box98, box99, box100, box101, div_row10, death_model1,box102, box103, box104, box105, box106, box107, box108, death_model2,box109, box110, box111, box112, box113, box114, box115, div_row11, box116, box117, box118, box119, box120, box121, box122, box123, box124, div_row12, box125, box126, box127, box128, box129, div_row13, box130,box131,box132,self.bool7,self.bool8,chemotaxis_btn,self.bool9,box133,box134,div_row14, box135,box136,box137,box138,box139,box140,box141,box142,box143,box144,box145,div_row15, div_row16,          box146,
          box147,
          box148,
          box149,
          box150,
          box151,
          box152,
          box153,
          box154,
          box155,
          box156,
          box157,
          box158,
          box159,
          box160,
          box161,
          box162,
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
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox1)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = CD8 Tcell
        #  ------------------------- 
        div_row17 = Button(description='phenotype:cycle (model: flow_cytometry_separated_cycle_model; code=6)', disabled=True, layout=divider_button_layout)
        div_row17.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 1 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float184 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float184, units_btn, ]
        box196 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 1 -> Phase 2 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float185 = FloatText(value='0.00208333', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float185, units_btn, ]
        box197 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 2 -> Phase 3 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float186 = FloatText(value='0.00416667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float186, units_btn, ]
        box198 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 3 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float187 = FloatText(value='0.0166667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float187, units_btn, ]
        box199 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row18 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row18.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float188 = FloatText(value='2.8e-4', step='1e-05', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float188, units_btn, ]
        box200 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float189 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float189, units_btn, ]
        box201 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float190 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float190, units_btn, ]
        box202 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float191 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float191, units_btn, ]
        box203 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float192 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float192, units_btn, ]
        box204 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float193 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float193, units_btn, ]
        box205 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float194 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float194, units_btn, ]
        box206 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float195 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float195, units_btn, ]
        box207 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float196 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float196, units_btn, ]
        box208 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float197 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float197, units_btn, ]
        box209 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float198 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float198, units_btn, ]
        box210 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float199 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float199, units_btn, ]
        box211 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float200 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float200, units_btn, ]
        box212 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float201 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float201, units_btn, ]
        box213 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row19 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row19.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float202 = FloatText(value='478', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float202, units_btn, ]
        box214 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float203 = FloatText(value='0.75', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float203, units_btn, ]
        box215 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float204 = FloatText(value='47.8', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float204, units_btn, ]
        box216 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float205 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float205, units_btn, ]
        box217 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float206 = FloatText(value='0.0045', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float206, units_btn, ]
        box218 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float207 = FloatText(value='0.0055', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float207, units_btn, ]
        box219 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcified_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float208 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float208, units_btn, ]
        box220 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float209 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float209, units_btn, ]
        box221 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float210 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float210, units_btn, ]
        box222 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row20 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row20.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float211 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float211, units_btn, ]
        box223 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float212 = FloatText(value='10', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float212, units_btn, ]
        box224 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float213 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float213, units_btn, ]
        box225 = Box(children=row, layout=box_layout)

        self.bool10 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float214 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool10, name_btn, self.float214, units_btn, ]
        box226 = Box(children=row, layout=box_layout)

        self.bool11 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float215 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool11, name_btn, self.float215, units_btn, ]
        box227 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row21 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row21.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float216 = FloatText(value='4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float216, units_btn]
        box228 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float217 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float217, units_btn]
        box229 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float218 = FloatText(value='0.70', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float218, units_btn]
        box230 = Box(children=row, layout=box_layout)
        self.bool12 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        self.bool13 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool14 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate3 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate3]
        box231 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction3 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction3]
        box232 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row22 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row22.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text8 = Text(value='interferon 1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text8]
        box233 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float219 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float219, units_btn]
        box234 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text9 = Text(value='pro-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text9]
        box235 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float220 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float220, units_btn]
        box236 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float221 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float221, units_btn]
        box237 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text10 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text10]
        box238 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float222 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float222, units_btn]
        box239 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float223 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float223, units_btn]
        box240 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text11 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text11]
        box241 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float224 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float224, units_btn]
        box242 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float225 = FloatText(value='0.1', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float225, units_btn]
        box243 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row23 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row23.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        div_row24 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row24.style.button_color = 'cyan'
        name_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float226 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float226, units_btn, description_btn] 

        box244 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float227 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='uncoated endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float227, units_btn, description_btn] 

        box245 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_RNA', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float228 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='RNA', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='total (functional) viral RNA copies', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float228, units_btn, description_btn] 

        box246 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_protein', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float229 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='protein', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total assembled sets of viral protein', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float229, units_btn, description_btn] 

        box247 = Box(children=row, layout=box_layout)
        name_btn = Button(description='assembled_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float230 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='total assembled virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float230, units_btn, description_btn] 

        box248 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_uncoating_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float231 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which an internalized virion is uncoated', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float231, units_btn, description_btn] 

        box249 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_to_RNA_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float232 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which uncoated virion makes its mRNA available', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float232, units_btn, description_btn] 

        box250 = Box(children=row, layout=box_layout)
        name_btn = Button(description='protein_synthesis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float233 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at mRNA creates complete set of proteins', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float233, units_btn, description_btn] 

        box251 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_assembly_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float234 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which viral proteins are assembled into complete virion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float234, units_btn, description_btn] 

        box252 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_export_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float235 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which a virion is exported from a live cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float235, units_btn, description_btn] 

        box253 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float236 = FloatText(value='1000', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of unbound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float236, units_btn, description_btn] 

        box254 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float237 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of bound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float237, units_btn, description_btn] 

        box255 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float238 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of internalized unbound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float238, units_btn, description_btn] 

        box256 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float239 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of internalized bound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float239, units_btn, description_btn] 

        box257 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float240 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor-virus binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float240, units_btn, description_btn] 

        box258 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_endocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float241 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus endocytosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float241, units_btn, description_btn] 

        box259 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_cargo_release_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float242 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor-virus cargo release rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float242, units_btn, description_btn] 

        box260 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_recycling_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float243 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor recycling rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float243, units_btn, description_btn] 

        box261 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_infected_apoptosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float244 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='maximum rate of cell apoptosis due to viral infection', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float244, units_btn, description_btn] 

        box262 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_apoptosis_half_max', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float245 = FloatText(value='250', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='viral load at which cells reach half max apoptosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float245, units_btn, description_btn] 

        box263 = Box(children=row, layout=box_layout)
        name_btn = Button(description='apoptosis_hill_power', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float246 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Hill power for viral load apoptosis response', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float246, units_btn, description_btn] 

        box264 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virus_fraction_released_at_death', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float247 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='fraction of internal virus released at cell death', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float247, units_btn, description_btn] 

        box265 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float248 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='max rate that infected cells secrete chemokine', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float248, units_btn, description_btn] 

        box266 = Box(children=row, layout=box_layout)
        name_btn = Button(description='debris_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float249 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate that dead cells release debris', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float249, units_btn, description_btn] 

        box267 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_activated', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float250 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='used internally to track activation of chemokine secretion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float250, units_btn, description_btn] 

        box268 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_secretion_rate_via_infection', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float251 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Type-1 interferon secretion rate for infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float251, units_btn, description_btn] 

        box269 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_interferon_secretion_rate_via_paracrine', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float252 = FloatText(value='0.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Type-1 interferon secretion rate after activation by Type-1 interferon', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float252, units_btn, description_btn] 

        box270 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_response_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float253 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Interferon response scales linearly until Int-1 exceeds this threshold', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float253, units_btn, description_btn] 

        box271 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_activation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float254 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Current interferon signaling activation state (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float254, units_btn, description_btn] 

        box272 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_virus_inhibition', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float255 = FloatText(value='0.9', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='At max interferon activation, max inhibition of viral replication (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float255, units_btn, description_btn] 

        box273 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_viral_RNA_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float256 = FloatText(value='2', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='infected cell interferon secretion saturates at this viral RNA level', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float256, units_btn, description_btn] 

        box274 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float257 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='tracks total contact time with CD8 T cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float257, units_btn, description_btn] 

        box275 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float258 = FloatText(value='0.2', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='the rate at which the cell attaches to cells in contact', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float258, units_btn, description_btn] 

        box276 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_lifetime', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float259 = FloatText(value='8.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the mean duration of a cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float259, units_btn, description_btn] 

        box277 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_death_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float260 = FloatText(value='50', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='threshold CD8 T cell contact time to trigger apoptosis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float260, units_btn, description_btn] 

        box278 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_attachment_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float261 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float261, units_btn, description_btn] 

        box279 = Box(children=row, layout=box_layout)
        name_btn = Button(description='elastic_attachment_coefficient', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float262 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='elastic coefficient for cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float262, units_btn, description_btn] 

        box280 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_to_next_phagocytosis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float263 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='time it takes for the apoptotic material to be phagocytosed', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float263, units_btn, description_btn] 

        box281 = Box(children=row, layout=box_layout)
        name_btn = Button(description='material_internalisation_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float264 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float264, units_btn, description_btn] 

        box282 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_macrophage_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float265 = FloatText(value='6500', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float265, units_btn, description_btn] 

        box283 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_neutrophil_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float266 = FloatText(value='1581', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float266, units_btn, description_btn] 

        box284 = Box(children=row, layout=box_layout)
        name_btn = Button(description='exhausted_macrophage_death_rat', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float267 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float267, units_btn, description_btn] 

        box285 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ability_to_phagocytose_infected_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float268 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Boolean for whether macrophages can phagocytose infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float268, units_btn, description_btn] 

        box286 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_of_DC_departure', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float269 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Time DC leaves tissue after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float269, units_btn, description_btn] 

        box287 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float270 = FloatText(value='0.167', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float270, units_btn, description_btn] 

        box288 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float271 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float271, units_btn, description_btn] 

        box289 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_chemokine_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float272 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to chemokine in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float272, units_btn, description_btn] 

        box290 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float273 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float273, units_btn, description_btn] 

        box291 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float274 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float274, units_btn, description_btn] 

        box292 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_immune_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float275 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='used internally to track activation state', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float275, units_btn, description_btn] 

        box293 = Box(children=row, layout=box_layout)

        self.cell_def_vbox2 = VBox([
          div_row17, box196, box197, box198, box199, div_row18, death_model1,box200, box201, box202, box203, box204, box205, box206, death_model2,box207, box208, box209, box210, box211, box212, box213, div_row19, box214, box215, box216, box217, box218, box219, box220, box221, box222, div_row20, box223, box224, box225, box226, box227, div_row21, box228,box229,box230,self.bool12,self.bool13,chemotaxis_btn,self.bool14,box231,box232,div_row22, box233,box234,box235,box236,box237,box238,box239,box240,box241,box242,box243,div_row23, div_row24,          box244,
          box245,
          box246,
          box247,
          box248,
          box249,
          box250,
          box251,
          box252,
          box253,
          box254,
          box255,
          box256,
          box257,
          box258,
          box259,
          box260,
          box261,
          box262,
          box263,
          box264,
          box265,
          box266,
          box267,
          box268,
          box269,
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
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox2)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = macrophage
        #  ------------------------- 
        div_row25 = Button(description='phenotype:cycle (model: flow_cytometry_separated_cycle_model; code=6)', disabled=True, layout=divider_button_layout)
        div_row25.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 1 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float276 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float276, units_btn, ]
        box294 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 1 -> Phase 2 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float277 = FloatText(value='0.00208333', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float277, units_btn, ]
        box295 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 2 -> Phase 3 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float278 = FloatText(value='0.00416667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float278, units_btn, ]
        box296 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 3 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float279 = FloatText(value='0.0166667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float279, units_btn, ]
        box297 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row26 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row26.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float280 = FloatText(value='2.1e-4', step='1e-05', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float280, units_btn, ]
        box298 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float281 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float281, units_btn, ]
        box299 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float282 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float282, units_btn, ]
        box300 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float283 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float283, units_btn, ]
        box301 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float284 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float284, units_btn, ]
        box302 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float285 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float285, units_btn, ]
        box303 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float286 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float286, units_btn, ]
        box304 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float287 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float287, units_btn, ]
        box305 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float288 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float288, units_btn, ]
        box306 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float289 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float289, units_btn, ]
        box307 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float290 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float290, units_btn, ]
        box308 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float291 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float291, units_btn, ]
        box309 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float292 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float292, units_btn, ]
        box310 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float293 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float293, units_btn, ]
        box311 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row27 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row27.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float294 = FloatText(value='4849', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float294, units_btn, ]
        box312 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float295 = FloatText(value='0.75', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float295, units_btn, ]
        box313 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float296 = FloatText(value='485', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float296, units_btn, ]
        box314 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float297 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float297, units_btn, ]
        box315 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float298 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float298, units_btn, ]
        box316 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float299 = FloatText(value='0.0055', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float299, units_btn, ]
        box317 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcified_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float300 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float300, units_btn, ]
        box318 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float301 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float301, units_btn, ]
        box319 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float302 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float302, units_btn, ]
        box320 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row28 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row28.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float303 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float303, units_btn, ]
        box321 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float304 = FloatText(value='10', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float304, units_btn, ]
        box322 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float305 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float305, units_btn, ]
        box323 = Box(children=row, layout=box_layout)

        self.bool15 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float306 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool15, name_btn, self.float306, units_btn, ]
        box324 = Box(children=row, layout=box_layout)

        self.bool16 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float307 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool16, name_btn, self.float307, units_btn, ]
        box325 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row29 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row29.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float308 = FloatText(value='4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float308, units_btn]
        box326 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float309 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float309, units_btn]
        box327 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float310 = FloatText(value='0.7', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float310, units_btn]
        box328 = Box(children=row, layout=box_layout)
        self.bool17 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        self.bool18 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool19 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate4 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate4]
        box329 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction4 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction4]
        box330 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row30 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row30.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text12 = Text(value='interferon 1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text12]
        box331 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float311 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float311, units_btn]
        box332 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text13 = Text(value='pro-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text13]
        box333 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float312 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float312, units_btn]
        box334 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float313 = FloatText(value='0.1', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float313, units_btn]
        box335 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text14 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text14]
        box336 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float314 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float314, units_btn]
        box337 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float315 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float315, units_btn]
        box338 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text15 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text15]
        box339 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float316 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float316, units_btn]
        box340 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float317 = FloatText(value='0.1', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float317, units_btn]
        box341 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row31 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row31.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        div_row32 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row32.style.button_color = 'cyan'
        name_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float318 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float318, units_btn, description_btn] 

        box342 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float319 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='uncoated endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float319, units_btn, description_btn] 

        box343 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_RNA', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float320 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='RNA', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='total (functional) viral RNA copies', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float320, units_btn, description_btn] 

        box344 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_protein', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float321 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='protein', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total assembled sets of viral protein', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float321, units_btn, description_btn] 

        box345 = Box(children=row, layout=box_layout)
        name_btn = Button(description='assembled_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float322 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='total assembled virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float322, units_btn, description_btn] 

        box346 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_uncoating_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float323 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which an internalized virion is uncoated', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float323, units_btn, description_btn] 

        box347 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_to_RNA_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float324 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which uncoated virion makes its mRNA available', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float324, units_btn, description_btn] 

        box348 = Box(children=row, layout=box_layout)
        name_btn = Button(description='protein_synthesis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float325 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at mRNA creates complete set of proteins', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float325, units_btn, description_btn] 

        box349 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_assembly_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float326 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which viral proteins are assembled into complete virion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float326, units_btn, description_btn] 

        box350 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_export_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float327 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which a virion is exported from a live cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float327, units_btn, description_btn] 

        box351 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float328 = FloatText(value='1000', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of unbound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float328, units_btn, description_btn] 

        box352 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float329 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of bound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float329, units_btn, description_btn] 

        box353 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float330 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of internalized unbound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float330, units_btn, description_btn] 

        box354 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float331 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of internalized bound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float331, units_btn, description_btn] 

        box355 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float332 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor-virus binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float332, units_btn, description_btn] 

        box356 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_endocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float333 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus endocytosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float333, units_btn, description_btn] 

        box357 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_cargo_release_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float334 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor-virus cargo release rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float334, units_btn, description_btn] 

        box358 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_recycling_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float335 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor recycling rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float335, units_btn, description_btn] 

        box359 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_infected_apoptosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float336 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='maximum rate of cell apoptosis due to viral infection', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float336, units_btn, description_btn] 

        box360 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_apoptosis_half_max', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float337 = FloatText(value='250', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='viral load at which cells reach half max apoptosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float337, units_btn, description_btn] 

        box361 = Box(children=row, layout=box_layout)
        name_btn = Button(description='apoptosis_hill_power', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float338 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Hill power for viral load apoptosis response', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float338, units_btn, description_btn] 

        box362 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virus_fraction_released_at_death', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float339 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='fraction of internal virus released at cell death', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float339, units_btn, description_btn] 

        box363 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float340 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='max rate that infected cells secrete chemokine', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float340, units_btn, description_btn] 

        box364 = Box(children=row, layout=box_layout)
        name_btn = Button(description='debris_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float341 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate that dead cells release debris', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float341, units_btn, description_btn] 

        box365 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_activated', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float342 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='used internally to track activation of chemokine secretion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float342, units_btn, description_btn] 

        box366 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_secretion_rate_via_infection', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float343 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Type-1 interferon secretion rate for infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float343, units_btn, description_btn] 

        box367 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_interferon_secretion_rate_via_paracrine', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float344 = FloatText(value='0.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Type-1 interferon secretion rate after activation by Type-1 interferon', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float344, units_btn, description_btn] 

        box368 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_response_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float345 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Interferon response scales linearly until Int-1 exceeds this threshold', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float345, units_btn, description_btn] 

        box369 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_activation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float346 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Current interferon signaling activation state (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float346, units_btn, description_btn] 

        box370 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_virus_inhibition', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float347 = FloatText(value='0.9', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='At max interferon activation, max inhibition of viral replication (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float347, units_btn, description_btn] 

        box371 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_viral_RNA_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float348 = FloatText(value='2', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='infected cell interferon secretion saturates at this viral RNA level', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float348, units_btn, description_btn] 

        box372 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float349 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='tracks total contact time with CD8 T cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float349, units_btn, description_btn] 

        box373 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float350 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='the rate at which the cell attaches to cells in contact', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float350, units_btn, description_btn] 

        box374 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_lifetime', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float351 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the mean duration of a cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float351, units_btn, description_btn] 

        box375 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_death_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float352 = FloatText(value='50', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='threshold CD8 T cell contact time to trigger apoptosis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float352, units_btn, description_btn] 

        box376 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_attachment_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float353 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float353, units_btn, description_btn] 

        box377 = Box(children=row, layout=box_layout)
        name_btn = Button(description='elastic_attachment_coefficient', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float354 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='elastic coefficient for cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float354, units_btn, description_btn] 

        box378 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_to_next_phagocytosis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float355 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='time it takes for the apoptotic material to be phagocytosed', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float355, units_btn, description_btn] 

        box379 = Box(children=row, layout=box_layout)
        name_btn = Button(description='material_internalisation_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float356 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float356, units_btn, description_btn] 

        box380 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_macrophage_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float357 = FloatText(value='6500', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float357, units_btn, description_btn] 

        box381 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_neutrophil_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float358 = FloatText(value='1581', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float358, units_btn, description_btn] 

        box382 = Box(children=row, layout=box_layout)
        name_btn = Button(description='exhausted_macrophage_death_rat', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float359 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float359, units_btn, description_btn] 

        box383 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ability_to_phagocytose_infected_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float360 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Boolean for whether macrophages can phagocytose infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float360, units_btn, description_btn] 

        box384 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_of_DC_departure', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float361 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Time DC leaves tissue after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float361, units_btn, description_btn] 

        box385 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float362 = FloatText(value='0.167', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float362, units_btn, description_btn] 

        box386 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float363 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float363, units_btn, description_btn] 

        box387 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_chemokine_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float364 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to chemokine in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float364, units_btn, description_btn] 

        box388 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float365 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float365, units_btn, description_btn] 

        box389 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float366 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float366, units_btn, description_btn] 

        box390 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_immune_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float367 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='used internally to track activation state', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float367, units_btn, description_btn] 

        box391 = Box(children=row, layout=box_layout)

        self.cell_def_vbox3 = VBox([
          div_row25, box294, box295, box296, box297, div_row26, death_model1,box298, box299, box300, box301, box302, box303, box304, death_model2,box305, box306, box307, box308, box309, box310, box311, div_row27, box312, box313, box314, box315, box316, box317, box318, box319, box320, div_row28, box321, box322, box323, box324, box325, div_row29, box326,box327,box328,self.bool17,self.bool18,chemotaxis_btn,self.bool19,box329,box330,div_row30, box331,box332,box333,box334,box335,box336,box337,box338,box339,box340,box341,div_row31, div_row32,          box342,
          box343,
          box344,
          box345,
          box346,
          box347,
          box348,
          box349,
          box350,
          box351,
          box352,
          box353,
          box354,
          box355,
          box356,
          box357,
          box358,
          box359,
          box360,
          box361,
          box362,
          box363,
          box364,
          box365,
          box366,
          box367,
          box368,
          box369,
          box370,
          box371,
          box372,
          box373,
          box374,
          box375,
          box376,
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
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox3)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = neutrophil
        #  ------------------------- 
        div_row33 = Button(description='phenotype:cycle (model: flow_cytometry_separated_cycle_model; code=6)', disabled=True, layout=divider_button_layout)
        div_row33.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 1 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float368 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float368, units_btn, ]
        box392 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 1 -> Phase 2 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float369 = FloatText(value='0.00208333', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float369, units_btn, ]
        box393 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 2 -> Phase 3 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float370 = FloatText(value='0.00416667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float370, units_btn, ]
        box394 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 3 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float371 = FloatText(value='0.0166667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float371, units_btn, ]
        box395 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row34 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row34.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float372 = FloatText(value='8.9e-4', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float372, units_btn, ]
        box396 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float373 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float373, units_btn, ]
        box397 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float374 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float374, units_btn, ]
        box398 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float375 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float375, units_btn, ]
        box399 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float376 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float376, units_btn, ]
        box400 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float377 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float377, units_btn, ]
        box401 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float378 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float378, units_btn, ]
        box402 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float379 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float379, units_btn, ]
        box403 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float380 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float380, units_btn, ]
        box404 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float381 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float381, units_btn, ]
        box405 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float382 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float382, units_btn, ]
        box406 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float383 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float383, units_btn, ]
        box407 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float384 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float384, units_btn, ]
        box408 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float385 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float385, units_btn, ]
        box409 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row35 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row35.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float386 = FloatText(value='1437', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float386, units_btn, ]
        box410 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float387 = FloatText(value='0.75', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float387, units_btn, ]
        box411 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float388 = FloatText(value='143.7', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float388, units_btn, ]
        box412 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float389 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float389, units_btn, ]
        box413 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float390 = FloatText(value='0.045', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float390, units_btn, ]
        box414 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float391 = FloatText(value='0.0055', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float391, units_btn, ]
        box415 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcified_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float392 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float392, units_btn, ]
        box416 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float393 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float393, units_btn, ]
        box417 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float394 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float394, units_btn, ]
        box418 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row36 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row36.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float395 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float395, units_btn, ]
        box419 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float396 = FloatText(value='10', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float396, units_btn, ]
        box420 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float397 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float397, units_btn, ]
        box421 = Box(children=row, layout=box_layout)

        self.bool20 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float398 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool20, name_btn, self.float398, units_btn, ]
        box422 = Box(children=row, layout=box_layout)

        self.bool21 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float399 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool21, name_btn, self.float399, units_btn, ]
        box423 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row37 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row37.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float400 = FloatText(value='19', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float400, units_btn]
        box424 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float401 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float401, units_btn]
        box425 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float402 = FloatText(value='0.91', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float402, units_btn]
        box426 = Box(children=row, layout=box_layout)
        self.bool22 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        self.bool23 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool24 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate5 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate5]
        box427 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction5 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction5]
        box428 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row38 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row38.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text16 = Text(value='interferon 1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text16]
        box429 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float403 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float403, units_btn]
        box430 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text17 = Text(value='pro-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text17]
        box431 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float404 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float404, units_btn]
        box432 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float405 = FloatText(value='0.1', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float405, units_btn]
        box433 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text18 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text18]
        box434 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float406 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float406, units_btn]
        box435 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float407 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float407, units_btn]
        box436 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text19 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text19]
        box437 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float408 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float408, units_btn]
        box438 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float409 = FloatText(value='0.1', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float409, units_btn]
        box439 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row39 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row39.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        div_row40 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row40.style.button_color = 'cyan'
        name_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float410 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float410, units_btn, description_btn] 

        box440 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float411 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='uncoated endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float411, units_btn, description_btn] 

        box441 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_RNA', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float412 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='RNA', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='total (functional) viral RNA copies', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float412, units_btn, description_btn] 

        box442 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_protein', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float413 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='protein', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total assembled sets of viral protein', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float413, units_btn, description_btn] 

        box443 = Box(children=row, layout=box_layout)
        name_btn = Button(description='assembled_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float414 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='total assembled virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float414, units_btn, description_btn] 

        box444 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_uncoating_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float415 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which an internalized virion is uncoated', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float415, units_btn, description_btn] 

        box445 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_to_RNA_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float416 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which uncoated virion makes its mRNA available', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float416, units_btn, description_btn] 

        box446 = Box(children=row, layout=box_layout)
        name_btn = Button(description='protein_synthesis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float417 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at mRNA creates complete set of proteins', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float417, units_btn, description_btn] 

        box447 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_assembly_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float418 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which viral proteins are assembled into complete virion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float418, units_btn, description_btn] 

        box448 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_export_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float419 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which a virion is exported from a live cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float419, units_btn, description_btn] 

        box449 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float420 = FloatText(value='1000', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of unbound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float420, units_btn, description_btn] 

        box450 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float421 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of bound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float421, units_btn, description_btn] 

        box451 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float422 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of internalized unbound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float422, units_btn, description_btn] 

        box452 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float423 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of internalized bound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float423, units_btn, description_btn] 

        box453 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float424 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor-virus binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float424, units_btn, description_btn] 

        box454 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_endocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float425 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus endocytosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float425, units_btn, description_btn] 

        box455 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_cargo_release_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float426 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor-virus cargo release rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float426, units_btn, description_btn] 

        box456 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_recycling_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float427 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor recycling rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float427, units_btn, description_btn] 

        box457 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_infected_apoptosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float428 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='maximum rate of cell apoptosis due to viral infection', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float428, units_btn, description_btn] 

        box458 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_apoptosis_half_max', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float429 = FloatText(value='250', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='viral load at which cells reach half max apoptosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float429, units_btn, description_btn] 

        box459 = Box(children=row, layout=box_layout)
        name_btn = Button(description='apoptosis_hill_power', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float430 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Hill power for viral load apoptosis response', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float430, units_btn, description_btn] 

        box460 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virus_fraction_released_at_death', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float431 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='fraction of internal virus released at cell death', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float431, units_btn, description_btn] 

        box461 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float432 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='max rate that infected cells secrete chemokine', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float432, units_btn, description_btn] 

        box462 = Box(children=row, layout=box_layout)
        name_btn = Button(description='debris_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float433 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate that dead cells release debris', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float433, units_btn, description_btn] 

        box463 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_activated', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float434 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='used internally to track activation of chemokine secretion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float434, units_btn, description_btn] 

        box464 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_secretion_rate_via_infection', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float435 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Type-1 interferon secretion rate for infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float435, units_btn, description_btn] 

        box465 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_interferon_secretion_rate_via_paracrine', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float436 = FloatText(value='0.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Type-1 interferon secretion rate after activation by Type-1 interferon', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float436, units_btn, description_btn] 

        box466 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_response_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float437 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Interferon response scales linearly until Int-1 exceeds this threshold', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float437, units_btn, description_btn] 

        box467 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_activation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float438 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Current interferon signaling activation state (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float438, units_btn, description_btn] 

        box468 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_virus_inhibition', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float439 = FloatText(value='0.9', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='At max interferon activation, max inhibition of viral replication (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float439, units_btn, description_btn] 

        box469 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_viral_RNA_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float440 = FloatText(value='2', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='infected cell interferon secretion saturates at this viral RNA level', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float440, units_btn, description_btn] 

        box470 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float441 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='tracks total contact time with CD8 T cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float441, units_btn, description_btn] 

        box471 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float442 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='the rate at which the cell attaches to cells in contact', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float442, units_btn, description_btn] 

        box472 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_lifetime', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float443 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the mean duration of a cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float443, units_btn, description_btn] 

        box473 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_death_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float444 = FloatText(value='50', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='threshold CD8 T cell contact time to trigger apoptosis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float444, units_btn, description_btn] 

        box474 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_attachment_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float445 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float445, units_btn, description_btn] 

        box475 = Box(children=row, layout=box_layout)
        name_btn = Button(description='elastic_attachment_coefficient', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float446 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='elastic coefficient for cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float446, units_btn, description_btn] 

        box476 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_to_next_phagocytosis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float447 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='time it takes for the apoptotic material to be phagocytosed', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float447, units_btn, description_btn] 

        box477 = Box(children=row, layout=box_layout)
        name_btn = Button(description='material_internalisation_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float448 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float448, units_btn, description_btn] 

        box478 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_macrophage_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float449 = FloatText(value='6500', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float449, units_btn, description_btn] 

        box479 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_neutrophil_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float450 = FloatText(value='1581', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float450, units_btn, description_btn] 

        box480 = Box(children=row, layout=box_layout)
        name_btn = Button(description='exhausted_macrophage_death_rat', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float451 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float451, units_btn, description_btn] 

        box481 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ability_to_phagocytose_infected_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float452 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Boolean for whether macrophages can phagocytose infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float452, units_btn, description_btn] 

        box482 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_of_DC_departure', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float453 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Time DC leaves tissue after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float453, units_btn, description_btn] 

        box483 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float454 = FloatText(value='0.117', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float454, units_btn, description_btn] 

        box484 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float455 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float455, units_btn, description_btn] 

        box485 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_chemokine_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float456 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to chemokine in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float456, units_btn, description_btn] 

        box486 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float457 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float457, units_btn, description_btn] 

        box487 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float458 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float458, units_btn, description_btn] 

        box488 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_immune_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float459 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='used internally to track activation state', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float459, units_btn, description_btn] 

        box489 = Box(children=row, layout=box_layout)

        self.cell_def_vbox4 = VBox([
          div_row33, box392, box393, box394, box395, div_row34, death_model1,box396, box397, box398, box399, box400, box401, box402, death_model2,box403, box404, box405, box406, box407, box408, box409, div_row35, box410, box411, box412, box413, box414, box415, box416, box417, box418, div_row36, box419, box420, box421, box422, box423, div_row37, box424,box425,box426,self.bool22,self.bool23,chemotaxis_btn,self.bool24,box427,box428,div_row38, box429,box430,box431,box432,box433,box434,box435,box436,box437,box438,box439,div_row39, div_row40,          box440,
          box441,
          box442,
          box443,
          box444,
          box445,
          box446,
          box447,
          box448,
          box449,
          box450,
          box451,
          box452,
          box453,
          box454,
          box455,
          box456,
          box457,
          box458,
          box459,
          box460,
          box461,
          box462,
          box463,
          box464,
          box465,
          box466,
          box467,
          box468,
          box469,
          box470,
          box471,
          box472,
          box473,
          box474,
          box475,
          box476,
          box477,
          box478,
          box479,
          box480,
          box481,
          box482,
          box483,
          box484,
          box485,
          box486,
          box487,
          box488,
          box489,
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox4)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = DC
        #  ------------------------- 
        div_row41 = Button(description='phenotype:cycle (model: flow_cytometry_separated_cycle_model; code=6)', disabled=True, layout=divider_button_layout)
        div_row41.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 1 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float460 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float460, units_btn, ]
        box490 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 1 -> Phase 2 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float461 = FloatText(value='0.00208333', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float461, units_btn, ]
        box491 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 2 -> Phase 3 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float462 = FloatText(value='0.00416667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float462, units_btn, ]
        box492 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 3 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float463 = FloatText(value='0.0166667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float463, units_btn, ]
        box493 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row42 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row42.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float464 = FloatText(value='8.9e-4', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float464, units_btn, ]
        box494 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float465 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float465, units_btn, ]
        box495 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float466 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float466, units_btn, ]
        box496 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float467 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float467, units_btn, ]
        box497 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float468 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float468, units_btn, ]
        box498 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float469 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float469, units_btn, ]
        box499 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float470 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float470, units_btn, ]
        box500 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float471 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float471, units_btn, ]
        box501 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float472 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float472, units_btn, ]
        box502 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float473 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float473, units_btn, ]
        box503 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float474 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float474, units_btn, ]
        box504 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float475 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float475, units_btn, ]
        box505 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float476 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float476, units_btn, ]
        box506 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float477 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float477, units_btn, ]
        box507 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row43 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row43.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float478 = FloatText(value='1767', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float478, units_btn, ]
        box508 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float479 = FloatText(value='0.75', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float479, units_btn, ]
        box509 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float480 = FloatText(value='176.7', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float480, units_btn, ]
        box510 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float481 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float481, units_btn, ]
        box511 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float482 = FloatText(value='0.045', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float482, units_btn, ]
        box512 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float483 = FloatText(value='0.0055', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float483, units_btn, ]
        box513 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcified_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float484 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float484, units_btn, ]
        box514 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float485 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float485, units_btn, ]
        box515 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float486 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float486, units_btn, ]
        box516 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row44 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row44.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float487 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float487, units_btn, ]
        box517 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float488 = FloatText(value='10', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float488, units_btn, ]
        box518 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float489 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float489, units_btn, ]
        box519 = Box(children=row, layout=box_layout)

        self.bool25 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float490 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool25, name_btn, self.float490, units_btn, ]
        box520 = Box(children=row, layout=box_layout)

        self.bool26 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float491 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool26, name_btn, self.float491, units_btn, ]
        box521 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row45 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row45.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float492 = FloatText(value='2', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float492, units_btn]
        box522 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float493 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float493, units_btn]
        box523 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float494 = FloatText(value='0.7', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float494, units_btn]
        box524 = Box(children=row, layout=box_layout)
        self.bool27 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        self.bool28 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool29 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate6 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate6]
        box525 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction6 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction6]
        box526 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row46 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row46.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text20 = Text(value='interferon 1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text20]
        box527 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float495 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float495, units_btn]
        box528 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text21 = Text(value='pro-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text21]
        box529 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float496 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float496, units_btn]
        box530 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float497 = FloatText(value='0.1', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float497, units_btn]
        box531 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text22 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text22]
        box532 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float498 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float498, units_btn]
        box533 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float499 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float499, units_btn]
        box534 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text23 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text23]
        box535 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float500 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float500, units_btn]
        box536 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float501 = FloatText(value='0.1', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float501, units_btn]
        box537 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row47 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row47.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        div_row48 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row48.style.button_color = 'cyan'
        name_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float502 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float502, units_btn, description_btn] 

        box538 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float503 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='uncoated endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float503, units_btn, description_btn] 

        box539 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_RNA', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float504 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='RNA', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='total (functional) viral RNA copies', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float504, units_btn, description_btn] 

        box540 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_protein', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float505 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='protein', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total assembled sets of viral protein', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float505, units_btn, description_btn] 

        box541 = Box(children=row, layout=box_layout)
        name_btn = Button(description='assembled_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float506 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='total assembled virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float506, units_btn, description_btn] 

        box542 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_uncoating_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float507 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which an internalized virion is uncoated', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float507, units_btn, description_btn] 

        box543 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_to_RNA_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float508 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which uncoated virion makes its mRNA available', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float508, units_btn, description_btn] 

        box544 = Box(children=row, layout=box_layout)
        name_btn = Button(description='protein_synthesis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float509 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at mRNA creates complete set of proteins', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float509, units_btn, description_btn] 

        box545 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_assembly_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float510 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which viral proteins are assembled into complete virion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float510, units_btn, description_btn] 

        box546 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_export_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float511 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which a virion is exported from a live cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float511, units_btn, description_btn] 

        box547 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float512 = FloatText(value='1000', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of unbound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float512, units_btn, description_btn] 

        box548 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float513 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of bound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float513, units_btn, description_btn] 

        box549 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float514 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of internalized unbound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float514, units_btn, description_btn] 

        box550 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float515 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of internalized bound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float515, units_btn, description_btn] 

        box551 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float516 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor-virus binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float516, units_btn, description_btn] 

        box552 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_endocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float517 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus endocytosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float517, units_btn, description_btn] 

        box553 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_cargo_release_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float518 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor-virus cargo release rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float518, units_btn, description_btn] 

        box554 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_recycling_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float519 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor recycling rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float519, units_btn, description_btn] 

        box555 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_infected_apoptosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float520 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='maximum rate of cell apoptosis due to viral infection', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float520, units_btn, description_btn] 

        box556 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_apoptosis_half_max', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float521 = FloatText(value='250', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='viral load at which cells reach half max apoptosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float521, units_btn, description_btn] 

        box557 = Box(children=row, layout=box_layout)
        name_btn = Button(description='apoptosis_hill_power', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float522 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Hill power for viral load apoptosis response', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float522, units_btn, description_btn] 

        box558 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virus_fraction_released_at_death', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float523 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='fraction of internal virus released at cell death', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float523, units_btn, description_btn] 

        box559 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float524 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='max rate that infected cells secrete chemokine', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float524, units_btn, description_btn] 

        box560 = Box(children=row, layout=box_layout)
        name_btn = Button(description='debris_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float525 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate that dead cells release debris', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float525, units_btn, description_btn] 

        box561 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_activated', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float526 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='used internally to track activation of chemokine secretion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float526, units_btn, description_btn] 

        box562 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_secretion_rate_via_infection', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float527 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Type-1 interferon secretion rate for infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float527, units_btn, description_btn] 

        box563 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_interferon_secretion_rate_via_paracrine', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float528 = FloatText(value='0.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Type-1 interferon secretion rate after activation by Type-1 interferon', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float528, units_btn, description_btn] 

        box564 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_response_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float529 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Interferon response scales linearly until Int-1 exceeds this threshold', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float529, units_btn, description_btn] 

        box565 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_activation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float530 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Current interferon signaling activation state (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float530, units_btn, description_btn] 

        box566 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_virus_inhibition', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float531 = FloatText(value='0.9', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='At max interferon activation, max inhibition of viral replication (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float531, units_btn, description_btn] 

        box567 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_viral_RNA_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float532 = FloatText(value='2', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='infected cell interferon secretion saturates at this viral RNA level', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float532, units_btn, description_btn] 

        box568 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float533 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='tracks total contact time with CD8 T cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float533, units_btn, description_btn] 

        box569 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float534 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='the rate at which the cell attaches to cells in contact', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float534, units_btn, description_btn] 

        box570 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_lifetime', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float535 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the mean duration of a cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float535, units_btn, description_btn] 

        box571 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_death_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float536 = FloatText(value='50', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='threshold CD8 T cell contact time to trigger apoptosis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float536, units_btn, description_btn] 

        box572 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_attachment_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float537 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float537, units_btn, description_btn] 

        box573 = Box(children=row, layout=box_layout)
        name_btn = Button(description='elastic_attachment_coefficient', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float538 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='elastic coefficient for cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float538, units_btn, description_btn] 

        box574 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_to_next_phagocytosis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float539 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='time it takes for the apoptotic material to be phagocytosed', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float539, units_btn, description_btn] 

        box575 = Box(children=row, layout=box_layout)
        name_btn = Button(description='material_internalisation_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float540 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float540, units_btn, description_btn] 

        box576 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_macrophage_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float541 = FloatText(value='6500', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float541, units_btn, description_btn] 

        box577 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_neutrophil_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float542 = FloatText(value='1581', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float542, units_btn, description_btn] 

        box578 = Box(children=row, layout=box_layout)
        name_btn = Button(description='exhausted_macrophage_death_rat', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float543 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float543, units_btn, description_btn] 

        box579 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ability_to_phagocytose_infected_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float544 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Boolean for whether macrophages can phagocytose infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float544, units_btn, description_btn] 

        box580 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_of_DC_departure', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float545 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Time DC leaves tissue after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float545, units_btn, description_btn] 

        box581 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float546 = FloatText(value='0.167', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float546, units_btn, description_btn] 

        box582 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float547 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float547, units_btn, description_btn] 

        box583 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_chemokine_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float548 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to chemokine in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float548, units_btn, description_btn] 

        box584 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float549 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float549, units_btn, description_btn] 

        box585 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float550 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float550, units_btn, description_btn] 

        box586 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_immune_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float551 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='used internally to track activation state', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float551, units_btn, description_btn] 

        box587 = Box(children=row, layout=box_layout)

        self.cell_def_vbox5 = VBox([
          div_row41, box490, box491, box492, box493, div_row42, death_model1,box494, box495, box496, box497, box498, box499, box500, death_model2,box501, box502, box503, box504, box505, box506, box507, div_row43, box508, box509, box510, box511, box512, box513, box514, box515, box516, div_row44, box517, box518, box519, box520, box521, div_row45, box522,box523,box524,self.bool27,self.bool28,chemotaxis_btn,self.bool29,box525,box526,div_row46, box527,box528,box529,box530,box531,box532,box533,box534,box535,box536,box537,div_row47, div_row48,          box538,
          box539,
          box540,
          box541,
          box542,
          box543,
          box544,
          box545,
          box546,
          box547,
          box548,
          box549,
          box550,
          box551,
          box552,
          box553,
          box554,
          box555,
          box556,
          box557,
          box558,
          box559,
          box560,
          box561,
          box562,
          box563,
          box564,
          box565,
          box566,
          box567,
          box568,
          box569,
          box570,
          box571,
          box572,
          box573,
          box574,
          box575,
          box576,
          box577,
          box578,
          box579,
          box580,
          box581,
          box582,
          box583,
          box584,
          box585,
          box586,
          box587,
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox5)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = CD4 Tcell
        #  ------------------------- 
        div_row49 = Button(description='phenotype:cycle (model: flow_cytometry_separated_cycle_model; code=6)', disabled=True, layout=divider_button_layout)
        div_row49.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 1 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float552 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float552, units_btn, ]
        box588 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 1 -> Phase 2 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float553 = FloatText(value='0.00208333', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float553, units_btn, ]
        box589 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 2 -> Phase 3 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float554 = FloatText(value='0.00416667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float554, units_btn, ]
        box590 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 3 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float555 = FloatText(value='0.0166667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float555, units_btn, ]
        box591 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row50 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row50.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float556 = FloatText(value='2.8e-4', step='1e-05', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float556, units_btn, ]
        box592 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float557 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float557, units_btn, ]
        box593 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float558 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float558, units_btn, ]
        box594 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float559 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float559, units_btn, ]
        box595 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float560 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float560, units_btn, ]
        box596 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float561 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float561, units_btn, ]
        box597 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float562 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float562, units_btn, ]
        box598 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float563 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float563, units_btn, ]
        box599 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float564 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float564, units_btn, ]
        box600 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float565 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float565, units_btn, ]
        box601 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float566 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float566, units_btn, ]
        box602 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float567 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float567, units_btn, ]
        box603 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float568 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float568, units_btn, ]
        box604 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float569 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float569, units_btn, ]
        box605 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row51 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row51.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float570 = FloatText(value='478', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float570, units_btn, ]
        box606 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float571 = FloatText(value='0.75', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float571, units_btn, ]
        box607 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float572 = FloatText(value='47.8', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float572, units_btn, ]
        box608 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float573 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float573, units_btn, ]
        box609 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float574 = FloatText(value='0.0045', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float574, units_btn, ]
        box610 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float575 = FloatText(value='0.0055', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float575, units_btn, ]
        box611 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcified_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float576 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float576, units_btn, ]
        box612 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float577 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float577, units_btn, ]
        box613 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float578 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float578, units_btn, ]
        box614 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row52 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row52.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float579 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float579, units_btn, ]
        box615 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float580 = FloatText(value='10', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float580, units_btn, ]
        box616 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float581 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float581, units_btn, ]
        box617 = Box(children=row, layout=box_layout)

        self.bool30 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float582 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool30, name_btn, self.float582, units_btn, ]
        box618 = Box(children=row, layout=box_layout)

        self.bool31 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float583 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool31, name_btn, self.float583, units_btn, ]
        box619 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row53 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row53.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float584 = FloatText(value='4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float584, units_btn]
        box620 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float585 = FloatText(value='5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float585, units_btn]
        box621 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float586 = FloatText(value='0.70', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float586, units_btn]
        box622 = Box(children=row, layout=box_layout)
        self.bool32 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        self.bool33 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool34 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate7 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate7]
        box623 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction7 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction7]
        box624 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row54 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row54.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text24 = Text(value='interferon 1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text24]
        box625 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float587 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float587, units_btn]
        box626 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text25 = Text(value='pro-inflammatory cytokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text25]
        box627 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float588 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float588, units_btn]
        box628 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float589 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float589, units_btn]
        box629 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text26 = Text(value='chemokine', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text26]
        box630 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float590 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float590, units_btn]
        box631 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float591 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float591, units_btn]
        box632 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text27 = Text(value='debris', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text27]
        box633 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float592 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless substrate concentration', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float592, units_btn]
        box634 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float593 = FloatText(value='0.1', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float593, units_btn]
        box635 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row55 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row55.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        div_row56 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row56.style.button_color = 'cyan'
        name_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float594 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float594, units_btn, description_btn] 

        box636 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float595 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='virions', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='uncoated endocytosed virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float595, units_btn, description_btn] 

        box637 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_RNA', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float596 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='RNA', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='total (functional) viral RNA copies', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float596, units_btn, description_btn] 

        box638 = Box(children=row, layout=box_layout)
        name_btn = Button(description='viral_protein', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float597 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='protein', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='total assembled sets of viral protein', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float597, units_btn, description_btn] 

        box639 = Box(children=row, layout=box_layout)
        name_btn = Button(description='assembled_virion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float598 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='total assembled virions', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float598, units_btn, description_btn] 

        box640 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_uncoating_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float599 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which an internalized virion is uncoated', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float599, units_btn, description_btn] 

        box641 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uncoated_to_RNA_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float600 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which uncoated virion makes its mRNA available', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float600, units_btn, description_btn] 

        box642 = Box(children=row, layout=box_layout)
        name_btn = Button(description='protein_synthesis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float601 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at mRNA creates complete set of proteins', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float601, units_btn, description_btn] 

        box643 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_assembly_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float602 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate at which viral proteins are assembled into complete virion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float602, units_btn, description_btn] 

        box644 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virion_export_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float603 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate at which a virion is exported from a live cell', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float603, units_btn, description_btn] 

        box645 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float604 = FloatText(value='1000', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of unbound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float604, units_btn, description_btn] 

        box646 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_external_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float605 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of bound ACE2 receptors on surface', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float605, units_btn, description_btn] 

        box647 = Box(children=row, layout=box_layout)
        name_btn = Button(description='unbound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float606 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='initial number of internalized unbound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float606, units_btn, description_btn] 

        box648 = Box(children=row, layout=box_layout)
        name_btn = Button(description='bound_internal_ACE2', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float607 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='receptors', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='initial number of internalized bound ACE2 receptors', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float607, units_btn, description_btn] 

        box649 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_binding_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float608 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor-virus binding rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float608, units_btn, description_btn] 

        box650 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_endocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float609 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor-virus endocytosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float609, units_btn, description_btn] 

        box651 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_cargo_release_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float610 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='ACE2 receptor-virus cargo release rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float610, units_btn, description_btn] 

        box652 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ACE2_recycling_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float611 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='ACE2 receptor recycling rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float611, units_btn, description_btn] 

        box653 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_infected_apoptosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float612 = FloatText(value='0.001', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='maximum rate of cell apoptosis due to viral infection', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float612, units_btn, description_btn] 

        box654 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_apoptosis_half_max', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float613 = FloatText(value='250', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='virion', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='viral load at which cells reach half max apoptosis rate', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float613, units_btn, description_btn] 

        box655 = Box(children=row, layout=box_layout)
        name_btn = Button(description='apoptosis_hill_power', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float614 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Hill power for viral load apoptosis response', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float614, units_btn, description_btn] 

        box656 = Box(children=row, layout=box_layout)
        name_btn = Button(description='virus_fraction_released_at_death', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float615 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='fraction of internal virus released at cell death', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float615, units_btn, description_btn] 

        box657 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float616 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='max rate that infected cells secrete chemokine', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float616, units_btn, description_btn] 

        box658 = Box(children=row, layout=box_layout)
        name_btn = Button(description='debris_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float617 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='rate that dead cells release debris', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float617, units_btn, description_btn] 

        box659 = Box(children=row, layout=box_layout)
        name_btn = Button(description='infected_cell_chemokine_secretion_activated', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float618 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='none', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='used internally to track activation of chemokine secretion', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float618, units_btn, description_btn] 

        box660 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_secretion_rate_via_infection', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float619 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Type-1 interferon secretion rate for infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float619, units_btn, description_btn] 

        box661 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_interferon_secretion_rate_via_paracrine', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float620 = FloatText(value='0.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Type-1 interferon secretion rate after activation by Type-1 interferon', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float620, units_btn, description_btn] 

        box662 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_response_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float621 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Interferon response scales linearly until Int-1 exceeds this threshold', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float621, units_btn, description_btn] 

        box663 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_activation', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float622 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Current interferon signaling activation state (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float622, units_btn, description_btn] 

        box664 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_max_virus_inhibition', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float623 = FloatText(value='0.9', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='At max interferon activation, max inhibition of viral replication (between 0 and 1)', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float623, units_btn, description_btn] 

        box665 = Box(children=row, layout=box_layout)
        name_btn = Button(description='interferon_viral_RNA_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float624 = FloatText(value='2', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='infected cell interferon secretion saturates at this viral RNA level', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float624, units_btn, description_btn] 

        box666 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float625 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='tracks total contact time with CD8 T cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float625, units_btn, description_btn] 

        box667 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float626 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='the rate at which the cell attaches to cells in contact', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float626, units_btn, description_btn] 

        box668 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_attachment_lifetime', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float627 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='the mean duration of a cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float627, units_btn, description_btn] 

        box669 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TCell_contact_death_threshold', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float628 = FloatText(value='50', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='threshold CD8 T cell contact time to trigger apoptosis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float628, units_btn, description_btn] 

        box670 = Box(children=row, layout=box_layout)
        name_btn = Button(description='max_attachment_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float629 = FloatText(value='15', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float629, units_btn, description_btn] 

        box671 = Box(children=row, layout=box_layout)
        name_btn = Button(description='elastic_attachment_coefficient', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float630 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='elastic coefficient for cell-cell attachment', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float630, units_btn, description_btn] 

        box672 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_to_next_phagocytosis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float631 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='time it takes for the apoptotic material to be phagocytosed', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float631, units_btn, description_btn] 

        box673 = Box(children=row, layout=box_layout)
        name_btn = Button(description='material_internalisation_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float632 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float632, units_btn, description_btn] 

        box674 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_macrophage_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float633 = FloatText(value='6500', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float633, units_btn, description_btn] 

        box675 = Box(children=row, layout=box_layout)
        name_btn = Button(description='threshold_neutrophil_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float634 = FloatText(value='1581', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='micron', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float634, units_btn, description_btn] 

        box676 = Box(children=row, layout=box_layout)
        name_btn = Button(description='exhausted_macrophage_death_rat', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float635 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float635, units_btn, description_btn] 

        box677 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ability_to_phagocytose_infected_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float636 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='Boolean for whether macrophages can phagocytose infected cells', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float636, units_btn, description_btn] 

        box678 = Box(children=row, layout=box_layout)
        name_btn = Button(description='time_of_DC_departure', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float637 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='Time DC leaves tissue after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float637, units_btn, description_btn] 

        box679 = Box(children=row, layout=box_layout)
        name_btn = Button(description='phagocytosis_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float638 = FloatText(value='0.167', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float638, units_btn, description_btn] 

        box680 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_debris_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float639 = FloatText(value='1.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='relative sensitivity to debris in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float639, units_btn, description_btn] 

        box681 = Box(children=row, layout=box_layout)
        name_btn = Button(description='sensitivity_to_chemokine_chemotaxis', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float640 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='relative sensitivity to chemokine in chemotaxis', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float640, units_btn, description_btn] 

        box682 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float641 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='speed after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float641, units_btn, description_btn] 

        box683 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_cytokine_secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float642 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='rate of secreting pro-inflamatory cytokine after activation', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float642, units_btn, description_btn] 

        box684 = Box(children=row, layout=box_layout)
        name_btn = Button(description='activated_immune_cell', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float643 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='used internally to track activation state', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float643, units_btn, description_btn] 

        box685 = Box(children=row, layout=box_layout)

        self.cell_def_vbox6 = VBox([
          div_row49, box588, box589, box590, box591, div_row50, death_model1,box592, box593, box594, box595, box596, box597, box598, death_model2,box599, box600, box601, box602, box603, box604, box605, div_row51, box606, box607, box608, box609, box610, box611, box612, box613, box614, div_row52, box615, box616, box617, box618, box619, div_row53, box620,box621,box622,self.bool32,self.bool33,chemotaxis_btn,self.bool34,box623,box624,div_row54, box625,box626,box627,box628,box629,box630,box631,box632,box633,box634,box635,div_row55, div_row56,          box636,
          box637,
          box638,
          box639,
          box640,
          box641,
          box642,
          box643,
          box644,
          box645,
          box646,
          box647,
          box648,
          box649,
          box650,
          box651,
          box652,
          box653,
          box654,
          box655,
          box656,
          box657,
          box658,
          box659,
          box660,
          box661,
          box662,
          box663,
          box664,
          box665,
          box666,
          box667,
          box668,
          box669,
          box670,
          box671,
          box672,
          box673,
          box674,
          box675,
          box676,
          box677,
          box678,
          box679,
          box680,
          box681,
          box682,
          box683,
          box684,
          box685,
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox6)



        row = [name_btn, self.float643, units_btn, description_btn] 
        box635 = Box(children=row, layout=box_layout)

        self.tab = VBox([
          self.cell_type_parent_row,  
self.cell_def_vbox0, self.cell_def_vbox1, self.cell_def_vbox2, self.cell_def_vbox3, self.cell_def_vbox4, self.cell_def_vbox5, self.cell_def_vbox6,         ])
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
        self.text1.value = uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]').attrib['name']
        self.float36.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]//secretion_target').text)
        self.float37.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]//uptake_rate').text)
        self.text2.value = uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]').attrib['name']
        self.float38.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]//secretion_target').text)
        self.float39.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]//uptake_rate').text)
        self.text3.value = uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]').attrib['name']
        self.float40.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]//secretion_target').text)
        self.float41.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]//uptake_rate').text)
        # ---------  molecular
        # ------------------ cell_definition: lung epithelium
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        self.float92.value = float(uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        self.float93.value = float(uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[2]').text)
        self.float94.value = float(uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[3]').text)
        self.float95.value = float(uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[4]').text)
        # ---------  death 
        self.float96.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[1]//death_rate').text)
        self.float97.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text)
        self.float98.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text)
        self.float99.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float100.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text)
        self.float101.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//calcification_rate').text)
        self.float102.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//relative_rupture_volume').text)
        self.float103.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[2]//death_rate').text)
        self.float104.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        self.float105.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        self.float106.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float107.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        self.float108.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//calcification_rate').text)
        self.float109.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)
        # ---------  volume 
        self.float110.value = float(uep.find('.//cell_definition[2]//phenotype//volume//total').text)
        self.float111.value = float(uep.find('.//cell_definition[2]//phenotype//volume//fluid_fraction').text)
        self.float112.value = float(uep.find('.//cell_definition[2]//phenotype//volume//nuclear').text)
        self.float113.value = float(uep.find('.//cell_definition[2]//phenotype//volume//fluid_change_rate').text)
        self.float114.value = float(uep.find('.//cell_definition[2]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        self.float115.value = float(uep.find('.//cell_definition[2]//phenotype//volume//nuclear_biomass_change_rate').text)
        self.float116.value = float(uep.find('.//cell_definition[2]//phenotype//volume//calcified_fraction').text)
        self.float117.value = float(uep.find('.//cell_definition[2]//phenotype//volume//calcification_rate').text)
        self.float118.value = float(uep.find('.//cell_definition[2]//phenotype//volume//relative_rupture_volume').text)
        # ---------  mechanics 
        self.float119.value = float(uep.find('.//cell_definition[2]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float120.value = float(uep.find('.//cell_definition[2]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float121.value = float(uep.find('.//cell_definition[2]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool5.value = ('true' == (uep.find('.//cell_definition[2]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool6.value = ('true' == (uep.find('.//cell_definition[2]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float124.value = float(uep.find('.//cell_definition[2]//phenotype//motility//speed').text)
        self.float125.value = float(uep.find('.//cell_definition[2]//phenotype//motility//persistence_time').text)
        self.float126.value = float(uep.find('.//cell_definition[2]//phenotype//motility//migration_bias').text)
        self.bool7.value = ('true' == (uep.find('.//cell_definition[2]//phenotype//motility//options//enabled').text.lower()))
        self.bool8.value = ('true' == (uep.find('.//cell_definition[2]//phenotype//motility//options//use_2D').text.lower()))
        self.bool9.value = ('true' == (uep.find('.//cell_definition[2]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate2.value = uep.find('.//cell_definition[2]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction2.value = uep.find('.//cell_definition[2]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text4.value = uep.find('.//cell_definition[2]//phenotype//secretion//substrate[1]').attrib['name']
        self.float127.value = float(uep.find('.//cell_definition[2]//phenotype//secretion//substrate[1]//secretion_target').text)
        self.text5.value = uep.find('.//cell_definition[2]//phenotype//secretion//substrate[2]').attrib['name']
        self.float128.value = float(uep.find('.//cell_definition[2]//phenotype//secretion//substrate[2]//secretion_target').text)
        self.float129.value = float(uep.find('.//cell_definition[2]//phenotype//secretion//substrate[2]//uptake_rate').text)
        self.text6.value = uep.find('.//cell_definition[2]//phenotype//secretion//substrate[3]').attrib['name']
        self.float130.value = float(uep.find('.//cell_definition[2]//phenotype//secretion//substrate[3]//secretion_target').text)
        self.float131.value = float(uep.find('.//cell_definition[2]//phenotype//secretion//substrate[3]//uptake_rate').text)
        self.text7.value = uep.find('.//cell_definition[2]//phenotype//secretion//substrate[4]').attrib['name']
        self.float132.value = float(uep.find('.//cell_definition[2]//phenotype//secretion//substrate[4]//secretion_target').text)
        self.float133.value = float(uep.find('.//cell_definition[2]//phenotype//secretion//substrate[4]//uptake_rate').text)
        # ---------  molecular
        # ------------------ cell_definition: CD8 Tcell
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        self.float184.value = float(uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        self.float185.value = float(uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[2]').text)
        self.float186.value = float(uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[3]').text)
        self.float187.value = float(uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[4]').text)
        # ---------  death 
        self.float188.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[1]//death_rate').text)
        self.float189.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text)
        self.float190.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text)
        self.float191.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float192.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text)
        self.float193.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//calcification_rate').text)
        self.float194.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//relative_rupture_volume').text)
        self.float195.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[2]//death_rate').text)
        self.float196.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        self.float197.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        self.float198.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float199.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        self.float200.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//calcification_rate').text)
        self.float201.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)
        # ---------  volume 
        self.float202.value = float(uep.find('.//cell_definition[3]//phenotype//volume//total').text)
        self.float203.value = float(uep.find('.//cell_definition[3]//phenotype//volume//fluid_fraction').text)
        self.float204.value = float(uep.find('.//cell_definition[3]//phenotype//volume//nuclear').text)
        self.float205.value = float(uep.find('.//cell_definition[3]//phenotype//volume//fluid_change_rate').text)
        self.float206.value = float(uep.find('.//cell_definition[3]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        self.float207.value = float(uep.find('.//cell_definition[3]//phenotype//volume//nuclear_biomass_change_rate').text)
        self.float208.value = float(uep.find('.//cell_definition[3]//phenotype//volume//calcified_fraction').text)
        self.float209.value = float(uep.find('.//cell_definition[3]//phenotype//volume//calcification_rate').text)
        self.float210.value = float(uep.find('.//cell_definition[3]//phenotype//volume//relative_rupture_volume').text)
        # ---------  mechanics 
        self.float211.value = float(uep.find('.//cell_definition[3]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float212.value = float(uep.find('.//cell_definition[3]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float213.value = float(uep.find('.//cell_definition[3]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool10.value = ('true' == (uep.find('.//cell_definition[3]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool11.value = ('true' == (uep.find('.//cell_definition[3]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float216.value = float(uep.find('.//cell_definition[3]//phenotype//motility//speed').text)
        self.float217.value = float(uep.find('.//cell_definition[3]//phenotype//motility//persistence_time').text)
        self.float218.value = float(uep.find('.//cell_definition[3]//phenotype//motility//migration_bias').text)
        self.bool12.value = ('true' == (uep.find('.//cell_definition[3]//phenotype//motility//options//enabled').text.lower()))
        self.bool13.value = ('true' == (uep.find('.//cell_definition[3]//phenotype//motility//options//use_2D').text.lower()))
        self.bool14.value = ('true' == (uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate3.value = uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction3.value = uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text8.value = uep.find('.//cell_definition[3]//phenotype//secretion//substrate[1]').attrib['name']
        self.float219.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[1]//secretion_target').text)
        self.text9.value = uep.find('.//cell_definition[3]//phenotype//secretion//substrate[2]').attrib['name']
        self.float220.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[2]//secretion_target').text)
        self.float221.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[2]//uptake_rate').text)
        self.text10.value = uep.find('.//cell_definition[3]//phenotype//secretion//substrate[3]').attrib['name']
        self.float222.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[3]//secretion_target').text)
        self.float223.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[3]//uptake_rate').text)
        self.text11.value = uep.find('.//cell_definition[3]//phenotype//secretion//substrate[4]').attrib['name']
        self.float224.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[4]//secretion_target').text)
        self.float225.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[4]//uptake_rate').text)
        # ---------  molecular
        # ------------------ cell_definition: macrophage
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        self.float276.value = float(uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        self.float277.value = float(uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[2]').text)
        self.float278.value = float(uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[3]').text)
        self.float279.value = float(uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[4]').text)
        # ---------  death 
        self.float280.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[1]//death_rate').text)
        self.float281.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text)
        self.float282.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text)
        self.float283.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float284.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text)
        self.float285.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//calcification_rate').text)
        self.float286.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//relative_rupture_volume').text)
        self.float287.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[2]//death_rate').text)
        self.float288.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        self.float289.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        self.float290.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float291.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        self.float292.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//calcification_rate').text)
        self.float293.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)
        # ---------  volume 
        self.float294.value = float(uep.find('.//cell_definition[4]//phenotype//volume//total').text)
        self.float295.value = float(uep.find('.//cell_definition[4]//phenotype//volume//fluid_fraction').text)
        self.float296.value = float(uep.find('.//cell_definition[4]//phenotype//volume//nuclear').text)
        self.float297.value = float(uep.find('.//cell_definition[4]//phenotype//volume//fluid_change_rate').text)
        self.float298.value = float(uep.find('.//cell_definition[4]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        self.float299.value = float(uep.find('.//cell_definition[4]//phenotype//volume//nuclear_biomass_change_rate').text)
        self.float300.value = float(uep.find('.//cell_definition[4]//phenotype//volume//calcified_fraction').text)
        self.float301.value = float(uep.find('.//cell_definition[4]//phenotype//volume//calcification_rate').text)
        self.float302.value = float(uep.find('.//cell_definition[4]//phenotype//volume//relative_rupture_volume').text)
        # ---------  mechanics 
        self.float303.value = float(uep.find('.//cell_definition[4]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float304.value = float(uep.find('.//cell_definition[4]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float305.value = float(uep.find('.//cell_definition[4]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool15.value = ('true' == (uep.find('.//cell_definition[4]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool16.value = ('true' == (uep.find('.//cell_definition[4]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float308.value = float(uep.find('.//cell_definition[4]//phenotype//motility//speed').text)
        self.float309.value = float(uep.find('.//cell_definition[4]//phenotype//motility//persistence_time').text)
        self.float310.value = float(uep.find('.//cell_definition[4]//phenotype//motility//migration_bias').text)
        self.bool17.value = ('true' == (uep.find('.//cell_definition[4]//phenotype//motility//options//enabled').text.lower()))
        self.bool18.value = ('true' == (uep.find('.//cell_definition[4]//phenotype//motility//options//use_2D').text.lower()))
        self.bool19.value = ('true' == (uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate4.value = uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction4.value = uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text12.value = uep.find('.//cell_definition[4]//phenotype//secretion//substrate[1]').attrib['name']
        self.float311.value = float(uep.find('.//cell_definition[4]//phenotype//secretion//substrate[1]//secretion_target').text)
        self.text13.value = uep.find('.//cell_definition[4]//phenotype//secretion//substrate[2]').attrib['name']
        self.float312.value = float(uep.find('.//cell_definition[4]//phenotype//secretion//substrate[2]//secretion_target').text)
        self.float313.value = float(uep.find('.//cell_definition[4]//phenotype//secretion//substrate[2]//uptake_rate').text)
        self.text14.value = uep.find('.//cell_definition[4]//phenotype//secretion//substrate[3]').attrib['name']
        self.float314.value = float(uep.find('.//cell_definition[4]//phenotype//secretion//substrate[3]//secretion_target').text)
        self.float315.value = float(uep.find('.//cell_definition[4]//phenotype//secretion//substrate[3]//uptake_rate').text)
        self.text15.value = uep.find('.//cell_definition[4]//phenotype//secretion//substrate[4]').attrib['name']
        self.float316.value = float(uep.find('.//cell_definition[4]//phenotype//secretion//substrate[4]//secretion_target').text)
        self.float317.value = float(uep.find('.//cell_definition[4]//phenotype//secretion//substrate[4]//uptake_rate').text)
        # ---------  molecular
        # ------------------ cell_definition: neutrophil
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        self.float368.value = float(uep.find('.//cell_definition[5]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        self.float369.value = float(uep.find('.//cell_definition[5]//phenotype//cycle//phase_transition_rates//rate[2]').text)
        self.float370.value = float(uep.find('.//cell_definition[5]//phenotype//cycle//phase_transition_rates//rate[3]').text)
        self.float371.value = float(uep.find('.//cell_definition[5]//phenotype//cycle//phase_transition_rates//rate[4]').text)
        # ---------  death 
        self.float372.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[1]//death_rate').text)
        self.float373.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text)
        self.float374.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text)
        self.float375.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float376.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text)
        self.float377.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//calcification_rate').text)
        self.float378.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//relative_rupture_volume').text)
        self.float379.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[2]//death_rate').text)
        self.float380.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        self.float381.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        self.float382.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float383.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        self.float384.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//calcification_rate').text)
        self.float385.value = float(uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)
        # ---------  volume 
        self.float386.value = float(uep.find('.//cell_definition[5]//phenotype//volume//total').text)
        self.float387.value = float(uep.find('.//cell_definition[5]//phenotype//volume//fluid_fraction').text)
        self.float388.value = float(uep.find('.//cell_definition[5]//phenotype//volume//nuclear').text)
        self.float389.value = float(uep.find('.//cell_definition[5]//phenotype//volume//fluid_change_rate').text)
        self.float390.value = float(uep.find('.//cell_definition[5]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        self.float391.value = float(uep.find('.//cell_definition[5]//phenotype//volume//nuclear_biomass_change_rate').text)
        self.float392.value = float(uep.find('.//cell_definition[5]//phenotype//volume//calcified_fraction').text)
        self.float393.value = float(uep.find('.//cell_definition[5]//phenotype//volume//calcification_rate').text)
        self.float394.value = float(uep.find('.//cell_definition[5]//phenotype//volume//relative_rupture_volume').text)
        # ---------  mechanics 
        self.float395.value = float(uep.find('.//cell_definition[5]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float396.value = float(uep.find('.//cell_definition[5]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float397.value = float(uep.find('.//cell_definition[5]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool20.value = ('true' == (uep.find('.//cell_definition[5]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool21.value = ('true' == (uep.find('.//cell_definition[5]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float400.value = float(uep.find('.//cell_definition[5]//phenotype//motility//speed').text)
        self.float401.value = float(uep.find('.//cell_definition[5]//phenotype//motility//persistence_time').text)
        self.float402.value = float(uep.find('.//cell_definition[5]//phenotype//motility//migration_bias').text)
        self.bool22.value = ('true' == (uep.find('.//cell_definition[5]//phenotype//motility//options//enabled').text.lower()))
        self.bool23.value = ('true' == (uep.find('.//cell_definition[5]//phenotype//motility//options//use_2D').text.lower()))
        self.bool24.value = ('true' == (uep.find('.//cell_definition[5]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate5.value = uep.find('.//cell_definition[5]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction5.value = uep.find('.//cell_definition[5]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text16.value = uep.find('.//cell_definition[5]//phenotype//secretion//substrate[1]').attrib['name']
        self.float403.value = float(uep.find('.//cell_definition[5]//phenotype//secretion//substrate[1]//secretion_target').text)
        self.text17.value = uep.find('.//cell_definition[5]//phenotype//secretion//substrate[2]').attrib['name']
        self.float404.value = float(uep.find('.//cell_definition[5]//phenotype//secretion//substrate[2]//secretion_target').text)
        self.float405.value = float(uep.find('.//cell_definition[5]//phenotype//secretion//substrate[2]//uptake_rate').text)
        self.text18.value = uep.find('.//cell_definition[5]//phenotype//secretion//substrate[3]').attrib['name']
        self.float406.value = float(uep.find('.//cell_definition[5]//phenotype//secretion//substrate[3]//secretion_target').text)
        self.float407.value = float(uep.find('.//cell_definition[5]//phenotype//secretion//substrate[3]//uptake_rate').text)
        self.text19.value = uep.find('.//cell_definition[5]//phenotype//secretion//substrate[4]').attrib['name']
        self.float408.value = float(uep.find('.//cell_definition[5]//phenotype//secretion//substrate[4]//secretion_target').text)
        self.float409.value = float(uep.find('.//cell_definition[5]//phenotype//secretion//substrate[4]//uptake_rate').text)
        # ---------  molecular
        # ------------------ cell_definition: DC
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        self.float460.value = float(uep.find('.//cell_definition[6]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        self.float461.value = float(uep.find('.//cell_definition[6]//phenotype//cycle//phase_transition_rates//rate[2]').text)
        self.float462.value = float(uep.find('.//cell_definition[6]//phenotype//cycle//phase_transition_rates//rate[3]').text)
        self.float463.value = float(uep.find('.//cell_definition[6]//phenotype//cycle//phase_transition_rates//rate[4]').text)
        # ---------  death 
        self.float464.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[1]//death_rate').text)
        self.float465.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text)
        self.float466.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text)
        self.float467.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float468.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text)
        self.float469.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//calcification_rate').text)
        self.float470.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//relative_rupture_volume').text)
        self.float471.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[2]//death_rate').text)
        self.float472.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        self.float473.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        self.float474.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float475.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        self.float476.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//calcification_rate').text)
        self.float477.value = float(uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)
        # ---------  volume 
        self.float478.value = float(uep.find('.//cell_definition[6]//phenotype//volume//total').text)
        self.float479.value = float(uep.find('.//cell_definition[6]//phenotype//volume//fluid_fraction').text)
        self.float480.value = float(uep.find('.//cell_definition[6]//phenotype//volume//nuclear').text)
        self.float481.value = float(uep.find('.//cell_definition[6]//phenotype//volume//fluid_change_rate').text)
        self.float482.value = float(uep.find('.//cell_definition[6]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        self.float483.value = float(uep.find('.//cell_definition[6]//phenotype//volume//nuclear_biomass_change_rate').text)
        self.float484.value = float(uep.find('.//cell_definition[6]//phenotype//volume//calcified_fraction').text)
        self.float485.value = float(uep.find('.//cell_definition[6]//phenotype//volume//calcification_rate').text)
        self.float486.value = float(uep.find('.//cell_definition[6]//phenotype//volume//relative_rupture_volume').text)
        # ---------  mechanics 
        self.float487.value = float(uep.find('.//cell_definition[6]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float488.value = float(uep.find('.//cell_definition[6]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float489.value = float(uep.find('.//cell_definition[6]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool25.value = ('true' == (uep.find('.//cell_definition[6]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool26.value = ('true' == (uep.find('.//cell_definition[6]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float492.value = float(uep.find('.//cell_definition[6]//phenotype//motility//speed').text)
        self.float493.value = float(uep.find('.//cell_definition[6]//phenotype//motility//persistence_time').text)
        self.float494.value = float(uep.find('.//cell_definition[6]//phenotype//motility//migration_bias').text)
        self.bool27.value = ('true' == (uep.find('.//cell_definition[6]//phenotype//motility//options//enabled').text.lower()))
        self.bool28.value = ('true' == (uep.find('.//cell_definition[6]//phenotype//motility//options//use_2D').text.lower()))
        self.bool29.value = ('true' == (uep.find('.//cell_definition[6]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate6.value = uep.find('.//cell_definition[6]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction6.value = uep.find('.//cell_definition[6]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text20.value = uep.find('.//cell_definition[6]//phenotype//secretion//substrate[1]').attrib['name']
        self.float495.value = float(uep.find('.//cell_definition[6]//phenotype//secretion//substrate[1]//secretion_target').text)
        self.text21.value = uep.find('.//cell_definition[6]//phenotype//secretion//substrate[2]').attrib['name']
        self.float496.value = float(uep.find('.//cell_definition[6]//phenotype//secretion//substrate[2]//secretion_target').text)
        self.float497.value = float(uep.find('.//cell_definition[6]//phenotype//secretion//substrate[2]//uptake_rate').text)
        self.text22.value = uep.find('.//cell_definition[6]//phenotype//secretion//substrate[3]').attrib['name']
        self.float498.value = float(uep.find('.//cell_definition[6]//phenotype//secretion//substrate[3]//secretion_target').text)
        self.float499.value = float(uep.find('.//cell_definition[6]//phenotype//secretion//substrate[3]//uptake_rate').text)
        self.text23.value = uep.find('.//cell_definition[6]//phenotype//secretion//substrate[4]').attrib['name']
        self.float500.value = float(uep.find('.//cell_definition[6]//phenotype//secretion//substrate[4]//secretion_target').text)
        self.float501.value = float(uep.find('.//cell_definition[6]//phenotype//secretion//substrate[4]//uptake_rate').text)
        # ---------  molecular
        # ------------------ cell_definition: CD4 Tcell
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        self.float552.value = float(uep.find('.//cell_definition[7]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        self.float553.value = float(uep.find('.//cell_definition[7]//phenotype//cycle//phase_transition_rates//rate[2]').text)
        self.float554.value = float(uep.find('.//cell_definition[7]//phenotype//cycle//phase_transition_rates//rate[3]').text)
        self.float555.value = float(uep.find('.//cell_definition[7]//phenotype//cycle//phase_transition_rates//rate[4]').text)
        # ---------  death 
        self.float556.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[1]//death_rate').text)
        self.float557.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text)
        self.float558.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text)
        self.float559.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float560.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text)
        self.float561.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//calcification_rate').text)
        self.float562.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//relative_rupture_volume').text)
        self.float563.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[2]//death_rate').text)
        self.float564.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        self.float565.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        self.float566.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float567.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        self.float568.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//calcification_rate').text)
        self.float569.value = float(uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)
        # ---------  volume 
        self.float570.value = float(uep.find('.//cell_definition[7]//phenotype//volume//total').text)
        self.float571.value = float(uep.find('.//cell_definition[7]//phenotype//volume//fluid_fraction').text)
        self.float572.value = float(uep.find('.//cell_definition[7]//phenotype//volume//nuclear').text)
        self.float573.value = float(uep.find('.//cell_definition[7]//phenotype//volume//fluid_change_rate').text)
        self.float574.value = float(uep.find('.//cell_definition[7]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        self.float575.value = float(uep.find('.//cell_definition[7]//phenotype//volume//nuclear_biomass_change_rate').text)
        self.float576.value = float(uep.find('.//cell_definition[7]//phenotype//volume//calcified_fraction').text)
        self.float577.value = float(uep.find('.//cell_definition[7]//phenotype//volume//calcification_rate').text)
        self.float578.value = float(uep.find('.//cell_definition[7]//phenotype//volume//relative_rupture_volume').text)
        # ---------  mechanics 
        self.float579.value = float(uep.find('.//cell_definition[7]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float580.value = float(uep.find('.//cell_definition[7]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float581.value = float(uep.find('.//cell_definition[7]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool30.value = ('true' == (uep.find('.//cell_definition[7]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool31.value = ('true' == (uep.find('.//cell_definition[7]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float584.value = float(uep.find('.//cell_definition[7]//phenotype//motility//speed').text)
        self.float585.value = float(uep.find('.//cell_definition[7]//phenotype//motility//persistence_time').text)
        self.float586.value = float(uep.find('.//cell_definition[7]//phenotype//motility//migration_bias').text)
        self.bool32.value = ('true' == (uep.find('.//cell_definition[7]//phenotype//motility//options//enabled').text.lower()))
        self.bool33.value = ('true' == (uep.find('.//cell_definition[7]//phenotype//motility//options//use_2D').text.lower()))
        self.bool34.value = ('true' == (uep.find('.//cell_definition[7]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate7.value = uep.find('.//cell_definition[7]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction7.value = uep.find('.//cell_definition[7]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text24.value = uep.find('.//cell_definition[7]//phenotype//secretion//substrate[1]').attrib['name']
        self.float587.value = float(uep.find('.//cell_definition[7]//phenotype//secretion//substrate[1]//secretion_target').text)
        self.text25.value = uep.find('.//cell_definition[7]//phenotype//secretion//substrate[2]').attrib['name']
        self.float588.value = float(uep.find('.//cell_definition[7]//phenotype//secretion//substrate[2]//secretion_target').text)
        self.float589.value = float(uep.find('.//cell_definition[7]//phenotype//secretion//substrate[2]//uptake_rate').text)
        self.text26.value = uep.find('.//cell_definition[7]//phenotype//secretion//substrate[3]').attrib['name']
        self.float590.value = float(uep.find('.//cell_definition[7]//phenotype//secretion//substrate[3]//secretion_target').text)
        self.float591.value = float(uep.find('.//cell_definition[7]//phenotype//secretion//substrate[3]//uptake_rate').text)
        self.text27.value = uep.find('.//cell_definition[7]//phenotype//secretion//substrate[4]').attrib['name']
        self.float592.value = float(uep.find('.//cell_definition[7]//phenotype//secretion//substrate[4]//secretion_target').text)
        self.float593.value = float(uep.find('.//cell_definition[7]//phenotype//secretion//substrate[4]//uptake_rate').text)
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
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text1.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]//secretion_target').text = str(self.float36.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]//uptake_rate').text = str(self.float37.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text2.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]//secretion_target').text = str(self.float38.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]//uptake_rate').text = str(self.float39.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]').attrib['name'] = str(self.text3.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]//secretion_target').text = str(self.float40.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]//uptake_rate').text = str(self.float41.value)
        # ---------  molecular
        # ------------------ cell_definition: lung epithelium
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float92.value)
        uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[2]').text = str(self.float93.value)
        uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[3]').text = str(self.float94.value)
        uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[4]').text = str(self.float95.value)
        # ---------  death 
        uep.find('.//cell_definition[2]//phenotype//death//model[1]//death_rate').text = str(self.float96.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text = str(self.float97.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text = str(self.float98.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float99.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text = str(self.float100.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//calcification_rate').text = str(self.float101.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[1]//parameters//relative_rupture_volume').text = str(self.float102.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[2]//death_rate').text = str(self.float103.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text = str(self.float104.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text = str(self.float105.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float106.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text = str(self.float107.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//calcification_rate').text = str(self.float108.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[2]//parameters//relative_rupture_volume').text = str(self.float109.value)
        # ---------  volume 
        uep.find('.//cell_definition[2]//phenotype//volume//total').text = str(self.float110.value)
        uep.find('.//cell_definition[2]//phenotype//volume//fluid_fraction').text = str(self.float111.value)
        uep.find('.//cell_definition[2]//phenotype//volume//nuclear').text = str(self.float112.value)
        uep.find('.//cell_definition[2]//phenotype//volume//fluid_change_rate').text = str(self.float113.value)
        uep.find('.//cell_definition[2]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float114.value)
        uep.find('.//cell_definition[2]//phenotype//volume//nuclear_biomass_change_rate').text = str(self.float115.value)
        uep.find('.//cell_definition[2]//phenotype//volume//calcified_fraction').text = str(self.float116.value)
        uep.find('.//cell_definition[2]//phenotype//volume//calcification_rate').text = str(self.float117.value)
        uep.find('.//cell_definition[2]//phenotype//volume//relative_rupture_volume').text = str(self.float118.value)
        # ---------  mechanics 
        uep.find('.//cell_definition[2]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float119.value)
        uep.find('.//cell_definition[2]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float120.value)
        uep.find('.//cell_definition[2]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float121.value)
        uep.find('.//cell_definition[2]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool5.value)
        uep.find('.//cell_definition[2]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool6.value)
        # ---------  motility 
        uep.find('.//cell_definition[2]//phenotype//motility//speed').text = str(self.float124.value)
        uep.find('.//cell_definition[2]//phenotype//motility//persistence_time').text = str(self.float125.value)
        uep.find('.//cell_definition[2]//phenotype//motility//migration_bias').text = str(self.float126.value)
        uep.find('.//cell_definition[2]//phenotype//motility//options//enabled').text = str(self.bool7.value)
        uep.find('.//cell_definition[2]//phenotype//motility//options//use_2D').text = str(self.bool8.value)
        uep.find('.//cell_definition[2]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool9.value)
        uep.find('.//cell_definition[2]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate2.value)
        uep.find('.//cell_definition[2]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction2.value)
        # ---------  secretion 
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text4.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[1]//secretion_target').text = str(self.float127.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text5.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[2]//secretion_target').text = str(self.float128.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[2]//uptake_rate').text = str(self.float129.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text6.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[3]//secretion_target').text = str(self.float130.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[3]//uptake_rate').text = str(self.float131.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[4]').attrib['name'] = str(self.text7.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[4]//secretion_target').text = str(self.float132.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[4]//uptake_rate').text = str(self.float133.value)
        # ---------  molecular
        # ------------------ cell_definition: CD8 Tcell
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float184.value)
        uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[2]').text = str(self.float185.value)
        uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[3]').text = str(self.float186.value)
        uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[4]').text = str(self.float187.value)
        # ---------  death 
        uep.find('.//cell_definition[3]//phenotype//death//model[1]//death_rate').text = str(self.float188.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text = str(self.float189.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text = str(self.float190.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float191.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text = str(self.float192.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//calcification_rate').text = str(self.float193.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[1]//parameters//relative_rupture_volume').text = str(self.float194.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[2]//death_rate').text = str(self.float195.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text = str(self.float196.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text = str(self.float197.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float198.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text = str(self.float199.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//calcification_rate').text = str(self.float200.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[2]//parameters//relative_rupture_volume').text = str(self.float201.value)
        # ---------  volume 
        uep.find('.//cell_definition[3]//phenotype//volume//total').text = str(self.float202.value)
        uep.find('.//cell_definition[3]//phenotype//volume//fluid_fraction').text = str(self.float203.value)
        uep.find('.//cell_definition[3]//phenotype//volume//nuclear').text = str(self.float204.value)
        uep.find('.//cell_definition[3]//phenotype//volume//fluid_change_rate').text = str(self.float205.value)
        uep.find('.//cell_definition[3]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float206.value)
        uep.find('.//cell_definition[3]//phenotype//volume//nuclear_biomass_change_rate').text = str(self.float207.value)
        uep.find('.//cell_definition[3]//phenotype//volume//calcified_fraction').text = str(self.float208.value)
        uep.find('.//cell_definition[3]//phenotype//volume//calcification_rate').text = str(self.float209.value)
        uep.find('.//cell_definition[3]//phenotype//volume//relative_rupture_volume').text = str(self.float210.value)
        # ---------  mechanics 
        uep.find('.//cell_definition[3]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float211.value)
        uep.find('.//cell_definition[3]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float212.value)
        uep.find('.//cell_definition[3]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float213.value)
        uep.find('.//cell_definition[3]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool10.value)
        uep.find('.//cell_definition[3]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool11.value)
        # ---------  motility 
        uep.find('.//cell_definition[3]//phenotype//motility//speed').text = str(self.float216.value)
        uep.find('.//cell_definition[3]//phenotype//motility//persistence_time').text = str(self.float217.value)
        uep.find('.//cell_definition[3]//phenotype//motility//migration_bias').text = str(self.float218.value)
        uep.find('.//cell_definition[3]//phenotype//motility//options//enabled').text = str(self.bool12.value)
        uep.find('.//cell_definition[3]//phenotype//motility//options//use_2D').text = str(self.bool13.value)
        uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool14.value)
        uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate3.value)
        uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction3.value)
        # ---------  secretion 
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text8.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[1]//secretion_target').text = str(self.float219.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text9.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[2]//secretion_target').text = str(self.float220.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[2]//uptake_rate').text = str(self.float221.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text10.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[3]//secretion_target').text = str(self.float222.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[3]//uptake_rate').text = str(self.float223.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[4]').attrib['name'] = str(self.text11.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[4]//secretion_target').text = str(self.float224.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[4]//uptake_rate').text = str(self.float225.value)
        # ---------  molecular
        # ------------------ cell_definition: macrophage
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float276.value)
        uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[2]').text = str(self.float277.value)
        uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[3]').text = str(self.float278.value)
        uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[4]').text = str(self.float279.value)
        # ---------  death 
        uep.find('.//cell_definition[4]//phenotype//death//model[1]//death_rate').text = str(self.float280.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text = str(self.float281.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text = str(self.float282.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float283.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text = str(self.float284.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//calcification_rate').text = str(self.float285.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[1]//parameters//relative_rupture_volume').text = str(self.float286.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[2]//death_rate').text = str(self.float287.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text = str(self.float288.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text = str(self.float289.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float290.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text = str(self.float291.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//calcification_rate').text = str(self.float292.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[2]//parameters//relative_rupture_volume').text = str(self.float293.value)
        # ---------  volume 
        uep.find('.//cell_definition[4]//phenotype//volume//total').text = str(self.float294.value)
        uep.find('.//cell_definition[4]//phenotype//volume//fluid_fraction').text = str(self.float295.value)
        uep.find('.//cell_definition[4]//phenotype//volume//nuclear').text = str(self.float296.value)
        uep.find('.//cell_definition[4]//phenotype//volume//fluid_change_rate').text = str(self.float297.value)
        uep.find('.//cell_definition[4]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float298.value)
        uep.find('.//cell_definition[4]//phenotype//volume//nuclear_biomass_change_rate').text = str(self.float299.value)
        uep.find('.//cell_definition[4]//phenotype//volume//calcified_fraction').text = str(self.float300.value)
        uep.find('.//cell_definition[4]//phenotype//volume//calcification_rate').text = str(self.float301.value)
        uep.find('.//cell_definition[4]//phenotype//volume//relative_rupture_volume').text = str(self.float302.value)
        # ---------  mechanics 
        uep.find('.//cell_definition[4]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float303.value)
        uep.find('.//cell_definition[4]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float304.value)
        uep.find('.//cell_definition[4]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float305.value)
        uep.find('.//cell_definition[4]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool15.value)
        uep.find('.//cell_definition[4]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool16.value)
        # ---------  motility 
        uep.find('.//cell_definition[4]//phenotype//motility//speed').text = str(self.float308.value)
        uep.find('.//cell_definition[4]//phenotype//motility//persistence_time').text = str(self.float309.value)
        uep.find('.//cell_definition[4]//phenotype//motility//migration_bias').text = str(self.float310.value)
        uep.find('.//cell_definition[4]//phenotype//motility//options//enabled').text = str(self.bool17.value)
        uep.find('.//cell_definition[4]//phenotype//motility//options//use_2D').text = str(self.bool18.value)
        uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool19.value)
        uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate4.value)
        uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction4.value)
        # ---------  secretion 
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text12.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[1]//secretion_target').text = str(self.float311.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text13.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[2]//secretion_target').text = str(self.float312.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[2]//uptake_rate').text = str(self.float313.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text14.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[3]//secretion_target').text = str(self.float314.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[3]//uptake_rate').text = str(self.float315.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[4]').attrib['name'] = str(self.text15.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[4]//secretion_target').text = str(self.float316.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[4]//uptake_rate').text = str(self.float317.value)
        # ---------  molecular
        # ------------------ cell_definition: neutrophil
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        uep.find('.//cell_definition[5]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float368.value)
        uep.find('.//cell_definition[5]//phenotype//cycle//phase_transition_rates//rate[2]').text = str(self.float369.value)
        uep.find('.//cell_definition[5]//phenotype//cycle//phase_transition_rates//rate[3]').text = str(self.float370.value)
        uep.find('.//cell_definition[5]//phenotype//cycle//phase_transition_rates//rate[4]').text = str(self.float371.value)
        # ---------  death 
        uep.find('.//cell_definition[5]//phenotype//death//model[1]//death_rate').text = str(self.float372.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text = str(self.float373.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text = str(self.float374.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float375.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text = str(self.float376.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//calcification_rate').text = str(self.float377.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[1]//parameters//relative_rupture_volume').text = str(self.float378.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[2]//death_rate').text = str(self.float379.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text = str(self.float380.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text = str(self.float381.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float382.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text = str(self.float383.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//calcification_rate').text = str(self.float384.value)
        uep.find('.//cell_definition[5]//phenotype//death//model[2]//parameters//relative_rupture_volume').text = str(self.float385.value)
        # ---------  volume 
        uep.find('.//cell_definition[5]//phenotype//volume//total').text = str(self.float386.value)
        uep.find('.//cell_definition[5]//phenotype//volume//fluid_fraction').text = str(self.float387.value)
        uep.find('.//cell_definition[5]//phenotype//volume//nuclear').text = str(self.float388.value)
        uep.find('.//cell_definition[5]//phenotype//volume//fluid_change_rate').text = str(self.float389.value)
        uep.find('.//cell_definition[5]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float390.value)
        uep.find('.//cell_definition[5]//phenotype//volume//nuclear_biomass_change_rate').text = str(self.float391.value)
        uep.find('.//cell_definition[5]//phenotype//volume//calcified_fraction').text = str(self.float392.value)
        uep.find('.//cell_definition[5]//phenotype//volume//calcification_rate').text = str(self.float393.value)
        uep.find('.//cell_definition[5]//phenotype//volume//relative_rupture_volume').text = str(self.float394.value)
        # ---------  mechanics 
        uep.find('.//cell_definition[5]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float395.value)
        uep.find('.//cell_definition[5]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float396.value)
        uep.find('.//cell_definition[5]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float397.value)
        uep.find('.//cell_definition[5]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool20.value)
        uep.find('.//cell_definition[5]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool21.value)
        # ---------  motility 
        uep.find('.//cell_definition[5]//phenotype//motility//speed').text = str(self.float400.value)
        uep.find('.//cell_definition[5]//phenotype//motility//persistence_time').text = str(self.float401.value)
        uep.find('.//cell_definition[5]//phenotype//motility//migration_bias').text = str(self.float402.value)
        uep.find('.//cell_definition[5]//phenotype//motility//options//enabled').text = str(self.bool22.value)
        uep.find('.//cell_definition[5]//phenotype//motility//options//use_2D').text = str(self.bool23.value)
        uep.find('.//cell_definition[5]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool24.value)
        uep.find('.//cell_definition[5]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate5.value)
        uep.find('.//cell_definition[5]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction5.value)
        # ---------  secretion 
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text16.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[1]//secretion_target').text = str(self.float403.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text17.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[2]//secretion_target').text = str(self.float404.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[2]//uptake_rate').text = str(self.float405.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text18.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[3]//secretion_target').text = str(self.float406.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[3]//uptake_rate').text = str(self.float407.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[4]').attrib['name'] = str(self.text19.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[4]//secretion_target').text = str(self.float408.value)
        uep.find('.//cell_definition[5]//phenotype//secretion//substrate[4]//uptake_rate').text = str(self.float409.value)
        # ---------  molecular
        # ------------------ cell_definition: DC
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        uep.find('.//cell_definition[6]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float460.value)
        uep.find('.//cell_definition[6]//phenotype//cycle//phase_transition_rates//rate[2]').text = str(self.float461.value)
        uep.find('.//cell_definition[6]//phenotype//cycle//phase_transition_rates//rate[3]').text = str(self.float462.value)
        uep.find('.//cell_definition[6]//phenotype//cycle//phase_transition_rates//rate[4]').text = str(self.float463.value)
        # ---------  death 
        uep.find('.//cell_definition[6]//phenotype//death//model[1]//death_rate').text = str(self.float464.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text = str(self.float465.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text = str(self.float466.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float467.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text = str(self.float468.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//calcification_rate').text = str(self.float469.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[1]//parameters//relative_rupture_volume').text = str(self.float470.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[2]//death_rate').text = str(self.float471.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text = str(self.float472.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text = str(self.float473.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float474.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text = str(self.float475.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//calcification_rate').text = str(self.float476.value)
        uep.find('.//cell_definition[6]//phenotype//death//model[2]//parameters//relative_rupture_volume').text = str(self.float477.value)
        # ---------  volume 
        uep.find('.//cell_definition[6]//phenotype//volume//total').text = str(self.float478.value)
        uep.find('.//cell_definition[6]//phenotype//volume//fluid_fraction').text = str(self.float479.value)
        uep.find('.//cell_definition[6]//phenotype//volume//nuclear').text = str(self.float480.value)
        uep.find('.//cell_definition[6]//phenotype//volume//fluid_change_rate').text = str(self.float481.value)
        uep.find('.//cell_definition[6]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float482.value)
        uep.find('.//cell_definition[6]//phenotype//volume//nuclear_biomass_change_rate').text = str(self.float483.value)
        uep.find('.//cell_definition[6]//phenotype//volume//calcified_fraction').text = str(self.float484.value)
        uep.find('.//cell_definition[6]//phenotype//volume//calcification_rate').text = str(self.float485.value)
        uep.find('.//cell_definition[6]//phenotype//volume//relative_rupture_volume').text = str(self.float486.value)
        # ---------  mechanics 
        uep.find('.//cell_definition[6]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float487.value)
        uep.find('.//cell_definition[6]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float488.value)
        uep.find('.//cell_definition[6]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float489.value)
        uep.find('.//cell_definition[6]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool25.value)
        uep.find('.//cell_definition[6]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool26.value)
        # ---------  motility 
        uep.find('.//cell_definition[6]//phenotype//motility//speed').text = str(self.float492.value)
        uep.find('.//cell_definition[6]//phenotype//motility//persistence_time').text = str(self.float493.value)
        uep.find('.//cell_definition[6]//phenotype//motility//migration_bias').text = str(self.float494.value)
        uep.find('.//cell_definition[6]//phenotype//motility//options//enabled').text = str(self.bool27.value)
        uep.find('.//cell_definition[6]//phenotype//motility//options//use_2D').text = str(self.bool28.value)
        uep.find('.//cell_definition[6]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool29.value)
        uep.find('.//cell_definition[6]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate6.value)
        uep.find('.//cell_definition[6]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction6.value)
        # ---------  secretion 
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text20.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[1]//secretion_target').text = str(self.float495.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text21.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[2]//secretion_target').text = str(self.float496.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[2]//uptake_rate').text = str(self.float497.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text22.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[3]//secretion_target').text = str(self.float498.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[3]//uptake_rate').text = str(self.float499.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[4]').attrib['name'] = str(self.text23.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[4]//secretion_target').text = str(self.float500.value)
        uep.find('.//cell_definition[6]//phenotype//secretion//substrate[4]//uptake_rate').text = str(self.float501.value)
        # ---------  molecular
        # ------------------ cell_definition: CD4 Tcell
        # ---------  cycle (flow_cytometry_separated_cycle_model)
        uep.find('.//cell_definition[7]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float552.value)
        uep.find('.//cell_definition[7]//phenotype//cycle//phase_transition_rates//rate[2]').text = str(self.float553.value)
        uep.find('.//cell_definition[7]//phenotype//cycle//phase_transition_rates//rate[3]').text = str(self.float554.value)
        uep.find('.//cell_definition[7]//phenotype//cycle//phase_transition_rates//rate[4]').text = str(self.float555.value)
        # ---------  death 
        uep.find('.//cell_definition[7]//phenotype//death//model[1]//death_rate').text = str(self.float556.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text = str(self.float557.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text = str(self.float558.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float559.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text = str(self.float560.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//calcification_rate').text = str(self.float561.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[1]//parameters//relative_rupture_volume').text = str(self.float562.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[2]//death_rate').text = str(self.float563.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text = str(self.float564.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text = str(self.float565.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float566.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text = str(self.float567.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//calcification_rate').text = str(self.float568.value)
        uep.find('.//cell_definition[7]//phenotype//death//model[2]//parameters//relative_rupture_volume').text = str(self.float569.value)
        # ---------  volume 
        uep.find('.//cell_definition[7]//phenotype//volume//total').text = str(self.float570.value)
        uep.find('.//cell_definition[7]//phenotype//volume//fluid_fraction').text = str(self.float571.value)
        uep.find('.//cell_definition[7]//phenotype//volume//nuclear').text = str(self.float572.value)
        uep.find('.//cell_definition[7]//phenotype//volume//fluid_change_rate').text = str(self.float573.value)
        uep.find('.//cell_definition[7]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float574.value)
        uep.find('.//cell_definition[7]//phenotype//volume//nuclear_biomass_change_rate').text = str(self.float575.value)
        uep.find('.//cell_definition[7]//phenotype//volume//calcified_fraction').text = str(self.float576.value)
        uep.find('.//cell_definition[7]//phenotype//volume//calcification_rate').text = str(self.float577.value)
        uep.find('.//cell_definition[7]//phenotype//volume//relative_rupture_volume').text = str(self.float578.value)
        # ---------  mechanics 
        uep.find('.//cell_definition[7]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float579.value)
        uep.find('.//cell_definition[7]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float580.value)
        uep.find('.//cell_definition[7]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float581.value)
        uep.find('.//cell_definition[7]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool30.value)
        uep.find('.//cell_definition[7]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool31.value)
        # ---------  motility 
        uep.find('.//cell_definition[7]//phenotype//motility//speed').text = str(self.float584.value)
        uep.find('.//cell_definition[7]//phenotype//motility//persistence_time').text = str(self.float585.value)
        uep.find('.//cell_definition[7]//phenotype//motility//migration_bias').text = str(self.float586.value)
        uep.find('.//cell_definition[7]//phenotype//motility//options//enabled').text = str(self.bool32.value)
        uep.find('.//cell_definition[7]//phenotype//motility//options//use_2D').text = str(self.bool33.value)
        uep.find('.//cell_definition[7]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool34.value)
        uep.find('.//cell_definition[7]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate7.value)
        uep.find('.//cell_definition[7]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction7.value)
        # ---------  secretion 
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text24.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[1]//secretion_target').text = str(self.float587.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text25.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[2]//secretion_target').text = str(self.float588.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[2]//uptake_rate').text = str(self.float589.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text26.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[3]//secretion_target').text = str(self.float590.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[3]//uptake_rate').text = str(self.float591.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[4]').attrib['name'] = str(self.text27.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[4]//secretion_target').text = str(self.float592.value)
        uep.find('.//cell_definition[7]//phenotype//secretion//substrate[4]//uptake_rate').text = str(self.float593.value)
        # ---------  molecular
