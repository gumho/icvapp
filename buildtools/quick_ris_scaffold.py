from random import randrange, randint

if __name__ == '__main__':
    _id = 556555
    
    for i in range(1,50):
        _id += 1
        acc = str(randint(55555, 999999))
        # acc = 24242424
        
        ref = str("'steven'")
        vis = str(randint(1000, 9999999))
        cpt = str(randint(10000,99999))
        icd = "'" + str(randint(100,999)) + '.' + str(randrange(1, 99)) + "'"
        
        year = str(randint(2011,2011))
        month = str(randint(1,1))
        day = str(randint(1,15))
        h = str(randint(10,23))
        m = str(randint(10, 59))
        s = str(randint(10,59))
        
        dt = "'" + year + '-' + month + '-' + day + ' ' + h + ':' + m + ':' + s + "'"
        # dt = "'2010-11-21 11:11:11'"
        
        print "INSERT INTO `ris`.`studies` (`id`, `accession`, `referring`, `visit`, `cpt`, `icd`, `date`)\
         VALUES (%s, %s, %s, %s, %s, %s, %s);" % (_id, acc, ref, vis, cpt, icd, dt)