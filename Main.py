import tkinter as tk
from AutoComplete import *
import os	
import urllib.request
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg') #set matplotlib to use tkinter anti-grain geometry
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

dp=os.path.join(os.path.dirname(__file__), '') #directory path to current folder

#define login info vars
loginUser=''
loginPass=''

smallFont = 'times 11 bold'

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
		footer.grid(row=20, column=28, rowspan=4, columnspan=30)
		
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
		
		for i in range(1, 52): #create spacer labels for total columns in the frame
			tk.Label(t, text=i, bg='lightgrey', fg='lightgrey', height=1, width=2).grid(row=i, column=0)
			tk.Label(t, text=i, bg='lightgrey', fg='lightgrey', height=1, width=2).grid(row=0, column=i)
		
		#objects for login window
		userLabel=tk.Label(t, text='Username', bg='lightgrey', font=smallFont)
		passLabel=tk.Label(t, text='Password', bg='lightgrey', font=smallFont)
		entryUser=tk.Entry(t)
		entryPass=tk.Entry(t, show='*')
		submitBtn=tk.Button(t, width=10, text='Submit', font=smallFont, command=submitInfo)
		errorLbl=tk.Label(t, text='', fg='red', bg='lightgrey', font=smallFont)
		entryUser.focus()
		
		#object positions for login window
		userLabel.grid(row=2, column=4, rowspan=1, columnspan=5)
		entryUser.grid(row=3, column=3, rowspan=1, columnspan=7)
		passLabel.grid(row=5, column=4, rowspan=1, columnspan=5)
		entryPass.grid(row=6, column=3, rowspan=1, columnspan=7)
		submitBtn.grid(row=8, column=4, rowspan=2, columnspan=5)
		errorLbl.grid(row=10, column=1, rowspan=1, columnspan=10)
		
class StatsPage(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		root.wm_title('MarkBoard - Overview')
		
		StatsPage.configure(self, bg='white')
		
		for i in range(1, 52): #create spacer labels for total columns in the frame
			tk.Label(self, text='', bg='white', fg='white', height=1, width=2).grid(row=i, column=0)
			tk.Label(self, text='', bg='white', fg='white', height=1, width=2).grid(row=0, column=i)
		
		def submitCourse():
			courseCodes.append(newCourse.get()[newCourse.get().find(':')-4: newCourse.get().find(':')])
			courseNames.append(newCourse.get())
		
		titleFont='Verdana 16 bold'
		infoFont='Verdana 14'
		egFont='Verdana 8 italic bold'
		
		titleLabel=tk.Label(self, text='Course Weight Towards \nCurrent Semester Average', bg='white', font=titleFont)
		infoLabel=tk.Label(self, text='Select Course From The Chart\n\nOR\n\nManually Input Courses', fg='red', bg='white', font=infoFont)
		newCourse=tk.Entry(self, width=37)
		egLabel=tk.Label(self, text='e.g. COMPENG 2DP4:Microprocessor Systems', bg='white', font=egFont)
		newButton=tk.Button(self, width=8, text='Submit', font='Verdana 8 bold', bg='red', command=submitCourse)
		
		titleLabel.place(x=520, y=50)
		infoLabel.place(x=545, y=150)
		newCourse.place(x=545, y=285)
		egLabel.place(x=545, y=305)
		newButton.place(x=770, y=285)
		
		fig=Figure(figsize=(5,5), dpi=100) #create figure object		
		ax=fig.add_subplot(111) #1x1 grid, first subplot
		ax.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)
		
		def make_picker(fig, wedges):
			def onclick(event):
				wedge = event.artist
				label = wedge.get_label()
				self.courseWindow(label, courseCodes.index(label))
				
			# Make wedges selectable
			for wedge in wedges:
				wedge.set_picker(True)
				
			fig.canvas.mpl_connect('pick_event', onclick)

		courseNames=[]
		courseCodes = ['1','2']
		weight = []

		for i in courseCodes:
			x = int(i[(len(i)-1):])
			weight.append(x)
		
		canvas=FigureCanvasTkAgg(fig, self) #create the plot canvas
		canvas.draw()
		canvas.get_tk_widget().place(x=20, y=0)
		
		ax.pie(weight, labels=courseCodes, autopct= '%1.2f%%', shadow=False)
		wedges, plt_labels = ax.pie(weight, labels=courseCodes, colors={'xkcd:pale blue', 'xkcd:sky blue', 'xkcd:lilac', 'xkcd:pastel green', 'xkcd:light mustard', 'xkcd:dusty orange'})
		ax.axis('equal')
		make_picker(fig, wedges)
		ax.plot()
		
	def courseWindow(self, course, index):
		t=tk.Toplevel(self)
		t.wm_title('MarkBoard - '+course)
		t.geometry('500x450')
		t.resizable(width=False, height=False)
		t.configure(bg='lightgrey')
		t.focus()
		t.attributes('-topmost', True) #force topmost window
		t.grab_set() #force focus
		t.wm_transient(root) #creates a transient window, only exit in top bar
		
		for i in range(1, 52): #create spacer labels for total columns in the frame
			tk.Label(t, text=i, bg='lightgrey', fg='lightgrey', height=1, width=2).grid(row=i, column=0)
			tk.Label(t, text=i, bg='lightgrey', fg='lightgrey', height=1, width=2).grid(row=0, column=i)
				
		courseTitle = tk.Label(t, text='d', bg='lightgrey')
		weightDists = tk.Label(t, text='wghtDist', bg='lightgrey')
		weightDists = tk.Label(t, text='wghtDist', bg='lightgrey')
		
		courseTitle.grid(row=1, column=5)
		#weightDists.grid(row=1, column=5)
		#weightDists.grid(row=1, column=5)
		
		frame=tk.Frame(t)
		frame.grid(row=9, column=1, rowspan=15, columnspan=20)
		
		evalLb=tk.Listbox(frame, width=49, font='Verdana 10 bold')
		evalLb.pack(side="left", fill="y")

		scrollbar = tk.Scrollbar(frame, orient="vertical")
		scrollbar.config(command=evalLb.yview)
		scrollbar.pack(side="right", fill="y")

		evalLb.config(yscrollcommand=scrollbar.set)

		evalLb.insert(1, 'Assignment 1, Mark: 80%, Weight: 2%')
		evalLb.insert(2, 'Assignment 2, Mark: 60%, Weight: 2%')
		evalLb.insert(3, 'Lab 1, Mark: 40%, Weight: 5%')
		evalLb.insert(4, 'Lab 1, Mark: 40%, Weight: 5%')	
		evalLb.insert(5, 'Lab 1, Mark: 40%, Weight: 5%')	
		evalLb.insert(6, 'Lab 1, Mark: 40%, Weight: 5%')	
		evalLb.insert(7, 'Lab 1, Mark: 40%, Weight: 5%')	
		evalLb.insert(8, 'Lab 1, Mark: 40%, Weight: 5%')	
		evalLb.insert(9, 'Lab 1, Mark: 40%, Weight: 5%')	
		evalLb.insert(10, 'Lab 1, Mark: 40%, Weight: 5%')	
		evalLb.insert(11, 'Lab 1, Mark: 40%, Weight: 5%')	
		
if __name__ == '__main__': #code only executed to run as a program not when simply imported as a module
	root=tk.Tk()
	root.wm_title('MarkBoard - Welcome')
	root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file=dp+'Target.png'))
	root.geometry('860x483')
	root.resizable(width=False, height=False)
	showFrame(StatsPage(root)) #start with HomePage
	root.mainloop()