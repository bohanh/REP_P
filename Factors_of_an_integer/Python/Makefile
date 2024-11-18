ifndef FILE
	FILE=Factors_of_an_integer.py
endif

ifndef TASK
	TASK=Factors_of_an_integer
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
	

