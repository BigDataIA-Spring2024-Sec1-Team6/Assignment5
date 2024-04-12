import streamlit as st

def app():
    st.title("Generate Q/A")

    if st.button("Generate Question Bank"):
        # Generate question bank here
        st.write("50 questions generated and stored in Pinecone")
