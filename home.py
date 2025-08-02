import streamlit as st
import pandas


st.set_page_config(layout= "wide")
col1, col2 = st.columns(2)


with col1:
    st.image("images/photo.png", width= 300)
    
with col2:
    st.title("Charles Taylor")
    content = """
    Hi, I'm a spiring developer and data analyst—currently sharpening my skills and building 
    cool stuff along the way. All projects include this website was made using python and I will branch out into other languages 
    to showcase my continuous development as a developer and analyst.
    """
    st.info(content)

statement="""
Below you can find some the apps I have built in Python. Feel free to contact me!
"""
st.info(statement)

col3,empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("project data.csv", sep=",")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source code]({row['url']})")
        
        
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source code]({row['url']})")