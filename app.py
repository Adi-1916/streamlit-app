# Import the libraries
import streamlit as st
from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = load_iris()
data = pd.DataFrame(iris.data, columns=iris.feature_names)
data['target'] = iris.target
target_names = iris.target_names

# Set the title and sidebar
st.title("Iris Dataset Visualizer")
st.sidebar.title("Visualizations")
st.sidebar.subheader("Choose a feature to plot")

# Create a sidebar with checkboxes for the features
feature_list = st.sidebar.multiselect(
    "Features",
    iris.feature_names,
    default=["sepal length (cm)", "sepal width (cm)"]
)

# Set random colors for the scatter plots
np.random.seed(0)
colors = sns.color_palette("bright", len(target_names))

# Create a scatter plot for each feature pair using Seaborn
if len(feature_list) > 1:
    for i in range(len(feature_list)):
        for j in range(i + 1, len(feature_list)):
            x_axis = feature_list[i]
            y_axis = feature_list[j]
            fig, ax = plt.subplots()
            for k, target_name in enumerate(target_names):
                sns.scatterplot(
                    x=x_axis,
                    y=y_axis,
                    data=data[data['target'] == k],
                    label=target_name,
                    color=colors[k]
                )
            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)
            ax.legend()
            st.pyplot(fig)
else:
    st.write("Please select at least two features.")

# Create a scatter plot for each feature pair using Plotly
if len(feature_list) > 1:
    fig = px.scatter_matrix(
        data,
        dimensions=feature_list,
        color="target",
        color_discrete_sequence=colors,
        title="Scatter Matrix"
    )
    st.plotly_chart(fig)
else:
    st.write("Please select at least two features.")
