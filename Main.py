import tkinter as tk
from AutoComplete import *
import os	
import urllib.request

dp = os.path.join(os.path.dirname(__file__), '')

#change the Tk window to display only the given frame
def showFrame(page):
		page.grid(row=0, column=0, sticky='nsew')
		page.tkraise()
		
class HomePage(tk.Frame):
	def __init__(self, master):
		
		logoImage=tk.PhotoImage(file=dp+'Target.png')
		
		#set up the tk window
		tk.Frame.__init__(self, master)
		root.geometry('860x483')
		root.resizable(width=False, height=False)
		HomePage.configure(self, bg='white')		
		
		#function to delete placeholder text on field entry
		def placeholderDelete(event):
			if autoComplete.get() != '':
				autoComplete.lb_up = True
			else:
				autoComplete.lb_up = False
			autoComplete.delete(0, 'end')
		
		#functiont to check that typed university is in list
		def uniSelect():
			if autoComplete.get()=='MCMASTER UNIVERSITY':
				self.loginWindow() #TODO: Disable button on click, center tk window popup, create 
			elif autoComplete.get()=='UNIVERSITY OF TORONTO':
				self.loginWindow()
			elif autoComplete.get()=='UNIVERSITY OF WATERLOO':
				self.loginWindow()
			else:
				print("Valid university not selected")
		
		for i in range(1, 52): #create spacer label for total columns in the frame
			tk.Label(self, text='', bg='white', fg='white', height=1, width=2).grid(row=i, column=0)
			tk.Label(self, text='', bg='white', fg='white', height=1, width=2).grid(row=0, column=i)
		
		#get all the university names
		uniFile = open(dp+'universities.txt', 'r')
		uniList = uniFile.readlines()
		uniFile.close()
		
		#define objects
		selectBtn = tk.Button(self, text="Select", fg='white', bg='red', bd=0, activeforeground='red', activebackground='lightgrey', width=10, relief='flat', command=uniSelect) #TODO: round corners, font for text, black border, how the button looks like when clicked
		autoComplete = AutoComplete(uniList, self, width=80)
		logo = tk.Label(self, image=logoImage, width=165, height=165)
		logo.image=logoImage #keep reference to image to avoid being cleared by Python's garbage-collector
		
		#define placements
		logo.grid(row=3, column=4, rowspan=8, columnspan=35)
		autoComplete.grid(row=12, column=1, rowspan=2, columnspan=36)
		selectBtn.grid(row=12, column=20, rowspan=2, columnspan=26)
			
		autoComplete.bind('<Button-1>', placeholderDelete) #clicking inside the entry input will call placeholderDelete and delete the current text

	#function for creating general toplevel login page
	def loginWindow(self):
		t = tk.Toplevel(self)
		t.wm_title("MarkBoard - Login")
		t.geometry('275x300')
		t.resizable(width=False, height=False)
		t.configure(bg='lightgrey')
		t.focus()
		
'''
class LoginPage(tk.Frame):
	def __init__(self, master, url):
		tk.Frame.__init__(self, master)
		root.wm_title("MarkBoard - Login")
		root.geometry('275x300')
		root.resizable(width=False, height=False)
		root.configure(bg='white')
		LoginPage.configure(self, bg='white')
'''
		
if __name__ == '__main__': #code only executed to run as a program not when simply imported as a module
	root = tk.Tk()
	root.wm_title("MarkBoard - Welcome")
	showFrame(HomePage(root)) #start with HomePage
	root.mainloop()