from crossconnector import *

def cross_connector_validate_fail_test():
	cc = CrossConnector()
	assert(cc.validate('000','111') == False)
	
def cross_connector_validate_pass_test():
	cc = CrossConnector()
	assert(cc.validate('111','111') == True)