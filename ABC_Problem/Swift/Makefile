ifndef FILE
	FILE=ABC_Problem.swift
endif

ifndef TASK
	TASK=ABC_Problem
endif

compile:
	/usr/bin/swiftc $(FILE) -Ounchecked -whole-module-optimization -I Include/swift/apr -o $(FILE)_run

measure:
	sudo ../../RAPL/main './$(FILE)_run' Swift $(TASK)

run:
	./$(FILE)_run

mem:
	/usr/bin/time -p ./$(FILE)_run

valgrind:
	valgrind --tool=massif --stacks=yes ./$(FILE)_run

valmem:
	valgrind --tool=massif --stacks=yes  ./$(FILE)_run

clean:
	rm -rf *_run

