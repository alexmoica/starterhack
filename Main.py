import tkinter as tk
from AutoComplete import *
import os

dp = os.path.join(os.path.dirname(__file__), '')

#change the Tk window to display only the given frame
def showFrame(page):
		page.grid(row=0, column=0, sticky='nsew')
		page.tkraise()

class HomePage(tk.Frame):
	def __init__(self, master):
	
		logoImage=tk.PhotoImage(file=dp+'LOGO.gif')
		
		#set up the tk window
		tk.Frame.__init__(self, master)
		root.geometry('875x480')
		root.resizable(width=False, height=False)
		
		#get all the university names
		uniFile = open(dp+'universities.txt', 'r')
		uniList = uniFile.readlines()
		uniFile.close()
		
		#define objects
		cLbl = tk.Label(self, text="hi")
		cBtn = tk.Button(self, text="$", fg='green', activeforeground='green', width=10)
		autoComplete = AutoComplete(uniList, self, width=100)
		logo = tk.Label(image=logoImage)
		logo.image=logoImage #keep reference to image to avoid being cleared by Python's garbage-collector
		
		#define placements
		cLbl.grid(row=0, column=0)
		cBtn.grid(row=1, column=0)
		autoComplete.grid(row=2, column=0)
		logo.grid(row=3, column=0)
		
		#function to delete placeholder text on field entry
		def placeholderDelete(event):
			if autoComplete.get() != '':
				autoComplete.lb_up = True
			else:
				autoComplete.lb_up = False
			autoComplete.delete(0, 'end')
			
		autoComplete.bind('<Button-1>', placeholderDelete) #clicking inside the entry input will call placeholderDelete and delete the current text
		
if __name__ == '__main__': #code only executed to run as a program not when simply imported as a module
	root = tk.Tk()
	root.wm_title("whatsmymark?")
	showFrame(HomePage(root)) #start with HomePage
	root.mainloop()