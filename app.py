from flask import Flask, jsonify
from models import Music, db
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://osir:osirphilip12345@localhost/mymusic'
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/music_list', methods=['GET'])
def index():
    music_items = Music.query.all()
    return jsonify([music_item.music_serializer() for music_item in music_items])


if __name__ == '__main__':
    app.run(port=5000, debug=True)
