
from . import web

@web.route('/user')
def user():
  return 'user'