from tkinter import *
import sys
from tkinter import ttk
import database as db
from tkinter import messagebox
  
top = Tk()
top.geometry('2500x2500')
k=0
l=0
n=3
#****************************************Contain All PhotoImage Object********************************
img=PhotoImage(file="D:\\coaching management syspem python\\Images\\banner-1.png")
img1=PhotoImage(file="D:\\coaching management syspem python\\Images\\ad.png")
img2=PhotoImage(file="D:\\coaching management syspem python\\Images\\us.png")
img4=PhotoImage(file="D:\\coaching management syspem python\\Images\\Programming-Language.png")
img5=PhotoImage(file="D:\\coaching management syspem python\\Images\\language2.png")
img6=PhotoImage(file="D:\\coaching management syspem python\\Images\\slide3.png")

#****************************************Contain All PhotoImage Object ends********************************

#******************************Create Frame With Images********************************************* 
def CraeteFront():
         Topframe=Frame(top,width=1440,height=100,relief='solid',bd=5,bg='#342267')
         
         Topframe.place(x=0,y=0)
         l1=Label(Topframe,width=130,height=3,text='Welcome in Matrix Computers Management System',font=('arial',15,'bold'),fg='#d00',bg='#fff')
         l1.place(x=0,y=0)
         
         Mainframe=Frame(top,width=1440,height=840,relief='solid',bd=5,bg='#fff')
         l1=Label(Mainframe,image=img6,width=1440,height=840,bg='#fff')
         l1.place(x=0,y=0)
         Mainframe.place(x=0,y=80)
         b=Button(Mainframe,text='Go',width=10,height=2,bg='#d00',fg='#fff',font=('arial',8,'bold'),command=create)
         b.place(x=720,y=100)
         
         
         

def CreateMainFrame():
         global Mainframe,Tolevelframe,Bottomlevelframe
         Mainframe=Frame(top,width=1440,height=840,relief='solid',bd=5,bg='#fff')
         Mainframe.place(x=0,y=0)
         Toplevelframe=Frame(Mainframe,width=1480,height=500,relief='solid',bd=3,bg='#fff')
         Toplevelframe.place(x=0,y=0)
         Bottomlevelframe=Frame(Mainframe,width=1430,height=450,relief='solid',bd=3,bg='#fff')
         Bottomlevelframe.place(x=0,y=500)
         
         l1=Label(Toplevelframe,image=img,width=1480,height=500,bg='#fff')
         l1.place(x=0,y=0)
         Toplevelframe.place(x=0,y=0)

def CreateFrame():
         
         global Mainframe,Tolevelframe,Bottomlevelframe
         Mainframe=Frame(top,width=1440,height=840,relief='solid',bd=5,bg='#fff')
         Mainframe.place(x=0,y=0)


         Toplevelframe=Frame(Mainframe,width=1430,height=300,relief='solid',bd=3,bg='#fff')
         l1=Label(Toplevelframe,image=img4,bg='#fff')
         
         Toplevelframe.place(x=0,y=0)
         l1.place(x=0,y=0)

         Bottomlevelframe=Frame(Mainframe,width=1430,height=750,relief='solid',bd=3,bg='#fff')
         Bottomlevelframe.place(x=0,y=300)

def CreateFrame1():
         
         global Mainframe,Tolevelframe,Bottomlevelframe
         Mainframe=Frame(top,width=1440,height=840,relief='solid',bd=5,bg='#fff')
         Mainframe.place(x=0,y=0)


         Toplevelframe=Frame(Mainframe,width=1430,height=300,relief='solid',bd=3,bg='#fff')
         l1=Label(Toplevelframe,image=img5,bg='#fff')
         
         Toplevelframe.place(x=0,y=0)
         l1.place(x=0,y=0)

         Bottomlevelframe=Frame(Mainframe,width=1430,height=750,relief='solid',bd=3,bg='#fff')
         Bottomlevelframe.place(x=0,y=300)
#****************************************Image Frames Ends***************************************************


#***********************************Section Of All List*************************************************          
l1=[StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
    ,StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
    ,StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
    ,StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]
print(len(l1))
tlist=['Id','Name','ContactNo','Address','E-Mail','Subject']
blist=['Lecture','Faculty','Starting_Date','Ending_Date','Srart_Time','End_Time']
elist=['Enquiry No','Date','Student Name','Father Name','Wapp No','Mob No','FMob No','Fat Occu','EMail-Id'
       ,'Father Name','College Name','Class','Semester','Branch','Course','Time Preff','Branch Preff']

Slist=['id','SName','FName','Course','Mno']
#**************************************List Section Ends***********************************************


#*****************************Section for Create Label With Entry*************************************
def createlabel(frame,tex,texvar,x1,y1,x2,y2):
         Firmlab=Label(frame,font=('arial',15,'bold'),text=tex,justify='left',width=15,fg='#d00',bg='#fff')
         Firmlab.place(x=x1,y=y1)
         E1=Entry(frame,font=('arial',20,'bold'),textvariable=texvar,justify='left',width=35,bg='#ffffff',fg='#d00')
         E1.place(x=x2,y=y2)
def createlabel2(frame,tex,texvar,x1,y1,x2,y2):
         Firmlab=Label(frame,font=('arial',15,'bold'),fg='#d00',bg='#fff',text=tex,width=13)
         Firmlab.place(x=x1,y=y1)
         E1=Entry(frame,font=('arial',20,'bold'),textvariable=texvar,bg='#ffffff',fg='#d00',justify='left',width=10)
         E1.place(x=x2,y=y2)
def createlabel3(frame,tex,texvar,x1,y1,x2,y2):
         Firmlab=Label(frame,font=('arial',15,'bold'),fg='#d00',bg='#fff',text=tex,width=20)
         Firmlab.place(x=x1,y=y1)
         E1=Entry(frame,font=('arial',20,'bold'),textvariable=texvar,bg='#ffffff',fg='#d00',justify='left',width=73)
         E1.place(x=x2,y=y2)
#******************************Section for Create Label With Entry Ends*****************************

#******************************Create Simple Label*************************************************
def Createlabel(frame,tex,ro,col):
         label=Label(frame,text=tex,width=11,height=2,fg='#d00',bg='#fff',font=('arial',8,'bold'))
         label.grid(row=ro,column=col,padx=0,pady=0)
def Createlabel1(frame,tex,ro,col):
         label=Label(frame,text=tex,width=11,height=2,fg='#d00',bg='#fff',font=('arial',10,'bold'))
         label.grid(row=ro,column=col,padx=50,pady=0)
#******************************Create Simple Label Ends*************************************************

#*************************************Create Button*************************************************
def CreateButton(frame,tex,com,x,y):
         b1=Button(frame,width=12,height=2,text=tex,command=com,bg='#d00',fg='#fff',font=('arial',15,'bold'))
         b1.place(x=x,y=y)
def CreateButton2(frame,tex,com,r,c):
         b1=Button(frame,width=16,height=2,text=tex,command=com,bg='#d00',fg='#fff',font=('arial',15,'bold'))
         b1.grid(row=r,column=c,padx=42,pady=140)
#******************************Create Button ends******************************************************

#******************************Section for Create Label With Combobox *********************************************         
def createlabelwithcombobox(frame,tex,taxvar,x1,y1,x2,y2,X):
         lb=Label(frame,text=tex,width=20,height=2,fg='#d00',bg='#fff',font=('arial',15,'bold'))
         lb.place(x=x1,y=y1)
         Combo=ttk.Combobox(frame,state='readonly',width=20,height=5,textvariable=taxvar)
         Combo['values']=X
         Combo.place(x=x2,y=y2)
#******************************Section for Create Label With Combobox Ends******************************
A=()
def BatchInfo1():
         global X
         global A
         global B
         CreateFrame()
         Bottomlevelframe=Frame(Mainframe,width=1430,height=750,relief='solid',bd=3,bg='#fff')
         Bottomlevelframe.place(x=0,y=300)
         
         X=list(set(db.Fac()))
         for i in X:
                  print("i=",i)
                  A=A+(i,)
         B=tuple(set(A))
         
         createlabelwithcombobox(Bottomlevelframe,'Please Select Faculty',l1[31],450,100,700,115,B)
         b=Button(Bottomlevelframe,text='Ok',width=10,height=2,bg='#d00',fg='#fff',
                  font=('arial',8,'bold'),command=BatchInfo2)
         b.place(x=600,y=200)
         
         b=Button(Mainframe,text='Back',width=10,height=2,bg='#d00',fg='#fff',
                  font=('arial',8,'bold'),command=admin)
         b.place(x=600,y=750)

def BatchInfo2():
         if l1[31].get()==B[0]:
                  CreateFrame1()
                  Bottomlevelframe=Frame(Mainframe,width=1430,height=750,relief='solid',bd=3,bg='#fff')
                  Bottomlevelframe.place(x=0,y=300)
                  lab=Label(Bottomlevelframe,text=f'Three Subjects Are Assigned for {B[0]} Palese select a Subject',font=('arial',10,'bold'),width=60,height=3,bg='#d00',fg='#fff')
                  lab.place(x=520,y=100)
                  Y=db.Bat(B[0])
                  print(Y)
                  createlabelwithcombobox(Bottomlevelframe,'Please Select Subject',l1[33],500,200,750,215,
                                 Y)
                  b=Button(Bottomlevelframe,text='Ok',width=10,height=2,bg='#d00',fg='#fff',font=('arial',8,'bold'),
                           command=ShowTable)
                  b.place(x=650,y=300)
         elif l1[31].get()==B[1]:
                  CreateFrame1()
                  Bottomlevelframe=Frame(Mainframe,width=1430,height=750,relief='solid',bd=3,bg='#fff')
                  Bottomlevelframe.place(x=0,y=300)
                  lab=Label(Bottomlevelframe,text=f'Two Subjects Are Assigned for {B[1]} Palese select a Subject',font=('arial',10,'bold'),width=60,height=3,bg='#d00',fg='#fff')
                  lab.place(x=470,y=100)
                  Y=db.Bat(B[1])
                  createlabelwithcombobox(Bottomlevelframe,'Please Select Subjects',l1[33],470,200,
                                          750,215,Y)
                  b=Button(Bottomlevelframe,text='Ok',width=10,height=2,bg='#d00',fg='#fff',font=('arial',8,'bold'),
                           command=ShowTable)
                  b.place(x=650,y=300)
                  


         b=Button(Mainframe,text='Back',width=10,height=2,bg='#d00',fg='#fff',
                  font=('arial',8,'bold'),command=BatchInfo1)
         b.place(x=650,y=750)


def ShowTable():
         if l1[33].get()=='Python':
                  CreateFrame1()
                  Bottomlevelframe=Frame(Mainframe,width=1430,height=750,relief='solid',bd=3,bg='#fff')
                  Bottomlevelframe.place(x=0,y=300)
                  lab=Label(Bottomlevelframe,text=f'Please Select A Time Slot for Python',font=('arial',10,'bold'),width=60,height=3,bg='#d00',fg='#fff')
                  lab.place(x=520,y=100)
                  X=db.PyBatch(l1[33].get())
                  print(X)
                  #Y=tuple(set(X))
                  createlabelwithcombobox(Bottomlevelframe,'Please Select Time ',l1[33],470,200,
                                          750,215,X)
                  b=Button(Bottomlevelframe,text='Ok',width=10,height=2,bg='#d00',fg='#fff',font=('arial',8,'bold'),
                           command=F)
                  b.place(x=650,y=300)
                  
         if l1[33].get()=='Java':
                  Javatable()

         b=Button(Mainframe,text='Back',width=10,height=2,bg='#d00',fg='#fff',
                  font=('arial',8,'bold'),command=BatchInfo2)
         b.place(x=650,y=750)
                  

         
         
         
         
         

#**********************************GUI For Lecture Details********************************************************                  
def addlecturedetails():
         
         CreateFrame()
         Bottomlevelframe=Frame(Mainframe,width=1430,height=750,relief='solid',bd=3,bg='#fff')
         Bottomlevelframe.place(x=0,y=300)
         createlabel(Bottomlevelframe,'Subject',l1[8],355,50,550,50)
         createlabelwithcombobox(Bottomlevelframe,'Faculty Name',l1[9],345,200,550,220,('','Lalit Jangid','Kamal Bhatiya','Prashant Hemrajani'))
         createlabel2(Bottomlevelframe,'Starting Date',l1[10],390,100,550,100)
         createlabel2(Bottomlevelframe,'Ending Date',l1[11],760,100,925,100)
         createlabel2(Bottomlevelframe,'Start Time',l1[12],375,150,550,150)
         createlabel2(Bottomlevelframe,'End Time',l1[13],748,150,925,150)
         CreateButton(Bottomlevelframe,'Submit',addintobatch,350,300)
         CreateButton(Bottomlevelframe,'View  All',batchtable,550,300)
         CreateButton(Bottomlevelframe,'Assign Batch',Addintobatch,750,300)
         CreateButton(Bottomlevelframe,'Reset',Reset,950,300)
         b=Button(Mainframe,text='Back',width=10,height=2,bg='#d00',fg='#fff',
                  font=('arial',8,'bold'),command=admin)
         b.place(x=675,y=750)
#***********************************GUI For Lecture Details Ends****************************************************


#***********************************GUI For Faculty Details ********************************************************
def teacher():
         CreateFrame()
         
         
         createlabel(Bottomlevelframe,'Faculty Id',l1[2],464,50,670,50)
         createlabel(Bottomlevelframe,'Faculty Name',l1[3],480,100,670,100)
         createlabel(Bottomlevelframe,'Contact Number',l1[4],490,150,670,150)
         createlabel(Bottomlevelframe,'Address',l1[5],455,200,670,200)
         createlabel(Bottomlevelframe,'Email Id',l1[6],455,250,670,250)
         createlabel(Bottomlevelframe,'Subjects',l1[7],455,300,670,300)
         CreateButton(Bottomlevelframe,"Submit",addintofaculty,550,360)
         CreateButton(Bottomlevelframe,"View",teachertabel,750,360)
         CreateButton(Bottomlevelframe,"Reset",Reset,950,360)
         b=Button(Bottomlevelframe,text='Back',width=10,height=2,bg='#d00',fg='#fff',
                  font=('arial',8,'bold'),command=admin)
         b.place(x=675,y=450)
#***********************************GUI For Faculty Details Ends****************************************************


#***********************************GUI For Enquiry Form Details ********************************************************
def EnquiryForm():
         global Mainframe,Tolevelframe,Bottomlevelframe
         Mainframe=Frame(top,width=1440,height=840,relief='solid',bd=5,bg='#fff')
         Mainframe.place(x=0,y=0)
         l=Label(Mainframe,text='Enquiry Form',width=15,height=2,bg='#d00',fg='#fff',font=('arial',18,'bold'))
         l.place(x=600,y=10)
         createlabel2(Mainframe,'Enquiry No',l1[14],57,100,250,100)
         createlabel2(Mainframe,'Date',l1[15],1050,100,1195,100)
         createlabel3(Mainframe,'Student Name',l1[16],30,150,250,150)
         createlabel3(Mainframe,'Father Name',l1[17],28,200,250,200)
         createlabel2(Mainframe,'Wapp No',l1[18],48,250,250,250)
         createlabel2(Mainframe,'Mob No',l1[19],1050,250,1195,250)
         createlabel2(Mainframe,'FMob No',l1[20],48,300,250,300)
         createlabel2(Mainframe,'Fat Occu',l1[21],1050,300,1195,300)
         createlabel3(Mainframe,'EMail-Id',l1[22],2,350,250,350)
         createlabel3(Mainframe,'Address',l1[23],0,400,250,400)
         createlabel3(Mainframe,'College Name',l1[24],25,450,250,450)
         createlabel2(Mainframe,'Class',l1[25],25,500,250,500)
         createlabel2(Mainframe,'Semester',l1[26],460,500,650,500)
         createlabel2(Mainframe,'Branch',l1[27],985,500,1195,500)
         createlabel2(Mainframe,'Course',l1[28],30,550,250,550)
         createlabel2(Mainframe,'Time Preffered',l1[29],480,550,650,550)
         createlabel2(Mainframe,'Branch Preffered',l1[30],1030,550,1195,550)
         CreateButton(Mainframe,"Submit",addintoenquiry,450,650)
         CreateButton(Mainframe,"View",Enquirytabel,650,650)
         CreateButton(Mainframe,"Reset",Reset,850,650)
         b=Button(Mainframe,text='Back',width=10,height=2,bg='#d00',fg='#fff',
                  font=('arial',8,'bold'),command=admin)
         b.place(x=675,y=750)

#***********************************GUI For Enquiry Form Details Ends****************************************************

#***********************************GUI For Login *************************************************************************                 
def login():
         
         CreateMainFrame()
         #CreateFrame()

         Firmlab=Label(Bottomlevelframe,font=('arial',15,'bold'),width=10,height=2,text='UserName',fg='#d00',bg='#fff')
         Firmlab.place(x=450,y=30)
         E1=Entry(Bottomlevelframe,font=('arial',18,'bold'),textvariable=l1[0],bg='#ffffff',fg='#d00',width=30,justify='left',state=NORMAL)
         E1.place(x=600,y=35)

         Firmlab=Label(Bottomlevelframe,font=('arial',15,'bold'),text='Password',fg='#d00',bg='#fff',width=10,height=2)
         Firmlab.place(x=450,y=100)
         E1=Entry(Bottomlevelframe,font=('arial',18,'bold'),textvariable=l1[1],bg='#fff',fg='#d00',width=30,justify='left',state=NORMAL)
         E1.place(x=600,y=105)
         CreateButton(Bottomlevelframe,'Submit',verify1,550,170)
         CreateButton(Bottomlevelframe,'Reset',Reset,750,170)
         b=Button(Bottomlevelframe,text='Back',width=10,height=2,bg='#d00',fg='#fff',font=('arial',8,'bold'),command=create)
         b.place(x=675,y=280)
#***********************************GUI For Login Ends************************************************************************
#***********************************GUI For Admin Starts*************************************************************************
def admin():
         #CreateFrame()
         CreateMainFrame()
         CreateButton2(Bottomlevelframe,"Enquiry Form",EnquiryForm,1,0)
         CreateButton2(Bottomlevelframe,"Add New Faculty",teacher,1,1)
         CreateButton2(Bottomlevelframe,"Add New Batch",addlecturedetails,1,2)
         CreateButton2(Bottomlevelframe,"Batch Info",BatchInfo1,1,3)
         CreateButton2(Bottomlevelframe,"See Attendance",enquiryform,1,4)
         CreateButton2(Bottomlevelframe,"Update Information",enquiryform,1,5)
         
         b=Button(Bottomlevelframe,text='Back',width=10,height=2,bg='#d00',fg='#fff',
                  font=('arial',8,'bold'),command=login)
         b.place(x=675,y=250)
#***********************************GUI For Admin Ends*************************************************************************


#***********************************GUI For Create FrontPage*************************************************************************
def create():
         #CreateFrame()
         CreateMainFrame()
         
         Mainbtn1=Button(Bottomlevelframe,command=login,image=img1,bg='#d00',fg='#fff')
         Mainbtn1.place(x=520,y=100)
         lab=Label(Bottomlevelframe,text='Admin',width=10,height=1,font=('arial',15,'bold'),fg='#fff',bg='#d00')
         lab.place(x=520,y=232)
         Mainbtn2=Button(Bottomlevelframe,bd=1,image=img2,bg='#d00',fg='#fff')
         Mainbtn2.place(x=780,y=100)
         lab=Label(Bottomlevelframe,text='User',width=10,height=1,font=('arial',15,'bold'),fg='#fff',bg='#d00')
         lab.place(x=780,y=232)
         b=Button(Bottomlevelframe,text='Back',width=10,height=2,bg='#d00',fg='#fff',
                  font=('arial',8,'bold'),command=CraeteFront)
         b.place(x=675,y=350)
         


#***********************************GUI For FrontPage Ends*************************************************************************

         
         
         

#*****************************Function for Insert Data in Table**************************************
def addintoenquiry():
         db.Insertdataintoenquiry([l1[14],l1[15],l1[16],l1[17],l1[18],l1[19],l1[20],l1[21],l1[22],l1[23],l1[24],l1[25],l1[26],l1[27],l1[28],l1[29],l1[30]])


def addintofaculty():
         db.Insertdata((l1[2],l1[3],l1[4],l1[5],l1[6],l1[7]))
         '''createlabelwithcombobox(Toplevelframe,'SubjectName',0,0,('Python','Java','C','C++','Excel'))
         createlabelwithcombobox(Toplevelframe,'BranchName',0,1,('Mansarover','PratapNager'))
         CreateButton(Toplevelframe,'Save',Saveadditionalinformation,4,2)'''


def addintobatch():
         db.Insertdataintobatch([l1[8],l1[9],l1[10],l1[11],l1[12],l1[13]])

def Addintobatch():
         if l1[9].get()=='Lalit Jangid':
                  X=db.P()
                  db.InsertdataintoPython(X)
                  db.deletefromenquiry(X[0])
         if l1[9].get()=='Kamal Bhatiya':
                  X=db.J()
                  db.InsertdataintoJava(X)
                  db.deletefromenquiry(X[0])
                  
         if l1[9].get()=='Prashant Hemrajani':
                  X=db.C()
                  db.InsertdataintoC(X)
                  db.deletefromenquiry(X[0])
                  

#*****************************Function for Insert Data in Table**************************************         


#****************************************Function for Create Table Of Batch*****************************
def batchtable():
         '''global root2
         global blist
         top.iconify()
         root2=Tk()
         root2.geometry('3000x3000')
         root2.configure(bg='#fff')'''
         
         Mainframe=Frame(top,width=1440,height=840,relief='solid',bd=5,bg='#fff')
         Mainframe.pack(side='top',expand='yes',fill='both')
         
         
         for i in range(0,6):
                  global l
                  Createlabel1(Mainframe,blist[l],0,l)
                  l=l+1
         X=db.Displaydataofbatch()
         for i in  X:
                  for j in i:
                           global k
                           global n
                  

                           Createlabel1(Mainframe,j,n,k)
                           k=k+1
                  n=n+1
                  k=0
         b=Button(top,text='Back',width=10,height=2,bg='#d00',fg='#fff',font=('arial',8,'bold'),
                  command=addlecturedetails)
         b.pack(side='top')
#****************************************Function for Create Table Of Batch Ends*****************************


#****************************************Function for Create Table Of Teacher Table*****************************         
def teachertabel():
         global root2
         global tlist
         top.iconify()
         root2=Tk()
         root2.geometry('3000x3000')
         
         img5=PhotoImage(file="C:\\Users\\shyam tailor\\Desktop\\baack.png")
         Mainframe=Frame(root2,width=1440,height=840,relief='solid',bd=5,bg='#fff')
         Mainframe.pack(side='top')
         for i in range(0,6):
                  global l
                  Createlabel1(Mainframe,tlist[l],2,l)
                  l=l+1
         X=db.Displaydata()
         for i in  X:
                  for j in i:
                           global k
                           global n

                           Createlabel1(Mainframe,j,n,k)
                           k=k+1
                  n=n+1
                  k=0
         print("n and k=",n,k)
         #CreateButton2(Mainframe,'Back',deiconify,n,k+2)
         b=Button(root2,text='Back',width=10,height=2,bg='#d00',fg='#fff',font=('arial',8,'bold'),command=deiconify)
         b.pack(side='top')
#****************************************Function for Create Table Of Teacher Ends*****************************



#****************************************Function for Create Table Of Enquiry Starts*****************************
def Enquirytabel():
         
         Mainframe=Frame(top,width=1440,height=840,relief='solid',bd=5,bg='#fff')
         Mainframe.pack(side='top',expand='yes',fill='both')
         
         
         for i in range(0,17):
                  global l
                  Createlabel(Mainframe,elist[l],2,l)
                  l=l+1
         X=db.Displaydataofenquiry()
         for i in  X:
                  for j in i:
                           global k
                           global n

                           Createlabel(Mainframe,j,n,k)
                           k=k+1
                  n=n+1
                  k=0
         print("n and k=",n,k)
         b=Button(top,text='Back',width=10,height=2,bg='#d00',fg='#fff',font=('arial',8,'bold'),command=EnquiryForm)
         b.pack(side='top')
#****************************************Function for Create Table Of Enquiry Ends*****************************
def Pythontable():
         Mainframe=Frame(top,width=1440,height=840,relief='solid',bd=5,bg='#fff')
         Mainframe.pack(side='top',expand='yes',fill='both')
         
         
         for i in range(0,5):
                  global l
                  Createlabel(Mainframe,Slist[l],2,l)
                  l=l+1
         X=db.DisplaydataofOython()
         for i in  X:
                  for j in i:
                           global k
                           global n

                           Createlabel(Mainframe,j,n,k)
                           k=k+1
                  n=n+1
                  k=0
         b=Button(top,text='Back',width=10,height=2,bg='#d00',fg='#fff',font=('arial',8,'bold'),command=BatchInfo2)
         b.pack(side='top')

def Javatable():
         Mainframe=Frame(top,width=1440,height=840,relief='solid',bd=5,bg='#fff')
         Mainframe.pack(side='top',expand='yes',fill='both')
         
         
         for i in range(0,5):
                  global l
                  Createlabel(Mainframe,Slist[l],2,l)
                  l=l+1
         X=db.DisplaydataofJava()
         for i in  X:
                  for j in i:
                           global k
                           global n

                           Createlabel(Mainframe,j,n,k)
                           k=k+1
                  n=n+1
                  k=0
         b=Button(top,text='Back',width=10,height=2,bg='#d00',fg='#fff',font=('arial',8,'bold'),command=BatchInfo2)
         b.pack(side='top')
         





#******************************Verification of PassWord**********************************************
def verify1():
         if  l1[0].get()=='admin' and l1[1].get()=='123':
                  admin()
                  messagebox.showinfo("Title","Your Welcome Admin")

def Reset():
         for i in l1:
                  i.set('')

#******************************Verification of PassWord Ends**********************************************
def Saveadditionalinformation():
         pass
def deiconify():
         root2.withdraw()
         top.deiconify()
def enquiryform():
         print("Hello")
def F():
         print("Hello")
CraeteFront()
#CreateMainFrame()
#create()
top.mainloop()
  
  
