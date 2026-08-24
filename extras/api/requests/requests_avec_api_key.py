import requests
import json


class GitHubClient:

    # Le constructeur prend un token en paramètre et initialise une session avec les entêtes nécessaires
    # Pour générer un "fine-grained token", allez sur github.com, cliquez sur votre avatar, puis sur "Settings",
    # ensuite sur "Developer settings", puis sur "Personal access tokens", "fined-grained access token" et générer un
    # token.
    def __init__(self, token: str):
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": "Bearer " + token,
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
        })

    def get_repos(self):
        response = self.session.get("https://api.github.com/user/repos")
        return response.json()

    @staticmethod
    def sauvegarder_json(json_doc: dict, fichier: str):
        with open(fichier, "w") as f:
            f.write(json.dumps(json_doc, indent=4))


# Passer le token de votre "fine-grained token" ici
ghc = GitHubClient("votre_token")
GitHubClient.sauvegarder_json(ghc.get_repos(), "repolist.json")

