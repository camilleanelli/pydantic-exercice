from pydantic import BaseModel, field_validator, model_validator, Field
from typing import Optional


class Command(BaseModel):
  id: str
  produit: str
  quantite: int
  prix_unitaire: float
  reduction: Optional[float] = None
  prix_total: float


  @model_validator(mode="after")
  # on utilise model validator pour valider apres avoir crée une instance de la class Command
  # on crée la fonction de validation custom
  def calculate_total_price(self) -> 'Command':
    prix_calcule = self.quantite * self.prix_unitaire * (1 - self.reduction/100 if self.reduction else 1)
    prix_calcule = round(prix_calcule, 2)
    if abs(self.prix_total - prix_calcule) > 0.01:  # Tolérance pour les erreurs d'arrondi
        raise ValueError(f'Le prix total {self.prix_total} ne correspond pas au calcul {prix_calcule}')
    self.prix_total = prix_calcule
    return self

command_data = {
    "id": "CMD001",
    "produit": "Smartphone XYZ",
    "quantite": 2,
    "prix_unitaire": 599.99,
    "reduction": 10,
    "prix_total": 1079.98
  }

command = Command.model_validate(command_data)
print(command)

### Gestion des données manquantes et des valeurs par défaut

class Sondage(BaseModel):
  id: int
  question: str
  reponse: Optional[str] = None
  score: float = Field(default=0.0, ge=0.0, le=10.0)
  commentaire: str = ""

sondage_complet = Sondage(id=1, question="Êtes-vous satisfait ?", reponse="Oui", score=8.5)
print(sondage_complet)
sondage_partiel = Sondage(id=2, question="Do you like our service?")
print(sondage_partiel)
