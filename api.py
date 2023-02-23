import flask
from flask import request, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True


# Create some test data for our catalog in the form of dictionaries.

books = [
    {'id': 0,
      'name': 'Jamie Morrissey',
      'phone_number': '1-333-444-5555',
      'year_born': '1982'},
    {'id': 1,
      'name': 'Charles Korkegian',
      'phone_number': '1-444-555-6666',
      'year_born': '1958'}
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>This is a formulated Python backend API written with dictionary key values</h1><li>Hello</li><li>I hope this project gets me a job</li><li>The second part of this project shows how to use the cURL linux utility</li>"

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    
    # Create an empty List for our results

    results = []

    for book in books:
        if book['id'] == id:
            results.append(book)

    return jsonify(results)


app.run()