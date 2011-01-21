import web

from controllers import *

urls = (
	'/', 'index',
	'/search', 'search',
	'/faq', 'faq'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
