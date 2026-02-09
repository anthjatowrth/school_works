import streamlit as st
import pandas as pd
import requests 

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv", sep=",")


st.title("Bienvenue sur le site web d'Anthony")
pickup = st.selectbox("Indiquez votre arrodissement de récupération",df['dropoff_borough'].unique().tolist())
st.write("Tu as choisis :", pickup)

url = "https://api.unsplash.com/search/photos"
params = {"query": pickup, "client_id": "bGs3AByT8I1C3jFoxXfbxsicR5sYmQkxOCqQNKcPxrA"}
response = requests.get(url, params=params)
data = response.json()
print(data)
image_url = data["results"][0]["urls"]["small"]

st.image(image_url)