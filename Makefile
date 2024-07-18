.PHONY: all
all: environment code_style run

.PHONY: environment
environment:
	python3 -m venv btc_map_extraction
	btc_map_extraction/bin/pip install --upgrade pip
	btc_map_extraction/bin/pip install black isort
	btc_map_extraction/bin/pip install -r requirements.txt

.PHONY: code_style
code_style:
	btc_map_extraction/bin/black --exclude '/(venv|env|build|dist|btc_map_extraction)/' .
	btc_map_extraction/bin/isort . --skip venv --skip env --skip btc_map_extraction

.PHONY: data_extraction
data_extraction:
	btc_map_extraction/bin/python main.py

.PHONY: run
run:
	shiny run shiny_app/app.py

.PHONY: build_shinylive
build_shinylive:
	shinylive export shiny_app docs
	python3 -m http.server --directory docs --bind localhost 8080

.PHONY: clean
clean:
	rm -rf btc_map_extraction
	find . -name '*.pyc' -delete

.PHONY: clear
clear: clean
	btc_map_extraction/bin/pip uninstall -y -r requirements.txt