#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/cities_by_states')
def cities_by_states():
    """ Display a HTML page with states and their cities. """
    states = storage.all(State).values()
    return render_template('cities_by_states.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """ Close the storage on teardown. """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
