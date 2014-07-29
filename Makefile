.PHONY: test description check dist release clean

test:
	nosetests --with-coverage --cover-package=mdx_subscript

description:
	rst2html.py DESCRIPTION.rst > description.html

check:
	python setup.py check

dist:
	python setup.py sdist --formats=gztar,zip bdist_wheel
	gpg --armor --detach-sign -u 5878672C -a dist/MarkdownSubscript*.whl
	gpg --armor --detach-sign -u 5878672C -a dist/MarkdownSubscript*.tar.gz
	gpg --armor --detach-sign -u 5878672C -a dist/MarkdownSubscript*.zip

release:
	twine upload dist/*

clean:
	rm -rf __pycache__
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
