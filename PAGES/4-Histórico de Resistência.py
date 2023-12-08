import streamlit as st
import pandas as pd
import plotly.express as px

file_path = "DG.csv"
df = pd.read_csv(file_path, sep=";")

st.title("Histórico de Resistência")

# Seleção de Bactérias
bacterias_disponiveis = list(df['ds_micro_organismo'].unique())
bacteria_selecionada = st.selectbox('Selecione a bactéria:', bacterias_disponiveis)

# Verificar se há casos de resistência para o microorganismo selecionado
resistencia_disponivel = df[(df['ds_micro_organismo'] == bacteria_selecionada) & 
                            (df['cd_interpretacao_antibiograma'] == 'Resistente')].shape[0] > 0

# Se não houver casos de resistência para o microorganismo selecionado, mostrar aviso
if not resistencia_disponivel:
    st.warning(f"Não há casos de resistência para {bacteria_selecionada}.")
else:
    antibioticos_com_resistencia = list(df[(df['ds_micro_organismo'] == bacteria_selecionada) & 
                                           (df['cd_interpretacao_antibiograma'] == 'Resistente')]['ds_antibiotico_microorganismo'].unique())

    antibiotico_selecionado = st.selectbox('Selecione o antibiótico:', antibioticos_com_resistencia)

    # Filtragem de dados
    df_filtrado = df[(df['ds_micro_organismo'] == bacteria_selecionada) & 
                     (df['ds_antibiotico_microorganismo'] == antibiotico_selecionado) & 
                     (df['cd_interpretacao_antibiograma'] == 'Resistente')]

    # Verificar se há dados após a filtragem
    if df_filtrado.empty:
        st.warning(f"Não há dados de resistência para {antibiotico_selecionado} em {bacteria_selecionada}.")
    else:
        # Restante do código para criar o gráfico
        df_filtrado['dh_coleta_exame'] = pd.to_datetime(df_filtrado['dh_coleta_exame'])
        df_filtrado['ano_mes'] = df_filtrado['dh_coleta_exame'].dt.to_period('M')
        df_contagem = df_filtrado.groupby('ano_mes').size().reset_index(name='Contagem')
        df_contagem['Frequencia Cumulativa'] = df_contagem['Contagem'].cumsum()
        df_contagem['ano_mes'] = df_contagem['ano_mes'].dt.to_timestamp()
        df_contagem = df_contagem.sort_values(by='ano_mes')

        # Adicionar contagem de microorganismos resistentes
        texto_info = f"Contagem de {bacteria_selecionada} Resistentes a {antibiotico_selecionado}: {df_contagem['Contagem'].sum()}"

        # Ajustar a escala do eixo y para garantir que todos os valores sejam visíveis
        y_max = max(df_contagem['Frequencia Cumulativa']) * 1.1

        if df_filtrado['ano_mes'].nunique() == 1:
            # Caso único de resistência, criar gráfico de barras
            fig_bar = px.bar(df_contagem, x='ano_mes', y='Contagem', title=f'História de Resistência de {bacteria_selecionada} a {antibiotico_selecionado}',
                             labels={'ano_mes': 'Mês', 'Contagem': 'Frequência'},
                             height=400)
            st.plotly_chart(fig_bar, use_container_width=True)
        else:
            # Casos múltiplos de resistência, criar gráfico de linha com marcadores
            fig = px.line(df_contagem, x='ano_mes', y='Frequencia Cumulativa',
                          labels={'ano_mes': 'Data de Coleta', 'Frequencia Cumulativa': f'Frequência Cumulativa de Casos de Resistência'},
                          title=f'História de Resistência de {bacteria_selecionada} a {antibiotico_selecionado}',
                          range_y=[0, y_max], markers=True)  # Adiciona marcadores

            # Ajustar a escala do eixo x
            fig.update_xaxes(
                dtick="M1",  # Exibir marcações mensais
                tickformat="%Y-%m",  # Formato da marcação
                tickangle=45,  # Ângulo de rotação das marcações para melhorar a legibilidade
            )

            # Adicionar texto informativo sobre a contagem de resistência
            fig.add_annotation(
                text=texto_info,
                showarrow=False,
                xref="paper", yref="paper",
                x=0.5, y=1.1,
                font=dict(size=12),
            )

            st.plotly_chart(fig, use_container_width=True)
