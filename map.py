from PIL import Image
im = Image.open('/home/marcel/Bilder/python.png')
im.resize((300,300),Image.ANTIALIAS)
print(im.size)
Image._show(im.resize((300,300),Image.ANTIALIAS))