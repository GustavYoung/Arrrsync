.PHONY: default, dev-install, upload

default: dev-install

dev-install:
	sudo python setup.py develop

install:
	sudo python setup.py install

clean:
	sudo rm -rf dist
	sudo rm -rf build
	sudo rm -rf arrrsync.egg-info

dist:
	sudo python setup.py sdist --formats=gztar,zip

upload: clean dist
	twine upload dist/*

register: clean dist
	twine register dist/*
