import flask
from flask import jsonify, request
from main import get_keyword
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
    # print(request.args.get('url'))
    # print("omg")
    args = request.args
    url = args.get('url')
    if 'url' not in args:
        return "Error: no url. Please input url"
    else:
        keyword = get_keyword(url)
        return jsonify(keyword)
# input data: url
# return data
# data: {
#     url: "url",
#     keyword: "a b c"
# }
app.run()