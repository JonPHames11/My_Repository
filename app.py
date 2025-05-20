import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("vehicles_us.csv")

st.header("Vehicle Data Explorer")

# Histogram of prices
fig_hist = px.histogram(df, x="price", nbins=50, title="Distribution of Vehicle Prices")
st.plotly_chart(fig_hist)

# Determine median price
median_price = df["price"].median()

# Checkbox to toggle between cheap and expensive vehicles
show_expensive = st.checkbox("Show expensive vehicles (price above median)")

# Filter data based on checkbox
if show_expensive:
    filtered_df = df[df["price"] > median_price]
    title = "Expensive Vehicles: Price vs. Odometer"
else:
    filtered_df = df[df["price"] <= median_price]
    title = "Cheap Vehicles: Price vs. Odometer"

# Scatter plot: price vs odometer (filtered)
fig_scatter = px.scatter(filtered_df, x="odometer", y="price", color="model", title=title)
st.plotly_chart(fig_scatter)
