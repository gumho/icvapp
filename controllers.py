import web

from core.risrecord import RISRecord
from utils.logger import Logger
import rprocessor

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
        
        #re-assign records to just risrecord objects
        records = risrecs.values()
        
        # validate records
        for r in records:
            r.validatePairs()
        
        LOG = Logger()
        for i in records:
            LOG.log(i.accession)
            
        LOG.log('------')
        
        # filter / paginate / sort items
        records = rprocessor.filter(records, status)
        records = rprocessor.sort(records, None) # FIXME: not None
        records = rprocessor.paginate(records, None)
        
        for i in records:
            LOG.log(i.accession)
        
        LOG.close()
        # jsonize
        json = ''
        for rec in records:
            json += rec.json() # TODO: this step for testing only
            
        
        
        
        # FIXME: change return
        # ALSO: NEED JSON RETURN? RESULTS? PAGINATION? 
        # for pagination --> create a for-loop iterator
        return json