from pathlib import Path

from django.conf import settings
from PIL import Image


def resize_image(image_django, new_width, optimaze=True, quality=60):
    image_path = Path(settings.MEDIA_ROOT / image_django.name).resolve()
    image_pillow = Image.open(image_path)
    orignal_width, original_height = image_pillow.size

    if orignal_width <= new_width:
        image_pillow.close()
        return image_pillow

    new_height = round(new_width * original_height / orignal_width)
    new_image = image_pillow.resize((new_width, new_height), Image.LANCZOS)
    new_image.save(
        image_path,  # caminho
        optimize=optimaze,
        quality=quality
    )
