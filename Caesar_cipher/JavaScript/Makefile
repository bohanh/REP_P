ifndef FILE
	FILE=Caesar_cipher.js
endif

ifndef TASK
	TASK=Caesar_cipher
endif

compile:
	

measure:
	sudo ../../RAPL/main '/opt/homebrew/bin/node $(TASK).js' JavaScript $(TASK)

run:
	/opt/homebrew/bin/node $(TASK)

mem:
	/usr/bin/time -p /opt/homebrew/bin/node $(TASK)

valgrind:
	valgrind --tool=massif --stacks=yes /opt/homebrew/bin/node $(TASK)

valmem:
	valgrind --tool=massif --stacks=yes  /opt/homebrew/bin/node $(TASK)

clean:
	

