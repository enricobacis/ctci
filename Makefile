.PHONY: all clean test

VENV = venv

all test: $(VENV)
	@ $(VENV)/bin/py.test

clean:
	@ rm -rf $(VENV)

$(VENV):
	virtualenv $(VENV)
	$(VENV)/bin/pip install pytest
