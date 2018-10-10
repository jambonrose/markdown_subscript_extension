.PHONY: all check clean dist release test

all:
	@echo 'Available Commands:'
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null \
		| awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' \
		| sort \
		| egrep -v -e '^[^[:alnum:]]' -e '^$@$$' \
		| xargs -I {} echo '    {}'

check:
	python setup.py check

clean:
	rm -rf *.egg-info
	rm -rf .coverage
	rm -rf .eggs
	rm -rf .pytest_cache
	rm -rf .tox
	rm -rf build
	rm -rf dist
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

dist:
	python setup.py sdist --formats=gztar bdist_wheel

release:
	twine upload dist/*

test:
	python setup.py test
