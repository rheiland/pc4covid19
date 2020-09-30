 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

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
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}

        param_name1 = Button(description='random_seed', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.random_seed = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        div_row1 = Button(description='--Immune activation parameters--', disabled=True, layout=divider_button_layout)

        param_name2 = Button(description='immune_dt', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.immune_dt = FloatText(
          value=10,
          step=1,
          style=style, layout=widget_layout)

        param_name3 = Button(description='immune_z_offset', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.immune_z_offset = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name4 = Button(description='macrophage_max_recruitment_rate', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.macrophage_max_recruitment_rate = FloatText(
          value=4e-9,
          step=1e-09,
          style=style, layout=widget_layout)

        param_name5 = Button(description='macrophage_recruitment_min_signal', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.macrophage_recruitment_min_signal = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name6 = Button(description='macrophage_recruitment_saturation_signal', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.macrophage_recruitment_saturation_signal = FloatText(
          value=0.3,
          step=0.01,
          style=style, layout=widget_layout)

        param_name7 = Button(description='neutrophil_max_recruitment_rate', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.neutrophil_max_recruitment_rate = FloatText(
          value=4e-9,
          step=1e-09,
          style=style, layout=widget_layout)

        param_name8 = Button(description='neutrophil_recruitment_min_signal', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.neutrophil_recruitment_min_signal = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name9 = Button(description='neutrophil_recruitment_saturation_signal', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.neutrophil_recruitment_saturation_signal = FloatText(
          value=0.3,
          step=0.01,
          style=style, layout=widget_layout)

        param_name10 = Button(description='CD8_Tcell_max_recruitment_rate', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.CD8_Tcell_max_recruitment_rate = FloatText(
          value=4e-9,
          step=1e-09,
          style=style, layout=widget_layout)

        param_name11 = Button(description='CD8_Tcell_recruitment_min_signal', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.CD8_Tcell_recruitment_min_signal = FloatText(
          value=0.4,
          step=0.1,
          style=style, layout=widget_layout)

        param_name12 = Button(description='CD8_Tcell_recruitment_saturation_signal', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.CD8_Tcell_recruitment_saturation_signal = FloatText(
          value=0.7,
          step=0.1,
          style=style, layout=widget_layout)

        div_row2 = Button(description='---Initialization Options--', disabled=True, layout=divider_button_layout)

        param_name13 = Button(description='multiplicity_of_infection', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.multiplicity_of_infection = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name14 = Button(description='use_single_infected_cell', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'tan'

        self.use_single_infected_cell = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name15 = Button(description='number_of_CD8_Tcells', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'lightgreen'

        self.number_of_CD8_Tcells = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name16 = Button(description='number_of_macrophages', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'tan'

        self.number_of_macrophages = IntText(
          value=50,
          step=1,
          style=style, layout=widget_layout)

        param_name17 = Button(description='number_of_neutrophils', disabled=True, layout=name_button_layout)
        param_name17.style.button_color = 'lightgreen'

        self.number_of_neutrophils = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name18 = Button(description='number_of_DCs', disabled=True, layout=name_button_layout)
        param_name18.style.button_color = 'tan'

        self.number_of_DCs = IntText(
          value=28,
          step=1,
          style=style, layout=widget_layout)

        param_name19 = Button(description='number_of_CD4_Tcells', disabled=True, layout=name_button_layout)
        param_name19.style.button_color = 'lightgreen'

        self.number_of_CD4_Tcells = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name20 = Button(description='DC_induced_CD8_proliferation', disabled=True, layout=name_button_layout)
        param_name20.style.button_color = 'tan'

        self.DC_induced_CD8_proliferation = FloatText(
          value=0.00208,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name21 = Button(description='DC_induced_CD8_attachment', disabled=True, layout=name_button_layout)
        param_name21.style.button_color = 'lightgreen'

        self.DC_induced_CD8_attachment = FloatText(
          value=0.6,
          step=0.1,
          style=style, layout=widget_layout)

        param_name22 = Button(description='departure_rate_of_DCs', disabled=True, layout=name_button_layout)
        param_name22.style.button_color = 'tan'

        self.departure_rate_of_DCs = FloatText(
          value=0.001,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name23 = Button(description='virions_needed_for_DC_activation', disabled=True, layout=name_button_layout)
        param_name23.style.button_color = 'lightgreen'

        self.virions_needed_for_DC_activation = IntText(
          value=10,
          step=1,
          style=style, layout=widget_layout)

        param_name24 = Button(description='epsilon_distance', disabled=True, layout=name_button_layout)
        param_name24.style.button_color = 'tan'

        self.epsilon_distance = FloatText(
          value=1.75,
          step=0.1,
          style=style, layout=widget_layout)

        param_name25 = Button(description='perecentage_tissue_vascularized', disabled=True, layout=name_button_layout)
        param_name25.style.button_color = 'lightgreen'

        self.perecentage_tissue_vascularized = FloatText(
          value=8.8,
          step=0.1,
          style=style, layout=widget_layout)

        div_row3 = Button(description='---Cell Color Options--', disabled=True, layout=divider_button_layout)

        param_name26 = Button(description='color_variable', disabled=True, layout=name_button_layout)
        param_name26.style.button_color = 'tan'

        self.color_variable = Text(
          value='assembled_virion',
          style=style, layout=widget_layout)

        param_name27 = Button(description='epithelial_opacity', disabled=True, layout=name_button_layout)
        param_name27.style.button_color = 'lightgreen'

        self.epithelial_opacity = FloatText(
          value=0.65,
          step=0.1,
          style=style, layout=widget_layout)

        param_name28 = Button(description='non_epithelial_opacity', disabled=True, layout=name_button_layout)
        param_name28.style.button_color = 'tan'

        self.non_epithelial_opacity = FloatText(
          value=0.8,
          step=0.1,
          style=style, layout=widget_layout)

        param_name29 = Button(description='apoptotic_epithelium_color', disabled=True, layout=name_button_layout)
        param_name29.style.button_color = 'lightgreen'

        self.apoptotic_epithelium_color = Text(
          value='black',
          style=style, layout=widget_layout)

        param_name30 = Button(description='apoptotic_immune_color', disabled=True, layout=name_button_layout)
        param_name30.style.button_color = 'tan'

        self.apoptotic_immune_color = Text(
          value='rosybrown',
          style=style, layout=widget_layout)

        param_name31 = Button(description='CD8_Tcell_color', disabled=True, layout=name_button_layout)
        param_name31.style.button_color = 'lightgreen'

        self.CD8_Tcell_color = Text(
          value='red',
          style=style, layout=widget_layout)

        param_name32 = Button(description='CD4_Tcell_color', disabled=True, layout=name_button_layout)
        param_name32.style.button_color = 'tan'

        self.CD4_Tcell_color = Text(
          value='orange',
          style=style, layout=widget_layout)

        param_name33 = Button(description='Macrophage_color', disabled=True, layout=name_button_layout)
        param_name33.style.button_color = 'lightgreen'

        self.Macrophage_color = Text(
          value='rgb(35,139,69)',
          style=style, layout=widget_layout)

        param_name34 = Button(description='activated_macrophage_color', disabled=True, layout=name_button_layout)
        param_name34.style.button_color = 'tan'

        self.activated_macrophage_color = Text(
          value='lime',
          style=style, layout=widget_layout)

        param_name35 = Button(description='exhausted_macrophage_color', disabled=True, layout=name_button_layout)
        param_name35.style.button_color = 'lightgreen'

        self.exhausted_macrophage_color = Text(
          value='rgb(116,196,118)',
          style=style, layout=widget_layout)

        param_name36 = Button(description='hyperactivated_macrophage_color', disabled=True, layout=name_button_layout)
        param_name36.style.button_color = 'tan'

        self.hyperactivated_macrophage_color = Text(
          value='rgb(168,221,181)',
          style=style, layout=widget_layout)

        param_name37 = Button(description='Neutrophil_color', disabled=True, layout=name_button_layout)
        param_name37.style.button_color = 'lightgreen'

        self.Neutrophil_color = Text(
          value='cyan',
          style=style, layout=widget_layout)

        param_name38 = Button(description='DC_color', disabled=True, layout=name_button_layout)
        param_name38.style.button_color = 'tan'

        self.DC_color = Text(
          value='rgb(129,15,124)',
          style=style, layout=widget_layout)

        param_name39 = Button(description='activated_DC_color', disabled=True, layout=name_button_layout)
        param_name39.style.button_color = 'lightgreen'

        self.activated_DC_color = Text(
          value='deeppink',
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'lightgreen'
        units_button3 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'tan'
        units_button4 = Button(description='micron', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'lightgreen'
        units_button5 = Button(description='cells/min/micron^3', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'tan'
        units_button6 = Button(description='substrate/micron^3', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'lightgreen'
        units_button7 = Button(description='substrate/micron^3', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'tan'
        units_button8 = Button(description='cells/min/micron^3', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'lightgreen'
        units_button9 = Button(description='substrate/micron^3', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'tan'
        units_button10 = Button(description='substrate/micron^3', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'lightgreen'
        units_button11 = Button(description='cells/min/micron^3', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'tan'
        units_button12 = Button(description='substrate/micron^3', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'lightgreen'
        units_button13 = Button(description='substrate/micron^3', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'tan'
        units_button14 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'
        units_button15 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'lightgreen'
        units_button16 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'tan'
        units_button17 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button17.style.button_color = 'lightgreen'
        units_button18 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button18.style.button_color = 'tan'
        units_button19 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button19.style.button_color = 'lightgreen'
        units_button20 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button20.style.button_color = 'tan'
        units_button21 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button21.style.button_color = 'lightgreen'
        units_button22 = Button(description='cells/min/micron^3', disabled=True, layout=units_button_layout) 
        units_button22.style.button_color = 'tan'
        units_button23 = Button(description='cells/min/micron^3', disabled=True, layout=units_button_layout) 
        units_button23.style.button_color = 'lightgreen'
        units_button24 = Button(description='cells/min/micron^3', disabled=True, layout=units_button_layout) 
        units_button24.style.button_color = 'tan'
        units_button25 = Button(description='virions', disabled=True, layout=units_button_layout) 
        units_button25.style.button_color = 'lightgreen'
        units_button26 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button26.style.button_color = 'tan'
        units_button27 = Button(description='percentage', disabled=True, layout=units_button_layout) 
        units_button27.style.button_color = 'lightgreen'
        units_button28 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button28.style.button_color = 'lightgreen'
        units_button29 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button29.style.button_color = 'tan'
        units_button30 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button30.style.button_color = 'lightgreen'
        units_button31 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button31.style.button_color = 'tan'
        units_button32 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button32.style.button_color = 'lightgreen'
        units_button33 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button33.style.button_color = 'tan'
        units_button34 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button34.style.button_color = 'lightgreen'
        units_button35 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button35.style.button_color = 'tan'
        units_button36 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button36.style.button_color = 'lightgreen'
        units_button37 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button37.style.button_color = 'tan'
        units_button38 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button38.style.button_color = 'lightgreen'
        units_button39 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button39.style.button_color = 'tan'
        units_button40 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button40.style.button_color = 'lightgreen'
        units_button41 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button41.style.button_color = 'tan'
        units_button42 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button42.style.button_color = 'lightgreen'

        desc_button1 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='how often we check to introduce immune cells' , tooltip='how often we check to introduce immune cells', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='immune cell position over the epithelium' , tooltip='immune cell position over the epithelium', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='max macrophage recruitment rate (for saturated signal)' , tooltip='max macrophage recruitment rate (for saturated signal)', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='min concentration to attract macrophages' , tooltip='min concentration to attract macrophages', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='saturating concentration to attract macrophages' , tooltip='saturating concentration to attract macrophages', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='max neutrophil recruitment rate (for saturated signal)' , tooltip='max neutrophil recruitment rate (for saturated signal)', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='min concentration to attract neutrophils' , tooltip='min concentration to attract neutrophils', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='saturating concentration to attract neutrophils' , tooltip='saturating concentration to attract neutrophils', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='max CD8 T cell recruitment rate (for saturated signal)' , tooltip='max CD8 T cell recruitment rate (for saturated signal)', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='min concentration to attract CD8 T cells' , tooltip='min concentration to attract CD8 T cells', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='saturating concentration to attract CD8 T cells' , tooltip='saturating concentration to attract CD8 T cells', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='multiplicity of infection: virions/cells at t=0' , tooltip='multiplicity of infection: virions/cells at t=0', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='Infect center cell with one virion (overrides MOI)' , tooltip='Infect center cell with one virion (overrides MOI)', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button15 = Button(description='initial number of CD8 T cells in tissue' , tooltip='initial number of CD8 T cells in tissue', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'
        desc_button16 = Button(description='initial number of macrophages' , tooltip='initial number of macrophages', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'
        desc_button17 = Button(description='initial number of neutrophils' , tooltip='initial number of neutrophils', disabled=True, layout=desc_button_layout) 
        desc_button17.style.button_color = 'lightgreen'
        desc_button18 = Button(description='initial number of Dendritic Cells' , tooltip='initial number of Dendritic Cells', disabled=True, layout=desc_button_layout) 
        desc_button18.style.button_color = 'tan'
        desc_button19 = Button(description='initial number of CD4 Tcells in tissue' , tooltip='initial number of CD4 Tcells in tissue', disabled=True, layout=desc_button_layout) 
        desc_button19.style.button_color = 'lightgreen'
        desc_button20 = Button(description='DC induced CD8 proliferation rate' , tooltip='DC induced CD8 proliferation rate', disabled=True, layout=desc_button_layout) 
        desc_button20.style.button_color = 'tan'
        desc_button21 = Button(description='DC induced CD8 attachement rate' , tooltip='DC induced CD8 attachement rate', disabled=True, layout=desc_button_layout) 
        desc_button21.style.button_color = 'lightgreen'
        desc_button22 = Button(description='Departure rate of activated DCs' , tooltip='Departure rate of activated DCs', disabled=True, layout=desc_button_layout) 
        desc_button22.style.button_color = 'tan'
        desc_button23 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button23.style.button_color = 'lightgreen'
        desc_button24 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button24.style.button_color = 'tan'
        desc_button25 = Button(description='percentage of tissue sitting above blood vessels' , tooltip='percentage of tissue sitting above blood vessels', disabled=True, layout=desc_button_layout) 
        desc_button25.style.button_color = 'lightgreen'
        desc_button26 = Button(description='color cells based on this variable' , tooltip='color cells based on this variable', disabled=True, layout=desc_button_layout) 
        desc_button26.style.button_color = 'tan'
        desc_button27 = Button(description='opacity of epithelial cells' , tooltip='opacity of epithelial cells', disabled=True, layout=desc_button_layout) 
        desc_button27.style.button_color = 'lightgreen'
        desc_button28 = Button(description='opacity of non-epithelial cells' , tooltip='opacity of non-epithelial cells', disabled=True, layout=desc_button_layout) 
        desc_button28.style.button_color = 'tan'
        desc_button29 = Button(description='apoptotic epithelial cell color' , tooltip='apoptotic epithelial cell color', disabled=True, layout=desc_button_layout) 
        desc_button29.style.button_color = 'lightgreen'
        desc_button30 = Button(description='apoptotic immune cell color' , tooltip='apoptotic immune cell color', disabled=True, layout=desc_button_layout) 
        desc_button30.style.button_color = 'tan'
        desc_button31 = Button(description='CD8 T cell color' , tooltip='CD8 T cell color', disabled=True, layout=desc_button_layout) 
        desc_button31.style.button_color = 'lightgreen'
        desc_button32 = Button(description='CD8 T cell color' , tooltip='CD8 T cell color', disabled=True, layout=desc_button_layout) 
        desc_button32.style.button_color = 'tan'
        desc_button33 = Button(description='macrophage color' , tooltip='macrophage color', disabled=True, layout=desc_button_layout) 
        desc_button33.style.button_color = 'lightgreen'
        desc_button34 = Button(description='color of activated macrophage' , tooltip='color of activated macrophage', disabled=True, layout=desc_button_layout) 
        desc_button34.style.button_color = 'tan'
        desc_button35 = Button(description='color of exhausted macrophage' , tooltip='color of exhausted macrophage', disabled=True, layout=desc_button_layout) 
        desc_button35.style.button_color = 'lightgreen'
        desc_button36 = Button(description='color of hyperactivated macrophage' , tooltip='color of hyperactivated macrophage', disabled=True, layout=desc_button_layout) 
        desc_button36.style.button_color = 'tan'
        desc_button37 = Button(description='neutrophil color' , tooltip='neutrophil color', disabled=True, layout=desc_button_layout) 
        desc_button37.style.button_color = 'lightgreen'
        desc_button38 = Button(description='DC color' , tooltip='DC color', disabled=True, layout=desc_button_layout) 
        desc_button38.style.button_color = 'tan'
        desc_button39 = Button(description='DC color' , tooltip='DC color', disabled=True, layout=desc_button_layout) 
        desc_button39.style.button_color = 'lightgreen'

        row1 = [param_name1, self.random_seed, units_button1, desc_button1] 
        row2 = [param_name2, self.immune_dt, units_button3, desc_button2] 
        row3 = [param_name3, self.immune_z_offset, units_button4, desc_button3] 
        row4 = [param_name4, self.macrophage_max_recruitment_rate, units_button5, desc_button4] 
        row5 = [param_name5, self.macrophage_recruitment_min_signal, units_button6, desc_button5] 
        row6 = [param_name6, self.macrophage_recruitment_saturation_signal, units_button7, desc_button6] 
        row7 = [param_name7, self.neutrophil_max_recruitment_rate, units_button8, desc_button7] 
        row8 = [param_name8, self.neutrophil_recruitment_min_signal, units_button9, desc_button8] 
        row9 = [param_name9, self.neutrophil_recruitment_saturation_signal, units_button10, desc_button9] 
        row10 = [param_name10, self.CD8_Tcell_max_recruitment_rate, units_button11, desc_button10] 
        row11 = [param_name11, self.CD8_Tcell_recruitment_min_signal, units_button12, desc_button11] 
        row12 = [param_name12, self.CD8_Tcell_recruitment_saturation_signal, units_button13, desc_button12] 
        row13 = [param_name13, self.multiplicity_of_infection, units_button15, desc_button13] 
        row14 = [param_name14, self.use_single_infected_cell, units_button16, desc_button14] 
        row15 = [param_name15, self.number_of_CD8_Tcells, units_button17, desc_button15] 
        row16 = [param_name16, self.number_of_macrophages, units_button18, desc_button16] 
        row17 = [param_name17, self.number_of_neutrophils, units_button19, desc_button17] 
        row18 = [param_name18, self.number_of_DCs, units_button20, desc_button18] 
        row19 = [param_name19, self.number_of_CD4_Tcells, units_button21, desc_button19] 
        row20 = [param_name20, self.DC_induced_CD8_proliferation, units_button22, desc_button20] 
        row21 = [param_name21, self.DC_induced_CD8_attachment, units_button23, desc_button21] 
        row22 = [param_name22, self.departure_rate_of_DCs, units_button24, desc_button22] 
        row23 = [param_name23, self.virions_needed_for_DC_activation, units_button25, desc_button23] 
        row24 = [param_name24, self.epsilon_distance, units_button26, desc_button24] 
        row25 = [param_name25, self.perecentage_tissue_vascularized, units_button27, desc_button25] 
        row26 = [param_name26, self.color_variable, units_button29, desc_button26] 
        row27 = [param_name27, self.epithelial_opacity, units_button30, desc_button27] 
        row28 = [param_name28, self.non_epithelial_opacity, units_button31, desc_button28] 
        row29 = [param_name29, self.apoptotic_epithelium_color, units_button32, desc_button29] 
        row30 = [param_name30, self.apoptotic_immune_color, units_button33, desc_button30] 
        row31 = [param_name31, self.CD8_Tcell_color, units_button34, desc_button31] 
        row32 = [param_name32, self.CD4_Tcell_color, units_button35, desc_button32] 
        row33 = [param_name33, self.Macrophage_color, units_button36, desc_button33] 
        row34 = [param_name34, self.activated_macrophage_color, units_button37, desc_button34] 
        row35 = [param_name35, self.exhausted_macrophage_color, units_button38, desc_button35] 
        row36 = [param_name36, self.hyperactivated_macrophage_color, units_button39, desc_button36] 
        row37 = [param_name37, self.Neutrophil_color, units_button40, desc_button37] 
        row38 = [param_name38, self.DC_color, units_button41, desc_button38] 
        row39 = [param_name39, self.activated_DC_color, units_button42, desc_button39] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)
        box19 = Box(children=row19, layout=box_layout)
        box20 = Box(children=row20, layout=box_layout)
        box21 = Box(children=row21, layout=box_layout)
        box22 = Box(children=row22, layout=box_layout)
        box23 = Box(children=row23, layout=box_layout)
        box24 = Box(children=row24, layout=box_layout)
        box25 = Box(children=row25, layout=box_layout)
        box26 = Box(children=row26, layout=box_layout)
        box27 = Box(children=row27, layout=box_layout)
        box28 = Box(children=row28, layout=box_layout)
        box29 = Box(children=row29, layout=box_layout)
        box30 = Box(children=row30, layout=box_layout)
        box31 = Box(children=row31, layout=box_layout)
        box32 = Box(children=row32, layout=box_layout)
        box33 = Box(children=row33, layout=box_layout)
        box34 = Box(children=row34, layout=box_layout)
        box35 = Box(children=row35, layout=box_layout)
        box36 = Box(children=row36, layout=box_layout)
        box37 = Box(children=row37, layout=box_layout)
        box38 = Box(children=row38, layout=box_layout)
        box39 = Box(children=row39, layout=box_layout)

        self.tab = VBox([
          box1,
          div_row1,
          box2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          box11,
          box12,
          div_row2,
          box13,
          box14,
          box15,
          box16,
          box17,
          box18,
          box19,
          box20,
          box21,
          box22,
          box23,
          box24,
          box25,
          div_row3,
          box26,
          box27,
          box28,
          box29,
          box30,
          box31,
          box32,
          box33,
          box34,
          box35,
          box36,
          box37,
          box38,
          box39,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.random_seed.value = int(uep.find('.//random_seed').text)
        self.immune_dt.value = float(uep.find('.//immune_dt').text)
        self.immune_z_offset.value = float(uep.find('.//immune_z_offset').text)
        self.macrophage_max_recruitment_rate.value = float(uep.find('.//macrophage_max_recruitment_rate').text)
        self.macrophage_recruitment_min_signal.value = float(uep.find('.//macrophage_recruitment_min_signal').text)
        self.macrophage_recruitment_saturation_signal.value = float(uep.find('.//macrophage_recruitment_saturation_signal').text)
        self.neutrophil_max_recruitment_rate.value = float(uep.find('.//neutrophil_max_recruitment_rate').text)
        self.neutrophil_recruitment_min_signal.value = float(uep.find('.//neutrophil_recruitment_min_signal').text)
        self.neutrophil_recruitment_saturation_signal.value = float(uep.find('.//neutrophil_recruitment_saturation_signal').text)
        self.CD8_Tcell_max_recruitment_rate.value = float(uep.find('.//CD8_Tcell_max_recruitment_rate').text)
        self.CD8_Tcell_recruitment_min_signal.value = float(uep.find('.//CD8_Tcell_recruitment_min_signal').text)
        self.CD8_Tcell_recruitment_saturation_signal.value = float(uep.find('.//CD8_Tcell_recruitment_saturation_signal').text)
        self.multiplicity_of_infection.value = float(uep.find('.//multiplicity_of_infection').text)
        self.use_single_infected_cell.value = ('true' == (uep.find('.//use_single_infected_cell').text.lower()) )
        self.number_of_CD8_Tcells.value = int(uep.find('.//number_of_CD8_Tcells').text)
        self.number_of_macrophages.value = int(uep.find('.//number_of_macrophages').text)
        self.number_of_neutrophils.value = int(uep.find('.//number_of_neutrophils').text)
        self.number_of_DCs.value = int(uep.find('.//number_of_DCs').text)
        self.number_of_CD4_Tcells.value = int(uep.find('.//number_of_CD4_Tcells').text)
        self.DC_induced_CD8_proliferation.value = float(uep.find('.//DC_induced_CD8_proliferation').text)
        self.DC_induced_CD8_attachment.value = float(uep.find('.//DC_induced_CD8_attachment').text)
        self.departure_rate_of_DCs.value = float(uep.find('.//departure_rate_of_DCs').text)
        self.virions_needed_for_DC_activation.value = int(uep.find('.//virions_needed_for_DC_activation').text)
        self.epsilon_distance.value = float(uep.find('.//epsilon_distance').text)
        self.perecentage_tissue_vascularized.value = float(uep.find('.//perecentage_tissue_vascularized').text)
        self.color_variable.value = (uep.find('.//color_variable').text)
        self.epithelial_opacity.value = float(uep.find('.//epithelial_opacity').text)
        self.non_epithelial_opacity.value = float(uep.find('.//non_epithelial_opacity').text)
        self.apoptotic_epithelium_color.value = (uep.find('.//apoptotic_epithelium_color').text)
        self.apoptotic_immune_color.value = (uep.find('.//apoptotic_immune_color').text)
        self.CD8_Tcell_color.value = (uep.find('.//CD8_Tcell_color').text)
        self.CD4_Tcell_color.value = (uep.find('.//CD4_Tcell_color').text)
        self.Macrophage_color.value = (uep.find('.//Macrophage_color').text)
        self.activated_macrophage_color.value = (uep.find('.//activated_macrophage_color').text)
        self.exhausted_macrophage_color.value = (uep.find('.//exhausted_macrophage_color').text)
        self.hyperactivated_macrophage_color.value = (uep.find('.//hyperactivated_macrophage_color').text)
        self.Neutrophil_color.value = (uep.find('.//Neutrophil_color').text)
        self.DC_color.value = (uep.find('.//DC_color').text)
        self.activated_DC_color.value = (uep.find('.//activated_DC_color').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//random_seed').text = str(self.random_seed.value)
        uep.find('.//immune_dt').text = str(self.immune_dt.value)
        uep.find('.//immune_z_offset').text = str(self.immune_z_offset.value)
        uep.find('.//macrophage_max_recruitment_rate').text = str(self.macrophage_max_recruitment_rate.value)
        uep.find('.//macrophage_recruitment_min_signal').text = str(self.macrophage_recruitment_min_signal.value)
        uep.find('.//macrophage_recruitment_saturation_signal').text = str(self.macrophage_recruitment_saturation_signal.value)
        uep.find('.//neutrophil_max_recruitment_rate').text = str(self.neutrophil_max_recruitment_rate.value)
        uep.find('.//neutrophil_recruitment_min_signal').text = str(self.neutrophil_recruitment_min_signal.value)
        uep.find('.//neutrophil_recruitment_saturation_signal').text = str(self.neutrophil_recruitment_saturation_signal.value)
        uep.find('.//CD8_Tcell_max_recruitment_rate').text = str(self.CD8_Tcell_max_recruitment_rate.value)
        uep.find('.//CD8_Tcell_recruitment_min_signal').text = str(self.CD8_Tcell_recruitment_min_signal.value)
        uep.find('.//CD8_Tcell_recruitment_saturation_signal').text = str(self.CD8_Tcell_recruitment_saturation_signal.value)
        uep.find('.//multiplicity_of_infection').text = str(self.multiplicity_of_infection.value)
        uep.find('.//use_single_infected_cell').text = str(self.use_single_infected_cell.value)
        uep.find('.//number_of_CD8_Tcells').text = str(self.number_of_CD8_Tcells.value)
        uep.find('.//number_of_macrophages').text = str(self.number_of_macrophages.value)
        uep.find('.//number_of_neutrophils').text = str(self.number_of_neutrophils.value)
        uep.find('.//number_of_DCs').text = str(self.number_of_DCs.value)
        uep.find('.//number_of_CD4_Tcells').text = str(self.number_of_CD4_Tcells.value)
        uep.find('.//DC_induced_CD8_proliferation').text = str(self.DC_induced_CD8_proliferation.value)
        uep.find('.//DC_induced_CD8_attachment').text = str(self.DC_induced_CD8_attachment.value)
        uep.find('.//departure_rate_of_DCs').text = str(self.departure_rate_of_DCs.value)
        uep.find('.//virions_needed_for_DC_activation').text = str(self.virions_needed_for_DC_activation.value)
        uep.find('.//epsilon_distance').text = str(self.epsilon_distance.value)
        uep.find('.//perecentage_tissue_vascularized').text = str(self.perecentage_tissue_vascularized.value)
        uep.find('.//color_variable').text = str(self.color_variable.value)
        uep.find('.//epithelial_opacity').text = str(self.epithelial_opacity.value)
        uep.find('.//non_epithelial_opacity').text = str(self.non_epithelial_opacity.value)
        uep.find('.//apoptotic_epithelium_color').text = str(self.apoptotic_epithelium_color.value)
        uep.find('.//apoptotic_immune_color').text = str(self.apoptotic_immune_color.value)
        uep.find('.//CD8_Tcell_color').text = str(self.CD8_Tcell_color.value)
        uep.find('.//CD4_Tcell_color').text = str(self.CD4_Tcell_color.value)
        uep.find('.//Macrophage_color').text = str(self.Macrophage_color.value)
        uep.find('.//activated_macrophage_color').text = str(self.activated_macrophage_color.value)
        uep.find('.//exhausted_macrophage_color').text = str(self.exhausted_macrophage_color.value)
        uep.find('.//hyperactivated_macrophage_color').text = str(self.hyperactivated_macrophage_color.value)
        uep.find('.//Neutrophil_color').text = str(self.Neutrophil_color.value)
        uep.find('.//DC_color').text = str(self.DC_color.value)
        uep.find('.//activated_DC_color').text = str(self.activated_DC_color.value)
