from PIL import Image
from PIL import ImageFilter

img=Image.open('bbt.jpg')
fmab=Image.open('fmab.jpg')
#print(img.size)
#print(format)
area=(100,100,300,375)
cropped_img=img.crop(area)

#img.show()
#cropped_img.show()

print(img.mode)

r,g,b=img.split()
r1,g1,b1=fmab.split()
#r.show()
#g.show()
#b.show()

new_img=Image.merge('RGB',(r,g,b))



#new_img.show()

got=Image.open('GoT.jpg')
sq_img=got.resize((500,500))
flip_img=got.transpose(Image.FLIP_LEFT_RIGHT)
rotate_img=got.transpose(Image.ROTATE_90)
#sq_img.show()
#flip_img.show()
#rotate_img.show()
