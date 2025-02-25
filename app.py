import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('/workspaces/sprint_7/vehicles_us.csv') # leer los datos
st.header('Visualizando gráficos con Render.')
hist_button = st.button('Construir histograma') # crear un botón para construir un histograma
disp_button = st.button('Construir diagrama de dispersión') # crear un botón para construir un diagrama de dispersión
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if disp_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)