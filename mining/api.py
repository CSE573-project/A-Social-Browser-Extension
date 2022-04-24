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
    <p>Go to /url and replace <strong>url</strong> in u=<strong>url</strong> with url to get keyword </p>
    <p>Go to /urls and POST urls</p>
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
        ["A cryptocurrency is a digital or virtual currency that uses cryptography and is difficult to counterfeit.", 
        "Lionel Andr\u00e9s Messi (Spanish pronunciation: [ljo\u02c8nel an\u02c8d\u027ees \u02c8mesi] (listen); born 24 June 1987), also known as Leo Messi, is an Argentine professional footballer who plays as a forward for  Ligue 1 club Paris Saint-Germain and captains the Argentina", 
        "Elon Reeve Musk  (; born June 28, 1971) is an entrepreneur, investor, and business magnate. He is the founder, CEO, and Chief Engineer at SpaceX; early-stage investor, CEO, and Product Architect of Tesla, Inc.; founder of The Boring Company; and co-f", 
        "Barack Hussein Obama II ( (listen) b\u0259-RAHK hoo-SAYN oh-BAH-m\u0259; born August 4, 1961) is an American politician who served as the 44th president of the United States from 2009 to 2017. A member of the Democratic Party, Obama was the first African-Ameri", 
        "Ukraine (Ukrainian: \u0423\u043a\u0440\u0430\u0457\u043d\u0430, romanized: Ukra\u00efna, pronounced [\u028akr\u0250\u02c8jin\u0250] (listen)) is a country in Eastern Europe. It is the second largest country in Europe after Russia, which borders it to the east and north-east. Ukraine also shares borders with B", 
        "The Pacific Ocean is the largest and deepest of Earth's five oceanic divisions. It extends from the Arctic Ocean in the north to the Southern Ocean (or, depending on definition, to Antarctica) in the south and is bounded by the continents of Asia and"]%

    """
    urls = request.form.get("urls")
    if not urls:
        return "Error: no url. Please input url"
    # print(args)
    keyword = get_keyword_multiple(urls)
    return json.dumps(keyword)
app.run()