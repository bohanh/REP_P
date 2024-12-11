# Energy Efficiency in Programming Languages
## Introduction
The project aims to analyse the energy efficiency of different programming languages by using codes from [Rosetta Code](https://rosettacode.org/wiki/Rosetta_Code) and analyse the energy consumption of CPU, GPU, and DRAM, as well as runtime.
## Reproducibility
### How to Reproduce the Results
#### **1. Requirements**
The project supports two operating systems, Linux (Ubuntu) and macOS.
The Docker environment will be set up in Ubuntu.
- Dependencies
  - Linux
    - C++ : GCC 11.4.0
    - Go : go 1.18.1
    - Java : OpenJDK 21
    - Javac : javac 21
    - JavaScript : node 18.16.0
    - OCaml : ocamlopt 4.13.1
    - Python : python3 3.10.12
#### **2. Setting Up the Environment**  
- Use the following instructions to create a reproducible environment with Dockerfile:  
    ```bash
    docker build -t reproducible-project .
    docker run -it reproducible-project
    ```
- For non x86-64 (AMD) architecture, run instead:
  ```bash
  docker build --platform linux/amd64 -t ubuntu-dev-environment .
  docker run -it reproducible-project
  ```

#### **3. Reproducing Results**  
   - To generate the necessary csv files contain the results, run:
     ```bash
     python3 compile_all.py compile
     python3 compile_all.py measure
     python3 compile_all.py clean
     
     python3 analyse.py
     ```
   - To analyse the results, run:
     ```bash
     python3 analyse_data.py
     ```

#### **4. Automation (Bonus)**  
   - Github workflow will execute analyse_data.py script automatically,which will produce the summary of efficiency of each language we used in all the cases.
   - Produce a graph of each case in folder "output_graphs"
    
### Encountered Issues and Improvements
- Report any challenges, errors, or deviations from the original study.
- Describe how these issues were resolved or improved, if applicable.

### Is the Original Study Reproducible?

## Replicability
### Variability Factors
- **List of Factors**:
  | Variability Factor | Possible Values     | Relevance                                   |
  |--------------------|---------------------|--------------------------------------------|
  | Hardware           | CPU, GPU (NVIDIA)  | Different computation time and results  |
  | Architect          | DRAM,CPU-only machine| The energy consumed is certainly different|
- | Operating system   | linux,windows       |Different system have different results |

- **Constraints Across Factors**:  
  - Document any constraints or interdependencies among variability factors.  
    For example:
    - Random Seed must align with dataset splits for consistent results.
    - Hardware constraints may limit the choice of GPU-based factors.

- **Exploring Variability Factors via CLI (Bonus)**  
   - Provide instructions to use the command-line interface (CLI) to explore variability factors and their combinations:  
     ```bash
     python explore_variability.py --random-seed 42 --hardware GPU --dataset-version v1.1
     ```
   - Describe the functionality and parameters of the CLI:
     - `--random-seed`: Specify the random seed to use.
     - `--hardware`: Choose between CPU or GPU.
     - `--dataset-version`: Select the dataset version.


### Replication Execution
#### **1. Instructions**  
   - Provide detailed steps or commands for running the replication(s):  
     ```bash
     bash scripts/replicate_experiment.sh
     ```

#### **2. Presentation and Analysis of Results**  
   - Include results in text, tables, or figures.
   - Analyze and compare with the original study's findings.

### Does It Confirm the Original Study?
- Summarize the extent to which the replication supports the original study’s conclusions.
- Highlight similarities and differences, if any.

## Conclusion
- Recap findings from the reproducibility and replicability sections.
- Discuss limitations of your
