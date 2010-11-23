from vendor.crosschecker import CrossChecker

class CrossConnector:
    """This module checks the icd-cpt database for validating codes. 
    Returns true if good code pair."""
    
    def validate(self, icd, cpt):
        checker = CrossChecker()
        return checker.checkPair(icd, cpt)