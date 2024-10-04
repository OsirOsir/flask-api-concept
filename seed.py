from models import Music, Artist, db
from app import app

with app.app_context():
    # Create some artists
    artist1 = Artist(name="Artist One")
    artist2 = Artist(name="Artist Two")

    # Add artists to the session
    db.session.add(artist1)
    db.session.add(artist2)
    db.session.commit()  # Commit to get artist IDs

    # Create music items linked to the artists
    music1 = Music(title="Test Song", album_image="image1.png",
                   album_link="link1.com", artist_id=artist1.id)
    music2 = Music(title="Test Song 2", album_image="image2.png",
                   album_link="link2.com", artist_id=artist2.id)

    # Add music items to the session
    db.session.add(music1)
    db.session.add(music2)

    # Commit the changes to the database
    db.session.commit()

    print("Seeding complete!")
