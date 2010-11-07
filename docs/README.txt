Dependencies:
1. web.py framework
2. sqlalchemy
3. python-mysqldb (for development)

Development pre-reqs:
1. Create the mock RIS database. "python models/rismodel.py"
2. Create the mock Crosscheck database. "python models/crossmodel.py"

Application package hierarchy:

icvapp
    config (config files)
    controllers.py (url handlers)
    docs
        CHANGES.txt (changelog)
        README.txt (this)
	icvapp.py (application main)
	interface (external connection managers)
	    crossconnector.py
	    risconnector.py
	models (schema mappings)
	    rismodel.py
	static (static content)
	    css
	    images
	    js (client-side code/AJAX)
	templates (html templates)
	    base.html
	    index.html
	    options.html
	tests (unit tests)
	web (web.py library, not our code)