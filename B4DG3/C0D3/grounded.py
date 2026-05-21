from PIL import Image, ImageDraw

img = Image.new("RGB", (20, 20), "white")

draw = ImageDraw.Draw(img)
draw.rectangle([(3, 0), (16, 19)], outline="black", fill="black", width=2)

draw.rectangle([(1, 1), (2, 3)], outline="black", fill="black", width=1)
draw.rectangle([(1, 6), (2, 8)], outline="red", fill="red", width=1)
draw.rectangle([(1, 11), (2, 13)], outline="red", fill="red", width=1)
draw.rectangle([(1, 16), (2, 18)], outline="black", fill="black", width=1)

draw.rectangle([(17, 1), (18, 3)], outline="black", fill="black", width=1)
draw.rectangle([(17, 6), (18, 8)], outline="red", fill="red", width=1)
draw.rectangle([(17, 11), (18, 13)], outline="black", fill="black", width=1)
draw.rectangle([(17, 16), (18, 18)], outline="black", fill="black", width=1)

img.save('grounded.png')
