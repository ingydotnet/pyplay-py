default:
	@echo 'No default action for make'

build test install register sdist upload clean::
	python setup.py $@

clean::
	find . -name '*.pyc' | xargs rm
	rm -fr build dist
