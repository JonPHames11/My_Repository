import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("vehicles_us.csv")

st.header("Vehicle Data Explorer")

# Histogram of prices
fig_hist = px.histogram(df, x="price", nbins=50, title="Distribution of Vehicle Prices")
st.plotly_chart(fig_hist)

# Scatter plot: price vs odometer
if st.checkbox("Show scatter plot"):
    fig_scatter = px.scatter(df, x="odometer", y="price", color="model", title="Price vs. Odometer")
    st.plotly_chart(fig_scatter)
