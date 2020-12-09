from os    import path
from flask import Flask
from flask import request, abort

app = Flask(__name__)

def check_flag(chal, flag):
    with open('./chal/{}.txt'.format(chal)) as f:
        if flag == f.read().strip('\n'):
            return 'true' , 200
        else:
            return 'false', 200

@app.route('/')
def hello():
    return 'This is not the routes you\'re looking for.'

@app.route('/submit/<chal>', methods=['POST'])
def try_submit(chal):
    if 'flag' not in request.form:
        return 'flag not set', 400
    if not path.exists('./chal/{}.txt'.format(chal)):
        return 'challenge not found', 400
    result = check_flag(chal, request.form['flag'])
    return result


