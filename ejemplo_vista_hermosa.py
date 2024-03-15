#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 09:23:55 2024

@author: dduque
"""

import pandas as pd
import seaborn as sbn
import os
import streamlit as st
import plotly.express as px
import numpy as np

municipios_link=r"bases_cuipo_contraloria/municipalities/"
municipio_code="211150711"

municipio=pd.read_csv(municipios_link+municipio_code+".csv")
municipio=municipio.replace('No Aplica', np.nan)

##El siguiente código es de Carlos Ortiz con adaptaciones
st.set_page_config(layout='wide')


filtrado1=pd.read_csv(
    r"dic/codigos_nombres")

st.title("gasto presupuestal")

tab0,tab1,tab2 = st.tabs(['selección','gastos',"nombres"])
with tab0:
     
    st.header("Treemap")
    
    fig = px.treemap(municipio, 
                     path=[px.Constant(municipio_code),
                               'CUENTA_NIVEL_01', 
                               'CUENTA_NIVEL_02',
                               'CUENTA_NIVEL_03',
                               'CUENTA_NIVEL_04',
                               'CUENTA_NIVEL_05',
                               ],
                    values='APROPIACION_DEFINITIVA',
                    color='CUENTA_NIVEL_01',
                    title="Matriz de composición anual de los municipios",
                    branchvalues = "remainder")
    
    fig.update_layout(width=1000, height=600)
    
    st.plotly_chart(fig)
