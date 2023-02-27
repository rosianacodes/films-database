from connect import *
import readFilms
import time

# filmID(integer), title(text), yearReleased(integer),rating(text),duration(integer),genre(text)

# subroutine 
def inserttblFilms():
    # create an empty list
    films = []
    # ask for user input for the tblFilms table (title, yearReleased, rating, duration, genre)
    title = input("Enter the film title: ")
    yearReleased = input("Enter the year the film was released: ")
    rating = input("Enter the film rating: ")
    duration = input("Enter the film duration: ") 
    genre = input("Enter the film genre: ")

    # append data to the list called
    films.append(title)
    films.append(yearReleased)
    films.append(rating)
    films.append(duration)
    films.append(genre)

    # Insert data from the films list into the tblFilms table
    # Use NULL(placeholder) to indicate that no data will be provided for filmID
    # INSERT INTO tblFilms VALUES(NULL, "a", "b","c","d","e") the NULL place holder required
    # INSERT INTO tblFilms(title, yearReleased, rating, duration, genre)  VALUES ("a", "b","c","d","e") the NULL place holder not required
    
    cursor.execute("INSERT INTO tblFilms values(NULL, ?,?,?,?,?)", films)
    #commit any pending transaction to the tblFilms table in the database
    conn.commit()

    print(f"Title {title} inserted in the tblFilms table")
    time.sleep(3)

    # read from the tblFilms table
    readFilms.read() #call the read subroutine from the readFilms python file

if __name__ == "__main__":
    inserttblFilms() #call/invoke the subroutine

    




