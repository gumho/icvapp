from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:password@localhost/icv', echo=True)

Base = declarative_base()
class Study(Base):
    __tablename__ = 'studies'

    accession = Column('accession', String(12), primary_key=True)
    referring = Column('referring', Integer)
    visit = Column('visit', Integer)
    cpt = Column('cpt', String(8))
    icd = Column('icd', String(8))
    
    def __init__(self, accession, referring, visit, cpt, icd):
		self.accession = accession
		self.referring = referring
		self.visit = visit
		self.cpt = cpt
		self.icd = icd
	
    def __repr__(self):
        return "<Study('%s','%s','%s','%s','%s',)>" % (self.accession, self.referring, self.visit, self.cpt, self.icd)

        studies_table = Study.__table__
		
metadata = Base.metadata

if __name__ == "__main__":
    metadata.create_all(engine)
