import os
from dotenv import load_dotenv
import os
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
def getOneRecette(volaille : bool, viande : bool):
    if viande == True:
        recetteRandom = recettes.aggregate([{"$match": {"volaille":volaille}},{"$sample":{"size":1}}])
        for i in recetteRandom:
            i.pop("_id")
            return i
    else :
        recetteRandom = recettes.aggregate([{"$match": {"volaille":volaille,"viande":viande}},{"$sample":{"size":1}}])
        for i in recetteRandom:
            i.pop("_id")
            return i      


@app.get("/Xrecettes")
def getXrecettes(numberOfRecettes : int, volaille : bool, viande : bool):
    listRecettes= []

    if viande == True:
        weekRecette = recettes.aggregate([{"$match": {"volaille":volaille}},{"$sample":{"size":numberOfRecettes}}])
        for i in weekRecette:
            i.pop("_id")
            listRecettes.append(i)
        return listRecettes
    
    else :
        weekRecette = recettes.aggregate([{"$match": {"volaille":volaille,"viande":viande}},{"$sample":{"size":numberOfRecettes}}])
        for i in weekRecette:
            listRecettes.append(i)
        return listRecettes


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
    