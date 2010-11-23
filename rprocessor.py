from operator import itemgetter, attrgetter, methodcaller
from utils.logger import Logger

"""
This module has methods for filtering, sorting, and
paginating a list of risrecords.
"""

PER_PAGE = 20

def filter(records, statuses):
    """takes a list of risrecords and removes statuses 
    that don't match the provided status"""    
    if len(statuses) == 1:
        records = [r for r in records if r.getStatus() == statuses[0]]
        
    return records
    
    
# TODO: make two params needed, asc/desc as well as the column needed 
# as suggested by francesco
def sort(records, by='status', sortdir='asc'):
    """sorts records by provided 'by' key. returns sorted records."""
    # TODO: sort by asc/desc
    if by == 'date':
        records = sorted(records, key=attrgetter('date'))
    elif by == 'accession':
        records = sorted(records, key=attrgetter('accession'))
    elif by == 'status':
        records = sorted(records, key=methodcaller('getStatus'))

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