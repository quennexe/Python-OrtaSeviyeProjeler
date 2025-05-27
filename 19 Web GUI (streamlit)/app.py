import streamlit as st

st.title("👋 Basit Streamlit Uygulaması")

# Kullanıcıdan isim al
name = st.text_input("Adınızı girin:")

if name:
    st.success(f"Merhaba, {name}!")

# Slider ile kare hesaplama
number = st.slider("Bir sayı seçin:", 1, 100)
st.write(f"{number} sayısının karesi: {number**2}")

# Not
st.info("Streamlit ile web arayüzleri bu kadar kolay!")
