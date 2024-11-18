ifndef FILE
	FILE=Remove_duplicate_elements.py
endif

ifndef TASK
	TASK=Remove_duplicate_elements
endif

compile:
	

measure:
	sudo ../../RAPL/main '/opt/anaconda3/bin/python -OO $(TASK).py' Python $(TASK)

run:
	/opt/anaconda3/bin/python -OO $(TASK).py

mem:
	/usr/bin/time -p /opt/anaconda3/bin/python -OO $(TASK).py

valgrind:
	valgrind --tool=massif --stacks=yes /opt/anaconda3/bin/python -OO $(TASK).py

valmem:
	valgrind --tool=massif --stacks=yes  /opt/anaconda3/bin/python -OO $(TASK).py

clean:
	

