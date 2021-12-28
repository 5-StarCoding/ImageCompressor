from PIL import Image
from tkinter.filedialog import *

file_name = askopenfilename()
img = Image.open(file_name)
width , height = img.size
compressed_image = img.resize((height,width),Image.ANTIALIAS)
save = asksaveasfilename()
compressed_image.save(save + "_compressed.jpg")
