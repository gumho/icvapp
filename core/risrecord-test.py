from risrecord import *

def code_pair_get_pair_test():
	pair = CodePair('000', '111')
	assert(pair.get_pair() == ('000', '111'))
	
def code_pair_validate_pass_test():
	pair = CodePair('111', '111')
	pair.validate()
	assert(pair.status == 'passed')
	
def code_pair_validate_fail_test():
	pair = CodePair('000', '111')
	pair.validate()
	assert(pair.status == 'failed')

def code_pair_json_test():
	pair = CodePair('000', '111')
	pair.status = 'failed'
	assert(pair.json() == '{"icd": "000","cpt": "111","status": "failed"}')

def code_pair_unchecked_test():
	pair = CodePair('000', '111')
	assert(pair.status == 'unchecked')

