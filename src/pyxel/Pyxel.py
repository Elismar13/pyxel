from PIL import Image

class Pyxel():
  def __init__(self):
    self.image = None
    self.imageDimensions = tuple()
    super().__init__()
  
  def openImage(self, filePath: str):
    self.image = Image.open(filePath)
    self.imageDimensions = self.image.size

  def pixelColorCount(self):
    rgb_image = self.toColorPalette('RGB')
    width, height = self.imageDimensions
    pixel_color_count = dict()

    for x in range(width):
      for y in range(height):
        pixel = rgb_image.getpixel((x, y))

        if pixel in pixel_color_count:
          pixel_color_count[pixel] += 1
        else:
          pixel_color_count[pixel] = 1
    
    return pixel_color_count

  def toColorPalette(self, palette):
    return self.image.convert(palette)
