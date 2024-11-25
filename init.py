import os

tasks = [
    "ABC_Problem",
    "Caesar_cipher",
    "Factorial",
    "Factors_of_an_integer",
    "Fibonacci_sequence",
    "Greatest_common_divisor",
    "Least_common_multiple",
    "Remove_duplicate_elements",
    "Sieve_of_Eratosthenes"
]

languages = [
    "C++",
    "Go",
    "Java",
    "JavaScript",
    "OCaml",
    "Python"
]

suffix = {
    "C++": "cpp",
    "Go": "go",
    "Java": "java",
    "JavaScript": "js",
    "OCaml": "ocaml",
    "Python": "py",
}

source = {
    "time": "/usr/bin/time -p",
    "gcc": "/usr/bin/g++",
    "go": "go",
    "java": "/usr/bin/java",
    "javac": "/usr/bin/javac",
    "javascript": "node",
    "python": "python3"
}

makefiles_const_prefix = {
    "mem": f"{source['time']} ",
    "valgrind": "valgrind --tool=massif --stacks=yes ",
    "valmem": "valgrind --tool=massif --stacks=yes ",
}
makefiles = {
    "C++": {
        "compile": f"{source['gcc']} -c -pipe -O3 -fomit-frame-pointer -march=native -std=c++14 -I/usr/include/apr-1.0 $(FILE) -o $(FILE).o &&  {source['gcc']} $(FILE).o -o $(FILE)_run -lapr-1",
        "measure": "sudo ../../RAPL/main './$(FILE)_run' C++ $(TASK)",
        "run": "./$(FILE)_run",
        "clean": "rm -rf *.o *_run"
    },
    "Go": {
        "compile": f"{source['go']} build -o $(FILE)_run $(FILE)",
        "measure": "sudo ../../RAPL/main './$(FILE)_run' Go $(TASK)",
        "run": "./$(FILE)_run",
        "clean": "rm -rf *.go_run"
    },
    "Java": {
        "compile": f"{source['javac']} -d . $(TASK).java",
        "measure": f"sudo ../../RAPL/main '{source['java']} $(TASK)' Java $(TASK)",
        "run": f"{source['java']} $(TASK)",
        "clean": "rm *.class"
    },
    "JavaScript": {
        "compile": "",
        "measure": f"sudo ../../RAPL/main '{source['javascript']} $(TASK).js' JavaScript $(TASK)",
        "run": f"{source['javascript']} $(TASK)",
        "clean": ""
    },
    "OCaml": {
        "compile": "cp $(FILE) $(TASK).ml\n\t"
                   "ocamlopt -noassert -unsafe -nodynlink -inline 100 unix.cmxa $(TASK).ml -o $(FILE)_run\n\t"
                   "rm $(TASK).ml",
        "measure": "sudo ../../RAPL/main './$(FILE)_run' OCaml $(TASK)",
        "run": "./$(FILE)_run",
        "clean": "rm -rf *.ocaml_run *.cmi *.cmx *.o"
    },
    "Python": {
        "compile": "",
        "measure": f"sudo ../../RAPL/main '{source['python']} -OO $(TASK).py' Python $(TASK)",
        "run": f"{source['python']} -OO $(TASK).py",
        "clean": ""
    },
}

make_folder = "./makes_languages"


def formating(s):
    ss = s.split("_")
    for i in range(len(ss)):
        ss[i] = ss[i][0].capitalize() + ss[i][1:]
    return ''.join(ss)


def main():
    for task in tasks:
        print("Task:", task)
        task_mod = formating(task)
        if not os.path.exists(task_mod):
            os.makedirs(task_mod)
        for language in languages:
            if not os.path.exists(os.path.join(task_mod, language)):
                os.makedirs(os.path.join(task_mod, language))
            makefile = os.path.join(task_mod, language, "Makefile")
            code = os.path.join(task_mod, language, f"{task_mod}.{suffix[language]}")
            with open(makefile, "w") as file:
                file.write(f"ifndef FILE\n\tFILE={task_mod}.{suffix[language]}\nendif\n\n")
                file.write(f"ifndef TASK\n\tTASK={task_mod}\nendif\n\n")
                file.write(f"compile:\n\t{makefiles[language]['compile']}\n\n")
                file.write(f"measure:\n\t{makefiles[language]['measure']}\n\n")
                file.write(f"run:\n\t{makefiles[language]['run']}\n\n")
                file.write(f"mem:\n\t{makefiles_const_prefix['mem']}{makefiles[language]['run']}\n\n")
                file.write(f"valgrind:\n\t{makefiles_const_prefix['valgrind']}{makefiles[language]['run']}\n\n")
                file.write(f"valmem:\n\t{makefiles_const_prefix['valmem']}{makefiles[language]['run']}\n\n")
                file.write(f"clean:\n\t{makefiles[language]['clean']}\n\n")
            with open(code, "w"):
                pass


if __name__ == '__main__':
    main()
