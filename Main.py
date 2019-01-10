import tkinter as tk
from AutoComplete import *
import os	
import urllib.request

dp = os.path.join(os.path.dirname(__file__), '') #directory path to current folder

#change the Tk window to display only the given frame
def showFrame(page):
		page.grid(row=0, column=0, sticky='nsew')
		page.tkraise()
		
class HomePage(tk.Frame):
	def __init__(self, master):		
		#set up the tk window
		tk.Frame.__init__(self, master)
		HomePage.configure(self, bg='white')
		
		#TODO: turn focus on and off
		'''
		def focusCheck(event):
			print(HomePage.winfo_children(self))
			if('normal'==root.state()):
				selectBtn.configure(state='normal', bg='red')
				autoComplete.configure(state='normal')
		'''
		
		#function to delete placeholder text on field entry
		def placeholderDelete(event):
			if autoComplete.get() != '':
				autoComplete.lb_up = True
			else:
				autoComplete.lb_up = False
			autoComplete.delete(0, 'end')
		
		#function to check that typed university is in list
		def uniSelect():
			if autoComplete.get() in ('MCMASTER UNIVERSITY', 'UNIVERSITY OF TORONTO', 'UNIVERSITY OF WATERLOO'): #check if field entry matches a university in file
				self.loginWindow() #open login window
				selectBtn.configure(state='disabled', bg='lightgrey')
				autoComplete.configure(state='disabled')
			else:
				print('Valid university not selected')
		
		for i in range(1, 52): #create spacer labels for total columns in the frame
			tk.Label(self, text='', bg='white', fg='white', height=1, width=2).grid(row=i, column=0)
			tk.Label(self, text='', bg='white', fg='white', height=1, width=2).grid(row=0, column=i)
		
		#get all the university names
		uniFile = open(dp+'universities.txt', 'r')
		uniList = uniFile.readlines()			
		uniFile.close()
		
		#define objects
		logoImage=tk.PhotoImage(file=dp+'Target.png') #address of logo image
		selectBtn = tk.Button(self, text='Select', fg='white', bg='red', bd=0, activeforeground='white', activebackground='#c00e12', width=10, relief='flat', command=uniSelect) #TODO: round corners, font for text, black border, how the button looks like when clicked
		autoComplete = AutoComplete(uniList, self, width=80)
		logo = tk.Label(self, image=logoImage, width=165, height=165)
		logo.image=logoImage #keep reference to image to avoid being cleared by Python's garbage-collector
		
		#define placements
		logo.grid(row=3, column=4, rowspan=8, columnspan=35)
		autoComplete.grid(row=12, column=1, rowspan=2, columnspan=36)
		selectBtn.grid(row=12, column=20, rowspan=2, columnspan=26)
		
		#define bindings
		#root.bind('<Button-1>', focusCheck) #focus on main widget will enable button and field entry
		autoComplete.bind('<Button-1>', placeholderDelete) #clicking inside the entry input will call placeholderDelete and delete the current text

	#function for creating general toplevel login page
	def loginWindow(self):
		t = tk.Toplevel(self)
		t.wm_title('MarkBoard - Login')
		t.geometry('250x275')
		t.resizable(width=False, height=False)
		t.configure(bg='lightgrey')
		t.attributes('-topmost', True) #force focus on login window
		t.focus()
		t.wm_transient(root)
		
		#objects for login window
		userLabel = tk.Label(t, text='Username')
		passLabel = tk.Label(t, text='Password')
		userEntry = tk.Entry(t)
		passEntry = tk.Entry(t, show='*')
		submitBtn = tk.Button(t, width=10, text='Submit')
		
		#object positions for login window
		userLabel.pack()
		userEntry.pack()
		passLabel.pack()
		passEntry.pack()
		submitBtn.pack()
		
'''
class LoginPage(tk.Frame):
	def __init__(self, master, url):
		tk.Frame.__init__(self, master)
		root.wm_title('MarkBoard - Login')
		root.geometry('275x300')
		root.resizable(width=False, height=False)
		root.configure(bg='white')
		LoginPage.configure(self, bg='white')
'''

if __name__ == '__main__': #code only executed to run as a program not when simply imported as a module
	root = tk.Tk()
	root.wm_title('MarkBoard - Welcome')
	root.geometry('860x483')
	root.resizable(width=False, height=False)
	showFrame(HomePage(root)) #start with HomePage
	root.mainloop()