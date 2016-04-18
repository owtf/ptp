default:
	@echo "'make install'" for installation
	@echo "'make check'" for tests

install:
	python ./setup.py install

check:
	nosetests -v -d --with-coverage --cover-package=ptp
