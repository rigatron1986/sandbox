from PIL import Image
im = Image.open(r"D:\telegram_bot\saved\thamizhselvi_\2022-04-22_06-00-55_UTC_1.webp").convert("RGB")
im.save("D:/test.jpg","jpeg")