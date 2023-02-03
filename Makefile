.PHONY: install format lint test sec

install:
	@poetry install
format:
	@blue .
	@isort .
lint:
	@blue --check .
	@isort --check .
	@prospector --with-tool pydocstyle --doc-warning --no-autodetect -i data/
test:
	@pytest -v
sec:
	@pip-audit