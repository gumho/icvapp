class Logger():
    
    LOG_FILE = '/Users/ryan/Projects/icvapp/utils/templog.txt'
    
    def __init__(self):
        self.output = open(self.LOG_FILE, 'w')
    
    def log(self, stmt):
        """record a log statement"""
        self.output.write(stmt)
        self.output.write("\n")
    
    def close(self):
        self.output.close()
        