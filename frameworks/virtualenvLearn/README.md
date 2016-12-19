#virtualenv`

`virtualenv` is a way of separating different python environments for different projects. This is useful for mitigating packages different versions and incompatibilities that might arise as a result.

`virtualenv` is also useful in that it helps us ensure that we have the essential collection of python module coverage, in the specified versioning of such utilities.

**Make sure to have `virtualenv` installed in the first place:**

	pip install virtualenv

**List the Python modules available**

	pip list

**Make a directory `PROJECT` where you want to execute `virtualenv` as `VENV`

	mkdir PROJECT

	cd PROJECT

	virtualenv VENV

	virtualenv -p usr/bin/python2 VENV

	virtualenv -p usr/bin/python3 VENV

	source VENV/bin/activate 
	
	which python

	which pip

	python --version

	pip install numpy

	pip install PYTHON_MODULE

	pip list

	pip freeze --local > requirements.txt

	deactivate

	which python

	pip list

	ls

	rm -rf VENV

	ls

	virtualenv -p /usr/bin/python2.6 VENV_26

	ls

	source VENV_26/bin/activate

	which python

	python --version

	pip install -r requirements.txt

	pip list

	deactivate









	

	
