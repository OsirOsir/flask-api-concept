import psycopg2

def view_music():
    # Connect to your PostgreSQL database
    connection = psycopg2.connect(
        dbname='my_music',
        user='philip',
        password='12345',
        host='localhost'
    )

    cursor = connection.cursor()

    # Query data from the music table
    cursor.execute("SELECT * FROM music;")
    music_records = cursor.fetchall()

    # Print out the records
    print("Music Records:")
    for record in music_records:
        print(record)

    # Query data from the artists table
    cursor.execute("SELECT * FROM artists;")
    artist_records = cursor.fetchall()

    # Print out the records
    print("\nArtist Records:")
    for record in artist_records:
        print(record)


    # Close the cursor and connection
    cursor.close()
    connection.close()

if __name__ == '__main__':
    view_music()
