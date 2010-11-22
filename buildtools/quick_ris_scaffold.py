from random import randrange, randint

if __name__ == '__main__':
    _id = 323456
    
    for i in range(1,20):
        _id += 1
        #acc = str(randint(1000, 999999))
        acc = 24242424
        
        ref = str("'steven'")
        vis = str(randint(1000, 9999999))
        cpt = str(randint(100000,999999))
        icd = "'" + str(randint(100,999)) + ':' + str(randrange(10, 99)) + "'"
        
        #year = str(randint(2006,2010))
        #month = str(randint(10,12))
        #day = str(randint(10,30))
        #h = str(randint(10,23))
        #m = str(randint(10, 59))
        #s = str(randint(10,59))
        
        #dt = "'" + year + '-' + month + '-' + day + ' ' + h + ':' + m + ':' + s + "'"
        dt = "'2010-11-21 11:11:11'"
        
        print "INSERT INTO `ris`.`studies` (`id`, `accession`, `referring`, `visit`, `cpt`, `icd`, `date`)\
         VALUES (%s, %s, %s, %s, %s, %s, %s);" % (_id, acc, ref, vis, cpt, icd, dt)