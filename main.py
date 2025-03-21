

import streamlit as st
import importlib





# Page will not show the sidebar

st.set_page_config(initial_sidebar_state="collapsed", layout="wide")

# Initialize session state for tracking the active page
if "page" not in st.session_state:
    st.session_state.page = "about"  # Default page

def load_page(page_name):
    page_module = importlib.import_module(f'pages.{page_name}')
    page_module.show()

st.markdown("""
    <style>
        /* Top navigation bar styles */
    

        /* Button styles */
        .stButton {
            color: rgb(49, 51, 63);
            font-size: 20px;
            font-weight: bold;
            margin: 10px 0; /* Adjusted spacing between buttons */
            border: none;
            border-radius: 12px;
            cursor: pointer;
            padding: 15px 25px; /* Increased padding for a better appearance */
            transition: background-color 0.3s; /* Smooth transition for hover */
            background-color:rgb(71, 108, 209);
            box-shadow: 12px 12px 2px 1px rgba(65, 65, 182, 0.2);    
                }

        /* Hover effects, when the mouse is over it */

        .stButton:hover {
            background-color: rgba(255, 255, 255, 0.35);
        }

        /* Adjust active button style */
        .stButton:focus {
            background-color: rgba(255, 255, 255, 0.25);
        }
    </style>
""", unsafe_allow_html=True)

# st.markdown('<div class="topnav">', unsafe_allow_html=True)

# Create five columns for buttons
col1, col2, col3, col4 = st.columns(4)

# Define buttons in columns
with col1:
    if st.button('About'):
        st.session_state.page = "about"

with col2:
    if st.button('Process Data 📊'):
        
        st.session_state.page = "process"

with col3:
    if st.button('Visualization 🔍'):
        st.session_state.page = "visuals"
        

with col4:
    if st.button('Get my new dataset 🧠'):
        st.session_state.page = "download"

st.markdown('</div>', unsafe_allow_html=True)

# Display the selected page content based on session state
load_page(st.session_state.page)
