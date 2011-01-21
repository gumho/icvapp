============================
Dependencies
============================
1. web.py framework
2. sqlalchemy
3. python-mysqldb (for development)
4. python-nose (for testing)
5. python-paste (for testing)

============================
Development Pre-Reqs
============================
1. Create the mock RIS database. "python models/rismodel.py"

============================
Run unit/integration tests
============================
1. At top level of application, issue 'nosetests'

============================
Application Package Hierarchy
============================
icvapp
    buildtools (creation tools)
        ris_create_records.py
    config (config files)
    core 
        risrecord.py (risrecord/codepair objects)
        config_handler.py (reads/loads configuration info)
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
	rprocessor.py (result record processing module [sort, filter, paginate])
	static (static content)
	    css
	    images
	    js (client-side code/AJAX)
	templates (html templates)
	    base.html
	    index.html
	    options.html
    utils (application utilities)
        logger.py
	web (web.py library, not our code)