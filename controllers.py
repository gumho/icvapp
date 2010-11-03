import web

render = web.template.render('templates/', base='base')

class index:
	def GET(self):
		return render.index();

class options:
	def GET(self):
		return render.options()
		
class search():
	"""gets the search variables, searches for associated records,
	processes the records through the icd-cpt engine and returns results
	"""
	def POST(self):
		#process search vars
		i = web.input()
		
		#get list of records
		
		#process the records
		
		#assemble return format
		
		#return results
		return i.criteria_status