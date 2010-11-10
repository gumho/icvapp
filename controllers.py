import web
from core.risrecord import RISRecord
from utils.logger import Logger

from interface.risconnector import RISConnector

render = web.template.render('templates/', base='base')

class index:
    def GET(self):
        return render.index()

class options:
    def GET(self):        
        return render.options()
		
class search:
    """gets the search variables, searches for associated records,
    processes the records through the icd-cpt engine and returns results
    """
    def POST(self):        
        # process search vars
        i = web.input()
        
        start = i.criteria_start
        end = i.criteria_end
        status = i.criteria_status
        
        # get records in model.Study object format
        records = RISConnector().get_records(start, end)
        
        # convert sql records into risrecord objects
        risrecs = {}
        for r in records:
            acc = r.accession
            
            if not risrecs.has_key(acc):
                risrecs[acc] = RISRecord(
                    r.accession,
                    r.referring,
                    r.visit,
                    r.date
                )
            
            risrecs[acc].add_pair(r.icd, r.cpt)

        # validate records
        records = ''
        for (acckey, rec) in risrecs.items():
            rec.validatePairs()
            records += rec.html()
        
        # TODO: assemble return format

        # TODO: sort / filter results 
        
        # FIXME: change return
        return records