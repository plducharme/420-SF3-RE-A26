import requests


# exemple d'appel d'API en utilisant la librairie requests
# Utilise l'API de https://dog.ceo/dog-api/
# Cet API n'utilise aucun token d'authentification ou ApiKey
class ChienApiClient:

    @staticmethod
    def get_random_dog() -> str:
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        return response.json()["message"]

    @staticmethod
    def get_all_breeds() -> dict:
        response = requests.get("https://dog.ceo/api/breeds/list/all")
        return response.json()["message"]

    @staticmethod
    def get_images_url_by_breed(breed: str) -> list:
        url = f"https://dog.ceo/api/breed/{breed}/images"
        print(f"get_images_url_by_breed: {url}")
        response = requests.get(url)
        return response.json()["message"]

    @staticmethod
    def get_image_data(url: str) -> bytes:
        print(f"get_image_data: {url}")
        response = requests.get(url)
        return response.content


