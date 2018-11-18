import pathlib

import numpy as np
from PIL import Image

common_size = 100, 100

current_dir = pathlib.Path(__file__).parent
dogs_dir = current_dir / 'dogs'
hotdogs_dir = current_dir / 'hotdogs'

dogs = []
hotdogs = []

dogs_final_index = 1601
hotdogs_final_index = 1212

for dog_index in range(dogs_final_index + 1):
    dog_path = dogs_dir / "{dog_index}.png".format(dog_index=dog_index)
    if not dog_path.exists():
        continue

    dogs.append(np.array(Image.open(dog_path).resize(common_size)))

for hotdog_index in range(hotdogs_final_index + 1):
    hotdog_path = hotdogs_dir / "{hotdog_index}.png".format(hotdog_index=hotdog_index)
    if not hotdog_path.exists():
        continue

    hotdogs.append(np.array(Image.open(hotdog_path).resize(common_size)))


def dogs_and_hotdogs():
    return np.array(dogs), np.array(hotdogs)

