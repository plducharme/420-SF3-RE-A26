from huggingface_hub import InferenceClient
import json
from enum import Enum
from PIL import Image


class HuggingFaceClient:
    def __init__(self):
        with open("client.json") as client_json:
            data = json.load(client_json)
            token = data.get("access_token")
            if not token:
                raise ValueError("Jeton d'accès non trouvé dans client.json")
            self.token = token

    def executer_requete_chat(self, modele: str, fournissseur: Enum, texte_input: str):
        client = InferenceClient(model=modele, token=self.token, provider=fournissseur.value)
        client.chat.completions.create(
            messages=[{"role": "user", "content": texte_input}],
            stream=False,
        )
        completion = client.chat.completions.create(
            messages=[{"role": "user", "content": texte_input}],
            stream=False,
        )
        return completion.choices[0].message

    def generer_image(self, modele: str, texte_input: str, fournissseur: Enum):
        client = InferenceClient(model=modele, token=self.token, provider=fournissseur.value)
        image = client.text_to_image(prompt=texte_input, model=modele)
        image.show()

    def generer_image_pil(self, modele: str, texte_input: str, fournissseur: Enum):
        client = InferenceClient(model=modele, token=self.token, provider=fournissseur.value)
        image = client.text_to_image(prompt=texte_input, model=modele)
        return image


class Fournisseur(Enum):
    CEREBRAS = "cerebras"
    FAL_AI = "fal-ai"
    FIREWORKS = "fireworks-ai"
    HF_INFERENCE = "hf-inference"
    HYPERBOLIC = "hyperbolic"
    NEBIUS = "nebius"
    NOVITA = "novita"
    OPENAI = "openai"
    REPLICATE = "replicate"
    SAMBANOVA = "sambanova"
    TOGETHER = "together"
    BLACK_FOREST_LABS = "black-forest-labs"
    COHERE = "cohere"


if __name__ == "__main__":
    client = HuggingFaceClient()
    # Exemple d'utilisation chat
    # requete_chat = "Quel est le meilleur film de tous les temps?"
    # reponse = client.executer_requete_chat("deepseek-ai/DeepSeek-V3-0324", Fournisseur.FIREWORKS, requete_chat)
    # print(reponse)

    # Exemple de génération d'image
    texte_image = "Un ornithorynque humanoïde qui joue de la guitare sur une plage"
    client.generer_image("black-forest-labs/FLUX.1-dev", texte_image, Fournisseur.FAL_AI)

