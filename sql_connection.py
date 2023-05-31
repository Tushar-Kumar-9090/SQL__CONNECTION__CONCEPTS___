
def create_connection():
    import sqlite3
    co=sqlite3.connect('tushar.db')
    return co
co=create_connection()



def create_table(co):
    cursorobj=co.cursor()
    cursorobj.execute('create table Employee (id integer primary key, name text)')
    co.commit()
    print("table Created")
#% create_table(co)




def insert_table(co):
    cursorobj=co.cursor()
    cursorobj.execute('insert into Employee (id,name) values(6,"Naru")')
    co.commit()
    print("Insert Successful")
#%insert_table(co)




def retrieve_table(co):
    cursorobj=co.cursor()
    queryset=cursorobj.execute('select * from Employee')
    for i in queryset:
        print(i)
#%retrieve_table(co)




def update_table(co):
    cursorobj=co.cursor()
    cursorobj.execute('update Employee set name="Narshimha" where id=6')
    co.commit()
#%update_table(co)
#%retrieve_table(co)




def delete_table(co):
    cursorobj=co.cursor()
    cursorobj.execute('delete from Employee where id=6')
    co.commit()
delete_table(co)
retrieve_table(co)
