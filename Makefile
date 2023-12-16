RPYTHON ?= pypy/rpython/bin/rpython
RPYTHON_ARGS ?= -O2

all: targetkruntest-c

targetkruntest-c: rpython_krun/targetkruntest.py
	$(RPYTHON) $(RPYTHON_ARGS) $<

clean:
	$(RM) targetkruntest-c
