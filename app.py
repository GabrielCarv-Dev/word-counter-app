import streamlit as st
from collections import Counter
import re

st.title("Contador de Palavras")

st.write("Cole seu texto abaixo e clique em CONTAR para ver o resultado:")

texto = st.text_area("Texto para análise", height=200)

if st.button("Contar"):
    palavras = re.findall(r'\b\w+\b', texto.lower())
    contagem = Counter(palavras)

    st.subheader("Resultados:")
    st.write(f"Total de palavras: {len(palavras)}")
    st.write(f"Total de caracteres: {len(texto)}")

#teste de CI
