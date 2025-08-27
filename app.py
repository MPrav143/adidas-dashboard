import streamlit as st
import pandas as pd
import datetime
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

# Set page config
st.set_page_config(page_title="Adidas Dashboard", layout="wide")
st.markdown('<style>div.block-container{padding-top:1rem}</style>', unsafe_allow_html=True)

# Load Excel file
try:
    df = pd.read_excel("Adidas.xlsx")
    st.write("Excel file loaded successfully!")
except Exception as e:
    st.error(f"Error loading Excel file: {e}")
    st.stop()  # stop if data doesn't load

# Load logo
try:
    image = Image.open("adidas-logo.jpg")
    st.image(image, width=200)
except Exception as e:
    st.warning(f"Could not load logo: {e}")

# Show basic info
st.title("📊 Adidas Sales Dashboard")
st.write("Here’s a preview of the dataset:")
st.dataframe(df.head())

# Simple chart (example)
if "Total Sales" in df.columns and "Region" in df.columns:
    fig = px.bar(df, x="Region", y="Total Sales", color="Region", title="Sales by Region")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No 'Region' and 'Total Sales' columns found to plot a chart.")
