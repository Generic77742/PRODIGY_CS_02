from PIL import Image

image = Image.open('original.png')
print(f'Original mode: {image.mode}')

rgba_image = image.convert('RGBA')
print(f'Converted mode: {rgba_image.mode}')

pixels = rgba_image.load()

width, height = rgba_image.size
for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        pixels[x, y] = (r, g, b, 128)

rgba_image.save('manipulated_rgba.png')
print('Saved manipulated RGBA image as manipulated_rgba.png')

rgb_image_reverted = rgba_image.convert('RGB')
print(f'Reverted mode: {rgb_image_reverted.mode}')

rgb_image_reverted.save('reverted_example.jpg')
print('Saved reverted image as reverted_example.jpg')
