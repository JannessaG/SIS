from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
from tempfile import NamedTemporaryFile
import shutil
import csv 


display_list=[]
delete_list=[]
search_list=[]
search=[]
delete_id=[]
update=[]
update_id=[]
update_name=[]
update_gender=[]
update_course=[]
update_year=[]

def display_read_row(): 
	for i in tree.get_children():
		tree.delete(i)
	display_list.clear()
	search_list.clear()
	update_name.clear()
	update_id.clear()
	update_year.clear()
	update_course.clear()
	update_gender.clear()

	with open('students.csv','r') as csvfile:
		student_data =csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		for row in student_data:
			display_list.append(row)
		count=0
		tuples=[]
		for i in display_list:
			if len(i)==0:
				count+=1
			elif count !=0 and (i[0]) !="" and (i[0]) !="" and (i[0]) != "" and (i[0]) != "" and (i[0]) !="":
				index=0
				row_data = (i[0],i[1],i[2],i[3],i[4])
				tuples.append(row_data)
		for row in tuples:
			tree.insert("",index,value=row)
			index= index+1	


def create_row():
	display_list.clear()
	id=[]
	x=[]
	counter=0
	with open('students.csv','r') as csvfile:
		reader=csv.reader(csvfile)
		for row in reader:
			if len(row)==0:
				x.append(row)
		for j in x:
			counter+=1
		if counter>0 and counter<10:
			id.append("2021-000"+str(counter))
		if counter>=10 and counter<100:
			id.append("2021-00"+str(counter))
		if counter>=100 and counter<1000:
			id.append("2021-0"+str(counter))
		if counter>=1000 and counter<10000:
			id.append("2021-"+str(counter))

	stud_name=entry_name.get()
	stud_gender=entry_gender.get()
	stud_course=entry_course.get()
	stud_yearlvl=entry_year.get()

	with open('students.csv','a') as csvfile:
		writer= csv.writer(csvfile,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writer.writerow([id[0],str(stud_name),str(stud_course),str(stud_yearlvl),str(stud_gender)])
		with open('students.csv','r') as csvfile:
			reader= csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	
	id.clear()
	x.clear()
	display_read_row()

def search_row(): 
	x=entry_search.get()
	with open('students.csv','r')as csvfile:
		reader=csv.reader(csvfile)
		for row in reader:
			search.append(row)

	checkernum=0
	for e in search:
		if len(e)!=0:
			if str(e[0])==x or str(e[1])==x or str(e[2])==x or str(e[3])==x or str(e[4])==x:
				checkernum+=1
	if checkernum==0:
		messagebox.showerror("ERROR","Data doesn't exist")
	else:
		for i in search:
			if len(i)!=0:
				if str(i[0])==x or str(i[1])==x or str(i[2])==x or str(i[3])==x :
					search_list.append(i)
	for b in search_list:
		tree.insert("","end",values=b)

def update_record():
	selected=tree.focus()
	tree.item(selected,text="",values=(entry_search.get(),entry_name.get(),entry_course.get(),entry_year.get(),entry_gender.get()))
	
	search_list.clear()
	display_list.clear()
	delete_list.clear()
	update_id.clear()
	update_name.clear()
	update_course.clear()
	update_year.clear()
	update_gender.clear()

	id=update[0]
	name=entry_name.get()
	course=entry_course.get()
	year=entry_year.get()
	gender=entry_gender.get()
	
	update_id.append(id)
	update_name.append(name)
	update_course.append(course)
	update_year.append(year)
	update_gender.append(gender)

	filename='students.csv'
	tempfile=NamedTemporaryFile(mode='w',delete=False)

	fields=['ID no.','Name','Course','Year','Gender']

	with open(filename,'r') as csvfile,tempfile:
		reader=csv.DictReader(csvfile, fieldnames=fields)
		writer=csv.DictWriter(tempfile, fieldnames=fields)
		
		for row in reader:
			if row['ID no.']== str(update_id[0]):
				row['Name'],row['Course'],row['Year'],row['Gender']=update_name[0],update_course[0],update_year[0],update_gender[0]
			row={'ID no.':row['ID no.'],'Name':row['Name'],'Course': row['Course'],'Year':row['Year'],'Gender':row['Gender']}
			writer.writerow(row)

	shutil.move(tempfile.name,filename)
	entry_search.delete(0,END)
	entry_name.delete(0,END)
	entry_gender.delete(0,END)
	entry_course.delete(0,END)
	entry_year.delete(0,END)
	del_spaces()


def remove_row():
	a=delete_id[0]
	x=tree.selection()
	for selected_item in x:
		tree.delete(selected_item)
		with open('students.csv','r') as readfile:
			student_data=csv.reader(readfile)
			for row in student_data:
				delete_list.append(row)
			for i in delete_list:
				if len(i)!=0:
					if i[0]==a:
						delete_list.remove(i)

		with open('students.csv','w') as writefile:
			writer=csv.writer(writefile)
			writer.writerows(delete_list)
	clear()


def select_record(self):
	delete_id.clear()
	entry_search.delete(0,END)
	entry_name.delete(0,END)
	entry_gender.delete(0,END)
	entry_course.delete(0,END)
	entry_year.delete(0,END)

	selected=tree.focus()
	values=tree.item(selected,'values')
	delete_id.append(values[0])
	update.append(values[0])
	entry_search.insert(0,values[0])
	entry_name.insert(0,values[1])
	entry_course.insert(0,values[2])
	entry_year.insert(0,values[3])
	entry_gender.insert(0,values[4])
	entry_name.focus()

def del_spaces():
	a=[]
	with open('students.csv','r') as readfile:
		student_data=csv.reader(readfile)
		for row in student_data:
			if len(row)!=0:
				a.append(row)
	with open('students.csv','w') as writefile:
		writer=csv.writer(writefile)
		writer.writerows(a)

#------------------------------BUTTON FUNCTIONS---------------------------------------------------
def search_button(): 
	search_id=entry_search.get()
	search_list.clear()
	search.clear()
	for i in tree.get_children():
		tree.delete(i)
	if entry_search==" ":
		messagebox.showerror("ERROR","Invalid Data Entry")
		entry_search.focus()
	else:
		search_row()
		entry_search.focus()


def add_button(): 
	add_name=entry_name.get()
	add_gender=entry_gender.get()
	add_course=entry_course.get()
	add_year= entry_year.get()
	with open('students.csv','r') as csvfile:
		student_data=csv.reader(csvfile,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

		for row in student_data:
			search.append(row)

	checker=0
	for i in search:
		if len(i)!=0:
			if str(i[1]) == add_name and str(i[2]) == add_course and str(i[3]) == add_year and str(i[4]) == add_gender :
				checker+=1
	if checker>0:
		messagebox.showerror("Error","Data already excisted.")
	elif add_name =="" or add_gender =="" or add_course =="" or add_year =="":
			messagebox.showerror("Error","Invalid Data Entry")
	else:
		create_row()
		entry_search.delete(0,END)
		entry_name.delete(0,END)
		entry_gender.delete(0,END)
		entry_course.delete(0,END)
		entry_year.delete(0,END)
		messagebox.showinfo("Success","Data added successfully")
		entry_name.focus()


def delete_button():
	message=tk.messagebox.askquestion('Delete','Are you sure you want to delete this data? ')
	if message=='yes':
		remove_row()
		del_spaces()
		entry_name.focus()
	else:
		tk.messagebox.showinfo('Delete','Failed to delete')


def update_button():
		message=tk.messagebox.askquestion("Update Data","Update this data?")
		if message=='yes':
			update_record()
			entry_name.delete(0,END)
			entry_gender.delete(0,END)
			entry_course.delete(0,END)
			entry_year.delete(0,END)
			messagebox.showinfo("Update","Data is updated successfully!")
			entry_name.focus()
		else:
			tk.messagebox.showinfo("","Cancelled Update")


def clear():
	display_list.clear()
	delete_list.clear()
	search_list.clear()
	update_name.clear()
	update_course.clear()
	update_year.clear()
	update_gender.clear()
	entry_search.delete(0,END)
	entry_name.delete(0,END)
	entry_gender.delete(0,END)
	entry_course.delete(0,END)
	entry_year.delete(0,END)
	for i in tree.get_children():
		tree.delete(i)
	entry_name.focus()


#-------------------------------------------WINDOW OBJ------------------------------------
window= Tk()
window.geometry("800x430")
window.title("Student Information System")

#-----------------------Label and Entries---------------------------------------------
Name_text= StringVar()
Gender_text= StringVar()
Course_text= StringVar()
Year_text= StringVar()
ID_text= StringVar()

label_name=Label(window,text="Full Name")
label_name.grid(row=0,column=2)
entry_name=Entry(window,textvariable=Name_text)
entry_name.grid(row=0,column=3)

label_gender=Label(window,text="Gender")
label_gender.grid(row=1,column=2)
entry_gender=Entry(window,textvariable=Gender_text)
list1=['F','M']
droplist = OptionMenu(window,Gender_text,*list1)
droplist.config(width=15)
Gender_text.set('F')
droplist.grid(row=1,column=3)

label_course=Label(window,text="Course")
label_course.grid(row=0,column=4)
entry_course=Entry(window,textvariable=Course_text)
entry_course.grid(row=0,column=5)

label_year=Label(window,text="Year level")
label_year.grid(row=1,column=4)
entry_year=Entry(window,textvariable=Year_text)
list2=['1','2','3','4']
droplist = OptionMenu(window,Year_text,*list2)
droplist.config(width=15)
Year_text.set('1')
droplist.grid(row=1,column=5)


label_space=Label(window,text="             ")
label_space.grid(row=2,column=2)


label_searchId=Label(window,text="ID no.")
label_searchId.grid(row=3,column=3)
entry_search=Entry(window,textvariable=ID_text)
entry_search.grid(row=3,column=4)


label_space1=Label(window,text="            ")
label_space1.grid(row=4,column=0)

#-----------------------BUTTONS-----------------
button_search=Button(window,text="Search",width=12,command=search_button)
button_search.grid(row=3,column=5)

button_display=Button(window,text="Display All",width=12, command=display_read_row)
button_display.grid(row=6,column=2)

button_add=Button(window,text="Add",width=12,command=add_button)
button_add.grid(row=6,column=3)

button_update=Button(window,text="Update",width=12,command=update_button)
button_update.grid(row=6,column=4)

button_delete=Button(window,text="Delete",width=12,command=delete_button)
button_delete.grid(row=6,column=5)

#--------------------------TREE VIEW------------------------
tree = ttk.Treeview(window,selectmode='browse')
tree.place(x=10,y=170)
vsb= ttk.Scrollbar(window, orient ="vertical",command=tree.yview)
vsb.place(x=769,y=170,height=225)
tree.configure(yscrollcommand=vsb.set)
tree.bind('<ButtonRelease-1>',select_record)
tree["columns"]=("1","2","3","4","5")
tree["show"]="headings"
tree.column("1",width =150,anchor='c')
tree.column("2",width =150,anchor='c')
tree.column("3",width =150,anchor='c')
tree.column("4",width =150,anchor='c')
tree.column("5",width =150,anchor='c')
tree.heading("1",text="ID no.")
tree.heading("2",text="Name")
tree.heading("3",text="Course")
tree.heading("4",text="Year")
tree.heading("5",text="Gender")


window.mainloop()


