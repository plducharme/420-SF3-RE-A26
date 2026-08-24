from fastapi import FastAPI, Body

from etudiant import Etudiant


app = FastAPI()

# Normalement, on devrait utiliser une base de données pour stocker les étudiants.
# Pour les fins de l'exemple, on va utiliser une liste.
etudiants = []

@app.get("/etudiants")
async def liste_etudiants():
    return etudiants

@app.get("/etudiant/{no_da}")
async def get_etudiant(no_da: int):
    for etudiant in etudiants:
        if etudiant.no_da == no_da:
            return etudiant
    return "Étudiant introuvable"

@app.post("/etudiant/")
async def ajout_etudiant(etudiant: Etudiant = Body(...)):
    etudiants.append(etudiant)
    return etudiant

@app.delete("/etudiant/{no_da}")
async def supprimer_etudiant(no_da: int):
    for etudiant in etudiants:
        if etudiant.no_da == no_da:
            etudiants.remove(etudiant)
            return
    return "Étudiant introuvable"

@app.put("/etudiant/{no_da}")
async def modifier_etudiant(no_da: int, etudiant: Etudiant):
    for item in etudiants:
        if item.no_da == no_da:
            item.nom = etudiant.nom
            item.prenom = etudiant.prenom
            item.no_da = etudiant.no_da
            return etudiant
    return "Étudiant introuvable"

# Pour tester l'API, on peut utiliser l'outil curl ou Postman

# pour exécuter le serveur, on peut utiliser la commande: fastapi dev exemple_server.py
# ou: python -m uvicorn exemple_server:app --reload


# La documentation sera automatiquement générée par FastAPI à l'adresse http://127.0.0.1:8000/docs


