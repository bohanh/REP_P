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
	FILE=CaesarCipher.go
endif

ifndef TASK
	TASK=CaesarCipher
endif

compile:
	$(GO) build -o $(FILE)_run $(FILE)

measure:
	sudo ../../RAPL/main './$(FILE)_run' Go $(TASK)

run:
	./$(FILE)_run

mem:
	/usr/bin/time -p ./$(FILE)_run

valgrind:
	valgrind --tool=massif --stacks=yes ./$(FILE)_run

valmem:
	valgrind --tool=massif --stacks=yes ./$(FILE)_run

clean:
	rm -rf *.go_run

