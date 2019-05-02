import peewee

db=peewee.SqliteDatabase('student.db')
#create Subject Table
class Subject(peewee.Model):
	
	subject_name=peewee.TextField()
	subject_code=peewee.TextField()

	class Meta:
		database=db
#create EnterMarks Table
class EnterMarks(peewee.Model):
	student_name=peewee.TextField()
	usn=peewee.TextField()
	subject_name=peewee.TextField()
	internal_assessment_1_marks=peewee.IntegerField()
	internal_assessment_2_marks=peewee.IntegerField()
	internal_assessment_3_marks=peewee.IntegerField()
	external_marks=peewee.IntegerField()

	class Meta:
		database=db

	
db.connect()

db.create_tables([Subject,EnterMarks])



	
