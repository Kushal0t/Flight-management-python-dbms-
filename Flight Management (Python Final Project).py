import mysql.connector as mys
mycon = mys.connect(host='localhost',user='root',passwd='123456',database='flight_management')
mycursor = mycon.cursor()



mycursor.execute('select flight_ID from flight_list')
mydata = mycursor.fetchall()
fl_list = []
for i in mydata:
    fl_list.append(i[0])
    
origin_list = []
mycursor.execute('select origin from flight_list')
mydata = mycursor.fetchall()
for i in mydata:
    origin_list.append(i[0])
    
destination_list = []
mycursor.execute('select destination from flight_list')
mydata = mycursor.fetchall()
for i in mydata:
    destination_list.append(i[0])


def start():
    print('''
======================================
     FLIGHT MANAGEMENT SYSTEM
======================================      
''')

    print('Choose your action:')
    print('1:◀ Book a Ticket  ▶')
    print('2:◀ Cancel Ticket  ▶')
    print('3:◀ View Seat Map  ▶')
    print('4:◀ Search Flights ▶')
    print('5:◀ Admin Window   ▶')
    print('6:◀ Exit           ▶')



seats = ['A1','B1','C1','D1','E1','F1',
         'A2','B2','C2','D2','E2','F2',
         'A3','B3','C3','D3','E3','F3',
         'A4','B4','C4','D4','E4','F4',
         'A5','B5','C5','D5','E5','F5',
         'A6','B6','C6','D6','E6','F6',
         'A7','B7','C7','D7','E7','F7',
         'A8','B8','C8','D8','E8','F8']


def map_top():
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print(''' window middle aisle     aisle  middle window
◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫◫
   A      B      C         D      E      F''')   


def seat_map(a):
    mycursor.execute('select * from seats' + a)
    mydata = mycursor.fetchall()
    l = []
    for i in mydata:
        x, y = i
        l.append(x)

    r = 2
    c = 1
    print(1,end='  ')
    
    for i in seats:
        if c < 6:
            if i in l:
                print('■',end='      ')
            else:
                print('□',end='      ')
            c += 1
        else:
            if i in l:
                print('■')
            else:
                print('□')

            if i != "F8":
                print(r,end='  ')
                r += 1

            c = 1     

        if c == 4:
            print('   ',end='')

bk_id = 1

while True:
    start()
    n = int(input('Enter the no. for action(1-6): '))
    if n in [1, 2, 3, 4, 5]:
        c = input("Are you sure? (Y/N): ")

        while c.upper() not in ['Y', 'N']:
            print("Invalid choice! Enter Y or N only.")
            c = input("Are you sure? (Y/N): ")

        if c.upper() == 'N':
            print("Action cancelled. Returning to main menu...\n")
            continue

# ========================== BOOKING =================================

    if n == 1:
        print('=====TICKET BOOKING=====')
        print("Passenger Detail>>>")
        a = input('Name: ')
        b = input('Age: ')
        c = input('Gender(M/F/O): ')
        d = input('Phone No.: ')
        
        print('Flight Details>>>')
        e = input('Enter Origin City: ')
        
        while e not in origin_list:
            print("Sorry we dont operate here!")
            e = input('Enter Origin City: ')
            
        f = input('Enter Destination City: ')
        while f not in destination_list:
            print("Sorry we dont operate here!")
            f = input('Enter Destination City: ')
        
        print('Clases: [First][Buisness][Economy]')
        fl_cl = ['First','Buisness','Economy']
        g = input("Enter Seat Class: ")
        while g not in fl_cl:
            print('XXXXX Class Doesn’t Exist XXXXX')
            g = input("Enter Seat Class: ")
            

    
        mycursor.execute("SELECT flight_ID FROM flight_list WHERE origin = '" + e + "' AND destination = '" + f + "'")
        mydata = mycursor.fetchall()

        p = ""
        for i in mydata:
            p = i[0]
        if mydata == []:
            print("No flights found for that Origin–Destination. Returning to menu.")
            continue
            
        h = input('Enter SeatID: ')
        
        
        while True:
            mycursor.execute("select seat_no from seats" + p)
            mydata = mycursor.fetchall()

            z = []
            for i in mydata:
                z.append(i[0])
                
            if h not in seats:
                print("Wrong SeatID!")
                h = input("Enter SeatID: ")

            elif h in z:
                print("Seat already booked!")
                h = input("Enter SeatID: ")

            else:
                break


        # departure time
        mycursor.execute("select departure_time from flight_list where flight_ID='" + p +"'")
        mydata = mycursor.fetchall()
        for i in mydata:
            time = i[0]


        price = ['₹34000','₹15000','₹8099']
        print()
        print('========TICKET BOOKED========')
        print('Booking ID:', bk_id)
        print('Name:', a)
        print('Flight:', p)
        print('Seat:', h, ':', g, 'Class')
        print('Price:', price[fl_cl.index(g)])
        print('Departure Time:', time)
        print('=============================')

        i = str(bk_id)
        mycursor.execute("INSERT INTO ticket VALUES ('" + i + "', '" + a + "', '" + h + "', '" + p + "')")
        mycon.commit()
        
        table_name = "seats" + p  
        query = "INSERT INTO " + table_name + " VALUES ('" + h + "', '" + p + "')"
        mycursor.execute(query)
        mycon.commit()        

        bk_id += 1


# ========================== CANCELLATION ============================

    elif n == 2:
        print('========Ticket Cancellation=======')

        mycursor.execute('select booking_ID from ticket')
        mydata = mycursor.fetchall()
        l = []
        for i in mydata:
            l.append(i[0])

        a = input('Enter name: ')
        b = input('Enter booking ID: ')

        while b not in l:
            print("XXX Wrong Booking ID XXX")
            b = input('Enter booking ID: ')

        c = input("Enter Flight ID: ")
        while c not in fl_list:
            print('===== Invalid Flight ID =====')
            c = input("Enter Flight ID: ")

        d = input('Enter Seat ID: ')

        mycursor.execute("SELECT * FROM ticket WHERE booking_ID = '" + b + "'")
        mydata = mycursor.fetchall()

        for i in mydata:
            if b == i[0] and a == i[1] and d == i[2]:

                mycursor.execute("DELETE FROM ticket WHERE booking_ID = '" + b + "'")
                mycon.commit()

                table_name = "seats" + c
                query = "DELETE FROM " + table_name + " WHERE seat_no = '" + d + "'"
                mycursor.execute(query)
                mycon.commit()

                print("==== Ticket Cancelled Successfully ====")
                break

            else:
                print("The Details are Incorrect, TRY AGAIN:")
                
                a = input('Enter name: ')
                b = input('Enter booking ID: ')
                c = input("Enter Flight ID: ")
                d = input('Enter Seat ID: ')
                mycursor.execute("SELECT * FROM ticket WHERE booking_ID = '" + b + "'")
                mydata = mycursor.fetchall()


# ========================== SEAT MAP ================================

    elif n == 3:
        while True:
            a = input("Enter Flight ID: ")
            if a in fl_list:
                map_top()
                seat_map(a)
                break
            else:
                print("==========⨉ Wrong Flight ID ⨉==========")


# ========================  FLIGHT SEARCH =============================

    elif n == 4:
        print('======================================')
        print('         ✈  FLIGHT SEARCH  ✈')
        print('======================================')
        
        print('''Search flights by:
   1 ▸ Origin
   2 ▸ Destination
   3 ▸ Both''')
        i = int(input('Enter choice (1-3):'))
        if i == 1:
            print('-------------------------------------')
            a = input('Enter Origin:')
            print('-------------------------------------')
            r=[]
            mycursor.execute("SELECT Origin FROM flight_list WHERE origin = '" + a + "'")
            mydata = mycursor.fetchall()
            for i in mydata:
                r.append(i[0])
                if a in r:
                    print('''-------------------------------------
  ✈  Available Flights  
-------------------------------------''')
                    
                    fl_id = []
                    origin=[]
                    dstn=[]
                    time=[]
                    
                    mycursor.execute("SELECT flight_ID  FROM flight_list WHERE origin = '" + a + "'")
                    mydata = mycursor.fetchall()
                    for i in mydata:
                        fl_id.append(i[0])
                    
                    mycursor.execute("SELECT origin  FROM flight_list WHERE origin = '" + a + "'")
                    mydata = mycursor.fetchall()
                    for i in mydata:
                        origin.append(i[0])
                    
                    mycursor.execute("SELECT destination  FROM flight_list WHERE origin = '" + a + "'")
                    mydata = mycursor.fetchall()
                    for i in mydata:
                        dstn.append(i[0])
                    
                    mycursor.execute("SELECT departure_time  FROM flight_list WHERE origin = '" + a + "'")
                    mydata = mycursor.fetchall()
                    for i in mydata:
                        time.append(i[0])
                    
                    
                    long1=''                    
                    for i in fl_id:
                        if len(i) > len(long1):
                            long1=i
                        if len("FLIGHT_ID") > len(long1):
                            long1 = "FLIGHT_ID"
                                                      
                    long2=''
                    for i in origin:
                        if len(i) > len(long2):
                            long2=i
                        if len("ORIGIN") > len(long2):
                            long2 = "ORIGIN"
                            
                    long3=''                 
                    for i in dstn:
                        if len(i) > len(long3):
                            long3=i
                        if len("DESTINATION") > len(long3):
                            long3 = "DESTINATION"
                            
                            
                    
                    print("FLIGHT_ID" + " " * 4 +
      "ORIGIN" + " " * 4 +
      "DESTINATION" + " " * 4 +
      "DEPARTURE")
                    
                    for i in range(len(fl_id)):
                        s1 = (len(long1) - len(fl_id[i])) + 4
                        s2 = (len(long2) - len(origin[i])) + 4
                        s3 = (len(long3) - len(dstn[i])) + 4
                        x = str(time[i])
                        print(fl_id[i] + " " * s1 +
                              origin[i] + " " * s2 +
                              dstn[i] + " " * s3 +
                              x)
                   
            mycursor.execute("SELECT Origin FROM flight_list WHERE origin = '" + a + "'")
            mydata = mycursor.fetchall()
            if mydata == []:
                    print('❌ No flights found for this location.')
                    

        elif i == 2:
            print('-------------------------------------')
            a = input('Enter Destination:')
            print('-------------------------------------')
            r=[]
            mycursor.execute("SELECT destination FROM flight_list WHERE destination = '" + a + "'")
            mydata = mycursor.fetchall()
            for i in mydata:
                r.append(i[0])
                if a in r:
                    print('''-------------------------------------
  ✈  Available Flights  
-------------------------------------''')
                    
                    fl_id = []
                    origin=[]
                    dstn=[]
                    time=[]
                    
                    mycursor.execute("SELECT flight_ID  FROM flight_list WHERE destination = '" + a + "'")
                    mydata = mycursor.fetchall()
                    for i in mydata:
                        fl_id.append(i[0])
                    
                    mycursor.execute("SELECT origin  FROM flight_list WHERE destination = '" + a + "'")
                    mydata = mycursor.fetchall()
                    for i in mydata:
                        origin.append(i[0])
                    
                    mycursor.execute("SELECT destination  FROM flight_list WHERE destination = '" + a + "'")
                    mydata = mycursor.fetchall()
                    for i in mydata:
                        dstn.append(i[0])
                    
                    mycursor.execute("SELECT departure_time  FROM flight_list WHERE destination = '" + a + "'")
                    mydata = mycursor.fetchall()
                    for i in mydata:
                        time.append(i[0])
                    
                    
                    long1=''                    
                    for i in fl_id:
                        if len(i) > len(long1):
                            long1=i
                        if len("FLIGHT_ID") > len(long1):
                            long1 = "FLIGHT_ID"
                                                      
                    long2=''
                    for i in origin:
                        if len(i) > len(long2):
                            long2=i
                        if len("ORIGIN") > len(long2):
                            long2 = "ORIGIN"
                            
                    long3=''                 
                    for i in dstn:
                        if len(i) > len(long3):
                            long3=i
                        if len("DESTINATION") > len(long3):
                            long3 = "DESTINATION"
                            
                            
                    
                    print("FLIGHT_ID" + " " * 4 +
      "ORIGIN" + " " * 4 +
      "DESTINATION" + " " * 4 +
      "DEPARTURE")
                    
                    for i in range(len(fl_id)):
                        s1 = (len(long1) - len(fl_id[i])) + 4
                        s2 = (len(long2) - len(origin[i])) + 4
                        s3 = (len(long3) - len(dstn[i])) + 4
                        x = str(time[i])
                        print(fl_id[i] + " " * s1 +
                              origin[i] + " " * s2 +
                              dstn[i] + " " * s3 +
                              x)
                   
            mycursor.execute("SELECT destination FROM flight_list WHERE destination = '" + a + "'")
            mydata = mycursor.fetchall()
            if mydata == []:
                    print('❌ No flights found for this location.')
            
        elif i ==3:
            print('-------------------------------------')
            a = input('Enter Origin:')
            b= input('Enter Destination:')
            print('-------------------------------------')
            
            
            r=[]
            mycursor.execute("SELECT origin FROM flight_list WHERE origin='" + a + "' AND destination='" + b + "'")
            mydata = mycursor.fetchall()
            for i in mydata:
                r.append(i[0])
            
            s=[]
            mycursor.execute("SELECT destination FROM flight_list WHERE origin='" + a + "' AND destination='" + b + "'")
            mydata = mycursor.fetchall()
            for i in mydata:
                s.append(i[0])
            
                if a in r and b in s:
            
                    print('''-------------------------------------
  ✈  Available Flights  
-------------------------------------''')
                    
                    fl_id = []
                    origin=[]
                    dstn=[]
                    time=[]
                                                                    
                    mycursor.execute("SELECT flight_ID  FROM flight_list WHERE origin = '" + a + "' AND destination = '" + b + "'")
                    mydata = mycursor.fetchall()
                    for i in mydata:
                        fl_id.append(i[0])
                    
                    mycursor.execute("SELECT origin  FROM flight_list WHERE origin = '" + a + "' AND destination = '" + b + "'")
                    mydata = mycursor.fetchall()
                    for i in mydata:
                        origin.append(i[0])
                    
                    mycursor.execute("SELECT destination  FROM flight_list WHERE origin = '" + a + "' AND destination = '" + b + "'")
                    mydata = mycursor.fetchall()
                    for i in mydata:
                        dstn.append(i[0])
                    
                    mycursor.execute("SELECT departure_time FROM flight_list WHERE origin = '" + a + "' AND destination = '" + b + "'")
                    mydata = mycursor.fetchall()
                    for i in mydata:
                        time.append(i[0])
                    
                    
                    long1=''                    
                    for i in fl_id:
                        if len(i) > len(long1):
                            long1=i
                        if len("FLIGHT_ID") > len(long1):
                            long1 = "FLIGHT_ID"
                                                      
                    long2=''
                    for i in origin:
                        if len(i) > len(long2):
                            long2=i
                        if len("ORIGIN") > len(long2):
                            long2 = "ORIGIN"
                            
                    long3=''                 
                    for i in dstn:
                        if len(i) > len(long3):
                            long3=i
                        if len("DESTINATION") > len(long3):
                            long3 = "DESTINATION"
                            
                            
                    
                    print("FLIGHT_ID" + " " * 4 +
      "ORIGIN" + " " * 4 +
      "DESTINATION" + " " * 4 +
      "DEPARTURE")
                    
                    for i in range(len(fl_id)):
                        s1 = (len(long1) - len(fl_id[i])) + 4
                        s2 = (len(long2) - len(origin[i])) + 4
                        s3 = (len(long3) - len(dstn[i])) + 4
                        x = str(time[i])
                        print(fl_id[i] + " " * s1 +
                              origin[i] + " " * s2 +
                              dstn[i] + " " * s3 +
                              x)
                   
            query = "SELECT * FROM flight_list WHERE origin='" + a + "' AND destination='" + b + "'"
            mycursor.execute(query)
            mydata = mycursor.fetchall()

            if mydata == []:
                    print('❌ No flights found for this location.')
            
# ========================= ADMIN ====================================           
    
    elif n == 5:
        ps='Hello'
        a=input('Enter Password:')
        if a==ps:
            print('✅ CORRECT PASSWORD')
            print('Opening ADMIN window')
            print('===================== ADMIN =======================')
            while True:
                print('1: ADD FLIGHT')
                print('2: REMOVE FLIGHT')
                print('3: EDIT FLIGHT')
                print('4: EXIT WINDOW')
                print('----------------------------------------------------')
                a=int(input('Enter Choice(1-4):'))
                print('----------------------------------------------------')
                if a == 1:
                    print('----------------------------------------------------')
                    print('                ADD A NEW FLIGHT')
                    print('----------------------------------------------------')
                    
                    mycursor.execute("select flight_ID from flight_list")
                    mydata = mycursor.fetchall()

                    fl_list = []
                    for i in mydata:
                        fl_list.append(i[0])
                    j = input('Enter Flight ID            : ')
                    while j in fl_list:
                        print("⨉ This Flight ID already exists! Please enter a new one.")
                        j = input("Enter Flight ID            : ")
                    
                    
                    k = input('Enter Origin               : ')
                    l = input('Enter Destination          : ')
                    while True:
                        
                        m = input('Enter Departure Time       : ')
                        if len(m) != 8:
                            print("❌ Invalid format. Use HH:MM:SS")
                            continue
                        
                        x = m[0:2]
                        y = m[3:5]
                        z = m[6:8]
                        
                        if not (x.isdigit() and y.isdigit() and z.isdigit()):
                            print("❌ Hours, minutes and seconds must be numbers")
                            continue
                    
                        xx = int(x)
                        yy = int(y)
                        zz = int(z)
                        
                        if xx < 0 or xx > 23:
                            print("❌ Hours must be between 00 and 23")
                            continue
                        
                        if yy < 0 or yy > 59:
                            print("❌ Minutes must be between 00 and 59")
                            continue
                    
                        if zz < 0 or zz > 59:
                            print("❌ Seconds must be between 00 and 59")
                            continue
                        break
                    print("✔ Time accepted :", m)
                    
                             
                    query = "insert into flight_list values ('" + j + "','" + m + "','" + k + "','" + l + "')"
                    mycursor.execute(query)
                    mycon.commit()

                    tb_name = "seats" + j
                    query = "create table " + tb_name + " (seat_no varchar(3) primary key, flight_id varchar(10))"
                    mycursor.execute(query)
                    mycon.commit()
                
                elif a == 2:
                    print('----------------------------------------------------')
                    print('                 REMOVE A FLIGHT')
                    print('----------------------------------------------------')
                    
                    mycursor.execute("select flight_ID from flight_list")
                    mydata = mycursor.fetchall()

                    fl_list = []
                    for i in mydata:
                        fl_list.append(i[0])
                    l = input("Enter Flight ID: ")
                    while l not in fl_list:
                            print("⨉ Invalid Flight ID — Flight does not exist!")
                            l = input("Enter Flight ID again: ")
                    
                    tl_name = "seats" + l
                    query = "DROP TABLE " + tl_name
                    mycursor.execute(query)
                    mycon.commit()
                    
                    query = "DELETE FROM flight_list WHERE flight_ID = '" + l + "'"
                    mycursor.execute(query)
                    mycon.commit()

                    
                elif a == 3:
                    print('----------------------------------------------------')
                    print('                 EDIT A FLIGHT')
                    print('----------------------------------------------------')
                    print('1: Edit Flight ID')
                    print('2: Edit Flight Origin')
                    print('3: Edit Flight Destination')
                    print('4: Edit Departure Time')
                    print('5: Exit')
                    o=int(input('Enter Choice (1-4):'))
                    while True:
                        if o ==1:
                            mycursor.execute("select flight_ID from flight_list")
                            mydata = mycursor.fetchall()

                            fl_list = []
                            for i in mydata:
                                fl_list.append(i[0])
                                
                            l = input("Enter Flight ID: ")
                            while l not in fl_list:
                                print("⨉ Invalid Flight ID — Flight does not exist!")
                                l = input("Enter Flight ID again: ")
                            
                            x= input('Enter New Flight ID:')
                            while x in fl_list:
                                print('⨉ Invalid Flight ID — Flight already exist!')
                                x= input('Enter New Flight ID:')
                            
                            query = "UPDATE flight_list SET flight_ID = '" + x + "' WHERE flight_ID = '" + l + "'"
                            mycursor.execute(query)
                            mycon.commit()

                            
                            old_table = "seats" + l
                            new_table = "seats" + x
                            query = "RENAME TABLE " + old_table + " TO " + new_table
                            mycursor.execute(query)
                            mycon.commit()
                            
                            query = "UPDATE " + new_table + " SET flight_ID = '" + x + "'"
                            mycursor.execute(query)
                            mycon.commit()
                            
                            
                            print('----------------------------------------------------')
                            print('                 EDIT A FLIGHT')
                            print('----------------------------------------------------')
                            print('1: Edit Flight ID')
                            print('2: Edit Flight Origin')
                            print('3: Edit Flight Destination')
                            print('4: Edit Departure Time')
                            print('5: Exit')
                            o=int(input('Enter Choice (1-5):'))
                            
                        elif o ==2:
                            a= input('Enter Flight ID:')
                            
                            query = "SELECT origin FROM flight_list WHERE flight_ID = '" + a + "'"
                            mycursor.execute(query)
                            mydata = mycursor.fetchall()
                            
                            for i in mydata:
                                print('Current Origin:',i[0])
                            
                                
                            b=input('Enter (new) Origin:')
                            
                            query = "UPDATE flight_list SET origin = '" + b + "' WHERE flight_ID = '" + a + "'"
                            mycursor.execute(query)
                            mycon.commit()
                            
                            print('----------------------------------------------------')
                            print('                 EDIT A FLIGHT')
                            print('----------------------------------------------------')
                            print('1: Edit Flight ID')
                            print('2: Edit Flight Origin')
                            print('3: Edit Flight Destination')
                            print('4: Edit Departure Time')
                            print('5: Exit')
                            o=int(input('Enter Choice (1-5):'))
                            
                            
                            
                        elif o == 3:
                            a= input('Enter Flight ID:')
                            query = "SELECT destination FROM flight_list WHERE flight_ID = '" + a + "'"
                            mycursor.execute(query)
                            mydata = mycursor.fetchall()
                            
                            for i in mydata:
                                print('Current Destoination:',i[0])
                            
                            b = input('Enter (new) Destination:')
                            query = "UPDATE flight_list SET destination = '" + b + "' WHERE flight_ID = '" + a + "'"
                            mycursor.execute(query)
                            mycon.commit()

                            print('----------------------------------------------------')
                            print('                 EDIT A FLIGHT')
                            print('----------------------------------------------------')
                            print('1: Edit Flight ID')
                            print('2: Edit Flight Origin')
                            print('3: Edit Flight Destination')
                            print('4: Edit Departure Time')
                            print('5: Exit')
                            o=int(input('Enter Choice (1-5):'))
                            
                            
                            
                        elif o ==4:
                            
                            a= input('Enter Flight ID:')
                            
                            while True:
                                
                                m = input('Enter Departure Time       : ')
                                if len(m) != 8:
                                    print("❌ Invalid format. Use HH:MM:SS")
                                    continue
                                
                                x = m[0:2]
                                y = m[3:5]
                                z = m[6:8]
                                
                                if not (x.isdigit() and y.isdigit() and z.isdigit()):
                                    print("❌ Hours, minutes and seconds must be numbers")
                                    continue
                            
                                xx = int(x)
                                yy = int(y)
                                zz = int(z)
                                
                                if xx < 0 or xx > 23:
                                    print("❌ Hours must be between 00 and 23")
                                    continue
                                
                                if yy < 0 or yy > 59:
                                    print("❌ Minutes must be between 00 and 59")
                                    continue
                            
                                if zz < 0 or zz > 59:
                                    print("❌ Seconds must be between 00 and 59")
                                    continue
                                break
                            print("✔ Time accepted :", m)
                            
                            query = "UPDATE flight_list SET departure_time = '" + m + "' WHERE flight_ID = '" + a + "'"
                            mycursor.execute(query)
                            mycon.commit()
                            
                            print('----------------------------------------------------')
                            print('                 EDIT A FLIGHT')
                            print('----------------------------------------------------')
                            print('1: Edit Flight ID')
                            print('2: Edit Flight Origin')
                            print('3: Edit Flight Destination')
                            print('4: Edit Departure Time')
                            print('5: Exit')
                            o=int(input('Enter Choice (1-5):'))
                            
                        elif o == 5:
                            break
                        
                elif a == 4:
                    break
                    
        else:
            print('❌ INCORRECT PASSWORD')


# ========================== EXIT ====================================

    elif n == 6:
        break

mycon.close()