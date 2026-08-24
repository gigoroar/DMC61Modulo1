import streamlit as st
st.title("Especialización Python for Analytics")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Giovani Rosas")
valor_inicial =st.number_input("Ingrese el valor inicial")
valor_final =st.number_input("Ingrese el valor final")
lista_numeros = list(range(int(valor_inicial), int(valor_final)))
st.write(lista_numeros)
modulos = st.sidebar.selectbox ("Seleccione un Modulo",["Modulo Listas", "Modulo Arreglos", "Módulo Funciones"])
if modulos == "Modulo Listas": 
  st.write("Bienvenido al Módulo Listas")
elif modulos == "Modulo Arreglos": 
  st.write("Bienvenido al Módulo Arreglos")
elif modulos == "Módulo Funciones": 
  st.write("Bienvenido al Módulo Funciones")  
           
