install:
	python3 -m pip install -r requirements.txt
	pip install sqlite3
install_as_pkg:
	python3 -m pip install -e .
run:
	python3 main.py
