from tkinter import *
from views import add_students, get_subject_name
from main import Main
MED_FONT=("Verdana",18)  #font style for heading label

class EnterStudentDetails(Frame):
	
	def __init__(self, parent, controller):
		Frame.__init__(self, parent,background="#abcdef")
		self.controller = controller
		heading_label = Label(self, text="All Student Details", font=MED_FONT)
		self.name_label = Label(self, text="Student Name",font=10)
		self.usn_label =Label(self,text="USN",font=10)
		self.internal_assessment_1_marks_label = Label(self, text='IA 1 Marks', font=10)
		self.internal_assessment_2_marks_label = Label(self, text='IA 2 Marks', font=10)
		self.internal_assessment_3_marks_label = Label(self, text='IA 3 Marks', font=10)
		self.external_marks_label = Label(self, text='External Marks', font=10)


		self.student_name = Entry(self,width=48)
		self.usn = Entry(self,width=48)
		self.internal_assessment_1_marks = Entry(self,width=48)
		self.internal_assessment_2_marks = Entry(self,width=48)
		self.internal_assessment_3_marks = Entry(self,width=48)
		self.external_marks = Entry(self,width=48)

		self.save_btn = Button(self,text="Save",command=self.save,width=7,bg="green")
		self.back_btn = Button(self,text="Back",command=lambda:controller.show_frame(Main),width=10)



		#setting  position in frame

		self.name_label.grid(row=6, column=0, padx=10,sticky="W",pady=3 )
		heading_label.grid(row=0, column=0, padx=10, sticky="W",pady=5)
		self.usn_label.grid(row=7,column=0,padx=10,sticky="W")
		Label(self,text="Subject name",font=10).grid(row=8,column=0,padx=10,sticky="W",pady=3)
		self.internal_assessment_1_marks_label.grid(row=9 ,column=0,padx=10,sticky="W",pady=3)
		self.internal_assessment_2_marks_label.grid(row=10 ,column=0, padx=10, sticky="w",pady=3)
		self.internal_assessment_3_marks_label.grid(row=11 ,column=0, padx=10, sticky="w",pady=3)
		self.external_marks_label.grid(row=12, column=0, padx=10, sticky="w",pady=3)

		self.student_name.grid(row=6, column=1,columnspan=2)
		self.usn.grid(row=7,column=1,columnspan=2)
		self.internal_assessment_1_marks.grid(row=9 ,column=1,columnspan=2)
		self.internal_assessment_2_marks.grid(row=10 ,column=1,columnspan=2)
		self.internal_assessment_3_marks.grid(row=11 ,column=1,columnspan=2)
		self.external_marks.grid(row=12 ,column=1,columnspan=2)

		
		self.save_btn.grid(row=14, column=2, padx=40, pady=15,sticky="E")
		self.back_btn.grid(row=14, column=1, padx=70, pady=10, sticky="E")

		
		


		subject_names = get_subject_name()

		option=[]

		for sub_name in subject_names:
			option.append(sub_name)

		options = list(set(option))		#to obtain only unique events 
		self.variable = StringVar(self)
		self.variable.set(options[0])		#Setting the default event
		self.select = OptionMenu(self, self.variable,*options,options[0],command=self.get_value).grid(row =8,column =1,columnspan=2)
		


	def get_value(self,value):
		self.id=value

	def save(self):
		self.student=self.student_name.get()
		self.susn=self.usn.get()
		self.subject=self.id
		self.ia_1_marks = self.internal_assessment_1_marks.get()
		self.ia_2_marks = self.internal_assessment_2_marks.get()
		self.ia_3_marks = self.internal_assessment_3_marks.get()
		self.ext_marks = self.external_marks.get()
		
		add_students(student_name=self.student,
					 usn=self.susn, 
					 subject_name=self.subject,
					 ia1_marks=self.ia_1_marks,
					 ia2_marks=self.ia_2_marks,
			         ia3_marks=self.ia_3_marks,
			         external_marks=self.ext_marks,) 

