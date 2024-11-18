ifndef FILE
	FILE=Arithmetic-geometric_mean.go
endif

ifndef TASK
	TASK=Arithmetic-geometric_mean
endif

compile:
	/opt/homebrew/bin/go build -o $(FILE)_run $(FILE)

measure:
	sudo ../../RAPL/main './$(FILE)_run' Go $(TASK)

run:
	./$(FILE)_run

mem:
	/usr/bin/time -p ./$(FILE)_run

valgrind:
	valgrind --tool=massif --stacks=yes ./$(FILE)_run

valmem:
	valgrind --tool=massif --stacks=yes  ./$(FILE)_run

clean:
	rm -rf *.go_run

