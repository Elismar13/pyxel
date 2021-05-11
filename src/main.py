import os
from pyxel.Pyxel import Pyxel

imagePath = os.path.normpath(os.getcwd() + os.sep + 'Syngenta.bmp')

pyxel = Pyxel()
pyxel.openImage(imagePath)
pixelsCount = pyxel.pixelColorCount()

for rgbColor in pixelsCount.keys():
  if(rgbColor[0] != 0 and rgbColor[0] != 255):
    print(f"A imagem possui {pixelsCount[rgbColor]} pixels do tom de verde. RGB: {rgbColor}.")

message = pyxel.readTextFromImage()
print(f"A mensagem escondida é:\n\'{message.strip()}\'")