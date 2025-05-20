import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv("vehicles_us.csv")

st.header("Vehicle Data Dashboard")

# Histogram of price distribution
fig_hist = px.histogram(df, x="price", nbins=50, title="Distribution of Vehicle Prices")
st.plotly_chart(fig_hist)

# Checkbox to show scatter plot
if st.checkbox("Show Price vs. Odometer Scatter Plot"):
    fig_scatter = px.scatter(df, x="odometer", y="price", color="model", title="Price vs. Odometer")
    st.plotly_chart(fig_scatter)
