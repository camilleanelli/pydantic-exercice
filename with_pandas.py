import pandas as pd
from pydantic import BaseModel, Field, ValidationError, field_validator
from typing import List
from datetime import date

class Vente(BaseModel):
  date: date
  produit_id: int
  quantite: int = Field(gt=0)
  prix_unitaire: float = Field(gt=0)

  @field_validator('prix_unitaire')
  @classmethod
  def arrondir_prix(cls, value: float) -> float:
    return round(value, 2)

def data_validator(data: List[dict]) -> List[Vente]:
  valid_sells = []
  errors = []

  for index, data in enumerate(data):
    try:
      sell = Vente.model_validate(data)
      valid_sells.append(sell)
    except ValidationError as e:
      errors.append(f"Error line: {index + 1}: {e}")

  if errors:
    print("Detected errors:")
    for error in errors:
      print(error)

  return valid_sells


donnees_brutes = [
    {"date": "2023-08-01", "produit_id": 1, "quantite": 5, "prix_unitaire": 10.99},
    {"date": "2023-08-02", "produit_id": 2, "quantite": -1, "prix_unitaire": 15.50},  # Erreur : quantité négative
    {"date": "2023-08-03", "produit_id": 3, "quantite": 3, "prix_unitaire": 0},  # Erreur : prix nul
    {"date": "2023-08-04", "produit_id": 4, "quantite": 2, "prix_unitaire": 20.005},
]

ventes_validees = data_validator(donnees_brutes)

df_ventes = pd.DataFrame([v.model_dump() for v in ventes_validees])
print(df_ventes)
