import streamlit as st
import requests
from pathlib import Path

ASSETS_PATH = Path(__file__).absolute().parents[1] / "assets"

def layout():

    st.markdown("# RAGbit")
    st.markdown("Ask a question about different dwarf rabbits")
    text_input = st.text_input(label="Ask a questions")

    if st.button("Send") and text_input.strip() != "":
        response = requests.post(
            "http://127.0.0.1:8000/rag/query", json={"prompt": text_input}
        )

        data = response.json()

        st.markdown("## Question:")
        st.markdown(text_input)

        st.markdown("## Answer:")
        st.markdown(data["answer"])

        st.markdown("## Source:")
        st.markdown(data["filepath"])

        img_name = data.get("filename")
        # Safeguard: only try to load an image when we actually have a filename that exists on disk
        if img_name and str(img_name).lower() != "none" or "N/A":
            img_path = ASSETS_PATH / f"{img_name}.png"
            if img_path.exists():
                st.image(img_path)
            else:
                st.warning(f"Image not found for '{img_name}'.")
        else:
            st.warning("No image available for this answer.")

if __name__ == "__main__":
    layout()
