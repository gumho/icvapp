import web
import rprocessor

from core.risrecord import RISRecord
from interface.risconnector import RISConnector
from utils.logger import Logger

render = web.template.render('templates/', base='base')

class index:
    def GET(self):
        return render.index()
		
class search:
    """gets the search variables, searches for associated records,
    processes the records through the icd-cpt engine and returns results
    """
    def POST(self):        
        # process search vars
        i = web.input(status=[])
        
        start = i.begin_date
        end = i.end_date
        statuses = i.status # array
        
        sortby = i.sortby if hasattr(i, 'sortby') else 'status'
        sortdir = i.sortdir if hasattr(i, 'sortdir') else 'asc'
        page = int(i.page) if hasattr(i, 'page') else 1            
                
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
        
        # filter / paginate / sort items
        total_pages = rprocessor.howManyPages(records)
        records = rprocessor.filter(records, statuses)
        records = rprocessor.sort(records, sortby, sortdir)
        records = rprocessor.paginate(records, page)
        
        # jsonize
        # TODO: optimize so we're not using append operator
        json = ''
        json += '{'
        json += '"page":%d,' % page
        json += '"totalpages": %d,' % total_pages
        json += '"numresults":"%d",' % len(records)
        json += '"records": ['
        for i in range(len(records)):
            json += records[i].json()
            if(i + 1 < len(records)):
                json += ','
        json += ']'
        json += '}'
                
        return json