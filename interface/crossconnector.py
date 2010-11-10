from vendor.crosschecker import CrossChecker

class CrossConnector:
    """This module checks the icd-cpt database for validating codes. 
    Returns true if good code pair."""
    
    def validate(self, icd, cpt):
        checker = CrossChecker()
        return checker.checkPair(icd, cpt)
        
	def validatePairs(self, code_pair_list):
		"""Takes a list of records and batch checks them. returns list 
		with results. Returs false if not.
		"""
        pass