.PHONY: start topics list verify doctor

PL = venc/bin/pythonlings --root python_practice

start:
	$(PL)

topics:
	$(PL) topics

list:
	$(PL) list

verify:
	$(PL) verify

doctor:
	$(PL) doctor
