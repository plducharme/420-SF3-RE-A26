# doit installer PyTorch (torch) et transformers (transformers) pour exécuter ce code
# Attention, le package torch est très volumineux
# La génération d'images nécessite un GPU (carte graphique) avec au moins 16 Go de mémoire
# Pour le moment, sentencepiece supporte uniquement Python <=3.11
# pour faciliter le tout: dans le répertoire, pip install -r requirements.txt
import datetime
import os
from diffusers import FluxPipeline, AutoPipelineForText2Image
from transformers import pipeline
import torch


# La première fois que vous exécutez ce code, il va télécharger le modèle sur votre machine.
# Ceci peut prendre un certain temps
class ExemplesPipeline:

    # Classification si un texte est neutre, positif ou négatif
    @staticmethod
    def classification_sentiment_texte(texte):
        modele = "cardiffnlp/twitter-roberta-base-sentiment-latest"
        classifieur = pipeline("sentiment-analysis", model=modele)
        # le résultat est une liste de dictionnaires. label est la classe prédite (positive, négative, neutre)
        # et score est la probabilité que ça appartienne à cette classe (niveau de confiance)
        resultats = classifieur(texte)
        return resultats

    @staticmethod
    def texte_vers_image(texte):
        # Ceci utilise le GPU (carte graphique) pour le calcul. Si vous en avez plusieurs, vous pouvez changer l'index
        # de cuda
        pipeline = AutoPipelineForText2Image.from_pretrained('black-forest-labs/FLUX.1-dev',
                                                             torch_dtype=torch.bfloat16).to('cuda:0')
        pipeline.load_lora_weights('openfree/flux-chatgpt-ghibli-lora',
                                   weight_name='flux-chatgpt-ghibli-lora.safetensors')
        image = pipeline(texte).images[0]
        nom_fichier = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
        image.save(nom_fichier)
        return nom_fichier

    def conversation(self, texte):
        modele = "meta-llama/Llama-3.3-70B-Instruct"
        pipeline = FluxPipeline.from_pretrained(modele, torch_dtype=torch.bfloat16).to('cuda:0')
        pipeline.load_lora_weights('openfree/flux-chatgpt-ghibli-lora',
                                   weight_name='flux-chatgpt-ghibli-lora.safetensors')
        reponse = pipeline(texte)
        return reponse



if __name__ == "__main__":
    liste_textes = ["I hate chocolate", "I love chocolate", "I ate chocolate", "The chocolate is black"]

    for texte in liste_textes:
        resultats = ExemplesPipeline.classification_sentiment_texte(texte)
        print(f"Texte : {texte}")
        print(f"Résultats : {resultats}")

    # ExemplesPipeline.texte_vers_image("Un mouton faisant du surf sur une vague de chocolat")
