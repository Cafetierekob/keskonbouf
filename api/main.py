import os
from dotenv import load_dotenv
import os
import json
from fastapi import FastAPI
from pymongo import MongoClient
load_dotenv()

user = os.getenv("mongoUser")
mdp = os.getenv("mongoPass")
uri = f"mongodb+srv://{user}:{mdp}@cluster0.ovnztph.mongodb.net"

# Create a new client and connect to the server
client = MongoClient(uri)

# Connexion to the database
db = client["keskonbouf"]

# Connexion to the collection
recettes = db["recettes"]


# Instanciate the API controller

app = FastAPI(
    title="Keskonbouf",
    description="API de l'appli web Keskonbouf permettant de choisir un ensemble de recettes pour la semaine",
    version="0",
    openapi_tags=[

    ],
)

@app.get("/randomRecettes")
def getOneRecette():
    recette = recettes.find_one()
    recette.pop("_id")
    return recette

@app.put("/nouvelleRecette")
def addOneRecette(recetteToAdd : dict):
    recettes.insert_one(recetteToAdd)




if __name__ == "__main__":
    # DEV MODE: start local server for testing
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,)
    