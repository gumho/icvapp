import web

from processors import load_sqla
from controllers import *

urls = (
	'/', 'index',
	'/options', 'options',
	'/search', 'search',
	'/faq', 'faq'
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.add_processor(load_sqla)
    app.run()
