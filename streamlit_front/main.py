import sys
sys.path.insert(0,"/home/clement/Bureau/keskonbouf")
import streamlit as st
import requests
import pandas as pd

# Page metadata
st.set_page_config(
    page_title="Keskonbouf",
    page_icon=":spaghetti:",
    layout="centered",
    menu_items={
        "About": "Comment is free :smiling_imp: :crystal_ball:  \n_but facts are sacred_ :angel: :abacus:"
    },
)

# Page title
st.title("Keskonbouf :spaghetti:")
st.header("Générateur de planning de repas")
st.divider()

# Get a random recette
st.header("Besion d'une seule recette ?")

végé = st.checkbox("Végétarienne") # Végé or not


if végé:
    volaille = st.checkbox("Sans volaille",value= True, disabled=True) # with volaille or not
else:
    volaille = st.checkbox("Sans volaille")

végé = not végé
volaille = not volaille # Changing from "without viande" to "végé"


# fetch recette
submitted = st.button("Let's go !")
if submitted:
    parametres = {"volaille" : volaille,"viande" : végé}
    recette = requests.get("http://0.0.0.0:8000/randomRecettes", params=parametres)
    recette = recette.json()
    if recette == None:
        st.write("Aucune recette ne correspond à votre recherche")
    elif recette["localisation"]["principal"] == "Sur internet":
        st.write(f"{recette['name']}")
        st.write(f"La recette se trouve [ici]({recette['localisation']['url']})")
    elif recette["localisation"]["principal"] == "Dans un livre de recettes":
        st.write(f"{recette['name']}")
        st.write(f"La recette se trouve dans le livre {recette['localisation']['title']} à la page {recette['localisation']['page']}")
    elif recette["localisation"]["principal"] == "Recette officielle Mr Cuisine":
        st.write(f"{recette['name']}")
        st.write(f"La recette se trouve directement dans le Mr Cuisine")
    elif recette["localisation"]["principal"] == "Dans le carnet de recette":
        st.write(f"{recette['name']}")
        st.write(f"La recette se trouve dans le carnet de recettes dans la section {recette['localisation']['section']}")
    else :
        st.write(f"{recette['name']}")
st.divider()

# Get X recette for the week
st.header("Planning de la semaine")

# Dataframe of a week. 
with st.form("Semaine"):
    colonnes = {"Lundi": [False,False],"Mardi": [False,False],"Mercredi": [False,False],"Jeudi": [False,False],"Vendredi": [False,False],"Samedi": [False,False],"Dimanche": [False,False]}
    df = pd.DataFrame(data=colonnes, index=["Midi","Soir"] )
    edited_df = st.data_editor(df)

    formButton = st.form_submit_button("Let's Go !")

# Number of recettes
    if formButton:
        for column in df:
            a = edited_df[column].isin([True]).sum()
            if a != 0:
                nbr = edited_df.value_counts(column)[True].sum().sum()
                total += nbr
        st.write(total)

# Get recettes

