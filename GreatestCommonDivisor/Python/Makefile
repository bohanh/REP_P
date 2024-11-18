ifeq ($(shell uname), Linux)
	GO = /usr/local/go/bin/go
	NODE = /home/kirito/.nvm/versions/node/v18.16.0/bin/node
	PYTHON = /usr/bin/python3
else ifeq ($(shell uname), Darwin)
	GO = /opt/homebrew/bin/go
	NODE = /opt/homebrew/bin/node
	PYTHON = /opt/anaconda3/bin/python
else
	GO = 
	NODE = 
	PYTHON = 
endif

ifndef FILE
	FILE=GreatestCommonDivisor.py
endif

ifndef TASK
	TASK=GreatestCommonDivisor
endif

compile:
	

measure:
	sudo ../../RAPL/main '$(PYTHON) -OO $(TASK).py' Python $(TASK)

run:
	$(PYTHON) -OO $(TASK).py

mem:
	/usr/bin/time -p $(PYTHON) -OO $(TASK).py

valgrind:
	valgrind --tool=massif --stacks=yes $(PYTHON) -OO $(TASK).py

valmem:
	valgrind --tool=massif --stacks=yes $(PYTHON) -OO $(TASK).py

clean:
	

