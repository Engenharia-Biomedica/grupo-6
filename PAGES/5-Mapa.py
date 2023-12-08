import streamlit as st
from PIL import Image   
import pandas as pd
import altair as alt
# Configura a largura da tela
st.set_page_config(layout="wide")
   
# Título e subtítulo
st.title("Mapa Morumbi")
st.subheader("Explore o bloco do morumbi de acordo com o nível de bactérias em bloco.")
st.text("Verde - OK")
st.text("Amarelo - Cuidado")
st.text("Vermelho - Perigo")

imgBloco1DAmarelo = Image.open("Bloco1D-Amarelo.png")
imgBloco1DVermelho = Image.open("Bloco1D-Vermelho.png")
imgBloco1DVerde = Image.open("Bloco1D-Verde.png")
imgBloco2DAmarelo = Image.open("Bloco2D-Amarelo.png")
imgBloco2DVermelho = Image.open("Bloco2D-Vermelho.png")
imgBloco2DVerde = Image.open("Bloco2D-Verde.png")
imgBloco2AAmarelo = Image.open("Bloco2A-Amarelo.png")
imgBloco2AVerde = Image.open("Bloco2A-Verde.png")
imgBloco2AVermelho = Image.open("Bloco2A-Vermelho.png")
imgBlocoAVerde = Image.open("BlocoA-Verde.png")
imgBlocoAAmarelo = Image.open("BlocoA-Amarelo.png")
imgBlocoAVermelho = Image.open("BlocoA-Vermelho.png")
imgBlocoBAmarelo = Image.open("BlocoB-Amarelo.png")
imgBlocoBVerde = Image.open("BlocoB-Verde.png")
imgBlocoBVermelho = Image.open("BlocoB-Vermelho.png")
imgBlocoCVerde = Image.open("BlocoC-Verde.png")
imgBLocoCAmarelo = Image.open("BlocoC-Amarelo.png")
imgBlocoCVermelho = Image.open("BlocoC-Vermelho.png")
imgBlocoEVerde = Image.open("BlocoE-Verde.png")
imgBlocoEVermelho = Image.open("BlocoE-Vermelho.png")
imgBlocoEAmarelo = Image.open("BlocoE-Amarelo.png")
imgBlocoA1Verde = Image.open("BlocoA1-Verde.png")
imgBLocoA1Amarelo = Image.open("BlocoA1-Amarelo.png")
imgBlocoA1Vermelho = Image.open("BlocoA1-Vermelho.png")






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
        st.image(imgBlocoEVerde)
    elif num_registrosE > 0 and num_registrosE < 10:
        st.image(imgBlocoEAmarelo)
    else:
        st.image(imgBlocoEVermelho)
    st.write(f"Número de Registros: {num_registrosE}")
    
with col2:
    if num_registrosD == 0:
        st.image(imgBloco1DVerde)
        st.image(imgBloco2DVerde)
    elif num_registrosD > 0 and num_registrosD <= 10:
        st.image(imgBloco1DAmarelo)
        st.image(imgBloco2DAmarelo)
    else:
        st.image(imgBloco1DVermelho)
        st.image(imgBloco2DVermelho)
    st.write(f"Número de Registros: {num_registrosD}")
        
with col3:
    if num_registrosC == 0:
        st.image(imgBlocoCVerde)
    elif num_registrosC > 0 and num_registrosC <= 10:
        st.image(imgBLocoCAmarelo)
    elif num_registrosC > 10:
        st.image(imgBlocoCVermelho)
    st.write(f"Número de Registros: {num_registrosC}")
    
    if num_registrosB == 0:
        st.image(imgBlocoBVerde)
    elif num_registrosB > 0 and num_registrosB <= 10:
        st.image(imgBlocoBAmarelo)
    elif num_registrosB > 10:
        st.image(imgBlocoBVermelho)
    st.write(f"Número de Registros: {num_registrosB}")
        
with col4:
    if num_registrosA == 0:
        st.image(imgBlocoAVerde)
        st.image(imgBloco2AVerde)
    elif num_registrosA > 0 and num_registrosA <= 10:
        st.image(imgBlocoAAmarelo)
        st.image(imgBloco2AAmarelo)
    else:
        st.image(imgBlocoAVermelho)
        st.image(imgBloco2AVermelho)
    st.write(f"Número de Registros: {num_registrosA}")
        
with col6:
    if num_registrosA1 == 0:
        st.image(imgBlocoA1Verde)
    elif num_registrosA1 > 0 and num_registrosA1 <= 10:
        st.image(imgBLocoA1Amarelo)
    else:
        st.image(imgBlocoA1Vermelho)
    st.write(f"Número de Registros: {num_registrosA1}")


