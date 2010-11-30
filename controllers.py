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
    def GET(self):        
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

        # call validate method on records
        for r in records:
            r.validatePairs()
        
        # filter / sort items
        records = rprocessor.filter(records, statuses)
        records = rprocessor.sort(records, sortby, sortdir)
        
        #get number of results before we paginate
        total_pages = rprocessor.howManyPages(records)
        num_results = len(records)
        
        records = rprocessor.paginate(records, page)
        
        # jsonize
        json = ['{',
        '"page":%d,' % page,
        '"totalpages": %d,' % total_pages,
        '"numresults":"%d",' % num_results,
        '"records": ['
        ]
        
        for i in range(len(records)):
            json.append(records[i].json())
            if(i + 1 < len(records)):
                json.append(',')
                
        json.append(']}')
                
        return ''.join(json)