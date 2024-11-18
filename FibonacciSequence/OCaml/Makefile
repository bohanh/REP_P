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
	FILE=FibonacciSequence.ocaml
endif

ifndef TASK
	TASK=FibonacciSequence
endif

compile:
	cp $(FILE) $(TASK).ml
	ocamlopt -noassert -unsafe -nodynlink -inline 100 unix.cmxa $(TASK).ml -o $(FILE)_run
	rm $(TASK).ml

measure:
	sudo ../../RAPL/main './$(FILE)_run' OCaml $(TASK)

run:
	./$(FILE)_run

mem:
	/usr/bin/time -p ./$(FILE)_run

valgrind:
	valgrind --tool=massif --stacks=yes ./$(FILE)_run

valmem:
	valgrind --tool=massif --stacks=yes ./$(FILE)_run

clean:
	rm -rf *.ocaml_run *.cmi *.cmx *.o

