from flask import Flask 
from bd import Songs

app = Flask(__name__)

@app.route('/songs', methods=('GET'))
def get_musics():
    return

app.run()
