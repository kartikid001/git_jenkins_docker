import streamlit as st
import pandas as pd

data ={
    "Task": ["Extraxt", "Transform", "Load"],
    "Status": ["Done", "Processing", "Pending"],
    "Code": [12044, 76542, 96753]
}

df = pd.DataFrame(data)
st.text("Stream 2")
st.write(df)