import streamlit as st
import pandas as pd
import altair as alt


file_path = "DG.csv"
df = pd.read_csv(file_path,sep = ";")
# ================= MUDAR PARA CADA BACTÉRIA ===========================
bacteria_df = df[(df['ds_micro_organismo'] == 'Aeromonas caviae') & (df['cd_interpretacao_antibiograma'] == 'Resistente')]
st.title("Gráficos específico para Aeromonas Caviae Resistente")

colunas_validas = ['ds_unidade_coleta', 'dh_coleta_exame', ]


coluna_analise = st.selectbox("Selecione a coluna de unidade de coleta:", colunas_validas)

coluna_interpretacao = 'cd_interpretacao_antibiograma'  # fixa para "Resistente"

if coluna_analise:
    chart = alt.Chart(bacteria_df).mark_bar().encode(
        x=coluna_analise,
        y='count()',
        color=alt.Color('ds_antibiotico_microorganismo:N', legend=alt.Legend(title='Antibiótico')),
        tooltip=[coluna_analise, 'ds_antibiotico_microorganismo', 'count()']
    ).interactive()

    st.altair_chart(chart, use_container_width=True)
else:
    st.warning("Selecione a coluna para a análise.")

file = "HIAE.csv"
g = pd.read_csv(file,sep = ";")

bacteria_g = g[(g['ds_micro_organismo'] == 'Aeromonas caviae') & (g['cd_interpretacao_antibiograma'] == 'Resistente')]
st.title("Presença de Aeromonas Caviae por bloco do HIAE")

colunas_validas2 = ['ds_predio_coleta']

coluna_analise1 = st.selectbox("Selecione a coluna:", colunas_validas2)

coluna_interpretacao = 'cd_interpretacao_antibiograma'  # fixa para "Resistente"

if coluna_analise1:
    chart = alt.Chart(bacteria_g).mark_bar().encode(
        x=coluna_analise1,
        y='count()',
        color=alt.Color('ds_antibiotico_microorganismo:N', legend=alt.Legend(title='Antibiótico')),
        tooltip=[coluna_analise1, 'ds_antibiotico_microorganismo', 'count()']
    ).interactive()

    st.altair_chart(chart, use_container_width=True)
else:
    st.warning("Selecione")