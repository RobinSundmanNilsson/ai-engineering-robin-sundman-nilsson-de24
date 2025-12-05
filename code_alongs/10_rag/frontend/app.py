import streamlit as st
import requests


def layout():
    st.markdown("# RAGbit")
    st.markdown("RAGbit is an expert in small rabbits")
    text_input = st.text_input("Ask a question")

    if st.button("send") and text_input.strip() != "":
        response = requests.post(
            "http://127.0.0.1:8000/rag/query", json={"prompt": text_input}
        )

        json_data = response.json()

        st.markdown("## Question:")
        st.markdown(text_input)
        
        st.markdown("## Answer")
        st.markdown(json_data["answer"])
        
        st.markdown("## Source")
        st.markdown(json_data["filepath"])



if __name__ == "__main__":
    layout()