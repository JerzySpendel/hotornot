import pathlib

from PIL import Image

dx, dy = 224, 224

Image.MAX_IMAGE_PIXELS = 379782144
image = Image.open('hotornot.jpg')

num_x = image.size[0] // dx
num_y = image.size[1] // dy

crop_dir: pathlib.Path = pathlib.Path(__file__).parent / 'crops'
if not crop_dir.exists():
    crop_dir.mkdir()

for index, (x, y) in enumerate([(dx*step_x, dy*step_y) for step_x in range(num_x) for step_y in range(num_y)]):
    box = (x, y, x + dx, y + dy)
    image_box = image.crop(box)
    image_box.save(crop_dir / f"{index}.jpg")
