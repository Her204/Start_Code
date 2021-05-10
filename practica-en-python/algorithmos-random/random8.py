import sqlite3
conn = sqlite3.connect('alfabeth.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Characters')

cur.execute('''
CREATE TABLE Characters (letter TEXT, Count INTEGER)''')
def num_to_characters(x,y):
    letras = list()
    eg = 0 
    for a in range(1,y):
        eg += 1
        if len(x) >= a: 
            fun = x[a-1].upper()
            letras.append(fun)
            cur.execute('SELECT Letter FROM Characters WHERE Count = ? ', (fun,))
            cur.execute('SELECT Count FROM Characters WHERE Letter = ? ', (eg,))
            row = cur.fetchone()
            cur.execute('''INSERT INTO Characters (letter, Count)
                         VALUES (?, ?)''', (fun,eg,))
            conn.commit()
        if a > len(x):
            i = len(x) 
            for b in letras:
                if len(letras) <= y:
                     for c in x:
                         dd = b.upper() + c.upper()
                         letras.append(dd)
                         i += 1 
                         if i > y: break
                         cur.execute('SELECT Letter FROM Characters WHERE Count = ? ', (dd,))
                         cur.execute('SELECT Count FROM Characters WHERE Letter = ? ', (i,))
                         row = cur.fetchone()
                         cur.execute('''INSERT INTO Characters (letter, Count)
                                     VALUES (?, ?)''', (dd,i,))
                         conn.commit()
    
    sqlstr = 'SELECT letter, Count FROM Characters ORDER BY Letter DESC LIMIT 10'
    for row in cur.execute(sqlstr):
         print(str(row[0]), row[1])
    cur.close()
    return letras[-50:-1]
while True:
    f = input("Enter some of text: ") 
    talk = input("enter a number-")
    if len(talk) <= 1 or int(talk) > 17000: 
        break
    if not talk == "":
    
        talk = int(talk)
    print("\n", num_to_characters(f,talk), "\n")
