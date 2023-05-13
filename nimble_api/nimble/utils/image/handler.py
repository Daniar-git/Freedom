from dataclasses import dataclass

from defusedxml.ElementTree import fromstring
from PIL.Image import open


class ImageHandler:

    def get_image_dimensions(self, image):
        try:
            with open(image) as img:
                return img.width, img.height
        except Exception:
            return None

    def get_svg_dimensions(self, image):
        try:  # noqa: WPS229
            tree = fromstring(image.open().read())
            return tree.get('width', tree.get('height'))
        except Exception:
            return None

    def get_dimensions(self, image):
        image = self.get_image_dimensions(image)
        if image:
            return image
        svg = self.get_svg_dimensions(image)
        if svg:
            return svg
        return None



