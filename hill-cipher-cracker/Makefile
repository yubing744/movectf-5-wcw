.PHONY: install-deps crack

PWD := $(shell pwd)

install-deps:
	sudo apt-get install  sagemath sagemath-doc-en sagemath-jupyter

crack:
	docker run -it -v ${PWD}:/workspace sagemath/sagemath:8.9 sage /workspace/cribdrag.sage