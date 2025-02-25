# Import packages

import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

# Run the app
st.set_page_config(page_title="Happiness Dashboard", layout="wide")

# Load dataset
file_path = "worldhappiness.csv"
df = pd.read_csv(file_path)
df.head()
df.info()

# Compute globle average for each year
# Note: only 2 years with happiness score
global_avg = df.groupby("year")['Happiness Score'].mean().reset_index()
global_avg["Country"] = "Global Average"
#global_avg

# Streamlit UI
st.title("Happiness Score Dashboard")

# Country selection dropdown
selected_country = st.selectbox("Select a Country", df["Country"].dropna().unique())

# Filter data for the selected country
country_data = df[df["Country"] == selected_country]


# Line chart for happiness trend
st.subheader(f"Happiness Score Trend for {selected_country}")
fig_line = px.line(country_data, x="year", y="Happiness Score", markers=True, title=f"Happiness Score Trend for {selected_country}")
st.plotly_chart(fig_line)

# Grouped bar chart comparing with global average
compare_data = pd.concat([country_data, global_avg])
st.subheader(f"Comparison of {selected_country} with Global Average")
fig_bar = px.bar(compare_data, x="year", y="Happiness Score", color="Country", barmode="group", title=f"Comparison of {selected_country} with Global Average")
st.plotly_chart(fig_bar)


# Run the app
#st.set_page_config(page_title="Happiness Dashboard", layout="wide")
