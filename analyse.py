import os

import pandas as pd
#test
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


for task in tasks:
    result = pd.DataFrame(columns=['Language', 'CPU', 'GPU', 'DRAM', 'Time'])
    for language in languages:
        csv = os.path.join("./results", formating(task), language + ".csv")
        df = pd.read_csv(csv)
        df.columns = [col.strip().split(' ')[0].replace('?', '') for col in df.columns]
        if df['GPU'].isna:
            df.drop(columns=['GPU'], inplace=True)
        if df['DRAM'].isna:
            df.drop(columns=['DRAM'], inplace=True)
        df_dict = df.mean().to_dict()
        df_dict['Language'] = language
        result.loc[len(result)] = df_dict
    result.to_csv("./results/" + formating(task) + ".csv", index=False)
