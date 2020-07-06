from bs4 import BeautifulSoup
import requests
import string
from more_itertools import lstrip, strip

root_link = "http://www.blastwave-comic.com/index.php?p=comic&nro="
image_link = "http://www.blastwave-comic.com/"
comic_title = []
comic_link = []
exclude = set(string.punctuation)

for x in range(1, 87):
	response = requests.get(root_link + str(x))
	# response = requests.get(comic_link)
	soup = BeautifulSoup(response.content, "html.parser")
	body = soup.find("body")
	# print(body)
	image_src = body.find("img")
	image_name = image_src.attrs["alt"]
	image_name = ''.join(ch for ch in image_name if ch not in exclude)
	print("collecting: " + str(image_name))
	r = requests.get(image_link + image_src.attrs["src"])
	with open("images/" + image_name + ".png", "wb") as file:
		file.write(r.content)
