ifndef FILE
	FILE=SieveOfEratosthenes.py
endif

ifndef TASK
	TASK=SieveOfEratosthenes
endif

compile:
	

measure:
	sudo -S ../../RAPL/main 'python3 -OO $(TASK).py' Python $(TASK)

run:
	python3 -OO $(TASK).py

mem:
	/usr/bin/time -p python3 -OO $(TASK).py

valgrind:
	valgrind --tool=massif --stacks=yes python3 -OO $(TASK).py

valmem:
	valgrind --tool=massif --stacks=yes python3 -OO $(TASK).py

clean:
	

