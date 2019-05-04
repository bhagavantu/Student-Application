from tkinter import *
from tkinter.ttk import Treeview
from views import add_subjects
from main import Main

MED_FONT=("Verdana",18)

class AddSubjects(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller

		subject_label = Label(self, text="Subject Name",font=10)
		self.subject_name = Entry(self, width=50)
		code_label =Label(self,text="Subject Code",font=10)
		self.code=Entry(self, width=50)
		save_btn = Button(self,text="Save",command=self.add_subjects, width=15,bg="green",fg="#ffffff")
		back_btn=Button(self,text="Back",command=lambda:controller.show_frame(Main), width=15)
		heading_label = Label(self, text="Add New Subject", font=MED_FONT )


		#setting  position in frame
		heading_label.grid(row=0, column=0, sticky="W",columnspan=3,pady=20,padx=10)

		subject_label.grid(row=1, column=0,padx=10,pady=10)
		code_label.grid(row=2,column=0,pady=5,padx=10)

		self.subject_name.grid(row=1, column=1, columnspan=2,padx=40,pady=10)
		self.code.grid(row=2,column=1,padx=40, columnspan=2)

		back_btn.grid(row=3, column=1, pady=10)
		save_btn.grid(row=3, column=2, pady=10)

	def add_subjects(self):
		self.subname= self.subject_name.get()
		self.subcode = self.code.get()
		add_subjects(subject_name=self.subname,subject_code=self.subcode)

