import streamlit as st
import pandas as pd
import plotly.express as px

file_path = "DG.csv"
df = pd.read_csv(file_path, sep=";")

st.title("Gráficos Para Análise de Sensibilidade e Resistência de Bactérias")

# Seleção de Bactérias
bacterias_disponiveis = list(df['ds_micro_organismo'].unique())
bacteria_selecionada = st.selectbox('Selecione a bactéria:', bacterias_disponiveis)
df_filtrado_bacteria = df[df['ds_micro_organismo'] == bacteria_selecionada]

# Seleção de Locais
unidades_coleta_disponiveis = ['Todas'] + list(df['ds_unidade_coleta'].unique())
unidade_selecionada = st.selectbox('Selecione a unidade de coleta:', unidades_coleta_disponiveis)
if unidade_selecionada == 'Todas':
    df_filtrado_local = df_filtrado_bacteria.copy()
else:
    df_filtrado_local = df_filtrado_bacteria[df_filtrado_bacteria['ds_unidade_coleta'] == unidade_selecionada]

# Seleção de Datas
datas = ['Todas'] + list(df['dh_coleta_exame'].unique())
data_selecionada = st.selectbox('Selecione a data da coleta do exame:', datas)
if data_selecionada == 'Todas':
    df_filtrado_data = df_filtrado_local.copy()
else:
    df_filtrado_data = df_filtrado_local[df_filtrado_local['dh_coleta_exame'] == data_selecionada]

# Filtragem por Resistência e Sensibilidade
interpretacao_selecionada = st.selectbox('Selecione a interpretação:', ['Resistente', 'Sensivel'])
df_filtrado_interpretacao = df_filtrado_data[df_filtrado_data['cd_interpretacao_antibiograma'] == interpretacao_selecionada]

# Contagem das ocorrências
df_contagem = df_filtrado_interpretacao.groupby(['ds_unidade_coleta', 'ds_antibiotico_microorganismo']).size().reset_index(name='Contagem')

# Geração do Gráfico de Barras Empilhadas
fig = px.bar(df_contagem, x='ds_unidade_coleta', y='Contagem', color='ds_antibiotico_microorganismo',
             title=f'Bactéria: {bacteria_selecionada} - {interpretacao_selecionada}',
             labels={'ds_unidade_coleta': 'Unidade de Coleta', 'ds_antibiotico_microorganismo': 'Antibiótico'})
st.plotly_chart(fig, use_container_width=True)
