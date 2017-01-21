from bs4 import BeautifulSoup
messages = open('messages.txt', 'w')

soup = BeautifulSoup(open("Facebook Data/html/messages.htm"), 'lxml')
for message in soup.findAll("div", {"class":"message"}):
	for name in message.findAll("span", {"class": "user"}):
		if name.text == "Glenn Ren":
			# print message.find_next_siblings('p')[0].text
			messages.write((message.find_next_siblings('p')[0].text + '\n').encode('ascii', 'ignore'))