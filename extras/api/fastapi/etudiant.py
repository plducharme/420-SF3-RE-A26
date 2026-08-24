

from pydantic import BaseModel


class Etudiant(BaseModel):
    nom: str
    prenom: str
    no_da: int

