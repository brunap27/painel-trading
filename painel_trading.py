
import streamlit as st
import pandas as pd

def calcular_resultados(valores_compra, valores_venda_executadas, valores_ordens_abertas_venda):
    total_gasto = sum(valores_compra)
    total_recebido = sum(valores_venda_executadas) + sum(valores_ordens_abertas_venda)
    lucro_usdt = total_recebido - total_gasto
    porcentagem_lucro = (lucro_usdt / total_gasto) * 100

    dados = {
        'Descrição': ['Total Gasto', 'Total Recebido (incluindo ordens abertas)', 'Lucro (USDT)', 'Lucro (%)'],
        'Valor': [round(total_gasto, 4), round(total_recebido, 4), round(lucro_usdt, 4), round(porcentagem_lucro, 2)]
    }

    df = pd.DataFrame(dados)
    return df

st.title("Painel de Trading - Cálculo de Lucro")

st.write("Insira abaixo os valores de compras, vendas executadas e ordens abertas:")

valores_compra = st.text_area("Valores de Compra (separados por vírgula)")
valores_venda_executadas = st.text_area("Valores de Venda Executadas (separados por vírgula)")
valores_ordens_abertas_venda = st.text_area("Valores de Ordens Abertas de Venda (separados por vírgula)")

if st.button("Calcular"):
    try:
        compras = [float(x.strip()) for x in valores_compra.split(',') if x.strip()]
        vendas_executadas = [float(x.strip()) for x in valores_venda_executadas.split(',') if x.strip()]
        ordens_abertas = [float(x.strip()) for x in valores_ordens_abertas_venda.split(',') if x.strip()]

        resultado = calcular_resultados(compras, vendas_executadas, ordens_abertas)

        st.write("### Resultado do cálculo:")
        st.dataframe(resultado)

    except Exception as e:
        st.error(f"Erro ao calcular: {e}")
