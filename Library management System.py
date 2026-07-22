"""
Library Management System

Features:
- Add Book
- Search Book
- Show Books
- Edit Book
- Delete Book

Language: Python
Database: SQLite3
"""

import sqlite3
 
conn=sqlite3.connect("C:\\Users\\Center\\Desktop\\library.db")
cur=conn.cursor()


while True:
   try:
     choice=int(input("\nenter your operation:\n1.Add\n2.Show\n3.Search\n4.Edit\n5.Delete\n6.Exit\nSelect:"))
     if choice==1:
      try:
        h=int(input("enter the id:"))
        b=input("enter the name:")
        c=input("enter the autor:")
        cur.execute(f"INSERT INTO books(id,name,author) VALUES (?,?,?)",(h,b,c))
        conn.commit()
      except:
         print("\nenter a number.\n")
     elif choice==3:
      try:
        new_id=int(input("enter the id:"))
        cur.execute(
         f"SELECT * FROM books WHERE id=={new_id};"
        )
        rows=cur.fetchall()
        if not rows:
             print("\nno book in here\n")
        else:
             for row in rows:
                print(row)
      except:
         print("\ninvalid id.\n")
     elif choice==2:
        cur.execute(
            "SELECT * FROM books"
        )
        rows=cur.fetchall()
        if not rows:
             print("\nno book in here\n")
        else:
             for row in rows:
                print(row)
     elif choice==4:
           while True:
            try:
               id=int(input("which book do you want to edit?(id):"))
               choice2=int(input("what do you want to change?:\n1.id\n2.name\n3.author\n4.Exit\nselect:"))
               if choice2==1:
                  try:
                     c=int(input("enter the new id:"))
                     cur.execute(
                           "UPDATE books WHERE id=?",(c,))
                     conn.commit()
                  except:
                     print("\ninvalid id.\n")
               elif choice2==2:
                  c=input("enter the new name:")
                  cur.execute(
                        "UPDATE books SET name=? WHERE id=?",(c,a))
                  conn.commit()
               elif choice2==3:
                  c=input("enter the new author:")
                  cur.execute(
                        "UPDATE books SET author=? WHERE id=?",(c,a))
                  conn.commit()
               elif choice2==4:
                  conn.commit()
                  break
            except:
                print("\ninvalid id or number.\n")
     elif choice==5:
      try:
         b=int(input("enter the id:"))
         cur.execute(
            "DELETE FROM books WHERE id=?",(b,)
         )
         conn.commit()
      except:
          print("\ninvalid id.\n")
     elif choice==6:
          conn.close()
          break
   except:
      print("\nenter a number between 1 to 6.\n")
