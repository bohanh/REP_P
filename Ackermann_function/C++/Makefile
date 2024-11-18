ifndef FILE
	FILE=Ackermann_function.cpp
endif

ifndef TASK
	TASK=Ackermann_function
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
	valgrind --tool=massif --stacks=yes  ./$(FILE)_run

clean:
	rm -rf *.o *_run

