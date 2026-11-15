import streamlit as st

st.title("Мій перший додаток у хмарі")
st.write("Все працює!")
name = st.text_input("Як тебе звати?")
age = st.slider("Скільки тобі років?", 0, 100, 25)
if st.button("Привіт!"):
    st.write(f"Привіт, {name}! Тобі {age} років.")
