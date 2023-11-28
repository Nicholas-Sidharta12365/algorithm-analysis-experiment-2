# Algorithm Analysis and Design - Assignment 2
#### Nicholas Sidharta - 2106752294

### Description
This Repository is the comparisson of Branch Bound Algorithm and Greedy Algorithm on The Weighted Set Cover Problem. The problem is to find the minimum number of sets that can cover all the elements in the universe. The sets are weighted, and the weight of the solution is the sum of the weights of the sets used. Credits for making the algorithm is given to Andrea Rubbi. The algorithm and dataset generation are both implemented in Python.

### Contents
1. MergeSort.java = The implementation of Merge Sort Algorithm
2. TwoPivotBlockQuickSort.java = The implementation of Two Pivot Block Quick Sort Algorithm
3. ArrayGeneration.java = The implementation of array generation for testing datasets
4. SortBenchmark.java = The implementation of benchmarking runtime process between the two algorithms measured in miliseconds.
5. sorted_{number}.txt = The sorted array of {number} numbers
6. random_{number}.txt = The random array of {number} numbers
7. reverse_{number}.txt = The reverse sorted array of {number} numbers

### How to Run
1. Clone this repository
2. Open the terminal and go to the directory where the repository is cloned
3. Compile the codes using the following command
```
javac *.java
```
4. (Optionally) Generate the datasets using the following command
```
java ArrayGeneration
```
4. Run the benchmark process using the following command
```
java SortBenchmark
```

### Credits
Thank you to Martin Aum¨uller and Nikolaj Hass for the paper and the pseudocode as well as the idea of the two pivot block quick sort algorithm.

### Disclaimer
This repository isn't meant to be somekind of research paper, this is mainly used for educational purposes. The codes are made to be as close as possible to the pseudocode provided by the paper. Any kind of Feedback however is welcomed and appreciated.