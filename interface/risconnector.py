from sqlalchemy import and_
from sqlalchemy.orm import scoped_session, sessionmaker
from models.rismodel import Study, engine

class RISConnector:
    def get_records(self, start_date, end_date):
        """queries RIS for records based on date range between start_date and
        end_date"""
        
        session = scoped_session(sessionmaker(bind=engine))
        
        if start_date == end_date:
            start_date += ' 00:00:00'
            end_date += ' 24:59:59'
            
        records = session.query(Study).filter(and_(Study.date > start_date, Study.date < end_date)).all()

        return records
