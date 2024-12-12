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

#### **4. Automation**
   The data produced by the project is stored in ```/results``` and ```/output_graphs```. This process is automated by github actions ***Run project*** and ***Run data analysis***.
    
### Encountered Issues and Improvements
- In the original Git, results contain an extra column of data, in the form of: 
  ```
  Language, Task, CPU, GPU, ?, DRAM, Time
  ```
  The extra column contains mostly empty data (0.000...), we choose to therefore simply ignore this column. 
- Requiring a dedicative GPU for the hardware, the ```GPU and DRAM``` columns are empty in our results.

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
We have encountered several compile errors when using the original code.The original project framework will execute all the
fisher in folder and conserve these who can run successfully. We have modified the framework adding task attributes to
adjust the task we want to execute in case of replication.
A notebook file to run paper replication
replicate/result.ipynb

#### **2. Presentation and Analysis of Results**
We have output all the experiment data to the folder replicate for 7 tasks we have chosen. The graph illustrate the data
comparison.Time-o and cpu-o stands for the original data in the paper.

### Does It Confirm the Original Study?
-We have obtained a non consistency difference in different case. In general, the algo using go and javascript takes
much shorter time and less energy in our machine.c++ and java shows confirm the original study in all the cases. Ocaml and
python has a same results as original study in most tasks.

## Conclusion
The study aimed to evaluate the energy efficiency of various programming languages based on runtime and energy consumption of CPU, GPU, and DRAM. Using a reproducible Docker-based framework, we replicated the original study, applied necessary adjustments, and analyzed the results.

Reproducibility Challenges:

Compile errors in the original code required modifications to the framework, specifically adding task attributes to ensure smooth execution. These changes allowed us to focus on successfully replicating selected tasks.
Incomplete data in GPU and DRAM columns resulted from hardware constraints, which limited our ability to fully analyze energy efficiency for those metrics.
Results and Analysis:

Data was output to the replicate folder for seven selected tasks. Comparisons between original study data (Time-o, CPU-o) and our results were visualized through graphs.
Consistency of Results:
Go and JavaScript exhibited significantly improved runtime and energy efficiency on our hardware compared to the original study. This discrepancy may stem from advancements in modern runtime optimizations.
C++ and Java results consistently confirmed the findings of the original study, highlighting their stable and predictable performance across platforms.
OCaml and Python showed results consistent with the original study in most tasks, with occasional variations possibly due to hardware differences or dependency versions.
Implications:
The replication revealed both the strengths and limitations of the original study. While most results were reproducible, modern hardware and software advancements can introduce variability in outcomes. This underscores the need for continuous re-evaluation of empirical studies in rapidly evolving technological landscapes.

General Observations:

Energy Efficiency Trends: Languages like Go and JavaScript may be better suited for energy-efficient applications on modern hardware. On the other hand, C++ and Java remain reliable choices for consistent performance.
Framework Improvements: Adding task attributes to the framework enhanced its flexibility and allowed for better control in task replication.
