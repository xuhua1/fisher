'''
 create by xh
'''
__author__ = 'xh'

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', )
