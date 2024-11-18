ifndef FILE
	FILE=Guess_the_number.java
endif

ifndef TASK
	TASK=Guess_the_number
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

