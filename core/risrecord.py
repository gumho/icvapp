from interface.crossconnector import CrossConnector

class RISRecord():
    """RISRecord is a representation of one 'study' in the RIS system. This constitutes
    a patient visit with a unique accession number and all of the icd-cpt pairs that
    were assigned within the record"""
    
    def __init__(self, accession, referring, visit, date):
        self.accession = accession
        self.referring = referring
        self.visit = visit
        self.date = date
        self.codepairs = []
    
    def get_pairs(self):
        """return the icd-cpt pair list"""
        return self.codepairs
    
    def add_pair(self, icd, cpt):
        """adds an icd-cpt pair to the record"""
        self.codepairs.append(CodePair(icd, cpt))
    
    def validatePairs(self):
        """validate all code pairs within"""
        self.codepairs = [pair.validate() for pair in self.codepairs]
        
    def html(self):
        """convert record into HTML table row"""
        html = "\
        <tr>\
            <td>%s</td>\
            <td>%s</td>\
            <td>%s</td>\
            <td>%s</td>\
        </tr>\
        " % ('date', 'time', 'acc', 'status')
        
        return html

class CodePair():
    """a representation of an icd9 and cpt code pair."""
    def __init__(self, icd, cpt):
        self.icd = icd
        self.cpt = cpt
    
    def get_pair(self):
        """returns the code pair as a tuple"""
        return (self.icd, self.cpt)
    
    def validate(self):
        checker = CrossConnector()
        
        if checker.validate(self.icd, self.cpt):
            self.passed = True
        else:
            self.passed = False
            