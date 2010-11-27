'''
Created on Nov 22, 2010

@author: Ackus
'''
import re


class string_defs():

    def monthConvert(self, int):
        try:
            if int == 1:
                month = "Jan"
            elif int == 2:
                month = "Feb"
            elif int == 3:
                month = "Mar"
            elif int == 4:
                month = "Apr"
            elif int == 5:
                month = "May"
            elif int == 6:
                month = "Jun"
            elif int == 7:
                month = "Jul"
            elif int == 8:
                month = "Aug"
            elif int == 9:
                month = "Oct"
            elif int == 10:
                month = "Sep"
            elif int == 11:
                month = "Nov"
            elif int == 12:
                month = "Dec"
        except IOError:
            print 'invalid month', int
        else:
            return month
        
    def hourConvert(self, int):
        try:
            if  12 < int <= 24:
                printHour = "%s PM" % (int - 12)
            elif 0 < int <= 12:
                printHour = "%s AM" % (int)
        except IOError:
            print 'invalid hour', int
        else:
            return printHour

    def dateConvert(self, string):
        """Takes a datetime string "2010-11-21 23:00:04" => "Nov 21"
        If the given date is not from this year, then it appends the date (Nov 21, 2009).
        """
        dateTimePattern = re.compile(r'^(\d{4})-(\d{2})-(\d{2})\D+(\d{2})\D+(\d{2})\D+(\d{2})$')
        year = dateTimePattern.search(string).group(1)
        month = dateTimePattern.search(string).group(2)
        day = dateTimePattern.search(string).group(3)
        
        printMonth = self.monthConvert(month)
        
        if year == '2010':
            printDate = "%s %s" % (printMonth, day)
        else:
            printDate = "%s %s, %s" % (printMonth, day, year)
            
        return printDate
        
        
    def timeExtract(self, string):
        """timeExtract() takes the same datetime string and returns human readable time.
        So "2010-11-21 23:00:04" => "11:00 PM"
        """
        dateTimePattern = re.compile(r'^(\d{4})-(\d{2})-(\d{2})\D+(\d{2})\D+(\d{2})\D+(\d{2})$')
        hour = dateTimePattern.search(string).group(4)
        minute = dateTimePattern.search(string).group(5)
        #second = dateTimePattern.search(string).group(6)
        
        tempHour = self.hourConvert(hour)
        printHourPattern = re.compile(r'(\d{2})\D+(\d{2})$')
        printHour = printHourPattern.search(tempHour).group(1)
        ampm = printHourPattern.search(tempHour).group(2)
        
        printTime = ("%s:%s %s") % (printHour, minute, ampm)
        
        return printTime