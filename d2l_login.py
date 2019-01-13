import requests
from robobrowser import*
from bs4 import*
import re
import log

#direct link to 
link_avenue = "https://cap.mcmaster.ca/mcauth/login.jsp?app_id=1505&app_name=Avenue"

Browser = RoboBrowser()
Browser.open(link_avenue)
form = Browser.get_form()
#user name and pass is submitted to its respected fields (result: Successful)---------- change log.user and password. 
form['user_id'].value = log.user
form['pin'].value =log.password
Browser.session.headers['Referer'] = link_avenue
Browser.submit_form(form)

#copying the html code into a text file named dump.txt (result: Successful)
with open("dump.txt", "w") as outfile:
	outfile.write(str(Browser.parsed))

#string variable var is what we need to search in the dump file created,

var = "d2l-textblock d2l_1_111_"
Test_text = Browser.parsed.find_all("div", class_=re.compile(var))


#print(Test_text) #testing

#using this fuction to compare and void courses that have same name to ensure only one passed. (result: Successful)
def compare1(c, cr):
	for i in range(len(cr)):
		if str(cr[i]) == c:
			return False
	return True

cor=[] #array to store course--- extract this array

#below is the code to append courses to an array (result: Successful)
for course in Test_text:
	n=course.text #extracts the content within the div tags
	if compare1(str(n),cor) == True:
		cor.append(n)
		#print(n)

#for x in range(len(cor)):
#	print(cor[x])

