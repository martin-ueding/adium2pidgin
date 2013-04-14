# Copyright © 2012-2013 Martin Ueding <dev@martin-ueding.de>

###############################################################################
#                                   License                                   #
###############################################################################
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.

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
	$(RM) *.pyc *.pyo
	$(RM) -r build
	$(RM) -r html
