from PIL import Image, ImageDraw

text = input("Enter text here:\t")

new = Image.new('RGB',(200,300),color=(3,252,232))

d=ImageDraw.Draw(new)
d.text((100,100),text,fill=(255,255,255))

new.show()