import mysql.connector as ms
db= ms.connect(host="localhost", user= "root", passwd = "123", database= "Patient",auth_plugin='mysql_native_password')
f= db.cursor()





def display():
    c=0
    f.execute("Select p_id,p_name,p_phone,age,gender,blood_grp,date_of_a, date_of_d, dpt,doctor from details;")
    display=f.fetchall()
    for i in display:
        c=c+1
        print("Record",c)
        print("Patient ID:", i[0])
        print("Patient Name:", i[1])
        print("Phone Number:", i[2])
        print("Age:", i[3])
        print("Gender:", i[4])
        print("Blood Group:", i[5])
        print("Date of Admission:", i[6])
        print("Date of Discharge:", i[7])
        print("Department:", i[8])
        print("Doctor's Name:", i[9])
        print("------------------------------")
def insert():
    p_id= int(input("Enter patient id: "))
    p_name= input("Enter patient name: ")
    p_phone= input("Enter patient's phone number: ")
    dpt=input("Enter patient's department: ")
    age=int(input("Enter patient's age: "))
    gender=input("Enter patient's gender: ")
    bg=input("Enter patient's blood group: ")
    
    doa=input("Enter date of admission(YYYY-MM-DD): ")
    dod=input("Enter date of discharge(YYYY-MM-DD): ")
    doctor=input("Enter name of doctor: ")
    
    f.execute("insert into details(p_id,p_name,p_phone,age,gender,blood_grp,date_of_a, date_of_d,dpt,doctor) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(p_id,p_name,p_phone,age,gender,bg,doa,dod,dpt,doctor))
    f.execute("commit;")

    meds= int(input("Enter cost of medicine: "))
    icu= int(input("Enter days spent in ICU: "))
    ultras= int(input("Enter number of ultrasound done: "))
    xrays= int(input("Enter number of xrays taken: "))
    ct= int(input("Enter number of CT Scan done: "))
    misc= int(input("Enter miscellaneous costs: "))
    room=input("Enter patient's room type(standard/semi-deluxe/deluxe): ")
    days=int(input("Enter number of days patient stayed in hospital: "))
    f.execute("insert into course(p_id,medicine,icu,ultrasound,xrays,ct,misc,room,days) values({},{},{},{},{},{},{},'{}',{})".format(p_id,meds,icu,ultras,xrays,ct,misc,room,days))
    f.execute("commit;")
    print("Record added! ")


def modify():
 while True:
    
    p_id= int(input("Enter ID of patient whose record you want to modify record of: "))
    print("What do you want to modify?")
    print("1: Patient ID\n2:Patient Name\n3:Phone Number\n4:Patient Age\n5:Patient's Gender\n6:Patient's Blood Group\n7:Date of Admission\n8:Date of Discharge\n9:Department\n10:Doctor")
    print("11:Medicine Cost\n12:Room Type\n13:Number of days in ICU\n14:Number of Ultrasounds taken\n15:Number of X-rays taken\n16:Number of CT Scan done:\n17:Miscellaneous Costs\n18:Number of Days in Hospital")
    ch=int(input("Enter your choice: "))
    if ch==1:
        p_idnew= int(input("Enter new patient id: "))
        f.execute("update details set p_id= '{}' where p_id='{}';".format(p_idnew,p_id))
        f.execute("commit;")
    elif ch==2:
        p_name= input("Enter patient name: ")
        f.execute("update details set p_name= '{}' where p_id='{}';".format(p_name,p_id))
        f.execute("commit;")
        
    elif ch==3:
        p_phone= int(input("Enter patient's phone number: "))
        f.execute("update details set p_phone= '{}' where p_id='{}';".format(p_phone,p_id))
        f.execute("commit;")
    elif ch==4:
        age=int(input("Enter patient's age: "))
        f.execute("update details set age= '{}' where p_id='{}';".format(age,p_id))
        f.execute("commit;")

    elif ch==5:
        gender=input("Enter patient's gender: ")
        f.execute("update details set gender= '{}' where p_id='{}';".format(gender,p_id))
        f.execute("commit;")
    elif ch==6:
        bg=input("Enter patient's blood group: ")
        f.execute("update details set blood_grp= '{}' where p_id='{}';".format(bg,p_id))
        f.execute("commit;")
    elif ch==7:
        doa=input("Enter date of admission(YYYY-MM-DD): ")
        f.execute("update details set date_of_a= '{}' where p_id='{}';".format(doa,p_id))
        f.execute("commit;")
    elif ch==8:
        dod=input("Enter date of discharge(YYYY-MM-DD): ")
        f.execute("update details set date_of_d= '{}' where p_id='{}';".format(dod,p_id))
    

    elif ch==9:
        dpt=input("Enter patient's department: ")
        f.execute("update details set dpt= '{}' where p_id='{}';".format(dpt,p_id))
        f.execute("commit;")

    elif ch==10:
        doctor=input("Enter name of doctor: ")
        f.execute("update details set doctor= '{}' where p_id='{}';".format(doctor,p_id))
        f.execute("commit;")

    elif ch==11:
        meds= int(input("Enter cost of medicine: "))
        f.execute("update course set medicine= '{}' where p_id='{}';".format(meds,p_id))
        f.execute("commit;")
    elif ch==12:
        room=input("Enter patient's room type(standard/semi-deluxe/deluxe): ")
        f.execute("update course set room= '{}' where p_id='{}';".format(room,p_id))
        f.execute("commit;")
        
    elif ch==13:
        icu= int(input("Enter days spent in ICU: "))
        f.execute("update course set icu= '{}' where p_id='{}';".format(icu,p_id))
        f.execute("commit;")
    elif ch==14:
        ultras= int(input("Enter number of ultrasound done: "))
        f.execute("update course set ultrasound= '{}' where p_id='{}';".format(ultras,p_id))
        f.execute("commit;")
    elif ch==15:
        xrays= int(input("Enter number of xrays taken: "))
        f.execute("update course set xrays= '{}' where p_id='{}';".format(xrays,p_id))
        f.execute("commit;")
    elif ch==16:
        ct= int(input("Enter number of CT Scan done: "))
        f.execute("update course set ct= '{}' where p_id='{}';".format(ct,p_id))
        f.execute("commit;")
        
    elif ch==17:
        misc= int(input("Enter miscellaneous costs: "))
        f.execute("update course set misc= '{}' where p_id='{}';".format(misc,p_id))
        f.execute("commit;")
    elif ch==18:
        days=int(input("Enter number of days in hospital: "))
        f.execute("update course set days={} where p_id={};".format(days,p_id))
        f.execute("commit;")

    else:
        print("Invalid Choice")
    
    y_n=input("Do you want to modify more records?(y/n): ")
    if y_n=="n":
        print("Records updated!")
        break
    
       
    

def search():

    p_id= int(input("Enter patient's ID to search: "))
    f.execute("Select p_id,p_name,p_phone,age,gender,blood_grp,date_of_a, date_of_d,dpt,doctor from details where p_id={};".format(p_id))
    
    rec= f.fetchone()
    if rec== None:
        print("Patient ID not found")
    else:
        print("Patient ID:", rec[0])
        print("Patient Name:", rec[1])
        print("Phone Number:", rec[2])
        print("Age:", rec[3])
        print("Gender:", rec[4])
        print("Blood Group:", rec[5])
        print("Date of Admission:", rec[6])
        print("Date of Discharge:", rec[7])
        print("Department:", rec[8])
        print("Doctor's Name:", rec[9])


    


def delete():
    p_id= int(input("Enter patient id to delete: "))
    f.execute("delete from details where p_id= {};".format(p_id))
    f.execute("commit;")
    f.execute("delete from course where p_id= {};".format(p_id))
    f.execute("commit;")
    print("Record deleted")

def bill():
    total=0
    p_id = int(input("Enter Patient ID: "))
    f.execute("select medicine,icu,ultrasound,xrays,ct,misc,room,days from course where p_id={};".format(p_id))
    costs=f.fetchone()
    #medicine cost
    meds= costs[0]
    #No of scans
    icu= costs[1]
    ultras=costs[2]
    xrays=costs[3]
    ct=costs[4]
    #miscellaneous costs
    misc=costs[5]
    #Room type
    room= costs[6]
    #Days in hospital
    days= costs[7]
    #ROOM COSTS
    room_bill=0
    if room == "standard":
        room_bill= days*500
    elif room== "semi-deluxe":
        room_bill= days*2000
    elif room == "deluxe":
        room_bill= days*10000
    else:
        room_bill=0
        
    #scan cost
    icu_bill=100000*icu
    xray_bill= 700*xrays
    ct_bill= ct*1000
    ultras_bill = ultras*500

    #TOTAL
    total= room_bill+ icu_bill+xray_bill+ct_bill+ultras_bill+meds+misc
    #BILL
    
    display=f.fetchone()
    print("------SUSHMITA TIWARI HOSPITAL BILL---------------------------------")
    f.execute("Select p_id,p_name,age,gender,blood_grp,p_phone,date_of_a, date_of_d,dpt,doctor from details where p_id={};".format(p_id))
    rec=f.fetchone()
    print("Patient ID:", rec[0])
    print("Name: ", rec[1], end= "   ")
    print("Age: ", rec[2], end= "   ")
    print("Gender: ", rec[3], end= "    ")
    print("Blood Group: ", rec[4])
    print("Phone Number: ", rec[5])
    print("Date of Admission: ", rec[6])
    if rec[7] != None:
        print("Date of Discharge: ", rec[7])
    print("Department: ", rec[8],end="  ")
    print("Doctor: ",rec[9])
    print("------------------------------------------------------------------------------------------------------------")

    print("Room Charges= Rs", room_bill)
    if icu_bill !=0:
        print("ICU Charges= Rs", icu_bill)
    if xray_bill !=0:
        print("X- Ray Charges= Rs", xray_bill)
    if ct_bill !=0:
        print("CT Scan Charges= Rs", ct_bill)

    if ultras_bill !=0:
        print("Ultrasound Charges= Rs", ultras_bill)

    print("Medicine Charges= Rs", meds)
    print("Miscellaneous Charges= Rs", misc)
    print("Total charges before tax= Rs",total)
    print("GST Charged= 5%")
    tax= total*0.05
    print("Final cost to pay= Rs", total+tax)


'''def report():
    dr= input("Enter name of primary consultant(doctor): ")
    dr_2= input("Enter name of secondary consultant(doctor): ")
    days= int(input("Enter number of days in hospital: "))
    history= input("Enter past medical history of patient: ")
    diag= input("Enter diagnosis of patient: ")
    sym= input("Enter symptoms: ")
    treat = input("Enter treatment offered to patient: ")
    course = input("Enter hospitalization course of patient: ")
    response= input("Enter response of patient to treatment: ")
    medicine= input("Enter medicine provided to patient during hospitalization course: ")
    care= input("Enter follow-up care provided to patient: ")
    recom= input("Enter recommendations for patient: ")
    post_dis= input("Enter post-discharge instructions: ")
    dis_sts= input("Enter discharge status: ")
    prognosis= input("Enter prognosis of patient: ")

    #report generation
    print("------SUSHMITA TIWARI HOSPITAL BILL---------------------------------")
    f.execute("select p_id, p_name, age, sex, dpt from details where p_id= {};".format(p_id))
    rec=f.fetchone()
    print("Patient ID:", rec[0])
    print("Name: ", rec[1], end= "   ")
    print("Age: ", rec[2], end= "   ")
    print("Gender: ", rec[3])
    print("Number of days in hospital: ", days)
    print("Departemnt: ", rec[4])
    
    print("Primary Consultant: ", dr)
    print("--------------------------------------------------------------------")
    print("Secondary consultant: ", dr_2)
    print("Medical History: ")
    print(history)
    print("Diagnosis: ")
    print(diag)
    print("Symptoms: ")
    print(sym)
    print("Treament recieved: ")
    print(treat)
    print("Hospitalization Course: ")
    print(course)
    print("Response of patient: ")
    print(response)
    print("Medications: ")
    
    print("Follow up care: ")'''
    
    
    
    
    
while True:
    print ("SUSHMITA TIWARI HOSPITAL MANAGEMENT")        
    print("1: Display all the records of patients")
    print("2: Insert record of new patient")
    print("3: Modify an existing record")
    print("4: Delete record of existing patient")
    print("5: Search record of existing patient")
    print("6: Generate bill")
    print("7: Exit")
    n=int(input("Choose option you want to perform: "))

    if n==1:
        display()
    elif n==2:
        insert()
    elif n==3:
        modify()
    elif n==4:
        delete()
    elif n==5:
        search()
    elif n==6:
        bill()
    elif n==7:
        print("System is closed")
    else:
        print("wrong choice")    

    
        

    
    
