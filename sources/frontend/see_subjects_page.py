from tkinter import *
from tkinter.ttk import Treeview
from views import see_subjects
from main import Main

MED_FONT=("Verdana",18) #font style for heading label

class SeeSubjects(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent,background="#abcdef")
		self.controller = controller

		back_btn=Button(self,text="Back",command=lambda:controller.show_frame(Main), width=30)
		subject_tree=Treeview( self, columns=('#1','#2','#3'))

		subject_tree.heading('#1',text='Sl No.')
		subject_tree.heading('#2',text='Subject Name')
		subject_tree.heading('#3',text='Subject Code')

		subject_tree.column('#1',stretch=YES,width=80)
		subject_tree.column('#2',stretch=YES,width=250)
		subject_tree.column('#3',stretch=YES,width=190)


		subject_tree['show']='headings'

		subject_list = see_subjects()
		for subject in subject_list:
			subject_tree.insert("",'end',values=subject)
		
		heading_label = Label(self, text="All Subjects List", font=MED_FONT)
		heading_label.grid(row=0, column=0, padx=10,pady=5,sticky="W")

		subject_tree.grid(row=1, column=0, padx=50, pady=10, columnspan=2, sticky='nsew')
		back_btn.grid(row=2, column=0, padx=180, pady=10, sticky="W")


	

