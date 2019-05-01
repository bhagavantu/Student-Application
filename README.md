**Building a Student Result Management Application**
==


# About the project:
The "Student Result Management Application" has been developed to overide the problems prevailing in the practicing manual system.
The main objective of the project is to provide the examination result to the student in a simple way.
This project is useful for students and institutions for getting the results in simple manner.

# Project Architecture:

1. There are 8 different attributes of the project. They are:
    * Student name
    * Student USN
    * Subject Name
    * Subject code
    * Internal Assessment 1 marks
    * Internal Assessment 2 marks
    * Internal Assessment 3 marks
    * External marks
      
2. Since we need all of these information to create student application, we have 5 features they are:
      1. Add subject Details: To add the all subjects
      2. See All Subjects: To view the all subjects
      3. Student Details Entry: To add student details
      4. View Student Details: To get the particular student details by selecting USN of studen
      5. See IA Marks: To get the particular subject details by selecting the subject name
    
3. To store the data and present it to users in useful way , so we need to create Database for "Student Result Management Application". In this project we created two tables. They are:

      1. Subject Table: It contains the information of subject name and subject code 
      2. EnterMarks Table: It contains the information of student name, USN,subject name,internal marks of Test-1,Test-2 and Test-3, and External marks 
     
  # Documentation:
1. To run this project, clone or download this project on your computer.
2. After downoloading the project, open the python3 software if you installed already, otherwise download python 3 software and install    on your computer.
3. Open command prompt, Navigate to the project folder to run this project. For example: folder name is student app and in this    folder you have sources file so to open this file use command as mentioned below:

  	      $ cd student app/sources
4. After navigation of project folder path, click on program files and open the files on your workspace and save it.
5. To run this project, you have to Run main.py and execute the program using command as mentioned below:

	      $ python main.py
6. After running the program you can follow the instructions as displayed on your computer and while executing the program you need to      enter valid details then only you can get the correct output
