#need to enable connection pooling
#db = web.database(dbn='mysql', db='name', user='aoeu')

class RISConnector:
	"""connects to the RIS system and provides methods for extracting data"""
	def __init__(self, arg):
		pass
		
	def get_records(self, start_date, end_date, status=""):
		"""queries RIS for records based on date range between start_date and
		end_date and optionally, status"""
		pass