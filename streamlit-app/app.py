import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from collections import namedtuple

# Define a namedtuple to store points in the spiral
Point = namedtuple('Point', ['x', 'y'])

# Function to generate the spiral data
def generate_spiral(num_points, num_turns):
    data = []
    for i in range(num_points):
        angle = 2 * np.pi * num_turns * (i / num_points)
        radius = i / num_points
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        data.append(Point(x, y))
    return data

# Streamlit App Layout
st.title("Interactive Spiral Visualization")

# Sliders for user input
num_points = st.slider('Number of Points in Spiral', min_value=50, max_value=1000, value=500)
num_turns = st.slider('Number of Turns in Spiral', min_value=1, max_value=10, value=5)

# Generate the spiral data
spiral_data = generate_spiral(num_points, num_turns)

# Convert the spiral data to a DataFrame for visualization
spiral_df = pd.DataFrame(spiral_data, columns=['x', 'y'])

# Create the Altair chart to visualize the spiral
chart = alt.Chart(spiral_df).mark_circle(size=3).encode(
    x='x',
    y='y'
).properties(
    width=600,
    height=600
)

# Display the chart
st.altair_chart(chart, use_container_width=True)
