# Energy Efficiency in Programming Languages
## Introduction

## Reproducibility
### How to Reproduce the Results
#### **1. Requirements**
The project supports two operating systems, Linux (Ubuntu) and macOS.
The Docker environment will be set up in Ubuntu.
- Dependencies
  - Linux
    - C++ : GCC 11.4.0
    - Go : go 1.18.1
    - Java : OpenJDK 21.0.5
    - Javac : javac 21.0.5
    - JavaScript : node 18.16.0
    - OCaml : ocamlopt 4.13.1
    - Python : python3 3.10.12
#### **2. Setting Up the Environment**  
   - Provide instructions for using the Dockerfile to create a reproducible environment:  
     ```bash
     FROM ubuntu:22.04
     ENV DEBIAN_FRONTEND=noninteractive
     
     RUN apt-get update && apt-get install -y gcc-11 g++-11 && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 100 && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-11 100
     

     docker build -t reproducible-project .
     docker run -it reproducible-project
     ```

#### **3. Reproducing Results**  
   - Describe how to run the automated scripts or notebooks to reproduce data and analyze results:
     ```bash
     bash scripts/run_analysis.sh
     ```
   - Mention Jupyter notebooks (if applicable):  
     Open `notebooks/reproduce_results.ipynb` to execute the analysis step-by-step.

#### **4. Automation (Bonus)**  
   - Explain the included GitHub Action that produces or analyzes data automatically.  
    
### Encountered Issues and Improvements
- Report any challenges, errors, or deviations from the original study.
- Describe how these issues were resolved or improved, if applicable.

### Is the Original Study Reproducible?

## Replicability
### Variability Factors
- **List of Factors**: Identify all potential sources of variability (e.g., dataset splits, random seeds, hardware).  
  Example table:
  | Variability Factor | Possible Values     | Relevance                                   |
  |--------------------|---------------------|--------------------------------------------|
  | Random Seed        | [0, 42, 123]       | Impacts consistency of random processes    |
  | Hardware           | CPU, GPU (NVIDIA)  | May affect computation time and results    |
  | Dataset Version    | v1.0, v1.1         | Ensures comparability across experiments   |

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
