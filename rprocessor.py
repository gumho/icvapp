from operator import itemgetter, attrgetter, methodcaller
from utils.logger import Logger

"""
This module has methods for filtering, sorting, and
paginating a list of risrecords.
"""

PER_PAGE = 10

def filter(records, statuses):
    """takes a list of risrecords and removes statuses 
    that don't match the provided status"""    
    if len(statuses) == 1:
        records = [r for r in records if r.getStatus() == statuses[0]]
        
    return records
    
def sort(records, by='status', sortdir='asc'):
    """sorts records by provided 'by' key. returns sorted records."""
    
    if sortdir == 'desc':
        SORT_FLAG = True
    else:
        SORT_FLAG = False
        
    if by == 'date':
        records = sorted(records, key=attrgetter('date'), reverse=SORT_FLAG)
    elif by == 'accession':
        records = sorted(records, key=attrgetter('accession'), reverse=SORT_FLAG)
    elif by == 'status':
        records = sorted(records, key=methodcaller('getStatus'), reverse=SORT_FLAG)

    return records
    
def paginate(records, pagenum=1):
    """returns paginated list of records based on offset from the 
    beginning of the list and page number."""
    if pagenum > 0:
        return records[pagenum*PER_PAGE-PER_PAGE:pagenum*PER_PAGE]

def howManyPages(records):
    recs = len(records)
    pages = recs / PER_PAGE
    if recs % PER_PAGE > 0: 
        pages += 1
    return pages