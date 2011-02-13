from crosschecker import CrossChecker

# Verify whether a known false pair is checked as false by crosschecker
def checkPair_false_test():
	result = CrossChecker().checkPair('100', '999')
	assert(result == False)
	
# Verify whether a know true pair is checked as true by crosschecker
def checkPair_true_test():
	result = CrossChecker().checkPair('111', '999')
	assert(result == True)