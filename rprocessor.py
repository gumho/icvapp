from operator import itemgetter, attrgetter, methodcaller

"""
This module has methods for filtering, sorting, and
paginating a list of risrecords.
"""

PER_PAGE = 2

def filter(records, status):
    """takes a list of risrecords and removes statuses 
    that don't match the provided status"""
    if status in ('passed', 'failed'):
        records = [r for r in records if r.getStatus() == status]
    return records
    
    
def sort(records, by='status'):
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