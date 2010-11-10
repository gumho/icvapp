from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:password@localhost/ris', echo=True,
            pool_size=20, max_overflow=0)

Base = declarative_base()
class Study(Base):
    __tablename__ = 'studies'
    
    _id = Column('id', String(16), primary_key=True)
    accession = Column('accession', String(12))
    referring = Column('referring', String(64))
    visit = Column('visit', Integer)
    cpt = Column('cpt', String(8))
    icd = Column('icd', String(8))
    date = Column('date', DateTime())
    
    def __init__(self, _id, accession, referring, visit, cpt, icd, date):
        self._id = _id
        self.accession = accession
        self.referring = referring
        self.visit = visit
        self.cpt = cpt
        self.icd = icd
        self.date = date
	
    def __repr__(self):
        return "<Study('%s','%s','%s','%s','%s','%s','%s')>" % (self._id, self.accession, self.referring, self.visit, self.cpt, self.icd, self.date)

        studies_table = Study.__table__
		
metadata = Base.metadata

# script to create the tables if necessary
if __name__ == "__main__":
    metadata.create_all(engine)
