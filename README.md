#RTGraph

A python programme developed for the online display of a cosmic ray detector.
The detector itself is read out by some specific electronics and c++ software which output the data to its std::cout.
The standard output is redirected to the pipe of the python RTGraph which processes, analyzes and displays the data .


This code is a fork of https://github.com/ssepulveda/RTGraph.

## Operation
The program reads the standard output of the specified script. It expects the format:
[event number]\t[timestamp (int)]\t[val 0]\t... [val 511]\t

Each line represents a series of acquired values. These values are represented as a 2D matrix using reshape()
The graphs displayed are the 2D view of the event (+3D view in the branch "OpenDays2016" but not buggfree version), angular distribution of the muons, frequency of events and signal integration mode.

## Interface
The user interface includes a command window where all the detector parameters and the display modes can be set.
A live window allows to monitor event in real time whereas a saved windows can retrieve a measurement taken in the past. An auto window displays the different graphs one after the other (not that this makes the display quite slow).

##Dependencies
- Python 3 (3.4 or later).
- Numpy, multiprocessing, subprocess, signal, time, os, sys, platform, itertools, math, yaml, csv, select, functools, logging, argparse, 
- PyQt4.
- PyQtGraph

###Manual Installing

##Usage
This software is an extended version of some simplest tools developed: Please read the lines below.

The project is distributed under MIT License. A DOI is attached to the project for citations.

Link to the the source repository documentation:
[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.12789.svg)](http://dx.doi.org/10.5281/zenodo.12789)
