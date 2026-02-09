import streamlit as st
import pandas as pd
import requests 
import json
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv", sep=",")


st.title("Bienvenue sur le site web d'Anthony")
pickup = st.selectbox("Indiquez votre arrodissement de récupération",df['dropoff_borough'].unique().tolist())
st.write("Tu as choisis :", pickup)

url = "https://api.unsplash.com/search/photos"
params = {"query": pickup, "client_id": "bGs3AByT8I1C3jFoxXfbxsicR5sYmQkxOCqQNKcPxrA"}
response = requests.get(url, params=params)
data = response.json()
image_url = data["results"][0]["urls"]["small"]

st.image(image_url)

st.divider()

st.title("Manipulation de données et création de graphiques")

path = "data"      
branch = "main"
api_url = "https://api.github.com/repos/mwaskom/seaborn-data/contents/raw?ref=master"
files = requests.get(api_url).json()
csv_files = [f for f in files if f["name"].endswith(".csv")]

csv_dict = {f["name"].replace(".csv", ""): f["download_url"]for f in csv_files}

dataset =st.selectbox('Quel dataset veux-tu utiliser', csv_dict.keys())

csv_url = csv_dict[dataset]

df = pd.read_csv(csv_url, sep =",")
st.subheader("Tableau de données")
st.dataframe(df)
colsX = st.selectbox("Choisissez la colonne X",df.columns)
colsY = st.selectbox("Choisissez la colonne Y",df.drop(columns = colsX).columns)

chart = st.selectbox("Quel graphique veux-tu utiliser",["bar_chart","line_chart","scatter_chart"] )
st.subheader("Graphique")
if chart == "bar_chart":
    st.bar_chart(df, x=colsX, y=colsY)
elif chart == "line_chart":
    st.line_chart(df, x= colsX, y =colsY)
else:
    st.scatter_chart(df, x=colsX, y=colsY)

show_corr = st.checkbox("Afficher la matrice de corrélation (Pearson)")

if show_corr:
    st.subheader("Matrice de corrélation")
    corr_matrix = df[[colsX, colsY]].corr()
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(corr_matrix,ax=ax, annot=False, cmap="rocket",square=True,cbar=True,linewidths=0.5)
    ax.set_title("Matrice de corrélation", fontsize=16, pad=12)
    st.pyplot(fig, clear_figure=True)
