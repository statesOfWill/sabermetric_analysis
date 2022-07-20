import flask
from flask import request, jsonify
from flaskr.readGames import readGames

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# http://127.0.0.1:5000/api/v1/readGames?focus=ARI&opponents=SFN&years=1998+2021
@app.route('/api/v1/readGames', methods=['GET'])
def api_filter():
    query_parameters = request.args
    focusTeam = query_parameters.get('focus')
    opps = query_parameters.get('opponents')
    yearRange = query_parameters.get('years')
    oppsList = []
    years = []

    for year in yearRange.split(' '):
        years.append(year)

    for opp in opps.split(' '):
        oppsList.append('\"'+opp+'\"')

    return jsonify(readGames('\"'+focusTeam+'\"', oppsList, years))

app.run()
