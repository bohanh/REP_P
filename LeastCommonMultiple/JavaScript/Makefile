ifndef FILE
	FILE=LeastCommonMultiple.js
endif

ifndef TASK
	TASK=LeastCommonMultiple
endif

compile:
	

measure:
	sudo ../../RAPL/main 'node $(TASK).js' JavaScript $(TASK)

run:
	node $(TASK)

mem:
	/usr/bin/time -p node $(TASK)

valgrind:
	valgrind --tool=massif --stacks=yes node $(TASK)

valmem:
	valgrind --tool=massif --stacks=yes node $(TASK)

clean:
	

