import web
from core.risrecord import RISRecord
from utils.logging import Logger

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
        
        # get records
        records = RISConnector().get_records(start, end)
        
        # convert sql records into risrecord objects
        logger = Logger()
        
        d = {}
        for r in records:
            acc = r.accession
            if not d.has_key(acc):
                d[acc] = RISRecord(acc, r.referring, r.visit, r.date)
                
            d[acc].add_pair(r.icd, r.cpt)
        
        
            
        logger.close()
        # assemble return format

        # FIXME: change return
        return records