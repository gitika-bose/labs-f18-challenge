from flask import Flask, render_template
from string import Template
import json
import requests

app = Flask(__name__)

# HTML_TEMPLATE = Template("""<h1>Hello ${query_name}!</h1>""")

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<query>')
def query_pokemon(query):

	query_value = query
	r = requests.get('http://pokeapi.co/api/v2/pokemon/' + query_value)

	r_dict = r.json()

	result = r_dict["id"]

	return  query_value + " has ID " + str(result) 

@app.route('/pokemon/<int:query_int>')
def query_pokemon_int(query_int):

	query_value = query_int
	r = requests.get('http://pokeapi.co/api/v2/pokemon/' + str(query_value))

	r_dict = r.json()

	result = r_dict["forms"][0]["name"]

	return "The pokemon with ID " + str(query_value) + " is " + result 

if __name__ == '__main__':
	app.run()
