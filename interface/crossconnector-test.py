from crossconnector import *

# Verify correctness of fail item
def cross_connector_validate_fail_test():
	cc = CrossConnector()
	assert(cc.validate('000','111') == False)

# Verify correctness of pass item
def cross_connector_validate_pass_test():
	cc = CrossConnector()
	assert(cc.validate('111','111') == True)