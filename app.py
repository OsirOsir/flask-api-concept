from flask import Flask, jsonify
from models import Music, Artist, db
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://philip:12345@localhost/my_music'
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/music_list', methods=['GET'])
def index():
    music_items = Music.query.all()
    return jsonify([music_item.music_serializer() for music_item in music_items])

@app.route('/artists', methods=['GET'])
def get_artists():
    artists = Artist.query.all()
    return jsonify([{ 
        'id': artist.id, 
        'name': artist.name, 
        'music': [music.music_serializer() for music in artist.music] 
    } for artist in artists])

if __name__ == '__main__':
    app.run(port=5000, debug=True)
