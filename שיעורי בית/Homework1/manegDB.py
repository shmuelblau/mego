import sqlite3



def start():


    db=sqlite3.connect('my_db.db')

    cursor=db.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        phone TEXT NOT NULL,
        id_number TEXT NOT NULL UNIQUE,
        amount REAL NOT NULL
    )
    ''')
    db.commit()
    cursor.close()
    db.close()

    with open("db.csv", "r") as fd:
        lines = fd.read().splitlines()
        for line in lines:
            upsert_person('my_db.db', line)

            
    


    

    return 'my_db.db'



def upsert_person(db, info):
    
    first_name, last_name, id_number,phone, amount ,date = info.split(',')

    
    db=sqlite3.connect(db)
    cursor = db.cursor()

    
    cursor.execute("SELECT id FROM people WHERE id_number = ?", (id_number,))
    result = cursor.fetchone()
    a=''

    if result:  
        cursor.execute("UPDATE people SET amount = amount + ? WHERE id_number = ?",
               (float(amount), id_number))
        a= f"Updated amount for {first_name} {last_name} (ID: {id_number})."
    else:  
        cursor.execute("INSERT INTO people (first_name, last_name, phone, id_number, amount) VALUES (?, ?, ?, ?, ?)",
                       (first_name, last_name, phone, id_number, float(amount)))
        a= f"Inserted new person: {first_name} {last_name} (ID: {id_number})."

    
    db.commit()
    cursor.close()
    
    cursor.close()

    return a
    


def get_amount_by_id(db, id_number):
    
    db=sqlite3.connect(db)
    cursor = db.cursor()
    a=''

    if id_number !="":
        
        cursor.execute("SELECT first_name, last_name, amount FROM people WHERE id_number = ?", (id_number,))
        result = cursor.fetchone()
        

        if result:
            a= f"Name: {result[0]} {result[1]}, Amount: {result[2]}"
        else:
            a= f"No person found with the ID number {id_number}."
    else:
        
        cursor.execute("SELECT first_name, last_name, amount FROM people")
        results = cursor.fetchall()

        if results:
            
            print("All people and their amounts:")
            for row in results:
                a+= f"Name: {row[0]} {row[1]}, Amount: {row[2]}\n"

            
        else:
            a= "No data found in the database."

    
    cursor.close()
    db.close()
    return a

    
    

# דוגמת קריאה לפונקציה (מציג את הסכום של ת"ז מסוים)


# דוגמת קריאה לפונקציה ללא פרמטר (מציג את הסכומים של כולם)
#print(get_amount_by_id(start()))

# דוגמת קריאה לפונקציה
#person_info = "1,1,0528075188,2,20,30/08/24"
#print(upsert_person(start(), person_info))

#print(get_amount_by_id(start()))






