class RISRecord():
    """RISRecord is a representation of one 'study' in the RIS system. This constitutes
    a patient visit with a unique accession number and all of the icd-cpt pairs that
    were assigned within the record"""
    
    def __init__(self, accession):
        self.accession = accession
        self.codepairs = [] 
    
    def get_pairs(self):
        """return the icd-cpt pair list"""
        return self.codepairs
    
    def add_pair(self, icd, cpt):
        """adds an icd-cpt pair to the record"""
        self.codepairs.append(CodePair(icd, cpt))

class CodePair():
    """a representation of an icd9 and cpt code pair."""
    def __init__(self, icd, cpt):
        self.icd = icd
        self.cpt = cpt
    
    def get_pair(self):
        """returns the code pair as a tuple"""
        return (self.icd, self.cpt)