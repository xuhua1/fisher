

from . import web
from flask import request, current_app
from app.forms.book import SearchForm

@web.route('/book/search')
def book():
  q = request.args['q']
  form = SearchForm(request.args)
  if form.validate():
    q = form.q.data.strip()
    page = form.page.data
    perPage = current_app.config['PER_PAGE']
    return str(perPage) + str(page) + str(q)
  return False