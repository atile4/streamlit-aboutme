import streamlit as st
import numpy as np
from PIL import Image 

st.title("Atticus Wong")

col1, col2 = st.columns(2)

with col1:
   st.header("About Me")
   st.markdown("My name is Atticus Wong and I am currently a rising senior in high school. "
               "I enjoy making software programs and will sometimes dabble in machine learning."
               "I am planning on majoring in computer science or data science in college.")
   
   st.header("Hobbies")
   st.markdown("In my free time I like working on personal projects or playing Tetris and Minecraft.")

   st.header("Links")
   st.write("[Github](https://github.com/atile4) \n\n"
            "[Instagram](https://www.instagram.com/atticusw4/)")

img = Image.open("C:\\gitrepos\\AI Camp Guided Internship\\aboutme\\images\\20230630_102443.jpg")

with col2:
   st.image(img.rotate(-90), use_column_width=True)
   st.markdown("ID card from summer session at UCLA")

st.divider()

st.link_button("Email me!", "https://atticus1467@gmail.com/")



