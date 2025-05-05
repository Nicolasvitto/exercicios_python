from rembg import remove
from PIL import Image
input_image = Image.open('s.png')
output = remove (input_image)
output.save('img1.png')