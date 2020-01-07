'''
 create by xh
'''
__author__ = 'xh'

from flask import Flask, make_response

app = Flask(__name__)
app.config.from_object('config')


@app.route('/h2')
def hello():
    response = make_response('[1,2,3]', 404)
    response.headers = {
      'content-type': 'application/json'
    }
    return response


def hi():
    return 'hello world'


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', )
