from PIL import Image, ImageDraw
img = Image.new("RGB", (1200, 800), (240, 240, 240))
draw = ImageDraw.Draw(img)
draw.text((50, 50), "Lecture 5 Local Serverless Lab", fill=(0, 0, 0))
draw.text((50, 100), "Event-driven image processing pipeline", fill=(0, 0, 0))
img.save("/data/input/test_image.png")
print("Created /data/input/test_image.png")
