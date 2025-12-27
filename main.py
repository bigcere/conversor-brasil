import streamlit as st

# Título de la App
st.title("🇧🇷 Conversor Brasil - CERE")
st.subheader("Calculadora de Reales a Pesos")

# Entrada de datos
reales = st.number_input("Ingresá el monto en Reales:", min_value=0.0, value=100.0, step=10.0)

# El valor de la cotización (podés cambiarlo acá mismo)
cotizacion = 185.0
pesos = reales * cotizacion

# Mostrar el resultado con estilo
st.divider()
st.metric(label="Total en Pesos Argentinos", value=f"${pesos:,.2f}")
st.write(f"Cotización utilizada: $ {cotizacion}")

# Un toque del Rojo para personalizar
st.sidebar.markdown("---")
st.sidebar.write("Desarrollado por CERE 🔴")