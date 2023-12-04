import streamlit as st
from PIL import Image   
import pandas as pd
import altair as alt
# Configura a largura da tela
st.set_page_config(layout="wide")
   
# Título e subtítulo
st.title("Dashboard de Microbiologia")
st.subheader("Explorando Dados Microbiológicos de Forma Interativa")
img = Image.open("quadrado.png")

imgVerde = Image.open("quadrado.png")
imgAmarelo = Image.open("quadrado-amarelo.png")
imgVermelho = Image.open("quadrado-vermelho.png")




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

df_unidade = dados[dados['ds_unidade_coleta'] == 'HIAE Morumbi']            
tipos_datas = df_unidade['dh_coleta_exame'].unique()           
microorganismo_selecionada = st.selectbox("Selecione um microorganismo:", dados['ds_micro_organismo'].unique())
tipo_data_selecionado = st.selectbox("Selecione o tipo de data:", tipos_datas)

# Condição para verificar as características desejadas
df_filtrado_A = dados[
    (dados['ds_unidade_coleta'] == 'HIAE Morumbi') &
    (dados['ds_predio_coleta'] == 'Bloco A') &
    (dados['ds_micro_organismo'] == microorganismo_selecionada) &
    (df_unidade['dh_coleta_exame'] == tipo_data_selecionado )  
]
df_filtrado_A1 = dados[
    (dados['ds_unidade_coleta'] == 'HIAE Morumbi') &
    (dados['ds_predio_coleta'] == 'Bloco A1') &
    (dados['ds_micro_organismo'] == microorganismo_selecionada) &
    (df_unidade['dh_coleta_exame'] == tipo_data_selecionado )  
]
df_filtrado_B = dados[
    (dados['ds_unidade_coleta'] == 'HIAE Morumbi') &
    (dados['ds_predio_coleta'] == 'Bloco B') &
    (dados['ds_micro_organismo'] == microorganismo_selecionada) &
    (df_unidade['dh_coleta_exame'] == tipo_data_selecionado )  
]
df_filtrado_C = dados[
    (dados['ds_unidade_coleta'] == 'HIAE Morumbi') &
    (dados['ds_predio_coleta'] == 'Bloco C') &
    (dados['ds_micro_organismo'] == microorganismo_selecionada) &
    (df_unidade['dh_coleta_exame'] == tipo_data_selecionado )  
]
df_filtrado_D = dados[
    (dados['ds_unidade_coleta'] == 'HIAE Morumbi') &
    (dados['ds_predio_coleta'] == 'Bloco D') &
    (dados['ds_micro_organismo'] == microorganismo_selecionada) &
    (df_unidade['dh_coleta_exame'] == tipo_data_selecionado )  
]
df_filtrado_E = dados[
    (dados['ds_unidade_coleta'] == 'HIAE Morumbi') &
    (dados['ds_predio_coleta'] == 'Bloco E') &
    (dados['ds_micro_organismo'] == microorganismo_selecionada) &
    (df_unidade['dh_coleta_exame'] == tipo_data_selecionado )  
]
df_filtrado_F = dados[
    (dados['ds_unidade_coleta'] == 'HIAE Morumbi') &
    (dados['ds_predio_coleta'] == 'Bloco F') &
    (dados['ds_micro_organismo'] == microorganismo_selecionada) &
    (df_unidade['dh_coleta_exame'] == tipo_data_selecionado )  
]



# Obtém o número de registros
num_registrosA = df_filtrado_A.shape[0]
num_registrosA1 = df_filtrado_A1.shape[0]
num_registrosB = df_filtrado_B.shape[0]
num_registrosC = df_filtrado_C.shape[0]
num_registrosD = df_filtrado_D.shape[0]
num_registrosE = df_filtrado_E.shape[0]
num_registrosF = df_filtrado_F.shape[0]




col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    if num_registrosE == 0:
        st.image(imgVerde)
    elif num_registrosE > 0 and num_registrosE < 10:
        st.image(imgAmarelo)
    else:
        st.image(imgVermelho)
    st.write(f"Número de Registros: {num_registrosE}")
    
with col2:
    if num_registrosD == 0:
        st.image(imgVerde)
    elif num_registrosD > 0 and num_registrosD <= 10:
        st.image(imgAmarelo)
    else:
        st.image(imgVermelho)
    st.write(f"Número de Registros: {num_registrosD}")
        
with col3:
    if num_registrosC == 0:
        st.image(imgVerde)
    elif num_registrosC > 0 and num_registrosC <= 10:
        st.image(imgAmarelo)
    elif num_registrosC > 10:
        st.image(imgVermelho)
    st.write(f"Número de Registros: {num_registrosC}")
    
    if num_registrosB == 0:
        st.image(imgVerde)
    elif num_registrosB > 0 and num_registrosB <= 10:
        st.image(imgAmarelo)
    elif num_registrosB > 10:
        st.image(imgVermelho)
    st.write(f"Número de Registros: {num_registrosB}")
        
with col4:
    if num_registrosA == 0:
        st.image(imgVerde)
    elif num_registrosA > 0 and num_registrosA <= 10:
        st.image(imgAmarelo)
    else:
        st.image(imgVermelho)
    st.write(f"Número de Registros: {num_registrosA}")
        
with col6:
    if num_registrosA1 == 0:
        st.image(imgVerde)
    elif num_registrosA1 > 0 and num_registrosA1 <= 10:
        st.image(imgAmarelo)
    else:
        st.image(imgVermelho)
    st.write(f"Número de Registros: {num_registrosA1}")


