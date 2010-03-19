default:
	@echo 'No default action for make'

build test install sdist clean::
	python setup.py $@

clean::
	find . -name *.pyc | xargs rm
	rm -fr build dist

