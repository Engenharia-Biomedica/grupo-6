import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

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

# Interface no Streamlit
st.title("Dashboard - Guia de Hospital")
unidade_selecionada = st.selectbox('Selecione a unidade hospitalar:', list(dados_unidades.keys()))

# Filtra os dados pela unidade selecionada
prédios_unidade = dados_unidades[unidade_selecionada]

# Cria um DataFrame com as informações dos prédios
df_prédios = pd.DataFrame({'Prédios': prédios_unidade})

# Cria um gráfico de barras usando o Plotly Express
fig = px.bar(df_prédios, x=[1] * len(df_prédios), y=[1] * len(df_prédios),
             text='Prédios', width=800, height=400)

# Personalizações do layout
fig.update_traces(marker=dict(color='blue', line=dict(color='black', width=2)), selector=dict(type='bar'))

# Adiciona anotações de texto com a quantidade de bactérias em cada prédio
for i, row in enumerate(df_prédios.iterrows()):
    prédio_nome = row[1]['Prédios']
    
    # Filtra o DataFrame para o prédio específico
    df_prédio = df[df['ds_predio_coleta'] == prédio_nome]
    
    # Verifica se há bactérias para o prédio
    if not df_prédio.empty:
        # Obtém a lista de tipos de bactérias para o prédio específico
        tipos_bactérias = df_prédio['ds_micro_organismo'].tolist()
        # Usa uma paleta de cores padrão do Plotly para atribuir cores diferentes aos tipos de bactérias
        cores = px.colors.qualitative.Plotly[:len(tipos_bactérias)]
        # Mapeia os tipos de bactérias para as cores correspondentes
        cor_por_bactéria = dict(zip(tipos_bactérias, cores))
        
        # Cria uma lista de cores para cada bactéria no prédio
        cores_prédio = [cor_por_bactéria.get(bactéria, "gray") for bactéria in tipos_bactérias]

    else:
        # Se não há dados, use uma cor padrão
        cores_prédio = ["gray"]  # ou qualquer cor padrão
    
    fig.add_trace(go.Scatter(
        x=[i + 1] * len(cores_prédio),
        y=[1] * len(cores_prédio),
        text=[f"Bactéria: {bactéria}" for bactéria in tipos_bactérias],
        mode="markers+text",
        marker=dict(color=cores_prédio, size=20, line=dict(color='black', width=2)),
        textposition="bottom center",
    ))

fig.update_layout(
    showlegend=False,
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    title=f"Guia de Hospital - Unidade: {unidade_selecionada}",
)
st.plotly_chart(fig)
    
