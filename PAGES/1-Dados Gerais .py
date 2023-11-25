import pandas as pd 
import streamlit as st

st.header("Dados agrupados de todas as bactérias")

dados = pd.read_csv('dados.csv', sep=';') # ler a tabela 

 # aparecer a tabela 
left_col, cent_col, last_col = st.columns(3)

with cent_col:
    st.dataframe(dados, width=200)  # aparecer a tabela 