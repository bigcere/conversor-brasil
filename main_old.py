import streamlit as st

st.title("🇧🇷 Conversor Brasil - CERE")

# Entrada de Reales
reales = st.number_input("Ingresá Reales (BRL):", min_value=0.0, step=10.0)

# Cotizaciones (Ajustalas a tu gusto)
ars = reales * 185.0
usd = reales * 0.18

if reales > 0:
    st.success(f"Son aproximadamente **${ars:,.2f} Pesos Argentinos**")
    st.info(f"O unos **U$D {usd:,.2f} Dólares**")