import flask
from flask import request, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True


# Create some test data for our catalog in the form of dictionaries.

books = [
    {'id': 0,
      'name': 'Jamie Taylor Morrissey',
      'phone_number': '1-333-444-5555',
      'year_born': '1982'},
    {'id': 1,
      'name': 'Charles Korkegian',
      'phone_number': '1-444-555-6666',
      'year_born': '1958'}
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

app.run()