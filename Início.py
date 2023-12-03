import streamlit as st
from PIL import Image   
   
# Título e subtítulo
st.title("Dashboard de Microbiologia")
st.subheader("Explorando Dados Microbiológicos de Forma Interativa")
img = Image.open("ft.jpg")

left_col, cent_col, last_col = st.columns(3)
with left_col:
    st.image(img, width=700
             )

st.write(
    "Bem-vindo ao nosso dashboard de microbiologia! Aqui você poderá explorar e analisar dados microbiológicos de forma interativa."
)
# Rodapé
st.markdown("---")
st.write("Desenvolvido por GRUPO 06 - T1 - Engenharia Biomédica FICSAE")



