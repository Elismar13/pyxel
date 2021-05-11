from PIL import Image

class Pyxel():
  def __init__(self):
    self.image = None
    self.imageDimensions = tuple()
    super().__init__()
  
  def openImage(self, filePath: str):
    self.image = Image.open(filePath)
    self.imageDimensions = self.image.size
  
  

