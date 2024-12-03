import pandas as pd
import plotly.express as px
import streamlit as st
st.header('histograma')
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    # Botón para crear gráfico de dispersión
st.subheader("Gráfico de dispersión")
scatter_button = st.button('Construir gráfico de dispersión')  # Crear un botón para dispersión

if scatter_button:  # Al hacer clic en el botón
    st.write('Creación de un gráfico de dispersión que relaciona precio y kilometraje')
    # Crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", 
                             title="Relación entre kilometraje y precio",
                             labels={"odometer": "Kilometraje (millas)", "price": "Precio (USD)"})
    # Mostrar el gráfico de dispersión
    st.plotly_chart(fig_scatter, use_container_width=True)