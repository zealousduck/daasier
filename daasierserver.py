'''
daasierserver.py
Documentation as a Service Server
'''
# Use the Flask framework for our web service
from flask import Flask
app = Flask(__name__)
from flask import request

import codeParser

# Useful globals here
VERSION = '0.0.0'

@app.route('/', methods=['GET'])
def index():
    return ('DaaSier v{}\n'.format(VERSION))

@app.route('/parseFile', methods=['POST'])
def parseFile():
    _sampleBody = '{"uri": "https://www.host.com/path/to/foo.py"}'
    _hint = '{} requires a request body\ne.g. \'{}\'\n'.format(parseFile.__name__, _sampleBody)

    uri = ''
    try:
        data = request.get_json(force=True)
        uri = data['uri']
        print(uri)
    except KeyError as keyerror:
        print('KeyError')
        return ('ERROR: ' + _hint), 400

    if uri != '':
        return codeParser.code_to_json(uri)
    else:
        return ('ERROR: ' + _hint), 400

if __name__ == '__main__':
    app.run()
