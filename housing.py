import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8')

# Title with your name (replace [Your Name] as needed)
st.title('California Housing Data (1990) by [Your Name]')

# Load data
df = pd.read_csv('housing.csv')

# Slider: Minimal Median House Value
house_value_slider = st.slider(
    'Minimal Median House Value',
    min_value=0,
    max_value=500001,
    value=200000
)

# Subheader
st.subheader('See more filters in the sidebar:')

# Sidebar widgets
# Multiselect for ocean_proximity, all selected by default
location_options = df['ocean_proximity'].unique()
ocean_filter = st.sidebar.multiselect(
    'Choose the location type',
    location_options,
    location_options
)

# Radio button for income level
income_selection = st.sidebar.radio(
    'Choose income level',
    ('Low', 'Medium', 'High')
)

# ---------------------- Filter dataframe ----------------------
# 1. Filter by median house value
filtered_df = df[df['median_house_value'] >= house_value_slider]

# 2. Filter by ocean proximity
filtered_df = filtered_df[filtered_df['ocean_proximity'].isin(ocean_filter)]

# 3. Filter by income level using if statement
if income_selection == 'Low':
    filtered_df = filtered_df[filtered_df['median_income'] <= 2.5]
elif income_selection == 'Medium':
    filtered_df = filtered_df[(filtered_df['median_income'] > 2.5) & (filtered_df['median_income'] < 4.5)]
elif income_selection == 'High':
    filtered_df = filtered_df[filtered_df['median_income'] >= 4.5]

# Show map of filtered districts
st.map(filtered_df)

# Histogram of median_house_value with 30 bins
st.subheader('Histogram of Median House Value')
fig, ax = plt.subplots()
ax.hist(filtered_df['median_house_value'], bins=30)
ax.set_xlabel('Median House Value')
ax.set_ylabel('Count')
st.pyplot(fig)
