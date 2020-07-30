from flask import Flask, request, abort
from mutant import Mutant, Stats
import os

app = Flask(__name__)   
port = int(os.environ.get('PORT', 5000))

humano = Mutant()
estadisticas = Stats()


@app.route('/')
def index():
    return 'MeLi Challenge - Juan Fresneda'

@app.route('/mutant/', methods=['POST'])
def mutant():
    if not request.json or not 'dna' in request.json:
        abort(400)

    req_body = request.get_json()

    if humano.validate_dna(req_body['dna']):
        abort(400)
    if humano.is_mutant(req_body['dna']):
        return 'true'
    else:
        abort(403)


@app.route('/stats', methods=['GET'])
def stats():
    return estadisticas.get_stats_dna()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)