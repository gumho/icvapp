'''
Created on Nov 2, 2010

@author: Ackus
'''
from sqlalchemy import create_engine #@UnresolvedImport
from sqlalchemy import Column, Integer, String, DateTime #@UnusedImport @UnresolvedImport
from sqlalchemy.ext.declarative import declarative_base #@UnresolvedImport
import random
import datetime

engine = create_engine('mysql://root:password@localhost/ris', echo=True,
            pool_size=20, max_overflow=0)


Base = declarative_base()
class DB_Create(Base):
    """Generates a database creation scripts to set up our database.  
    One function should output the script needed to create the database and tables.
    Another function should fill the database with thousands of fake records.
    """

    def build_db(self, f):
        return
    
    def create_table(self):
    
        print "[insert %s here]" % ("nothing")
        
    def create_id(self, string):
        return    
    
    def create_accession(self, string):
        scans = ["CT", "IR", "US", "CR"]
        first = random.choice(scans)
        second = random.randint(1000,9999)
        accession = "%s-10-000%.0f" % (first, second)
        return accession
    
    def create_referring(self, string):
        ref = random.randint(0,100)
        return ref
    
    def create_visit(self, int):
        prefix = [9000, 2009, 2008]
        first = random.choice(prefix)
        suffix = random.randint(100000, 999999)
        visit = str(first) + str(suffix)
        return visit
                
    def create_cpt(self, string):
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
            
        """cpt = " %d " % random.randint(0,99999)"""
        return final_cpt
    
    def create_icd(self, string):
        first = random.randint(0,999)
        second = random.random()
        icd = "%.2f " % (first + second)
        return icd
    
    def create_date(self):
        return DateTime()