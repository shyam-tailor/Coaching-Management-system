import sqlite3

def createtable():
         con=sqlite3.connect("golu.db")
         con.execute('''CREATE TABLE  IF NOT EXISTS  Facultie(Id Integer,
                                  Name text,
                                  CONTECT_NO text ,
                                  ADDRESS text,
                                  Email text,
                                  Subjects text) ''');
         con.execute('''CREATE TABLE  IF NOT EXISTS  Batchess1(Lecture text,
                                  teacher text,
                                  startdate text ,
                                  enddate text,
                                  starttime text,
                                  endtime text)''');
         con.execute('''CREATE TABLE  IF NOT EXISTS  Enquiries(Enquiryno text,Date text,SName text ,FName text,Wno text,Mno text,FMno text,Foc text,Eid text,Address text,clgname text,class text,Semester text,Branch text,Course text,Timepre text,Branchpre text)''');
         con.execute('''CREATE TABLE  IF NOT EXISTS  PythonStud(Sid text Primary key,
                                  SName text,
                                  FName text,
                                  Course text,
                                  Mobno text)''');
         con.execute('''CREATE TABLE  IF NOT EXISTS  JavaStud(Sid text,
                                  SName text,
                                  FName text,
                                  Course text,
                                  Mobno text)''');
         con.execute('''CREATE TABLE  IF NOT EXISTS  CStud(Sid text,
                                  SName text,
                                  FName text,
                                  Course text,
                                  Mobno text)''');
         print("Table Created Successfully")
         con.close()


#******************************for Insert data in Faculty table**************************************
def Insertdata(l):
         a=l[0].get()
         b=l[1].get()
         c=l[2].get()
         d=l[3].get()
         e=l[4].get()
         f=l[5].get()
         
         
         con=sqlite3.connect("golu.db")
         print(a,b,c,d)
         con.execute(f"INSERT INTO Facultie values('{a}','{b}','{c}','{d}','{e}','{f}')")
         con.commit()
         print("Insert data Successfully")
         con.close()
#*****************************Ends******************************************************************



#******************************for Insert data in Batch table**************************************
def Insertdataintobatch(l):
         a=l[0].get()
         b=l[1].get()
         c=l[2].get()
         d=l[3].get()
         e=l[4].get()
         f=l[5].get()
         
         
         con=sqlite3.connect("golu.db")
         print(a,b,c,d)
         con.execute(f"INSERT INTO Batchess1 values('{a}','{b}','{c}','{d}','{e}','{f}')")
         con.commit()
         print("Insert data Successfully")
         con.close()
#*******************************************Ends*****************************************************



#******************************for Insert data in enquiry table**************************************
def Insertdataintoenquiry(l):
         print(len(l))
         a=l[0].get()
         b=l[1].get()
         c=l[2].get()
         d=l[3].get()
         e=l[4].get()
         f=l[5].get()
         g=l[6].get()
         h=l[7].get()
         i=l[8].get()
         j=l[9].get()
         k=l[10].get()
         z=l[11].get()
         m=l[12].get()
         n=l[13].get()
         o=l[14].get()
         p=l[15].get()
         q=l[16].get()
         con=sqlite3.connect("golu.db")
         con.execute(f"INSERT INTO Enquiries values('{a}','{b}','{c}','{d}','{e}','{f}','{g}','{h}','{i}','{j}','{k}','{z}','{m}','{n}','{o}','{p}','{q}')")
         con.commit()
         print("Insert data Successfully")
         con.close()
#*******************************************Ends*****************************************************


#*******************************************For display Faculty data *****************************************************
def Displaydata():
         con=sqlite3.connect("golu.db")
         rows=con.execute('''SELECT * from Facultie''')
         rows=rows.fetchall()
         return rows
         con.close
#*******************************************Ends*****************************************************

#*******************************************For display Batch data **********************************
def Displaydataofbatch():
         con=sqlite3.connect("golu.db")
         rows=con.execute('''SELECT * from Batchess1''')
         rows=rows.fetchall()
         return rows

         con.close
#*******************************************Ends ****************************************************
#*******************************************For display Enquiry data **********************************
def Displaydataofenquiry():
         con=sqlite3.connect("golu.db")
         rows=con.execute('''SELECT * from Enquiries''')
         rows=rows.fetchall()
         return rows
         con.close

def DisplaydataofOython():
         con=sqlite3.connect("golu.db")
         rows=con.execute('''SELECT * from PythonStud''')
         rows=rows.fetchall()
         return rows
         con.close

def DisplaydataofJava():
         con=sqlite3.connect("golu.db")
         rows=con.execute('''SELECT * from JavaStud''')
         rows=rows.fetchall()
         return rows
         con.close
#*******************************************Ends ****************************************************
#*******************************************For delete faculty  data ********************************

#*****************************************To Fetch Data from enquiry for every Course*****************************************
def P():
         con=sqlite3.connect("golu.db")
         rows=con.execute('''SELECT Enquiryno,SName,FName,Course,Mno from Enquiries where Course='Python' ''')
         rows=rows.fetchall()
         for i in rows:
                  return(i)
         con.close
def J():
         con=sqlite3.connect("golu.db")
         rows=con.execute('''SELECT Enquiryno,SName,FName,Course,Mno from Enquiries where Course='Java' ''')
         rows=rows.fetchall()
         for i in rows:
                  return(i)
         con.close
def C():
         con=sqlite3.connect("golu.db")
         rows=con.execute('''SELECT Enquiryno,SName,FName,Course,Mno from Enquiries where Course='C' ''')
         rows=rows.fetchall()
         for i in rows:
                  return(i)
         con.close
t=()
def Fac():
         global t
         con=sqlite3.connect("golu.db")
         rows=con.execute('''SELECT Name from Facultie  ''')
         rows=rows.fetchall()
         for i in rows:
                  t=t+i
         return t
         con.close

def Bat(X):
         
         con=sqlite3.connect("golu.db")
         rows=con.execute(f'''SELECT Subjects from Facultie where  Name='{X}' ''')
         rows=rows.fetchall()
         for i in rows:
                  t=i[0].split(',')
         return t
                  
                  
                  
                  
         
         con.close
#**************************************************Ends*********************************************************
#***************************************iNSER  DATA INTO  EVERY Course***************************************s
def InsertdataintoPython(X):
         print(X)
         
         
         con=sqlite3.connect("golu.db")
         con.execute(f"INSERT INTO PythonStud values('{X[0]}','{X[1]}','{X[2]}','{X[3]}','{X[4]}')")
         con.commit()
         print("Insert data Successfully in Python")
         con.close()
def InsertdataintoJava(X):
         print(X)
         
         
         con=sqlite3.connect("golu.db")
         con.execute(f"INSERT INTO JavaStud values('{X[0]}','{X[1]}','{X[2]}','{X[3]}','{X[4]}')")
         con.commit()
         print("Insert data Successfully in Java Batch")
         con.close()
def InsertdataintoC(X):
         print(X)
         
         
         con=sqlite3.connect("golu.db")
         con.execute(f"INSERT INTO CStud values('{X[0]}','{X[1]}','{X[2]}','{X[3]}','{X[4]}')")
         con.commit()
         print("Insert data Successfully in C")
         con.close()
         
def deletefromenquiry(X):
         
         con=sqlite3.connect("golu.db")
         con.execute(f"DELETE FROM Enquiries where Enquiryno='{X}'")
         con.commit()
         print("delete data Successfully ")
         con.close()
def deletefromFac(X):
         
         con=sqlite3.connect("golu.db")
         con.execute(f"DELETE FROM Facultie where Name='{X}'")
         con.commit()
         print("delete data Successfully ")
         con.close()

def PyBatch(A):
         con=sqlite3.connect("golu.db")
         rows=con.execute(f'''SELECT starttime, endtime from Batchess1 where Lecture='{A}'  ''')
         rows=rows.fetchall()
         #for i in rows:
         return rows
         con.close
         
         


createtable()


