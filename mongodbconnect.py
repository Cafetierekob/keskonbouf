
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
load_dotenv()

class mongoConnect:
    def __init__(self,user,mdp,db,collection)-> None:
        self.user = os.getenv(user)
        self.mdp = os.getenv(mdp)
        self.db = db
        self.collectionName = collection
        self.uri = f"mongodb+srv://{self.user}:{self.mdp}@cluster0.ovnztph.mongodb.net"

        # Create a new client and connect to the server
        self.client = MongoClient(self.uri)

        # Connexion to the database
        self.db = self.client[self.db]

        # Connexion to collection
        self.collection = self.db[self.collectionName]



        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command('ping')
            return (print("Pinged your deployment. You successfully connected to MongoDB!"))
        except Exception as e:
            return (print(e))

