from AnilistPython import Anilist
from PIL import Image
import requests


class AnimeData:

    def __init__(self):
        self.data = Anilist()

    def get_anime_data(self, word):
        return self.data.get_anime(word)

    def set_anime_image(self, anime):
        anime_data = self.data.get_anime(anime)
        # Send GET request
        url = anime_data['cover_image']
        headers = {'User-agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        file_name = "cover_img.jpg"
        # Save the image
        if response.status_code == 200:
            with open(file_name, "wb") as f:
                f.write(response.content)
        else:
            print(response.status_code)

if __name__ == "__main__":
    data = AnimeData()
    print(data.set_anime_image("spy family"))