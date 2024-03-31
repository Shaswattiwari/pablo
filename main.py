import streamlit as st
from streamlit_lottie import st_lottie
import json
from streamlit_option_menu import option_menu

from assumptions import assumptions
from variables import variables
#from insights import insights


# Define the load_lottie function
def load_lottie(path):
    with open(path,"r") as f:
        return json.load(f)

# Create the main page layout
    
with st.container():
        with st.container():
            col1, col2 = st.columns([1,1])
            with col1:
                st.title('Pablo Sizing Engine')
                st.subheader('Use assumptions, variables, and visualizations for optimization of sizing.')

            with col2:
                st_lottie(load_lottie('Animation.json'))



with st.expander("Assumptions"):
       assumptions()
with st.expander("variables"):
        variables()




