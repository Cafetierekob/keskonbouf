import sys
sys.path.insert(0,"/home/clement/Bureau/keskonbouf")
import streamlit as st
import requests
import pandas as pd
import datetime

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
st.title("Keskonbouf ce soir ?:spaghetti:")
st.header("Générateur de planning de repas")
st.divider()


# Get a random recette 
st.header("Besoin d'une seule recette ?")

typeOfPlate = st.selectbox("Quel type de recette souhaitez-vous ?", ("Plat Principal","Apéro", "Entrée",  "Dessert"))

# Random recette (Apéro, Entrée, Plat principal)
if typeOfPlate != "Dessert":
    végé = st.checkbox("Végétarienne") # Végé or not
    if végé:
        volaille = st.checkbox("Sans volaille",value= True, disabled=True) # with volaille or not
    else:
        volaille = st.checkbox("Sans volaille")
    végé = not végé
    volaille = not volaille # Changing from "without viande" to "végé"
    deSaison = st.checkbox("100\% de saison") # Only seasonal recipees
    myDatetime = datetime.datetime.today().strftime('%m') # Date for seasonal recipe
    if myDatetime in ["3","4","5"]:
        saisonActuelle = "Printemps"
    elif myDatetime in ["6","7","8"]:
        saisonActuelle = "Été"
    elif myDatetime in ["9","10","11"]:
        saisonActuelle = "Automne"
    else :
        saisonActuelle = "Hiver"

# fetch recette
    submitted = st.button("Let's go !")
    if submitted:
        parametres = {"volaille" : volaille,"viande" : végé, "deSaison" : deSaison, "saison" : saisonActuelle}
        recette = requests.get("http://api:8000/randomRecettes", params=parametres)
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


else : #random dessert
    submitted_dessert = st.button("Let's go !")
    if submitted_dessert:
        recette = requests.get("http://api:8000/dessert")
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

colonnes = {"Lundi": [False,False],"Mardi": [False,False],"Mercredi": [False,False],"Jeudi": [False,False],"Vendredi": [False,False],"Samedi": [False,False],"Dimanche": [False,False]}
df = pd.DataFrame(data=colonnes, index=["Midi","Soir"] )
edited_df = st.data_editor(df)


végé = st.checkbox("Végétarienne", key="multipleRecettesVege") # Végé or not
if végé:
    volaille = st.checkbox("Sans volaille",value= True, disabled=True, key="multipleRecettesVolaille") # with volaille or not
else:
    volaille = st.checkbox("Sans volaille",key="multipleRecettesVolaille")

végé = not végé
volaille = not volaille # Changing from "without viande" to "végé"

button = st.button("Let's Go !")

# Number of recettes
total=0
if button:
    for column in df:
        a = edited_df[column].isin([True]).sum()
        if a != 0:
            nbr = edited_df.value_counts(column)[True].sum().sum()
            total += nbr
    if total == 0:
        st.write("Pas besoin de recette si on mange pas de la semaine !")
    else:
# Get recettes
        parametres = {"numberOfRecettes":total,"volaille":volaille,"viande":végé}
        recettes = requests.get("http://api:8000/Xrecettes", params=parametres)
        recettes = recettes.json()
        if recettes == []:
            st.write("Aucune recette ne correspond à votre demande")
        else:
            for i in recettes:
                st.write(i)