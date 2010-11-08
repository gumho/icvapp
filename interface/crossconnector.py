from vendor import CrossChecker

class CrossConnector:
	"""this module checks the icd-cpt database for validating codes"""

	def checkRecords(self, icd, cpt):
		"""takes a list of records and batch checks them. returns list 
		with results.
		"""
		return CrossChecker.check_pair(icd, cpt)