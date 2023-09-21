import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Get data from happy.csv into a dataframe
happiness_df = pd.read_csv("happy.csv")

# Get all the column names from the dataframe
csv_cols = happiness_df.columns.values

print(type(csv_cols))

print(happiness_df)

st.title("In Search for Happiness")
xaxis = st.selectbox("Select the data for the x-axis",
                      csv_cols)
yaxis = st.selectbox("Select the data for the y-axis",
                      csv_cols)

st.subheader(f"{xaxis} and {yaxis}")

figure = px.scatter(x=getattr(happiness_df, xaxis.lower()), y=getattr(happiness_df, yaxis.lower()), labels={"x": xaxis.capitalize(), "y": yaxis.capitalize()})
st.plotly_chart(figure)

