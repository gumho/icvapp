import datetime

now = datetime.datetime.now()

months = {
    '01':'Jan',
    '02':'Feb',
    '03':'Mar',
    '04':'Apr',
    '05':'May',
    '06':'Jun',
    '07':'Jul',
    '08':'Aug',
    '09':'Sep',
    '10':'Oct',
    '11':'Nov',
    '12':'Dec',
}

def sql_datetime_to_human_date(dt):
    """converts sql datetime to human readable date. ex. 2010-11-29 10:30:15 => Nov 29"""
    m = months[dt[5:7]]
    d = dt[8:10]
    y = dt[0:4]
    
    if(y == str(now.year)):
        y = ''
    else:
        y = ', %s' % y
    
    return ''.join([m, ' ', d, y])

def sql_datetime_to_12hr_time(dt):
    """converts sql datetime to human readable time. ex. 2010-11-29 13:30:15 => 1:30 PM"""
    h = to12(dt[11:13])
    m = dt[14:16]
    
    if(h > 12): 
        suf = 'PM'
    else: 
        suf = 'AM'
    
    return ''.join([h, ':', m, ' ', suf])
    
def to12(hour24):
    return str((int(hour24) % 12) if (int(hour24) % 12) > 0 else 12)