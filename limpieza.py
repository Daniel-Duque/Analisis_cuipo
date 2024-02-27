# -*- coding: utf-8 -*-
"""analisis_territorial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AQnWOCqJUWkHUKJg-HgLbDXsLa72uWoS
"""


import streamlit
import pandas as pd
import os
import plotly.express as px



eje_gasto=pd.read_csv(r"bases_cuipo_contraloria/OVCF_-_CUIPO_-_Ejecuci_n_de_Gastos_20240213.csv",usecols=["NOMBRE_ENTIDAD"])


import streamlit as st

st.set_page_config(layout='wide')

municipio=eje_gasto["NOMBRE_ENTIDAD"].drop_duplicates()
st.title("gasto presupuestal")

tab0,tab1,tab2 = st.tabs(['selección','gastos',"nombres"])
with tab0:
  muni = st.selectbox("NOMBRE_ENTIDAD",
                        municipio)
                        
              
  filter_muni=eje_gasto[
  eje_gasto["NOMBRE_ENTIDAD"]== muni]
  filtrado1=filter_muni.index.values

  
  
  #pres_gasto=pd.read_csv(r"bases_cuipo_contraloria/OVCF_-_CUIPO_-_Programaci_n_de_Gastos_20240213.csv",skiprows=lambda x: x not in filter_muni)
  #pres_ingr=pd.read_csv(r"bases_cuipo_contraloria/OVCF_-_CUIPO_-_Programaci_n_de_Ingresos_20240213.csv",skiprows=lambda x: x not in filter_muni)
  eje_gasto=pd.read_csv(r"bases_cuipo_contraloria/OVCF_-_CUIPO_-_Ejecuci_n_de_Gastos_20240213.csv",skiprows=lambda x: x not in filtrado1)
  #eje_ingr=pd.read_csv(r"bases_cuipo_contraloria/OVCF_-_CUIPO_-_Ejecuci_n_de_Ingresos_20240213.csv",skiprows=lambda x: x not in filter_muni)
  
  print("first stage")
  
  
with tab1:

  cuenta3=eje_gasto[
	"NOMBRE_CUENTA"].drop_duplicates()

  category = st.selectbox("NOMBRE_CUENTA",
                        cuenta3)
  filter_category = eje_gasto[eje_gasto["NOMBRE_CUENTA"]== category]
  



  fig = px.line(filter_category, x="VIGENCIA", y='PAGOS', title='APROPIACION_INICIAL')
  st.plotly_chart(fig)

