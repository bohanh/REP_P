import os
import sys
from subprocess import call, Popen, PIPE

from lazyme.string import color_print

path = '.'
action = 'compile'
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


def formating(s):
    ss = s.split("_")
    for i in range(len(ss)):
        ss[i] = ss[i][0].capitalize() + ss[i][1:]
    return ''.join(ss)


def file_exists(file_path):
    if not file_path:
        return False
    else:
        return os.path.isfile(file_path)


def compile_rapl():
    path_rapl = "./RAPL"
    print(os.path.join(path_rapl, "Makefile"), end="")
    if file_exists(os.path.join(path_rapl, "Makefile")):
        cmd = 'cd ' + path_rapl + '; make compile'
        pipes = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        std_out, std_err = pipes.communicate()

        if pipes.returncode != 0:
            # an error happened!
            err_msg = "%s. Code: %s" % (std_err.strip(), pipes.returncode)
            color_print(' [E] Error on RAPL: ', color='red', bold=True)
            print(err_msg)
        elif len(std_err):
            # return code is 0 (no error), but we may want to
            # do something with the info on std_err
            # i.e. logger.warning(std_err)
            color_print(' [OK]', color='green')
        else:
            color_print(' [OK]', color='green')

        call(['sleep', '1'])


def main():
    if (action == 'compile') | (action == 'run'):
        print(" " * 27, end="")
        for language in languages:
            print(language.ljust(12), end="")
    for task in tasks:
        task_path = os.path.join(path, formating(task))
        if (action == 'compile') | (action == 'run') | (action == 'measure'):
            print("\n" + task.replace("_", " ").ljust(27), end="")
        for language in languages:
            root = os.path.join(task_path, language)
            makefile = os.path.join(root, 'Makefile')
            if file_exists(makefile):
                cmd = 'cd ' + root + '; make ' + action
                # cmd = 'ls -la'
                pipes = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
                std_out, std_err = pipes.communicate()

                if (action == 'compile') | (action == 'run') | (action == 'measure'):
                    if pipes.returncode != 0:
                        # an error happened!
                        err_msg = "%s. Code: %s" % (std_err.strip(), pipes.returncode)
                        color_print('[Error]', color='red', bold=True)
                        # print(err_msg)
                    elif len(std_err):
                        # return code is 0 (no error), but we may want to
                        # do something with the info on std_err
                        # i.e. logger.warning(std_err)
                        color_print('[OK]'.ljust(12), color='green', end="")
                    else:
                        color_print('[OK]'.ljust(12), color='green', end="")
                if action == 'measure':
                    call(['sleep', '1'])
    color_print("\nAction \"" + action + "\" completed", color='green', bold=True)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        act = sys.argv[1]
        if (act == 'compile') | (act == 'run') | (act == 'clean') | (act == 'measure'):
            color_print('Performing \"' + act + '\" action...', color='yellow', bold=True)
            action = act
            if act == 'compile':
                compile_rapl()
        else:
            color_print('Error: Unrecognized action \"' + act + '\"', color='red')
            sys.exit(1)
    else:
        color_print('Performing \"compile\" action...', color='yellow', bold=True)
        action = 'compile'
        compile_rapl()

    main()
