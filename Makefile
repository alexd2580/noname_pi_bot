default: venv

.PHONY: venv
venv:
	env
	python3 -m venv venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -r requirements.txt -r dev-requirements.txt --upgrade --no-cache-dir
