import os
import sys
sys.path.insert(0,"/home/clement/Bureau/keskonbouf")
from dotenv import load_dotenv
import os
import json
from fastapi import FastAPI
from pymongo import MongoClient
from mongodbconnect import mongoConnect
load_dotenv()

# Connexion to the database
keskonbouf = mongoConnect('mongoUser',"mongoPass","keskonbouf","recettes")
recettes = keskonbouf.collection

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
    recetteRandom = recettes.find_one()
    recetteRandom.pop("_id")
    return recetteRandom

@app.get("/Xrecettes")
def getXrecettes(numberOfRecettes : int, volaille : bool, viande : bool):
    list= []
    for i in recettes.find({"$and" : [{"volaille":volaille}, {"viande" : viande}]}).limit(int(numberOfRecettes)):
        list.append(i)
    return list

@app.put("/nouvelleRecette")
def addOneRecette(recetteToAdd : dict):
    recettes.insert_one(recetteToAdd)

@app.delete("/deleteRecette")
def deleteOneRecette(recetteToDelete : str):
    recettes.delete_one({"name" : recetteToDelete})



if __name__ == "__main__":
    # DEV MODE: start local server for testing
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,)
    