ifndef FILE
	FILE=N-queens_problem.java
endif

ifndef TASK
	TASK=N-queens_problem
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
	valgrind --tool=massif --stacks=yes  /usr/bin/javac $(TASK)

clean:
	rm *.class

