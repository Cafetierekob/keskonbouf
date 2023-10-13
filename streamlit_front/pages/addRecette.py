import streamlit as st
import requests
import json

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
st.header("Ajoutez une recette à votre carnet !")
st.divider()



# recette name
recetteName = st.text_input("Quelle recette souhaitez-vous ajouter ?")

# Type de recette
typeRecette = st.radio("C'est bon pour :",["L'apéro", "Le plat principal", "Le dessert"])

# Volaille ?
volaille = st.checkbox("La recette contient de la volaille")

# Viande ?
if volaille:
    viande = st.checkbox("La recette contient de la viande", value=True, disabled=True)
else:
    viande = st.checkbox("La recette contient de la viande")

# Saison ?
saison = st.selectbox("Est-ce un plat de saison ?",["Toutes saisons", "Printemps", "Été", "Automne", "Hiver"])

# Where is the recette?
recetteLocation = st.selectbox("Où la recette est-elle stockée ?", ("Sur internet", "Recette officielle Mr Cuisine", "Dans un livre de recettes", "Dans le carnet de recette", "Pas de recette précise"))

# Precise localisation
if recetteLocation == "Sur internet":
    url = st.text_input("URL de la recette")
    local = "internet"
elif recetteLocation == "Dans un livre de recettes":
    title = st.text_input("Nom du livre")
    page = st.text_input("N° de page")
    local = "livre"
elif recetteLocation == "Dans le carnet de recette":
    section = st.selectbox("Dans quelle section du carnet est-elle ?", ("Recettes salées", "Recettes sucrées"))
    local = "carnet"
elif recetteLocation == "Recette officielle Mr Cuisine":
    local = "mrCuisine"
else:
    local = "Sans recette"

# input to dict
if local == "mrCuisine":
    form = {"name" : recetteName, "typeRecette" : typeRecette, "volaille" : volaille, "viande" : viande, "saison" : saison, "localisation" : {"principal" : recetteLocation}}
elif local == "internet":
    form = {"name" : recetteName, "typeRecette" : typeRecette, "volaille" : volaille, "viande" : viande, "saison" : saison, "localisation" : {"principal" : recetteLocation, "url":url}}
elif local == "livre":
    form = {"name" : recetteName, "typeRecette" : typeRecette, "volaille" : volaille, "viande" : viande, "saison" : saison, "localisation" : {"principal" : recetteLocation, "title" : title, "page" : page}}
elif local == "carnet" :
    form = {"name" : recetteName, "typeRecette" : typeRecette, "volaille" : volaille, "viande" : viande, "saison" : saison, "localisation" : {"principal" : recetteLocation, "section" : section}}
else :
    form = {"name" : recetteName, "typeRecette" : typeRecette, "volaille" : volaille, "viande" : viande, "saison" : saison, "localisation" : {"principal" : recetteLocation}}



# Send to mongoDB
if st.button("Ajouter la recette !"):
    requests.put("http://api:8000/nouvelleRecette", data = json.dumps(form))
    st.text("La recette a bien été ajoutée !")
