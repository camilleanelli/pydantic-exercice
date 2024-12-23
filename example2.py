from pydantic import BaseModel
from typing import List, Dict

class Address(BaseModel):
  rue: str
  ville: str
  code_postal: str

class Historic_sells(BaseModel):
  date: str
  montant: float
  produits: List[str]

class ClientComplet(BaseModel):
  id: int
  nom: str
  adresses: List[Address]
  historique_achats: List[Historic_sells]
  preferences: Dict[str, float]

client_data = {
  "id": 3,
    "nom": "Charlie Brown",
    "adresses": [
        {"rue": "123 Rue Principale", "ville": "Paris", "code_postal": "75001"},
        {"rue": "456 Avenue Secondaire", "ville": "Lyon", "code_postal": "69001"}
    ],
    "historique_achats": [
        {"date": "2023-03-15", "montant": 150.75, "produits": ["Livre", "DVD"]},
        {"date": "2023-04-01", "montant": 89.99, "produits": ["T-shirt", "Chaussettes"]}
    ],
    "preferences": {"Électronique": 0.8, "Livres": 0.6, "Vêtements": 0.4}
}

client_complet = ClientComplet(**client_data)
print(client_complet)




