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
	FILE=Factorial.cpp
endif

ifndef TASK
	TASK=Factorial
endif

compile:
	/usr/bin/g++ -c -pipe -O3 -fomit-frame-pointer -march=native -std=c++14 -I/usr/include/apr-1.0 $(FILE) -o $(FILE).o &&  /usr/bin/g++ $(FILE).o -o $(FILE)_run -lapr-1

measure:
	sudo ../../RAPL/main './$(FILE)_run' C++ $(TASK)

run:
	./$(FILE)_run

mem:
	/usr/bin/time -p ./$(FILE)_run

valgrind:
	valgrind --tool=massif --stacks=yes ./$(FILE)_run

valmem:
	valgrind --tool=massif --stacks=yes ./$(FILE)_run

clean:
	rm -rf *.o *_run

