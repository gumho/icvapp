import web
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
        
        # process records
        
        # assemble return format

        # FIXME: change return
        return records