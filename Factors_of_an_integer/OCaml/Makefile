ifndef FILE
	FILE=Factors_of_an_integer.ocaml
endif

ifndef TASK
	TASK=Factors_of_an_integer
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
	valgrind --tool=massif --stacks=yes  ./$(FILE)_run

clean:
	rm -rf *.ocaml_run *.cmi *.cmx *.o

