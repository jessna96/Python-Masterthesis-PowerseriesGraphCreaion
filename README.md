# Python-Powerseries-Graph-Creation
Python script for the creation of a power series graph for the analysis of angular resolved spectroscopy measurement data.

## Description
The script creates a plot with the photoluminescence intensity, linewith and energy shift as a function of the excitation power. 
The sample data shows the necessary structure of the input data. Each row corresponds to a data point with the value of the excitation power, a comma
and the value of the intensity (arb. u.), linewith (eV) and energetic position (eV). 

## Example graph

<img width="500" alt="image" src="https://user-images.githubusercontent.com/35634254/189532544-ceae704b-aa7a-4add-bf99-f1e4539472e6.png">

## Excecution of the script

The following components must be installed locally:

- [python](https://www.python.org/downloads/) v3.9.7
- matplotlib, for example by typing:
```console
$ python -m pip install matplotlib
```

To run the project with the sample files locally, first change the path to where the python script is located in line 24:

<img width="521" alt="image" src="https://user-images.githubusercontent.com/35634254/189535415-68795e53-9922-4bd4-b37a-c0afde7fc42b.png">

(in case of Windows also change / to \\ \\, for macOS just leave it like this)

and then enter the following in Commandline / Bash:

```console
$ git clone https://github.com/jessna96/Python-Powerseries-Graph-Creation.git
$ cd Python-Powerseries-Graph-Creation
$ python PowerseriesGraphCreation_Masterthesis.py
```
