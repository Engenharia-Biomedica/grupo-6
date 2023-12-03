import os
import sys
def executa()-> None:
    diretorio_atual = os.getcwd()
    nome_arquivo_app_streamlit = "Início.py"
    caminho_app_streamlit = os.path.join(diretorio_atual, nome_arquivo_app_streamlit)
    comando = f"streamlit run {caminho_app_streamlit}"
    os.system(comando)

executa()

