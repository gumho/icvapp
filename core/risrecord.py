from interface.crossconnector import CrossConnector
from utils.logger import Logger

class RISRecord():
    """RISRecord is a representation of one 'study' in the RIS system. This constitutes
    a patient visit with a unique accession number and all of the icd-cpt pairs that
    were assigned within the record"""
    
    def __init__(self, accession, referring, visit, date):
        self.accession = accession
        self.referring = referring
        self.visit = visit
        self.date = date # this is a datetime!
        self.codepairs = []
    
    def get_pairs(self):
        """return the icd-cpt pair list"""
        return self.codepairs
    
    def add_pair(self, icd, cpt):
        """adds an icd-cpt pair to the record"""
        self.codepairs.append(CodePair(icd, cpt))
    
    def validatePairs(self):
        """validate all code pairs within"""
        for p in self.codepairs:
            p.validate()
        
    def json(self):
        """return record as JSON object"""
        json = ''
        json += '{'
        json += '"accession" : "%s",' % self.accession
        json += '"date" : "%s",' % self.getDate()
        json += '"time" : "%s",' % self.getTime() # TODO
        json += '"status" : "%s",' % self.getStatus()
        json += '"codepairs" : ['
        
        for i in range(len(self.codepairs)):
            json += self.codepairs[i].json()
            if i == len(self.codepairs) - 1:
                json += ''
            else:
                json += ','
        
        json += ']}'
        
        return json
        
    def html(self):
        """return record as HTML table row"""
        html = "\
        <tr>\
            <td>%s</td>\
            <td>%s</td>\
            <td>%s</td>\
            <td>%s</td>\
        </tr>\
        " % (self.date, self.getTime(), self.accession, self.getStatus())
        
        for p in self.codepairs:
            html += "\
            %s : %s - %s<br>\
            " % (p.icd, p.cpt, p.status)
        return html
        
    def getTime(self):
        return 'todo' # TODO
    
    def getDate(self):
        return 'todo' # TODO

    def getStatus(self):
        for pair in self.codepairs:
            if pair.status is 'failed':
                return 'failed'
        
        return 'passed'

class CodePair():
    """a representation of an icd9 and cpt code pair."""
    def __init__(self, icd, cpt):
        self.icd = icd
        self.cpt = cpt
        self.status = 'unchecked'
    
    def get_pair(self):
        """returns the code pair as a tuple"""
        return (self.icd, self.cpt)
    
    def validate(self):
        checker = CrossConnector()
        
        if checker.validate(self.icd, self.cpt):
            self.status = 'passed'
        else:
            self.status = 'failed'
    
    def json(self):
        """returns representation of self in JSON"""
        json = ['{', 
        '"icd": "%s",' % self.icd,
        '"cpt": "%s",' % self.cpt,
        '"status": "%s"' % self.status,
        '}'
        ]
        
        return ''.join(json)