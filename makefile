# Copyright © 2012-2013 Martin Ueding <dev@martin-ueding.de>

pythonfiles:=$(wildcard *.py */*.py)

all: adium2pidgin.1.gz

html/index.html: $(pythonfiles)
	epydoc -v $^

install:
	./setup.py install --install-layout=deb --prefix="$(DESTDIR)/usr"
	install -d "$(DESTDIR)/usr/share/man/man1"
	install -m 644 adium2pidgin.1.gz -t "$(DESTDIR)/usr/share/man/man1"

%.1: %.1.rst
	rst2man $< $@

%.1.gz: %.1
	gzip $<

.PHONY: clean
clean:
	$(RM) *.1.gz
	$(RM) *.pyc *.pyo
	$(RM) -r build
	$(RM) -r html
