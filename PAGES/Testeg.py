import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Crie um DataFrame de exemplo (substitua esta parte pelo seu próprio conjunto de dados)
file_path = "DG.csv"
df = pd.read_csv(file_path, sep=";")
# Filtrar o DataFrame com base nas entradas do usuário
bacteria_selecionada = st.selectbox('Selecione a bactéria:', df['ds_micro_organismo'].unique())
interpretacao_selecionada = st.selectbox('Selecione a interpretação:', df['cd_interpretacao_antibiograma'].unique())
antibiotico_selecionado = st.selectbox('Selecione o antibiótico:', df['ds_antibiotico_microorganismo'].unique())

# Filtrar o DataFrame com base nas seleções do usuário
df_filtrado = df[(df['ds_micro_organismo'] == bacteria_selecionada) &
                 (df['cd_interpretacao_antibiograma'] == interpretacao_selecionada) &
                 (df['ds_antibiotico_microorganismo'] == antibiotico_selecionado)]

# Verificar se há dados antes de tentar criar o gráfico
if not df_filtrado.empty:
    # Converter a coluna 'dh_coleta_exame' para o tipo de dados datetime
    df_filtrado['dh_coleta_exame'] = pd.to_datetime(df_filtrado['dh_coleta_exame'])

    # Criar um gráfico de dispersão com base no DataFrame filtrado
    fig, ax = plt.subplots()
    ax.scatter(df_filtrado['dh_coleta_exame'], range(len(df_filtrado)))

    # Configurar os rótulos dos eixos
    ax.set_xlabel('Data de Coleta do Exame')
    ax.set_ylabel('Frequência')

    # Exibir o gráfico no Streamlit
    st.pyplot(fig)
else:
    st.warning("Nenhum dado encontrado com as seleções feitas.")