from PIL import Image


water = "watermark.png"
with Image.open(water) as img_water:
    img_water.load()


img_water = Image.open(water)
img_water = img_water.resize((img_water.width // 2, img_water.height // 2))


filename = "cat.jpg"
with Image.open(filename) as img:
    img.load()


img.paste(img_water, (60, 10), img_water) #paste() предоставляет возможность вставки одного изображения в другое изображение
img.save("watermark_cat.jpg")