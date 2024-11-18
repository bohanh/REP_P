import os

tasks = [
    "ABC_Problem",
    "Arithmetic-geometric_mean",
    "Caesar_cipher",
    "Factors_of_an_integer",
    "Greatest_common_divisor",
    "Guess_the_number",
    "Remove_duplicate_elements",
    "Sieve_of_Eratosthenes",
    "Sorting_algorithms--Quicksort",
    "Towers_of_Hanoi"
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
    "Swift": "swift"
}

source = {
    "time": "/usr/bin/time -p",
    "gcc": "/usr/bin/g++",
    "go": "/opt/homebrew/bin/go",
    "java": "/usr/bin/javac",
    "javascript": "/opt/homebrew/bin/node",
    "python": "/opt/anaconda3/bin/python",
    "swift": "/usr/bin/swiftc"
}

makefiles_const_prefix = {
    "mem": f"{source['time']} ",
    "valgrind": "valgrind --tool=massif --stacks=yes ",
    "valmem": "valgrind --tool=massif --stacks=yes  ",
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
        "compile": f"{source['java']} -d . $(TASK).java",
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
    "Swift": {
        "compile": f"{source['swift']} $(FILE) -Ounchecked -whole-module-optimization -I Include/swift/apr -o $(FILE)_run",
        "measure": "sudo ../../RAPL/main './$(FILE)_run' Swift $(TASK)",
        "run": "./$(FILE)_run",
        "clean": "rm -rf *_run"
    },
}

make_folder = "./makes_languages"


def main():
    for folder in tasks:
        print("Task:", folder)
        if not os.path.exists(folder):
            os.makedirs(folder)
        for language in languages:
            if not os.path.exists(os.path.join(folder, language)):
                os.makedirs(os.path.join(folder, language))
            makefile = os.path.join(folder, language, "Makefile")
            code = os.path.join(folder, language, f"{folder}.{suffix[language]}")
            with open(makefile, "w") as file:
                file.write(f"ifndef FILE\n\tFILE={folder}.{suffix[language]}\nendif\n\n"
                           f"ifndef TASK\n\tTASK={folder}\nendif\n\n"
                           f"compile:\n\t{makefiles[language]['compile']}\n\n"
                           f"measure:\n\t{makefiles[language]['measure']}\n\n"
                           f"run:\n\t{makefiles[language]['run']}\n\n"
                           f"mem:\n\t{makefiles_const_prefix['mem']}{makefiles[language]['run']}\n\n"
                           f"valgrind:\n\t{makefiles_const_prefix['valgrind']}{makefiles[language]['run']}\n\n"
                           f"valmem:\n\t{makefiles_const_prefix['valmem']}{makefiles[language]['run']}\n\n"
                           f"clean:\n\t{makefiles[language]['clean']}\n\n")
            with open(code, "w"):
                pass


if __name__ == '__main__':
    main()
