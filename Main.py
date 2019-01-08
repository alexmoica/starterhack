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
		root.geometry('860x483')
		root.resizable(width=False, height=False)
		HomePage.configure(self, bg='white')		
		
		for i in range(1, 52): #create spacer label for total columns in the frame
			tk.Label(self, text=i, bg='black', fg='white', height=1, width=2).grid(row=i, column=0)
			tk.Label(self, text=i, bg='black', fg='white', height=1, width=2).grid(row=0, column=i)
			
		#get all the university names
		uniFile = open(dp+'universities.txt', 'r')
		uniList = uniFile.readlines()
		uniFile.close()
		
		#define objects
		cBtn = tk.Button(self, text="$", fg='green', activeforeground='green', width=10)
		autoComplete = AutoComplete(uniList, self, width=80)
		logo = tk.Label(self, image=logoImage, width=500, height=150)
		logo.image=logoImage #keep reference to image to avoid being cleared by Python's garbage-collector
		
		#define placements
		logo.grid(row=1, column=2, rowspan=8, columnspan=30)
		autoComplete.grid(row=11, column=1, rowspan=2, columnspan=36)
		cBtn.grid(row=11, column=20, rowspan=2, columnspan=26)
		
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