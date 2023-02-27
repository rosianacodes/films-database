from connect import *
import readFilms
import time

def delete():
    # which field can be used to delete record(s) in the films table?
    "Use the filmID(unique/primary key)"
    idField = input("Enter the filmID of the record to be deleted: ")

    cursor.execute(f"DELETE FROM tblFilms WHERE filmID = {idField}")
    # cursor.execute("DELETE FROM tblFilms WHERE filmID = >=1")
    # cursor.execute("DROP TABLE tblFilms")
    conn.commit()

    print(f"Record {idField} deleted from the tblFilms table")
    time.sleep(3)

    #read from the tblFilms table
    readFilms.read() #call the read subroutine from the readFilms python file

if __name__ == "__main__":
    delete() # call/invoke the delete subroutine


