import streamlit as st


st.set_page_config(layout= "wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width= 300)
    
with col2:
    st.title("Charles Taylor")
    content = """
    Hi, my name is Charles Taylor and a spiring programmer and data analyst—currently sharpening my skills and building 
    cool stuff along the way.
    """
    st.info(content)