import sqlite3
import time
import random
conn=sqlite3.connect("records.db")
cursor=conn.cursor()
back_to=None
tyu=None
cursor.execute("""CREATE TABLE IF NOT EXISTS books(book_id TEXT PRIMARY KEY,book_name TEXT,book_author TEXT,published_date TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS workers(worker_id TEXT PRIMARY KEY,worker_name TEXT,phone_number TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS users(uers_id TEXT PRIMARY KEY,user_name TEXT,user_num TEXT,book_name TEXT,date_brow TEXT,return_date TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS administrator(admin_name TEXT,admin_pass TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS student_acess(student_reg TEXT PRIMARY KEY,student_name TEXT,book_name TEXT,year_of_study TEXT)""")

def add_books():
    book_id=input("enter the book id: ")
    book_name=input("enter the book name: ")
    book_author=input("enter the book author: ")
    published_date=input("enter the date the book was published: ")
    cursor.execute("INSERT INTO books(book_id,book_name,book_author,published_date)VALUES(?,?,?,?)",(book_id,book_name,book_author,published_date))
    conn.commit()
    print("book sucesfully added")
def add_workers():
    worker_id=input("enter worker id: ")
    worker_name=input("enter worker name: ")
    phone_number=input("enter worker phone number: ")
    cursor.execute("INSERT INTO workers(worker_id,worker_name,phone_number)VALUES(?,?,?)",(worker_id,worker_name,phone_number))  
    conn.commit()
    print("worker added sucesfully")
def users_us():
    user_id=input("enter user ID: ")
    user_name=input("enter user name: ")
    user_num=input("enter user phone number: ")
    while True:
        book_name=input("enter the book borrowed by the user: ")
        cursor.execute("SELECT *FROM books WHERE book_name=?",(book_name,))
        record=cursor.fetchone()
        if record:
            print("book is available")
            break
        else:
            print("book is not in our library")
    date_brow=input("enter the date the book was borrowed: ")
    return_date=input("enter the date to return: ")
    cursor.execute("INSERT INTO users(user_id,user_name,user_num,book_name,date_brow,return_date)VALUES(?,?,?,?,?,?)",(user_id,user_name,user_num,book_name,date_brow,return_date))
    conn.commit()
    print("record updated sucessfully")
def student_borrow():
    student_reg=input("enter your regestration number: ")
    student_name=input("enter your name: ")
    while True:
        book_name=input("enter the name of the book you want: ")
        cursor.execute("SELECT *FROM books WHERE book_name=?",(book_name,))
        if cursor.fetchone():
            print("book is available")
            break
        else:
            print("book is not in our library")
    year_of_study=input("enter your year of study: ")
    cursor.execute("INSERT INTO student_acess(student_reg,student_name,book_name,year_of_study)VALUES(?,?,?,?)",(student_reg,student_name,book_name,year_of_study))
    conn.commit()
    print("you have sucessfully borrowed the book")
def digit_code():
    return random.randint(100000,999999)
def del_worker():
    worker_name=input("enter worker name to be deleted: ")
    confirm_ask=int(input("are you sure you want to delete the worker press 1 to confirm or press 2 to stop: "))
    if confirm_ask==1:
        cursor.execute("DELETE FROM workers WHERE worker_name=?",(worker_name,))
        conn.commit()
        print("worker deleted succesfully")
    else:
        print("you stoped the deletion")
def del_book():
    book_name=input("enter the book name or title: ")
    confirm_ask=int(input("are you sure you want to delete the book press 1 to confirm or press 2 to stop: "))
    if confirm_ask==1:
        cursor.execute("DELETE FROM books WHERE book_name=? ",(book_name,))
        conn.commit()
        print("book deleted")
    else:
        print("you stoped the deletion")
def admi_insert():
    admin_name=input("enter admin name: ")
    admin_pass=input("enter admin pass: ")
    cursor.execute("INSERT INTO administrator(admin_name,admin_pass)VALUES(?,?)",(admin_name,admin_pass))
    conn.commit()
    print("admin added sucessfully")
def change_pass():
    admin_pass=input("enter your current admin pass: ")
    new_pass=input("enter your new password: ")
    cursor.execute("UPDATE administrator SET admin_pass=? WHERE admin_pass=?",(new_pass,admin_pass))
    conn.commit()
    print("password changed successfully")
print("welcome to the library database system ")
print("")
print("enter the options bellow")
print("1. press 1 if you are a student ")
print("2. press 2 if you are a member ")
ask_user=int(input("enter your option below: "))
while True:
    if ask_user==1:
        print("welcome student")
        print("")
        print("select the following options")
        while True:
            print("1. to borrow a book press 1")
            print("2. see books in library press 2")
            print("3. press 3 to exit")
            print("")
            ask_student=int(input("enter your option below: "))
            if ask_student==1:
                print("you have to enter your details bellow")
                ask_s_n=int(input("enter number of books you want to borrow: "))
                for _ in range (ask_s_n):
                    student_borrow()
                print("")
                print("wait for your code to generate")
                time.sleep(2)
                print(digit_code())
            elif ask_student==2:
                print("welcom")
                p_a_k_t=input("press any key to continue: ")
                cursor.execute("SELECT *FROM books")
                rows=cursor.fetchall()
                for row in rows:
                    print(rows)
                p_a_k=input("pressany key to continue")
            elif ask_student==3:
                print("exiting............................")
                time.sleep(2)
                exit()
            else:
                print("invalid option")
                print("trying againg................")
                time.sleep(2)
                continue
    elif ask_user==2:
        entry=input("press any key to continue: ")
        print("")
        if entry=="09876":
            admi_insert()
            exit()
        else:
            while True:
                print("choose one of the following options: ")
                print("1. To operate the library database press 1")
                print("2. To view books in the library press 2 ")
                print("3. To view workes of the library press 3")
                print("4. To exit press 4 ")
                print("")
                try:
                    option=int(input("enter your option: "))
                    if option== 1:
                        rec_ask=input("are you a registered worker press R to continue if not press e: ")
                        if rec_ask=='r':
                            num_try=0
                            worker_name=input("enter your name: ")
                            worker_id=input("enter your worker_ID: ")
                            cursor.execute("SELECT *FROM workers WHERE worker_name=? AND worker_id=?",(worker_name,worker_id))
                            while True:
                                if cursor.fetchone():
                                    print("loging sucessfully")
                                    break
                                else:
                                    print("invalid loging details")
                                    worker_name=input("enter your name: ")
                                    worker_id=input("enter your worker_ID: ")
                                    num_try=num_try+1
                                if num_try>4:
                                    print("you cannot loging the database")
                                    print("contact the manager for help 0708707776")
                                    print("exiting............................")
                                    time.sleep(3)
                                    exit()
                            print("")
                            print("choose the following options")
                            print("1. to operate the library users and records press 1")
                            print("2. press 2 to exit")
                            library_ask=int(input("enter your option: "))
                            if library_ask==1:
                                print("")
                                while True:
                                    print("1. press R to add users of the library")
                                    print("2. press C to view records")
                                    print("3. press E to exit")
                                    libra_ask=input("enter your option: ")
                                    if libra_ask=='r':
                                        number_of_user=int(input("enter the number of users you want to add: "))
                                        for _ in range(number_of_user):
                                            users_us()
                                        continue
                                    elif libra_ask=='c':
                                        cursor.execute("SELECT *FROM users")
                                        rows=cursor.fetchall()
                                        for row in rows:
                                            print(row)
                                        continue
                                    elif libra_ask=='e':
                                        print("exiting database................")
                                        time.sleep(2)
                                        exit()
                                    else:
                                        print("invalid option")
                                        continue
                            else:
                                continue
                        else:
                            time.sleep(0.2)
                            continue
                    elif option==2:
                        print("")
                        print("enter the following options")
                        while True:
                            print("1. view books in library press 1")
                            print("2. to modifiy the books records press 2")
                            print("3. to exit press 3")
                            ask_book=int(input("enter your option : "))
                            if ask_book==1:
                                print("enter your details belows if you  are a worker")
                                worker_name=input("enter your worker name: ")
                                worker_id=input("enter your worker id: ")
                                cursor.execute("SELECT *FROM workers WHERE worker_name=? AND worker_id=?",(worker_name,worker_id))
                                while True:
                                    if cursor.fetchone():
                                        print("loging sucessfully")
                                        break
                                    else:
                                        print("invalid loging details")
                                        print("tying again...........................")
                                        time.sleep(2)
                                        worker_name=input("enter your worker name: ")
                                        worker_id=input("enter your worker id: ")
                                book_records=input("press any key to continue: ")
                                cursor.execute("SELECT *FROM books")
                                rows=cursor.fetchall()
                                for row in rows:
                                    print(row)
                                continue
                            elif ask_book==2:
                                print("")
                                print("enter the following options")
                                while True:
                                    print("1. to add books in the library press 1")
                                    print("2. to delete books from the library press 2")
                                    print("3. to see records press 3")
                                    print("4. to exit press 4")
                                    print("")
                                    book_admi=int(input("enter your option below: "))
                                    if book_admi==1:
                                        print("enter your worker details below")
                                        worker_name=input("enter the worker name: ")
                                        worker_id=input("enter the worker id: ")
                                        cursor.execute("SELECT *FROM workers WHERE worker_name=? AND worker_id=? ",(worker_name,worker_id))
                                        try_books=0
                                        while True:
                                            if cursor.fetchone():
                                                print("enter sucessful")
                                                break
                                            else:
                                                print("loging details are wrong")
                                                try_books+=1
                                                print(f"number of tries left {4-try_books}")
                                                worker_name=input("enter the worker name: ")
                                                worker_id=input("enter the worker id: ")
                                                print("trying again")
                                                time.sleep(2)
                                                if try_books==4:
                                                    print("an error occured")
                                                    back_to=input("press 1 to exit: ")
                                                    break
                                        if back_to=="1":
                                            break
                                        print("to modify any books records you require admin previlages")
                                        admin_name=input("enter the adminstrator user name: ")
                                        admin_pass=input("enter the adminstrator password: ")
                                        ad_try=0
                                        cursor.execute("SELECT *FROM administrator WHERE admin_name=? AND admin_pass=?",(admin_name,admin_pass))
                                        while True:
                                            if cursor.fetchone():
                                                print("acess granted...............")
                                                break
                                            else:
                                                print("acess denied........")
                                                print("try again")
                                                ad_try=ad_try+1
                                                print(f"number of tries left {4-ad_try}")
                                                adm_name=input("enter the adminstrator user name: ")
                                                adm_pass=input("enter the adminstrator password: ")
                                                if ad_try==3:
                                                    tyu=input("press 1 to exit: ")
                                                    break
                                        if tyu=="1":
                                            break
                                        ask_adbook=input("press any to continue: ")
                                        how_books=int(input("enter number of books you want to enter: "))
                                        for _ in range (how_books):
                                            add_books()
                                        break
                                    elif book_admi==2:
                                        print("enter your worker details below")
                                        worker_name=input("enter the worker name: ")
                                        worker_id=input("enter the worker id: ")
                                        cursor.execute("SELECT *FROM workers WHERE worker_name=? AND worker_id=? ",(worker_name,worker_id))
                                        while True:
                                            if cursor.fetchone():
                                                print("enter sucessful")
                                                break
                                            else:
                                                print("loging details are wrong")
                                                try_books=try_books+1
                                                print(f"number of tries left {4-try_books}")
                                                worker_name=input("enter the worker name: ")
                                                worker_id=input("enter the worker id: ")
                                                print("trying again")
                                                time.sleep(2)
                                                if try_books==4:
                                                    print("an error occured")
                                                    back_to=input("press 1 to exit: ")
                                                    break
                                        if back_to=="1":
                                            break
                                        print("to modify any books records you require admin previlages")
                                        admin_name=input("enter the adminstrator user name: ")
                                        admin_pass=input("enter the adminstrator password: ")
                                        ad_try=0
                                        cursor.execute("SELECT *FROM administrator WHERE admin_name=? AND admin_pass=?",(admin_name,admin_pass))
                                        while True:
                                            if cursor.fetchone():
                                                print("acess granted...............")
                                                break
                                            else:
                                                print("acess denied........")
                                                print("try again")
                                                ad_try=ad_try+1
                                                print(f"number of tries left {3 - ad_try}")
                                                adm_name=input("enter the adminstrator user name: ")
                                                adm_pass=input("enter the adminstrator password: ")
                                                if ad_try==3:
                                                    tyu=input("press 1 to exit: ")
                                                    break
                                        if tyu=="1":
                                            break
                                        ask_adbook=input("press any to continue: ")
                                        del_book()
                                        break
                                    elif book_admi==3:
                                        print("enter your worker details below")
                                        worker_name=input("enter the worker name: ")
                                        worker_id=input("enter the worker id: ")
                                        cursor.execute("SELECT *FROM workers WHERE worker_name=? AND worker_id=? ",(worker_name,worker_id))
                                        while True:
                                            if cursor.fetchone():
                                                print("enter sucessful")
                                                break
                                            else:
                                                print("loging details are wrong")
                                                worker_name=input("enter the worker name: ")
                                                worker_id=input("enter the worker id: ")
                                                print("trying again")
                                                time.sleep(2)
                                                try_books=try_books+1
                                            if try_books>=4:
                                                print("an error occured")
                                                back_to=input("press 1 to exit: ")
                                                break
                                            if back_to=="1":
                                                break
                                            see_books=input("press any key to continue: ")
                                            cursor.execute("SELECT *FROM books")
                                            rows=cursor.fetchall()
                                            for row in rows:
                                                print(row)
                                            break   
                                    elif book_admi==4:
                                        print("exiting.................")
                                        time.sleep(2)
                                        break
                            elif ask_book==3:
                                print("exiting form the books database.......................")
                                time.sleep(2)
                                break
                            else:
                                print("invalid option")
                                print("trying again...............")
                                time.sleep(2)
                                continue
                    elif option==3:
                        print("")
                        reg_worker=input("are you a registered worker press R to register now or press C to continue: ")
                        if reg_worker=='r':
                            ask_worker=input("are you an adminstrator enter your details below press A or else press E to return to main menu ")
                            if ask_worker=='a':
                                num_try=0
                                while True:
                                    admin_name=input("enter the administrator user name: ")
                                    admin_pass=input("enter the administator password: ")
                                    cursor.execute("SELECT *FROM administrator WHERE admin_name=? AND admin_pass=?",(admin_name,admin_pass))
                                    if cursor.fetchone():
                                        print("acess granted *****")
                                        break
                                    else:
                                        print("acess denied........")
                                        num_try=num_try+1
                                    if num_try >3:
                                        print("contact the IT for help 0708707776")
                                        print("closing database............")
                                        break
                                while True:
                                    print("")
                                    print("enter the following options")
                                    print("1. press A to add workers")
                                    print("2. press R to see records")
                                    print("3. press D to delete workers")
                                    print("4. press P to change password")
                                    print("5. press E to exit")
                                    print("")
                                    ask_admin=input("enter your option : ")
                                    if ask_admin=='a':
                                        employe_workers=int(input("enter number of workers you want to enter: "))
                                        for _ in range(employe_workers):
                                            add_workers()
                                        worker_rec=input("press R to view records or press E to return to main menu: ")
                                        if worker_rec=='r':
                                            cursor.execute("SELECT *FROM workers")
                                            rows=cursor.fetchall()
                                            for row in rows:
                                                print(row)
                                            time.sleep(4)
                                        else:
                                            print("returning to main menu............")
                                            print("")
                                            time.sleep(2)
                                            continue
                                    elif ask_admin=='d':
                                        while True:
                                            admi_del=input("press R to delete or press E to return to main: ")
                                            if admi_del=='r':
                                                del_worker()
                                            else:
                                                print("returining to main menu..........")
                                                time.sleep(2)
                                                break
                                    elif ask_admin=='r':
                                        cursor.execute("SELECT *FROM workers")
                                        rows=cursor.fetchall()
                                        for row in rows:
                                            print(row)
                                        time.sleep(3)
                                        continue
                                    elif ask_admin=='e':
                                        print("exiting....................")
                                        time.sleep(2)
                                        break
                                    elif ask_admin=='p':
                                        print("are you sure you want to change your password")
                                        print("press 1 to continue")
                                        print("press 2 to exit")
                                        admin_pree=int(input("enter your option:"))
                                        if admin_pree==1:
                                            admin_num_try=0
                                            tries=4
                                            admin_pass=input("enter your current password: ")
                                            cursor.execute("SELECT *FROM administrator WHERE admin_pass=?",(admin_pass,))
                                            while True:
                                                if cursor.fetchone():
                                                    print("correct password ")
                                                    time.sleep(1)
                                                    change_pass()
                                                    break
                                                else:
                                                    print("wrong password ")
                                                    print("try again")
                                                    admin_num_try+=1
                                                    tries-=1
                                                    print(f"number of tries left {4 - admin_num_try}")
                                                    admin_pass=input("enter your current password: ")
                                                    if admin_num_try==4:
                                                        print("out of tries")
                                                        time.sleep(2)
                                                        break
                                                    else:
                                                        continue
                                        else:
                                            print("exiting................")
                                            time.sleep(1)
                                    else:
                                        print("invalid option")
                                        continue
                            else:
                                print("returning back to main menu............")
                                print("")
                                time.sleep(3)
                                continue
                        else:
                            continue

                    else:
                        exit()

                except ValueError:
                    print("invalid option.....")
    else:
        print("invalid option")
        continue
conn.close()
