from paste.fixture import TestApp
from nose.tools import *
from icvapp import app

# Verify whether a test for 'failed' records results in only 'failed' tests
def failed_search_test():
	middleware = []
	testApp = TestApp(app.wsgifunc(*middleware))
	r = testApp.get('/search', params={'begin_date': '1000-01-01', 'end_date': '3000-01-01', 'status': 'failed'})
	assert(str(r).find('passed') == -1)

# Verify whether a test for 'passed' records results in only 'passed' tests
def passed_search_test():
	middleware = []
	testApp = TestApp(app.wsgifunc(*middleware))
	r = testApp.get('/search', params={'begin_date': '1000-01-01', 'end_date': '3000-01-01', 'status': 'passed'})
	assert(str(r).find('failed') == -1)

# Verify whether the system returns all records from a search. No results should
# be left out.
def correct_number_studies_search_test():
	NUM_RESULTS = '"numresults":"717"'
	middleware = []
	testApp = TestApp(app.wsgifunc(*middleware))
	r = testApp.get('/search', params={'begin_date': '1000-01-01', 'end_date': '3000-01-01', 'status': 'passed'})
	r.mustcontain(NUM_RESULTS)

# Verify whether detailed information and fields from a given search are correct
def correct_information_search_test():
	middleware = []
	testApp = TestApp(app.wsgifunc(*middleware))
	r = testApp.get('/search', params={'begin_date': '1000-01-01', 'end_date': '3000-01-01', 'status': 'passed'})
	r.mustcontain('[{"accession" : "877174","date" : "Jan 15","time" : "11:35 PM","status" : "passed","codepairs" : [{"icd": "253.67","cpt": "99249","status": "passed"}]},{"accession" : "604781","date" : "Jan 15","time" : "10:42 PM","status" : "passed","codepairs" : [{"icd": "186.33","cpt": "10007","status": "passed"}]},{"accession" : "699301","date" : "Jan 15","time" : "7:10 PM","status" : "passed","codepairs" : [{"icd": "817.51","cpt": "24094","status": "passed"}]},{"accession" : "132849","date" : "Jan 15","time" : "1:18 PM","status" : "passed","codepairs" : [{"icd": "455.32","cpt": "53448","status": "passed"}]},{"accession" : "847403","date" : "Jan 15","time" : "1:16 PM","status" : "passed","codepairs" : [{"icd": "649.48","cpt": "69209","status": "passed"}]},{"accession" : "472120","date" : "Jan 15","time" : "10:44 PM","status" : "passed","codepairs" : [{"icd": "357.2","cpt": "20930","status": "passed"}]},{"accession" : "858865","date" : "Jan 13","time" : "4:34 PM","status" : "passed","codepairs" : [{"icd": "193.47","cpt": "43744","status": "passed"}]},{"accession" : "571766","date" : "Jan 13","time" : "4:14 PM","status" : "passed","codepairs" : [{"icd": "129.57","cpt": "58683","status": "passed"}]},{"accession" : "464694","date" : "Jan 12","time" : "6:43 PM","status" : "passed","codepairs" : [{"icd": "415.27","cpt": "18593","status": "passed"}]},{"accession" : "941315","date" : "Jan 12","time" : "10:59 PM","status" : "passed","codepairs" : [{"icd": "617.89","cpt": "50732","status": "passed"}]}]')
	
if __name__ == '__main__':
	# or just run 'nosetests'
	failed_search_test()
	passed_search_test()
	correct_number_studies_search_test()
	correct_information_search_test()