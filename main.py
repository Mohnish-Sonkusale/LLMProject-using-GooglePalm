import streamlit as st
from llm_code import create_vector, QA_retriever

st.title("LLM Project 🤖 ")
btn = st.button("Create DB and save ") # it only have the acess of the developer
if btn:
    create_vector()

question = st.text_input("Question: ")

if question:
    chain = QA_retriever()
    response = chain(question)

    st.header("Answer")
    st.write(response["result"])

