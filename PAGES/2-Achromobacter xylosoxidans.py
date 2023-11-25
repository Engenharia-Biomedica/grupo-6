import pandas as pd 
import streamlit as st

st.header("LOCAL")
dados = pd.read_csv('DadosGerais.csv', sep=';')

selecao = st.selectbox("Escolha um local: ", ["Todos"] + dados["ds_unidade_coleta"].to_list())# possibilidade de fazer uma coluna 
if selecao == "Todos":
    st.bar_chart(data=dados, x="ds_unidade_coleta", y='cd_interpretacao_antibiograma')
else:
    dados_filtrado = dados[dados ["ds_unidade_coleta"]== selecao ]

    st.line_chart(data=dados_filtrado, x="ds_antibiotico_microorganismo", y='cd_interpretacao_antibiograma', color="ds_unidade_coleta")

st.header("ANTIBIÓTICO")
selecao1 = st.selectbox("Escolha um antibiótico: ", ["Todos"] + dados["ds_antibiotico_microorganismo"].to_list())# possibilidade de fazer uma coluna 
if selecao == "Todos":
    st.line_chart(data=dados, x="ds_unidade_coleta", y='cd_interpretacao_antibiograma', color="ds_unidade_coleta")
else:
    dados_filtrado = dados[dados ["ds_unidade_coleta"]== selecao ]

    st.line_chart(data=dados_filtrado, x="ds_antibiotico_microorganismo", y='cd_interpretacao_antibiograma', color="ds_unidade_coleta")

st.header("TEMPO")
selecao1 = st.selectbox("Escolha um antibiótico: ", ["Todos"] + dados["ds_antibiotico_microorganismo"].to_list())# possibilidade de fazer uma coluna 
if selecao == "Todos":
    st.line_chart(data=dados, x="ds_unidade_coleta", y='cd_interpretacao_antibiograma', color="ds_unidade_coleta")
else:
    dados_filtrado = dados[dados ["ds_unidade_coleta"]== selecao ]

    st.line_chart(data=dados_filtrado, x="ds_antibiotico_microorganismo", y='cd_interpretacao_antibiograma', color="ds_unidade_coleta")
