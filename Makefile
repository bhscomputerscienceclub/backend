env = .venv/bin/
debug:
	.venv/bin/uvicorn main:app --reload
init:
	python -m venv .env
	$(env)pip install -r requirements.txt
	$(env)pip install --upgrade wheel pip

freeze:
	$(env)pip freeze > requirements.txt
	
