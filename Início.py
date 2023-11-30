import pandas as pd
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns

# Header
st.header("Painel de Monitoramento de Resistência a Bactérias")

# carregando imagem para o logo
img = Image.open("antibióticos.jpeg")

# dividindo o espaçamento da tela em colunas
left_col, cent_col, last_col = st.columns(3)

# colocando o logo na coluna central
with cent_col:
    st.image(img, width=350)

# Texto introdutório

st.markdown("Dados da microbiologia do HIAE.")



