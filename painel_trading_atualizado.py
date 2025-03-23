
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

st.title("Lucro")

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

        # Histórico gráfico
        st.write("### Histórico de valores")
        historico = pd.DataFrame({
            'Compras': compras,
            'Vendas Executadas': vendas_executadas[:len(compras)] if len(vendas_executadas) >= len(compras) else vendas_executadas + [None]*(len(compras)-len(vendas_executadas)),
            'Ordens Abertas': ordens_abertas[:len(compras)] if len(ordens_abertas) >= len(compras) else ordens_abertas + [None]*(len(compras)-len(ordens_abertas))
        })
        st.dataframe(historico)

        st.write("### Gráfico comparativo")
        historico.plot(kind='bar')
        st.pyplot(plt.gcf())

    except Exception as e:
        st.error(f"Erro ao calcular: {e}")
