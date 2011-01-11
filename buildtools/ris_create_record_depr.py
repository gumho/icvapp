'''
Created on Nov 2, 2010

@author: Ackus
'''
from sqlalchemy import create_engine #@UnresolvedImport
from sqlalchemy import Column, Integer, String, DateTime #@UnusedImport @UnresolvedImport
from sqlalchemy.ext.declarative import declarative_base #@UnresolvedImport
import random
from datetime import datetime, date, time

engine = create_engine('mysql://root:password@localhost/ris', echo=True,
            pool_size=20, max_overflow=0)


Base = declarative_base()
class DB_Create(Base):
    """Generates a database creation scripts to set up our database.  
    One function should output the script needed to create the database and tables.
    Another function should fill the database with thousands of fake records.
    
    Functions to generate accession numbers, referring physicians, visit numbers,
    CPT codes, ICD codes, and dateTimes
    """
    def create_ids(self):
        self.create_id()
        return int
        
    def create_id(self, string):
        return    
    
    def create_accession(self):
        scans = ["CT", "IR", "US", "CR"]
        first = random.choice(scans)
        second = random.randint(1000,9999)
        accession = "%s-10-000%.0f" % (first, second)
        return accession
    
    def create_referring(self):
        """returns a referring physician from the list 'list'
        """
        list = ["101618^Kahn^Christopher", "089987^Lekawa^Michael", "106393^Al-Khoury^Lama", "106567^Ghostine^Samer", "098418^Lane^Christophe", "102145^Randall-Whitis^Leslie"]
        referring = random.choice(list)
        return referring
    
    def create_visit(self):
        prefix = [9000, 2009, 2008]
        first = random.choice(prefix)
        suffix = random.randint(100000, 999999)
        visit = str(first) + str(suffix)
        return visit
                
    def create_cpt(self):
        """returns a CPT code in the form:
        '12345'
        '67890'
        '04321'
        """
        cpt_int = random.randint(1,99999)
        if cpt_int > 9999:
            final_cpt = cpt_int
        elif 10000 > cpt_int > 999:
            final_cpt = "0" + str(cpt_int)
        elif 1000 > cpt_int > 99:
            final_cpt = "00" + str(cpt_int)
        elif 100 > cpt_int > 9:
            final_cpt = "000" + str(cpt_int)
        else:
            final_cpt = "0000" + str(cpt_int)
        return final_cpt
    
    def create_icd(self):
        """returns an ICD code in the form of a string in the format:
        '123.45'
        '678.90'
        """
        first = random.randint(0,999)
        second = random.random()
        icd = "%.2f " % (first + second)
        return icd
    
    def create_date(self):
        """ returns a date time in the format:
        datetime.datetime(2010, 11, 17, 13, 31, 34, 846339)
        datetime.datetime(year, month, day, hour, minute, second, microsecond)
        """
        d = datetime.today()
        newmonth = d.month - random.randomint(0,2)
        daynum = d.day
        newday = d.day - random.randomint(0,daynum-1)
        newtime = 21
        finalDateTime = d.replace(month = newmonth, day = newday)
        #datetime = "2010%i%i%i" % (newmonth, newday, newtime)
        return finalDateTime