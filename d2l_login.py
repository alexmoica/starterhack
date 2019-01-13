import requests
from robobrowser import*
from bs4 import*
import re
import log


link_avenue = "https://cap.mcmaster.ca/mcauth/login.jsp?app_id=1505&app_name=Avenue"

Browser = RoboBrowser()
Browser.open(link_avenue)
form = Browser.get_form()
#print(form)
form['user_id'].value = log.user
form['pin'].value =log.password
Browser.session.headers['Referer'] = link_avenue
Browser.submit_form(form)

#home = requests.get("https://avenue.cllmcmaster.ca/d2l/home")

with open("dump.txt", "w") as outfile:
	outfile.write(str(Browser.parsed))


Test_text = Browser.parsed.find(class_="d2l-navigation-s-item")
Test_text_all = Test_text.find('a')


n=Test_text_all.contents[0]
print(n)
