import streamlit as st
from PIL import Image

def show():
    st.markdown("<h1 style='text-align: center;'>👨‍💻 About Pre-Prox</h1>", unsafe_allow_html=True)
    
    # Create two columns for layout
    col1, col2 = st.columns([2, 1])

    with col1:
        # Add description
        st.markdown("""
        ### Hey there! 👋

        I'm Oween, an **AI student** 👨‍💻 who's always busy working on projects and my part-time job.  
        In an effort to optimize my time, I developed **Pre-Prox**, an app that helps me save time by automating the tedious process of cleaning and preparing data. This was something I had to do over and over again, and **Pre-Prox** truly saved me a lot of time ⏳!

        This app isn't just for me though; it's built to help **students** like you who are working on **Machine Learning (ML) projects**. Whether you're dealing with **data cleaning**, **visualization**, or deciding which **ML model** to choose — Pre-Prox is here to help!

        With **Pre-Prox**, you can:
        - Clean your data quickly 🧹
        - Visualize the relationships between your features 📊
        - Decide on the best ML approach (Classification, Regression, etc.) 🧠

        **Pre-Prox** is designed to make your ML journey easier and more efficient. Plus, the source code is available for you to explore and use in your own projects! 🚀

        [Find the source code here!](https://github.com/OweenCesar?tab=repositories) 💻

        _Let's make your data prep faster and smarter with Pre-Prox!_
                    
        Best Regards, 
        Oween Cesar
        """)

    with col2:
        # Add an image
        image = Image.open('images/pre_prox.jpeg')  # Make sure to change this to your image path
        st.image(image, caption="Pre-Prox - Data Science Made Simple", use_container_width=True)

 
