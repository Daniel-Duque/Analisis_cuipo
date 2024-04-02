# -*- coding: utf-8 -*-
"""analisis_territorial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AQnWOCqJUWkHUKJg-HgLbDXsLa72uWoS
"""


import pandas as pd
import os
import plotly.express as px
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objs as go


import streamlit as st

st.set_page_config(layout='wide')


filtrado1=pd.read_csv(
    r"dic/codigos_nombres")
municipios_link=r"bases_cuipo_contraloria/municipalities/"



st.title("gasto presupuestal")

tab0,tab1,tab2,tab3 = st.tabs(['selección','gastos según diferencias',"gastos","ingresos"])
with tab0:
  muni = st.selectbox("NOMBRE_ENTIDAD",
     filtrado1["NOMBRE_ENTIDAD"])
  
  ano1 = st.selectbox("primer año",
     [2021,2022,2023])
  ano2 = st.selectbox("segundo año",
     [2021,2022,2023])  
  municipio_code=str(filtrado1[filtrado1["NOMBRE_ENTIDAD"]==muni]["CODIGO_ENTIDAD"].iloc[0])


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

  municipio=municipio[municipio["TRIMESTRE"]=="Tercer Trimestre"]
  municipio=municipio[municipio["CUENTA"]!="2.99"]
  municipio=municipio[municipio["CUENTA"]!=""]

  municipio['leave'] = municipio["CUENTA"].apply(leave)

  municipio=municipio[municipio["leave"]==True]

  municipio2=municipio[municipio["VIGENCIA"]==ano1].drop_duplicates(subset=["CUENTA"])

  municipio=municipio[municipio["VIGENCIA"]==ano2].drop_duplicates(subset=["CUENTA"])


  municipiomerge=municipio.merge(municipio2,how="inner",on=["CUENTA"],suffixes=["","_y"])
  ##El siguiente código es de Carlos Ortiz con adaptaciones




  #municipiomerge['leave'] = municipiomerge["CUENTA"].apply(leave)

  #municipiomerge=municipiomerge[municipiomerge["leave"]==True]
  municipiomerge['APROPIACION_DEFINITIVA']=municipiomerge['APROPIACION_DEFINITIVA']-municipiomerge['APROPIACION_DEFINITIVA_y']
  municipiomerge["signo"]=municipiomerge['APROPIACION_DEFINITIVA'].apply(lambda x:"negativo" if x<0 else "positivo")
  municipiomerge['APROPIACION_DEFINITIVA']=municipiomerge['APROPIACION_DEFINITIVA'].apply(lambda x: x if x>0 else -x)



  filtrado1=pd.read_csv(
      r"dic/codigos_nombres")
  
  
  #pres_gasto=pd.read_csv(r"bases_cuipo_contraloria/OVCF_-_CUIPO_-_Programaci_n_de_Gastos_20240213.csv",skiprows=lambda x: x not in filter_muni)
  #pres_ingr=pd.read_csv(r"bases_cuipo_contraloria/OVCF_-_CUIPO_-_Programaci_n_de_Ingresos_20240213.csv",skiprows=lambda x: x not in filter_muni)
  
  #eje_ingr=pd.read_csv(r"bases_cuipo_contraloria/OVCF_-_CUIPO_-_Ejecuci_n_de_Ingresos_20240213.csv",skiprows=lambda x: x not in filter_muni)
  
  print("first stage")
  
  
with tab1:

    st.header("Treemap")
    
    fig = px.treemap(municipiomerge, 
                     path=[px.Constant(municipio_name),
                               
                               #'PROGRAMATICO_MGA',
                               'signo',
                               
                               'SECCION_PRESUPUESTAL',
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
                    branchvalues="remainder")
    
    fig.update_layout(width=1000, height=600)
    
    st.plotly_chart(fig)
     
    
  
with tab2:

    st.header("Treemap")
    fig = make_subplots(rows=1, cols=2)
    
    figures = [

    
    px.treemap(municipio, 
                     path=[px.Constant(municipio_name),
                               
                               #'PROGRAMATICO_MGA',                               
                               'SECCION_PRESUPUESTAL',
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
                    branchvalues="remainder"),

    px.treemap(municipio, 
                     path=[px.Constant(municipio_name),
                               
                               #'PROGRAMATICO_MGA',                               
                               'SECCION_PRESUPUESTAL',
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
                    branchvalues="remainder")
    ]
    fig = make_subplots(rows=1, cols=2,
                        specs=[[{"type": "treemap"}],[ {"type": "treemap"}]]) 
        

    fig.append_trace(figures[0], row=1, col=1)
    fig.append_trace(figures[0], row=1, col=2)    
    
    
    st.plotly_chart(fig) 


with tab3:
    
    st.header("Treemap")
    
    fig = px.treemap(municipio, 
                     path=[px.Constant(municipio_name),
                               
                               #'PROGRAMATICO_MGA',                               
                               'SECCION_PRESUPUESTAL',
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
                    branchvalues="remainder")
    
    fig.update_layout(width=1000, height=600)
    
    st.plotly_chart(fig) 
