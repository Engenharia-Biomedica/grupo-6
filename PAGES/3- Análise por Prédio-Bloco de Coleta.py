import pandas as pd
import streamlit as st
import altair as alt

#leitura do csv
file_path = "DG.csv"
dados = pd.read_csv(file_path,sep = ";")
#descobre todas as unidades:
lista_unidades = dados['ds_unidade_coleta'].unique().tolist()
print("\nUnidades Totais\n")
for c in lista_unidades:
    print(f"{c}") 
print(f"{len(lista_unidades)}")
df_filtrado = dados[dados['ds_unidade_coleta'] == 'HIEA Morumbi']
lista_predios = df_filtrado['ds_predio_coleta'].unique().tolist()
with open("blocos.txt","w") as arquivo:
    for unidade in lista_unidades:
        df_filtrado = dados[dados['ds_unidade_coleta'] == f'{unidade}']
        lista_predios = df_filtrado['ds_predio_coleta'].unique().tolist()
        arquivo.write(f"\nDados da unidade:{unidade}\n")
        for element in lista_predios:
            arquivo.write(f"{element}\n")
print(lista_predios)
df = dados.query('ds_unidade_coleta == "HIAE Morumbi"').copy()
lista = df['ds_predio_coleta'].unique().tolist()


#==============================parte do pqpilson===================================:
# Leitura do arquivo TXT
# Obtém as unidades e prédios do arquivo
file_path_txt = "blocos.txt"
with open(file_path_txt, "r") as arquivo:
    linhas = arquivo.readlines()
dados_unidades = {}
unidade_atual = None
for linha in linhas:
    linha = linha.strip()
    if linha:
        if linha.startswith('Dados da unidade:'):
            unidade_atual = linha.replace('Dados da unidade:', '').strip()
            dados_unidades[unidade_atual] = []
        else:
            dados_unidades[unidade_atual].append(linha)
#Interface dos gráficos:
# Dropdown para selecionar a unidade
unidade_selecionada = st.selectbox("Selecione a unidade:", dados['ds_unidade_coleta'].unique())

# Filtra os dados pela unidade selecionada
df_unidade = dados[dados['ds_unidade_coleta'] == unidade_selecionada]

# Obtem os tipos de datas únicos
tipos_datas = df_unidade['dh_coleta_exame'].unique()

# Dropdown para selecionar o tipo de data
tipo_data_selecionado = st.selectbox("Selecione o tipo de data:", tipos_datas)

# Filtra os dados pelo tipo de data selecionado
df_data = df_unidade[df_unidade['dh_coleta_exame'] == tipo_data_selecionado]

# Convertendo a coluna 'dh_coleta_exame' para datetime
df_data['dh_coleta_exame'] = pd.to_datetime(df_data['dh_coleta_exame'])
st.title("Estudo da frequência de bactérias Unidade/Prédios")
# Gráfico de barras usando Altair
if not df_data.empty:
    chart = (
        alt.Chart(df_data)
        .mark_bar()
        .encode(
            x=alt.X('ds_predio_coleta:N', title='Prédio de Coleta'),
            y=alt.Y('count()', title='Quantidade'),
            color='ds_micro_organismo:N',
            tooltip=['ds_predio_coleta', 'count()', 'ds_micro_organismo']
        )
        .properties(width=600, height=400)
    ).interactive()  # Adiciona interatividade

    # Adiciona regras de seleção ao gráfico
    selection = alt.selection_single()
    chart = chart.add_selection(selection)

    # Exibe o gráfico Altair no Streamlit
    st.altair_chart(chart, use_container_width=True)

    # Adiciona um DataFrame oculto para exibir os dados quando um ponto/barra for selecionado
    selected_data = df_data.loc[selection] if not selection.empty else pd.DataFrame()
    st.write(selected_data)

    # Use o ponto específico selecionado para realizar operações ou exibição
    if not selected_data.empty:
        ponto_selecionado = selected_data.iloc[0]
        st.write(f"Ponto Selecionado: {ponto_selecionado}")
else:
    st.warning(f"Não há dados disponíveis para a unidade {unidade_selecionada} e tipo de data selecionados.")
