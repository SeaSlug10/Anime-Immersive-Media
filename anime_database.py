from AnilistPython import Anilist
from PIL import Image
import requests


class AnimeData:

    def __init__(self):
        self.data = Anilist()

    def get_anime_data(self, word):
        try:
            return self.data.get_anime(word)
        except:
            return None

    def set_anime_image(self, anime):
        anime_data = self.data.get_anime(anime)
        for data, filename in [('cover_image', "cover_img.jpg"), ('banner_image', "banner_img.jpg")]:
            # Send GET request
            url = anime_data[data]
            if url != None:
                headers = {'User-agent': 'Mozilla/5.0'}
                response = requests.get(url, headers=headers)
                file_name = filename
                # Save the image
                if response.status_code == 200:
                    with open(file_name, "wb") as f:
                        f.write(response.content)
                else:
                    print(response.status_code)

if __name__ == "__main__":
    data = AnimeData()
    print(data.get_anime_data("itadaki seiki"))