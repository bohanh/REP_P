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
	FILE=SieveOfEratosthenes.java
endif

ifndef TASK
	TASK=SieveOfEratosthenes
endif

compile:
	/usr/bin/javac -d . $(TASK).java

measure:
	sudo ../../RAPL/main '/usr/bin/javac $(TASK)' Java $(TASK)

run:
	/usr/bin/javac $(TASK)

mem:
	/usr/bin/time -p /usr/bin/javac $(TASK)

valgrind:
	valgrind --tool=massif --stacks=yes /usr/bin/javac $(TASK)

valmem:
	valgrind --tool=massif --stacks=yes /usr/bin/javac $(TASK)

clean:
	rm *.class

