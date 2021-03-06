env = .venv/bin/
debug:
	.venv/bin/uvicorn main:app --reload
init:
	python -m venv .venv
	$(env)pip install -r requirements.txt
	$(env)pip install --upgrade wheel pip

freeze:
	$(env)pip freeze > requirements.txt
lint:
	$(env)black .
