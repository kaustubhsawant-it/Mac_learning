import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.datasets import load_iris

#title
st.title("Streamlit Visualizer App")

#Dataset - iris
iris = load_iris(as_frame=True)
df = iris.frame
print(df)

#sidebar
st.sidebar.header("Filter Options")
#mapping targets
target_names = ['Setosa','Versicolor','Virginica']
df['target'] = df['target'].map({0:'Setosa',1:'Versicolor',2:'Virginica'})
species = st.sidebar.multiselect("Select Species",df['target'].unique(),default=list(df['target'].unique()))

#filtered Data
filtered_df = df[df['target'].isin(species)]
st.write("Filtered Data ",filtered_df)

#Visualization Section
#Done individually 
st.html("<hr><h2>Visualization using Matplotlib</h2> <br><p>Individual Histogram</p>")
fig, ax = plt.subplots()
ax.hist(filtered_df['sepal length (cm)'],bins=15,color='orange',edgecolor='black')
ax.set_title("historgram - Sepal length")
st.pyplot(fig)

st.html("<p>Done using for loop</p>")
feature_names = ['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)']
for feature in feature_names:
    fig, ax = plt.subplots()
    ax.hist(filtered_df[f'{feature}'],bins=15,color='orange',edgecolor='black')
    ax.set_title(f"historgram - {feature}")
    st.pyplot(fig)

#seaborn 
st.html("<hr><h2>Visualization using Seaborn</h2> ")
fig2, ax2 = plt.subplots()
for feature in feature_names:
    sns.boxplot(x='target',y=f'{feature}', data=filtered_df, ax=ax2)
    ax2.set_title(f"BoxPlot - {feature} by Species")
    st.pyplot(fig2)


#plotly
st.html("<hr><h2>Visualization using Plotly</h2> ")

fig3 = px.scatter(
    filtered_df,
    x = 'sepal length (cm)',
    y = 'petal length (cm)' ,
    color = filtered_df['target'].astype(str),
    title="Plottly Scatter Plot - Sepal Vs Petal Length"
)
st.plotly_chart(fig3)

fig4 = px.scatter(
    filtered_df,
    x = 'sepal width (cm)',
    y = 'petal width (cm)',
    color = filtered_df['target'].astype(str),
    title="Plottly Scatter Plot - Sepal Vs Petal Width"
)
st.plotly_chart(fig4)

#Machine Learning
from sklearn.ensemble import RandomForestClassifier

st.sidebar.header("Model Input")

sl = st.sidebar.slider("Sepal Length",float(df['sepal length (cm)'].min()),float(df['sepal length (cm)'].max()))
sw = st.sidebar.slider("Sepal Width",float(df['sepal width (cm)'].min()),float(df['sepal width (cm)'].max()))
pl = st.sidebar.slider("Petal Length",float(df['petal length (cm)'].min()),float(df['petal length (cm)'].max()))
pw = st.sidebar.slider("Petal Width",float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))

input_df = pd.DataFrame([[sl,sw,pl,pw]], columns=iris.feature_names)

model = RandomForestClassifier()
model.fit(df[iris.feature_names],df['target'])
prediction = model.predict(input_df)[0]

st.subheader("Prediction")
st.write(f"Predicted Class: {prediction}")