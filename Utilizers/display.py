import streamlit as st
import pandas as pd

def display_extracted_data(data):
    extracted_df = pd.DataFrame(data)
    st.write("Extracted Data:")
    st.dataframe(extracted_df)

