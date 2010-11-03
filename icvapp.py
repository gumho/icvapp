import web

from controllers import *

urls = (
	'/', 'index',
	'/options', 'options',
	'/search', 'search',
	'/faq', 'faq'
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
