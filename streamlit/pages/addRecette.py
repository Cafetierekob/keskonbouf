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
recetteName = st.text_input("Quel recette souhaitez-vous ajouter ?")

# Volaille ?
volaille = st.checkbox("La recette contient de la volaille")

# Viande ?
viande = st.checkbox("La recette contient de la viande")

# Where is the recette?
recetteLocation = st.selectbox("Où la recette est-elle stockée ?", ("Sur internet", "Recette officielle Mr Cuisine", "Dans un livre de recettes", "Dans le carnet de recette"))

# Precise localisation and data formalization
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
else:
    local = "mrCuisine"

# input to dic
if local == "mrCuisine":
    form = {"name" : recetteName, "volaille" : volaille, "viande" : viande, "localisation" : {"principal" : recetteLocation}}
elif local == "internet":
    form = {"name" : recetteName, "volaille" : volaille, "viande" : viande, "localisation" : {"principal" : recetteLocation, "url":url}}
elif local == "livre":
    form = {"name" : recetteName, "volaille" : volaille, "viande" : viande, "localisation" : {"principal" : recetteLocation, "title" : title, "page" : page}}
else :
    form = {"name" : recetteName, "volaille" : volaille, "viande" : viande, "localisation" : {"principal" : recetteLocation, "section" : section}}




# Add button
if st.button("Ajouter la recette !"):
    requests.put("http://0.0.0.0:8000/nouvelleRecette", data = json.dumps(form))
    st.text("La recette a bien été ajoutée !")
