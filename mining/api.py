import flask
from flask import jsonify, request
import json
from main import get_keyword
from main import get_keyword_multiple
app = flask.Flask(__name__)
app.config["DEBUG"] = True
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
@app.route('/urls', methods=['POST'])
def urls():
    """
    Input data: url list
    Return data:
        A cryptocurrency is a digital or virtual currency that uses cryptography and is difficult to counterfeit.
    """
    urls = request.form.get("urls")
    if not urls:
        return "Error: no url. Please input url"
    # print(args)
    keyword = get_keyword_multiple(urls)
    return json.dumps(keyword)
app.run()