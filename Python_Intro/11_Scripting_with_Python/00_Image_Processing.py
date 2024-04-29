from PIL import Image, ImageFilter

try:
    image = Image.open('./Pokedex/pikachu.jpg')

except (FileNotFoundError):
    print("Check file path")

print(image.format) # Prints "JPEG"
print(image.size)   # Prints "640 x 640"
print(image.mode)   # Prints "RGB"

filtered_image = image.filter(ImageFilter.BLUR)
filtered_image = filtered_image.rotate(90)
filtered_image = filtered_image.resize((300,300))
cropped_image = filtered_image.crop((100,100,400,400))

cropped_image.save('Cropped_Pika.png', 'png')
filtered_image.save('Blured_Pika.png', 'png')