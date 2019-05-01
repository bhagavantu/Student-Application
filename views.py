from models import *

def add_students(student_name,usn,subject_name,ia1_marks,ia2_marks,ia3_marks,external_marks):
	EnterMarks.create(student_name=student_name,usn=usn,subject_name=subject_name, internal_assessment_1_marks=ia1_marks, 
		internal_assessment_2_marks=ia2_marks, internal_assessment_3_marks=ia3_marks, external_marks=external_marks)


def view_students(student_usn):
	student_list=[]

	for name in student_usn:
		students = EnterMarks.select().where(EnterMarks.usn==name)
		student_list.extend(students)
	
	return student_list


def add_subjects(subject_name,subject_code):
	Subject.create(subject_name=subject_name,subject_code=subject_code)


def see_subjects():
	subjects=[]
	for subject in Subject.select():
		subjects.append([subject.id,subject.subject_name,subject.subject_code])
	return subjects

def get_subject_name():
	subject_names = []
	for subject in Subject.select():
		subject_names.append(subject.subject_name)
	return subject_names

def get_student_usns():
	student_usn_list = []
	for student in EnterMarks.select():
		student_usn_list.append(student.usn)

	return student_usn_list
	
def view_ia(sub_name):
	student_list = EnterMarks.select().where(EnterMarks.subject_name==sub_name)
	return student_list





