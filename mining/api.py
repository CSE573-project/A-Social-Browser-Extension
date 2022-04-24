import flask
from flask import jsonify, request
from main import get_keyword
app = flask.Flask(__name__)
# app.config["DEBUG"] = True
@app.route('/', methods=['GET'])
def home():
    message = """
    <h1>Data mining API </h1>
    <p>Go to /url and replace <strong>url</strong> in u=<strong>url</strong> with url to get keyword</p>
    """
    return message
@app.route('/url', methods=['GET'])
def url():
    """
    Input data: url
    Return data:
        A cryptocurrency is a digital or virtual currency that uses cryptography and is difficult to counterfeit.
    """
    args = request.args
    url = args.get('url')
    if 'url' not in args:
        return "Error: no url. Please input url"
    else:
        keyword = get_keyword(url)
        return keyword

app.run()