from PIL import Image
import os
arr = os.listdir("images")
print(arr)
img_list = []

for image in arr:
	page = Image.open("images/" + image)
	page = page.convert("RGB")
	img_list.append(page)

page.save(r"Gone with the Blastwave.pdf", save_all=True,
			  append_images=img_list)

