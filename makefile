# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

pythonfiles:=$(wildcard *.py */*.py)

html/index.html: $(pythonfiles)
	epydoc -v $^

.PHONY: clean
clean:
	$(RM) *.pyc *.pyo
	$(RM) -r html
