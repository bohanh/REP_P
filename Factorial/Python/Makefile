ifndef FILE
	FILE=Factorial.py
endif

ifndef TASK
	TASK=Factorial
endif

compile:
	

measure:
	sudo ../../RAPL/main 'python3 -OO $(TASK).py' Python $(TASK)

run:
	python3 -OO $(TASK).py

mem:
	/usr/bin/time -p python3 -OO $(TASK).py

valgrind:
	valgrind --tool=massif --stacks=yes python3 -OO $(TASK).py

valmem:
	valgrind --tool=massif --stacks=yes python3 -OO $(TASK).py

clean:
	

