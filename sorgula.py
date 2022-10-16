import requests
from bs4 import BeautifulSoup

URL_LIST = [
	"https://github.com/utkusen/turkce-wordlist/blob/master/wordlist.txt"
]

password = input("sifrenizi girin: ")

for _url in URL_LIST:
	page = requests.get(url=_url)
	soup = BeautifulSoup(page.content, "html.parser")
	results = soup.find(class_="highlight tab-size js-file-line-container js-code-nav-container js-tagsearch-file")
	if not results:
		split_list = _url.split("github.com")
		_url = split_list[0] + "raw.githubusercontent.com" + split_list[1]
		split_list = _url.split("/blob/")
		_url = split_list[0] + "/" + split_list[1]

		page = requests.get(url=_url)
		soup = BeautifulSoup(page.content, "html.parser")
		results = True if str(soup).strip().find("!cetin") != -1 else False

		print("sifreniz bulundu, lutfen sifrenizi guncelleyin." if results else "sifreniz bulunamadi")
		if (results): break
	

	results = True if results.find("td", string="ademelmasi") else False
	print("sifreniz bulundu, lutfen sifrenizi guncelleyin." if results else "sifreniz bulunamadi")
	if (results): break
