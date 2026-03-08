import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("CMC Manufacturing Analytics Dashboard")

df = pd.read_csv("data/processed/training_dataset.csv")

st.subheader("Yield Distribution")

fig, ax = plt.subplots()

ax.hist(df["Yield"])

st.pyplot(fig)

st.subheader("Impurity vs Temperature")

fig, ax = plt.subplots()

ax.scatter(df["Reactor_Temp"], df["Total_Impurity"])

ax.set_xlabel("Temperature")

ax.set_ylabel("Total Impurity")

st.pyplot(fig)
