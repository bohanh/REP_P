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
	FILE=ABCProblem.js
endif

ifndef TASK
	TASK=ABCProblem
endif

compile:
	

measure:
	sudo ../../RAPL/main '$(NODE) $(TASK).js' JavaScript $(TASK)

run:
	$(NODE) $(TASK)

mem:
	/usr/bin/time -p $(NODE) $(TASK)

valgrind:
	valgrind --tool=massif --stacks=yes $(NODE) $(TASK)

valmem:
	valgrind --tool=massif --stacks=yes $(NODE) $(TASK)

clean:
	

