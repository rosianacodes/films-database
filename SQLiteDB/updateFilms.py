from connect import *
import readFilms
import time

def update():
    # which field can be used to update record(s) in the tblFilms table?
    "Use the filmID(unique/primary key)"
    idField = input("Enter the filmID of the record to be updated: ")
    # field name to be updated
    fieldName = input("Enter field name (title/yearReleased/rating/duration/genre): ").title()
    # fieldName1 = input("Enter value for title: ").title()
    # fieldName2 = input("Enter value for yearReleased): ").title()
    # fieldName3 = input("Enter value for rating): ").title()
    # fieldName4 = input("Enter value for duration: ").title()
    # fieldName5 = input("Enter value for genre): ").title()
    # fieldName1 =  "'" + fieldName1+ "'"
    # fieldName2 =  "'" + fieldName1+ "'"
    # fieldName3 =  "'" + fieldName3+ "'"
    # fieldName4 =  "'" + fieldName4+ "'"
    # fieldName5 =  "'" + fieldName5+ "'"
    newFieldValue = input("Enter the value for the {fieldName} field: ")
    # print(newFieldValue)
    # add single quotes to newFieldValue to match data as it is by the python interpretor
    newFieldValue = "'" + newFieldValue+ "'"
    # print(newFieldValue)

    # UPDATE tblFilms SET title/yearReleased/rating/duration/genre = title = Legally Blonde/yearReleased = 2001/rating = PG/duration = 96/genre = Comedy WHERE SongID = 1/2/3...
    cursor.execute(f"UPDATE tblFilms SET {fieldName} = {newFieldValue} WHERE filmID = {idField}")
    # cursor.execute(f"UPDATE songs SET {fieldName1} = {newFieldValue1}, {fieldName2} = {newFieldValue2},
    # {fieldName3} = {newFieldValue3}, {fieldName4} = {newFieldValue4}, {fieldName5} = {newFieldValue5},  WHERE SongID = {idField}")
    conn.commit()

    print(f"Record {idField} inserted in the tblFilms table")
    time.sleep(3)

    # read from the films table
    readFilms.read() #call the read subroutine from the readFilms python file

if __name__ == "__main__":
    update() # call/invoke the update subroutine