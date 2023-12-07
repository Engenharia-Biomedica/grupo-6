import streamlit as st
from PIL import Image   
import pandas as pd
import altair as alt
# Configura a largura da tela
st.set_page_config(layout="wide")
   
# Título e subtítulo
st.title("Dashboard de Microbiologia")
st.subheader("Explorando Dados Microbiológicos de Forma Interativa")
img = Image.open("ft.jpg")
st.image(img)

st.markdown("©Grupo6. Todos os direitos reservados.")



