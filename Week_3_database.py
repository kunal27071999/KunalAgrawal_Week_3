
from getpass import getpass
from mysql.connector import connect,Error

#create connection with database
try:
    with connect(host = "localhost",
        user = "root",
        password = "kunal123",
        database = "online_movie_rating"
        ) as connection:
        print(connection)

        # create_db_query = "CREATE DATABASE online_movie_rating"
        # with connection.cursor() as cursor:
        #     cursor.execute(create_db_query)

        create_movie_table_query = """
        CREATE TABLE MOVIES(id INT AUTO_INCREMENT PRIMARY KEY,
                            title VARCHAR(100),
                            release_year YEAR(4),
                            genre VARCHAR(100),
                            collection_in_mil INT
                            )
        """
        create_reviewers_table_query = """
        CREATE TABLE reviewers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100)
            )
        """

        create_ratings_table_query = """
            CREATE TABLE ratings (
                movie_id INT,
                reviewer_id INT,
                rating DECIMAL(2,1),
                FOREIGN KEY(movie_id) REFERENCES movies(id),
                FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
                PRIMARY KEY(movie_id, reviewer_id)
            )
        """
        show_table_query = "DESCRIBE movies"

        insert_movies_query = """
        INSERT INTO movies (title, release_year, genre, collection_in_mil)
        VALUES
            ("Forrest Gump", 1994, "Drama", 330.2),
            ("3 Idiots", 2009, "Drama", 2.4),
            ("Eternal Sunshine of the Spotless Mind", 2004, "Drama", 34.5),
            ("Good Will Hunting", 1997, "Drama", 138.1),
            ("Skyfall", 2012, "Action", 304.6),
            ("Gladiator", 2000, "Action", 188.7),
            ("Black", 2005, "Drama", 3.0),
            ("Titanic", 1997, "Romance", 659.2),
            ("The Shawshank Redemption", 1994, "Drama",28.4)
        """

        insert_reviewers_query = """
        INSERT INTO reviewers
            (first_name, last_name)
            VALUES ( %s, %s )
        """
        reviewers_records = [
            ("Chaitanya", "Baweja"),
            ("Mary", "Cooper"),
            ("John", "Wayne"),
            ("Thomas", "Stoneman"),
            ("Penny", "Hofstadter"),
            ("Mitchell", "Marsh"),
            ("Wyatt", "Skaggs"),
            ("Andre", "Veiga"),
            ("Sheldon", "Cooper"),
            ("Kimbra", "Masters"),
            ("Kat", "Dennings"),
            ("Bruce", "Wayne"),
            ("Domingo", "Cortes"),
            ("Rajesh", "Koothrappali"),]

        insert_ratings_query = """
            INSERT INTO ratings
            ( movie_id, reviewer_id,rating)
            VALUES ( %s, %s, %s)
        """
        ratings_records = [
        (1, 1, 5),(2, 2, 5.2),(3, 3, 9),(4, 4, 8),(5, 5, 7),(6, 6, 6)]

        select_movies_query = "SELECT * FROM movies LIMIT 5"

        movie_id = input("Enter movie id: ")
        reviewer_id = input("Enter reviewer id: ")
        new_rating = input("Enter new rating: ")
        update_query = """
        UPDATE
            ratings
        SET
            rating = %s
        WHERE
            movie_id = %s AND reviewer_id = %s;

        SELECT *
        FROM ratings
        WHERE
            movie_id = %s AND reviewer_id = %s
        """
        val_tuple = (
        new_rating,
        movie_id,
        reviewer_id,
        movie_id,
        reviewer_id,
        )

        with connection.cursor() as cursor:
            #cursor.execute(create_movie_table_query)
            #cursor.execute(create_reviewers_table_query)
            #cursor.execute(create_ratings_table_query)
            #cursor.execute(insert_movies_query)
            #cursor.executemany(insert_reviewers_query,reviewers_records)
            #cursor.executemany(insert_ratings_query, ratings_records)
            #connection.commit()
            # cursor.execute(show_table_query)
            # result = cursor.fetchall()
            # for row in result:
            #     print(row)
            # cursor.execute(select_movies_query)
            # result = cursor.fetchall()
            # for row in result:
            #     print(row)
            
            for result in cursor.execute(update_query, val_tuple, multi=True):
                if result.with_rows:
                    print(result.fetchall())
            connection.commit()

except Error as e :
    print(e)



