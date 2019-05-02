from tkinter import *
from tkinter.ttk import Treeview
from views import view_students, get_student_usns
from main import Main


MED_FONT=("Verdana",18)  #font style for heading label


class ViewStudentList(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent,bg="#abcdef")
		self.controller = controller

		self.student_tree=Treeview(self, columns=('#1','#2','#3','#4','#5','#6'))

		self.student_tree.heading('#1',text='Student Name')
		self.student_tree.heading('#2',text='Subject Name')
		self.student_tree.heading('#3',text='IA1 Marks')
		self.student_tree.heading('#4',text='IA2 Marks')
		self.student_tree.heading('#5',text='IA3 Marks')
		self.student_tree.heading('#6',text='External Marks')
	
		self.student_tree.column('#1',stretch=YES,width=95)
		self.student_tree.column('#2',stretch=YES,width=205)
		self.student_tree.column('#3',stretch=YES,width=70)
		self.student_tree.column('#4',stretch=YES,width=70)
		self.student_tree.column('#5',stretch=YES,width=70)
		self.student_tree.column('#6',stretch=YES,width=90)
		

		self.student_tree.grid(row=2, column=0, columnspan=10, padx=10, pady=10,sticky='nsew')
		self.student_tree['show']='headings'

		student_usn = get_student_usns()

		option=[]

		for name in student_usn:
			option.append(name)

		options = list(set(option))		#to obtain only unique events 
		self.variable = StringVar(self)
		self.variable.set(options[0])	
		self.variable.trace("w", self.update_table)	

		self.select = OptionMenu(self, self.variable, 
									*options,
									options[0], 
									command=self.get_value).grid(row =1,column =2,padx=10,pady=10)

		Label(self,text=" Student USN",font=10).grid(row=1,column=0,padx=10,pady=10,sticky="W")

		back_btn=Button(self,text="Back",command=lambda:controller.show_frame(Main),width=30,fg="#000fc0")
		back_btn.grid(row=3, column=0, padx=20, pady=20, sticky="W")
		
		heading_label = Label(self, text="View Student Details", font=MED_FONT)
		heading_label.grid(row=0, column=0, padx=5,pady=5, sticky="W")

	def update_table(self, *args):
		self.student_tree.delete(*self.student_tree.get_children())
		student_usn = self.variable.get()
		
		student_list=view_students([student_usn,])

		for students in student_list:
			self.student_tree.insert("", 'end', values=[students.student_name,
														students.subject_name,
														students.internal_assessment_1_marks,
														students.internal_assessment_2_marks,
														students.internal_assessment_3_marks,
														students.external_marks])

	def get_value(self,value):
		self.id=value
		