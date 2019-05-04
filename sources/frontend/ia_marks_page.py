from tkinter import *
from tkinter.ttk import Treeview

from views import view_ia, get_subject_name
from main import Main



MED_FONT=("Verdana",18)  #font style for heading label

		

class SeeIAMarks(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller

		self.IA_tree=Treeview(self, columns=('#1','#2','#3','#4','#5','#6'))

		#creating tabular column
		self.IA_tree.heading('#1',text='Student Name')
		self.IA_tree.heading('#2',text='Student USN')
		self.IA_tree.heading('#3',text='IA1 Marks')
		self.IA_tree.heading('#4',text='IA2 Marks')
		self.IA_tree.heading('#5',text='IA3 Marks')
		self.IA_tree.heading('#6',text='External Marks')
	
		self.IA_tree.column('#1',stretch=YES,width=95)
		self.IA_tree.column('#2',stretch=YES,width=95)
		self.IA_tree.column('#3',stretch=YES,width=95)
		self.IA_tree.column('#4',stretch=YES,width=95)
		self.IA_tree.column('#5',stretch=YES,width=95)
		self.IA_tree.column('#6',stretch=YES,width=95)
		
		
		

		self.IA_tree.grid(row=2, column=0, columnspan=10, padx=15, pady=10,sticky='nsew')
		self.IA_tree['show']='headings'

		
		subject_names = get_subject_name()

		option=[]

		for sub_name in subject_names:
			option.append(sub_name)

		options = list(set(option))		#to obtain only unique events 
		self.variable = StringVar(self)
		self.variable.set(options[0])
		self.variable.trace("w", self.update_table)	
		#Setting the default event
		self.select = OptionMenu(self, self.variable,*options,options[0],command=self.get_value).grid(row =1,column =1,padx=10,pady=10)
		
		Label(self,text=" Subject name",font=10).grid(row=1,column=0,padx=10,pady=10,sticky="W")

		back_btn=Button(self,text="Back",command=lambda:controller.show_frame(Main),width=30)
		back_btn.grid(row=3, column=0, padx=20, pady=20, sticky="W")
		
		heading_label = Label(self, text="Subject Details", font=MED_FONT)
		heading_label.grid(row=0, column=0, padx=5,pady=5, sticky="W")
    

    #values updating in treeview 
	def update_table(self, *args):
		self.IA_tree.delete(*self.IA_tree.get_children())
		sub_name = self.variable.get()
		student_list = view_ia(sub_name)
		for students in student_list:

			self.IA_tree.insert("", 'end', values=[students.student_name,
															students.usn,
															students.internal_assessment_1_marks,
															students.internal_assessment_2_marks,
															students.internal_assessment_3_marks,
															students.external_marks])

	def get_value(self,value):
		self.id=value
 

		
