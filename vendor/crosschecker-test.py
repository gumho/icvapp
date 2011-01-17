from crosschecker import CrossChecker

def checkPair_false_test():
	result = CrossChecker().checkPair('100', '999')
	assert(result == False)
	
def checkPair_true_test():
	result = CrossChecker().checkPair('111', '999')
	assert(result == True)