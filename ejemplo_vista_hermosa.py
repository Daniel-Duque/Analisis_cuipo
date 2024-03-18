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

municipio_name=municipio
municipio_name=municipio[municipio["CODIGO_ENTIDAD"]==int(municipio_code)][
    "NOMBRE_ENTIDAD"].iloc()[0]

municipio=municipio.replace('No Aplica', "")
cuentas=[ 'CUENTA_NIVEL_01', 
          'CUENTA_NIVEL_02',
          'CUENTA_NIVEL_03',
          'CUENTA_NIVEL_04',
          'CUENTA_NIVEL_05',
          'CUENTA_NIVEL_06',
          'CUENTA_NIVEL_07',
          'CUENTA_NIVEL_08',
                 
          ]

def leave(valor):
    pattern=valor+"."
    if True in municipio["CUENTA"].str.match(pattern).values:
        return False
    else:
        return True



# Apply the classification function to each row
municipio_ingresos=municipio[municipio["tipo"]=="eje_ingreso"]
municipio=municipio[municipio["VIGENCIA_DEL_GASTO"]=="VIGENCIA ACTUAL"]
municipio=municipio[municipio["VIGENCIA"]==2023]
municipio=municipio[municipio["TRIMESTRE"]=="Tercer Trimestre"]
municipio=municipio[municipio["CUENTA"]!="2.99"]
municipio=municipio[municipio["CUENTA"]!=""]
##El siguiente código es de Carlos Ortiz con adaptaciones


municipio['leave'] = municipio["CUENTA"].apply(leave)

municipio=municipio[municipio["leave"]==True]

st.set_page_config(layout='wide')


filtrado1=pd.read_csv(
    r"dic/codigos_nombres")

st.title("gasto presupuestal")

tab0,tab1,tab2 = st.tabs(['selección','gastos',"nombres"])

with tab0:
     
    st.header("Treemap")
    
    fig = px.treemap(municipio, 
                     path=[px.Constant(municipio_name),
                               'CUENTA_NIVEL_01',
                               'SECCION_PRESUPUESTAL',
                               #'PROGRAMATICO_MGA',
                               'CUENTA_NIVEL_02',
                               'CUENTA_NIVEL_03',
                               'CUENTA_NIVEL_04',
                               'CUENTA_NIVEL_05',
                               'CUENTA_NIVEL_06',
                               'CUENTA_NIVEL_07',
                               'CUENTA_NIVEL_08',
                               
                               ],
                    values='APROPIACION_DEFINITIVA',
                    title="Matriz de composición anual de los municipios",
                    branchvalues="remainder")
    
    fig.update_layout(width=1000, height=600)
    
    st.plotly_chart(fig)
    
with tab1:
     
    st.header("Treemap")
    
    fig = px.treemap(municipio, 
                     path=[px.Constant(municipio_code),
                               'SECCION_PRESUPUESTAL',
                               #'PROGRAMATICO_MGA',
                               'CUENTA_NIVEL_01', 
                               'CUENTA_NIVEL_02',
                               'CUENTA_NIVEL_03',
                               'CUENTA_NIVEL_04',
                               'CUENTA_NIVEL_05',
                               'CUENTA_NIVEL_06',
                               'CUENTA_NIVEL_07',
                               'CUENTA_NIVEL_08',
                               
                               ],
                    values='APROPIACION_DEFINITIVA',
                    title="Matriz de composición anual de los municipios",
                    branchvalues="total")
    
    fig.update_layout(width=1000, height=600)
    
    st.plotly_chart(fig)

with tab2:
     
    st.header("Treemap")
    
    fig = px.treemap(municipio, 
                     path=[px.Constant(municipio_code),
                               'SECCION_PRESUPUESTAL',
                               #'PROGRAMATICO_MGA',
                               'CUENTA_NIVEL_01', 
                               'CUENTA_NIVEL_02',
                               'CUENTA_NIVEL_03',
                               'CUENTA_NIVEL_04',
                               'CUENTA_NIVEL_05',
                               'CUENTA_NIVEL_06',
                               'CUENTA_NIVEL_07',
                               'CUENTA_NIVEL_08',
                               
                               ],
                    values='APROPIACION_DEFINITIVA',
                    title="Matriz de composición anual de los municipios",
                    branchvalues="total")
    
    fig.update_layout(width=1000, height=600)
    
    st.plotly_chart(fig)

