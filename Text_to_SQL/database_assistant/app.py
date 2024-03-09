import streamlit as st
from sql_chain import sql_chain

st.title("🤖 Virtual Database Assistant")

user_input = st.text_input("Your Question", "")

if user_input:
    chain = sql_chain()

    answer = chain.invoke(user_input)

    st.write("Response:", answer)
