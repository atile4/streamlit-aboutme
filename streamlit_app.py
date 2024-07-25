import streamlit as st

mainpage = st.Page("pages/main_page.py", title="Main Page", icon=":material/home:")
graphs = st.Page( "pages/graphs.py", title="Some Tetrio Stats", icon=":material/analytics:")
cats = st.Page( "pages/cats.py", title= "Meows", icon="😺")

pg = st.navigation([mainpage, graphs, cats])
st.set_page_config(page_title="About Me", page_icon=":material/edit:")

pg.run()