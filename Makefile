#thabang sambo
#makefile compilation python

#enviroment
venv:
	virtualenv -p python3 venv 

# Installation from text file
install:
	pip install -r requirements.txt

# Scenario 1
scenario1: 
	. venv/bin/activate; python Scenario1.py

# Scenario 2
scenario2: 
	. venv/bin/activate; python Scenario2.py

# Scenario 3
scenario3: 
	. venv/bin/activate; python Scenario3.py

# Clean
clean:
	rm -rf __pycache__
	rm -rf venv

