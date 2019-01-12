import tkinter as tk
from AutoComplete import *
import os	
import urllib.request
import matplotlib
matplotlib.use('TkAgg') #set matplotlib to use tkinter anti-grain geometry
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

dp=os.path.join(os.path.dirname(__file__), '') #directory path to current folder

#define login info vars
loginUser=''
loginPass=''

#change the Tk window to display only the given frame
def showFrame(page):
		page.grid(row=0, column=0, sticky='nsew')
		page.tkraise()
		page.focus()
		
class HomePage(tk.Frame):
	def __init__(self, master):		
		#set up the tk window
		tk.Frame.__init__(self, master)
		HomePage.configure(self, bg='white')
		
		#enables the focus of the button and entry if the HomePage is focused
		def focusCheck(event):
			if(self.focus_get()):
				selectBtn.configure(state='normal', bg='red')
				autoComplete.configure(state='normal')
	
		#function to delete placeholder text on field entry
		def placeholderDelete(event):
			if autoComplete.get() != '':
				autoComplete.lb_up=True
			else:
				autoComplete.lb_up=False
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
		uniFile=open(dp+'universities.txt', 'r')
		uniList=uniFile.readlines()			
		uniFile.close()
		
		#define objects
		logoImage=tk.PhotoImage(file=dp+'Target.png') #address of logo image
		footerImage=tk.PhotoImage(file=dp+'Footer.png')
		selectBtn=tk.Button(self, text='Select', fg='white', bg='red', bd=0, width=10, relief='flat', command=uniSelect) #TODO: round corners, font for text, how the button looks like when clicked
		autoComplete=AutoComplete(uniList, self, width=73)
		logo=tk.Label(self, image=logoImage, width=165, height=165, bg='white')
		logo.image=logoImage #keep reference to image to avoid being cleared by Python's garbage-collector
		footer=tk.Label(self, image=footerImage, width=150, height=20, bg='white')
		footer.image=footerImage
		
		#define placements
		logo.grid(row=1, column=4, rowspan=10, columnspan=35)
		autoComplete.grid(row=11, column=1, rowspan=2, columnspan=38)
		selectBtn.grid(row=11, column=20, rowspan=2, columnspan=26)
		footer.grid(row=20, column = 28, rowspan=4, columnspan=30)
		
		#define bindings
		root.bind('<Button-1>', focusCheck) #focus on main widget will enable button and field entry
		autoComplete.bind('<Button-1>', placeholderDelete) #clicking inside the entry input will call placeholderDelete and delete the current text

	#function for creating general toplevel login page
	def loginWindow(self):
		
		#function for submitting login info
		def submitInfo():
			global loginUser, loginPass
			if(entryUser.get()==''):
				errorLbl['text']='Please fill in Username field'
			elif(entryPass.get()==''):
				errorLbl['text']='Please fill in Password field'
			else:
				loginUser=entryUser.get()
				loginPass=entryPass.get()
				showFrame(StatsPage(root))
				t.destroy()
	
		t=tk.Toplevel(self)
		t.wm_title('MarkBoard - Login')
		t.geometry('250x275')
		t.resizable(width=False, height=False)
		t.configure(bg='lightgrey')
		t.focus()
		t.attributes('-topmost', True) #force topmost window
		t.grab_set() #force focus
		t.wm_transient(root) #creates a transient window, only exit in top bar
		
		#objects for login window
		userLabel=tk.Label(t, text='Username', bg='lightgrey')
		passLabel=tk.Label(t, text='Password', bg='lightgrey')
		entryUser=tk.Entry(t)
		entryPass=tk.Entry(t, show='*')
		submitBtn=tk.Button(t, width=10, text='Submit', command=submitInfo)
		errorLbl=tk.Label(t, text='', fg='red', bg='lightgrey')
		
		#object positions for login window
		userLabel.pack()
		entryUser.pack()
		passLabel.pack()
		entryPass.pack()
		submitBtn.pack()
		errorLbl.pack()
		
class StatsPage(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		root.wm_title('MarkBoard - Overview')
		StatsPage.configure(self, bg='white')
		
		lAbEl=tk.Label(self, text='GrAPhS').pack()

if __name__ == '__main__': #code only executed to run as a program not when simply imported as a module
	root=tk.Tk()
	root.wm_title('MarkBoard - Welcome')
	root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file=dp+'Target.png'))
	root.geometry('860x483')
	root.resizable(width=False, height=False)
	showFrame(HomePage(root)) #start with HomePage
	root.mainloop()