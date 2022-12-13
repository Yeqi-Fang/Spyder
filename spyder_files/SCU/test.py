from PIL import Image
a = Image.open(r"D:\multi_media\DeskTop\test.png")
a = a.crop((1270, 850, 1440, 925))
a.save(r"D:\multi_media\DeskTop\test1.png")