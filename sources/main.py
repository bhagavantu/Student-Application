from tkinter import *  #import tkinter library files

MED_FONT=("Verdana",18) #font style for heading label

class Event(Tk):

	def __init__(self,*args,**kwargs):

		Tk.__init__(self, *args,**kwargs)
		Tk.configure(self)
		
		self.container=Frame(self)
		self.container.grid()
		self.container.grid_rowconfigure(0,weight=1)
		self.container.grid_columnconfigure(0,weight=1)
			
		self.geometry("620x600")
		self.show_frame(Main)

	def show_frame(self, cont):
		frame=cont(parent=self.container, controller=self)
		frame.grid(row=0,column=0, sticky="NSEW")
		frame.tkraise()


#To create main frame or front page
class Main(Frame):
	def __init__(self, parent, controller):
		from frontend.add_subjects_page import AddSubjects
		from frontend.see_subjects_page import SeeSubjects
		from frontend.student_list_page import ViewStudentList
		from frontend.student_details_page import EnterStudentDetails
		from frontend.ia_marks_page import SeeIAMarks

		Frame.__init__(self,parent)
		self.controller=controller

		heading_label = Label(self, text="Student Result Management Application", font=MED_FONT,fg="blue")

		#define buttons
		add_student_details_btn = Button(self, text='Student Details Entry', width=25,command=lambda:controller.show_frame(EnterStudentDetails))
		see_student_details_btn = Button(self, text='View Student Details', width=25,command=lambda:controller.show_frame(ViewStudentList))
		add_subjects_btn = Button(self, text='Add New Subject', width=25,command=lambda:controller.show_frame(AddSubjects))
		see_subjects_btn = Button(self, text='See All Subjects', width=25,command=lambda:controller.show_frame(SeeSubjects))

		see_ia_marks_btn = Button(self, text='See IA Marks', width=25,command=lambda:controller.show_frame(SeeIAMarks))

		quit_btn = Button(self, text='Quit', width=25, command=self.controller.quit, background="#e74c3c", foreground="#ffffff")

		#define button position on frame
		heading_label.grid(row=0, column=0, padx=75, pady=30, columnspan=6)
		add_subjects_btn.grid(row=1, column=0, padx=10)
		see_subjects_btn.grid(row=1, column=1)
		add_student_details_btn.grid(row=1, column=2, padx=10)
		see_student_details_btn.grid(row=2, column=0, padx=10, pady=10,)
		see_ia_marks_btn.grid(row=2, column=1, pady=10,)
		quit_btn.grid(row=2, column=2, pady=10, padx=10)



if __name__ == "__main__":
	
	root= Event()
	root.title('student app')
	root.mainloop() 
	
