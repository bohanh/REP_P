ifndef FILE
	FILE=LeastCommonMultiple.java
endif

ifndef TASK
	TASK=LeastCommonMultiple
endif

compile:
	/usr/bin/javac -d . $(TASK).java

measure:
	sudo ../../RAPL/main '/usr/bin/javac $(TASK)' Java $(TASK)

run:
	/usr/bin/java $(TASK)

mem:
	/usr/bin/time -p /usr/bin/java $(TASK)

valgrind:
	valgrind --tool=massif --stacks=yes /usr/bin/java $(TASK)

valmem:
	valgrind --tool=massif --stacks=yes /usr/bin/java $(TASK)

clean:
	rm *.class

