from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    music = db.relationship('Music', backref='artist', lazy=True)  # Define the relationship

class Music(db.Model):
    __tablename__ = 'music'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)  # Foreign key to the Artist
    album_image = db.Column(db.String(200), nullable=True)
    album_link = db.Column(db.String(200), nullable=True)

    def music_serializer(self):
        return {
            'id': self.id,
            'title': self.title,
            'album_image': self.album_image,
            'album_link': self.album_link
        }
