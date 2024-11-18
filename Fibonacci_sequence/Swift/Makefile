ifndef FILE
	FILE=Fibonacci_sequence.swift
endif

ifndef TASK
	TASK=Fibonacci_sequence
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

