VENV = venv
ACTIVATE = $(VENV)/bin/activate
DEV_PACKAGES = ipython pycodestyle flake8 coverage tox \
  factory-boy # factory-boy is in setup.py, but is not getting loaded

$(VENV): Makefile
	@pip install virtualenv
	@rm -rf $(VENV)
	@virtualenv -p `which python3` $@
	@touch $(ACTIVATE)
	@. $(ACTIVATE) ; \
	  pip install -r requirements.txt; \
	  pip install $(DEV_PACKAGES)

clean:
	rm -rf $(VENV)
