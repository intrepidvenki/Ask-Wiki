import streamlit as st 

st.title("AI Web Scrapper")
url = st.text_input("Enter the website Url:  ")

if st.button("Scrape site"):
    st.write("scrapping website")