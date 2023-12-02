import streamlit as st
import pandas as pd
import plotly.express as px

file_path = "DG.csv"
df = pd.read_csv(file_path, sep=";")

st.title("Gráfico de Pizza para Frequência de Interpretação")

# Pré-seleção de Microorganismo e Antibiótico
microorganismo_selecionado = st.selectbox('Selecione o microorganismo:', df['ds_micro_organismo'].unique())
antibiotico_selecionado = st.selectbox('Selecione o antibiótico:', df['ds_antibiotico_microorganismo'].unique())

# Filtragem do DataFrame
df_filtrado = df[(df['ds_micro_organismo'] == microorganismo_selecionado) &
                 (df['ds_antibiotico_microorganismo'] == antibiotico_selecionado)]

# Contagem das ocorrências
df_contagem = df_filtrado.groupby('cd_interpretacao_antibiograma').size().reset_index(name='Contagem')

# Geração do Gráfico de Pizza
fig_pizza = px.pie(df_contagem, values='Contagem', names='cd_interpretacao_antibiograma',
                   title=f'Frequência de Interpretação para {microorganismo_selecionado} - {antibiotico_selecionado}')

st.plotly_chart(fig_pizza, use_container_width=True)
