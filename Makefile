env = .venv/bin/
debug:
	.venv/bin/uvicorn main:app --reload
init:
	python3 -m venv .venv
	$(env)pip3 install --upgrade wheel pip
	$(env)pip3 install -r requirements.txt


freeze:
	$(env)pip3 freeze > requirements.txt
lint:
	$(env)black .
