from connect import *

#subroutine 
def read():
    cursor.execute("SELECT * FROM tblFilms")
    # cursor.execute("SELECT * FROM films WHERE filmID = 1")
    # fetchall() method which fetches all rows selected from the select statement
    row = cursor.fetchall() # records fetched saved/passed in to the row variable
    for record in row:
        print(record)



if __name__ == "__main__":
    read()