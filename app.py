import streamlit as st

st.title("Давай знайомитися!")
st.write("Внеси інформацію про себе!")
name = st.text_input("Як тебе звати?")
age = st.slider("Скільки тобі років?", 0, 100, 25)
if st.button("Привіт!"):
    st.write(f"Привіт, {name}! Тобі {age} років.")
agree = st.checkbox("Я погоджуюсь з умовами")
option = st.selectbox("Виберіть місто:", ["Київ","Львів","Одеса"])
st.write("Ваш вибір:", option)
