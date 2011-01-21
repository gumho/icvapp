from paste.fixture import TestApp
from nose.tools import *
from icvapp import app

def failed_search_test():
	middleware = []
	testApp = TestApp(app.wsgifunc(*middleware))
	r = testApp.get('/search', params={'begin_date': '1000-01-01', 'end_date': '3000-01-01', 'status': 'failed'})
	assert(str(r).find('passed') == -1)

def passed_search_test():
	middleware = []
	testApp = TestApp(app.wsgifunc(*middleware))
	r = testApp.get('/search', params={'begin_date': '1000-01-01', 'end_date': '3000-01-01', 'status': 'passed'})
	assert(str(r).find('failed') == -1)
	
if __name__ == '__main__':
	# or just run 'nosetests'
	failed_search_test()