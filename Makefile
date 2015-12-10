help:
	@echo "clean            clean"

clean: clean-build clean-pyc
	@rm -fr cover/

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

clean-pyc:
	@find . -type f -name '*.pyc' -delete
	@find . -type f -name '*.pyo' -delete
	@find . -type f -name '*~' -delete
	@find . -type f -name '*,cover' -delete
