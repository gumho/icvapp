from rprocessor import *

# This test module tests correctness as well as scale of 
# the custom howManyPages() and paginate() functions

#ASSUME MAX RECORDS IS 10

def below_threshold_number_pages_test():
	records = [] #0 records
	assert(howManyPages(records) == 0)

def below_threshold_number_pages_test():
	records = [x for x in range(5)] #5 records
	assert(howManyPages(records) == 1)

def equal_threshold_number_pages_test():
	records = [x for x in range(10)] #10 records
	assert(howManyPages(records) == 1)

def greater_threshold_number_pages_test():
	records = [x for x in range(11)] #11 records
	assert(howManyPages(records) == 2)

def big_threshold_number_pages_test():
	records = [x for x in range(10000)] #1000 records
	assert(howManyPages(records) == 1000)

def first_page_paginate_test():
	records = [x for x in range(30)] #30 records
	page = 1
	assert(paginate(records, page) == [x for x in range(0,10)])
		
def mid_paginate_test():
	records = [x for x in range(30)] #30 records
	page = 2
	assert(paginate(records, page) == [x for x in range(10,20)])



if __name__ == '__main__':
	paginate_test()