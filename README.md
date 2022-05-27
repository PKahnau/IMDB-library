# IMDB-library
Short programme that interacts with actor and movie names from a text file to return outputs

Code Language: Python

Group ID: 1149

## Table of contents
* [Introduction](#Introduction)
* [Content](#Content)
* [Instructions](#Instructions)
* [Repository](#Repository)
* [Requirements](#Requirements)
  
## Introduction
This code was written for a group project  as part of the course “FS22-7,789,1.00 Skills: Programming with Advanced Computer Languages” supervised by Dr. Mario Silic in the Autumn semester 2021, at the University of St. Gallen. The group members are:
Thom Tingen
Karol Ciesluk
Maxime Zehnder
Philipp Kahnau


## Content

The code works with a text(.txt) file which contains movie names along with the actors that star in it. There is an example file in the repository with a limited selection of movies (movies.txt). Via the IMDB database other text files can be downloaded which provide a more extensive selection of movies.
The program aids as a search tool which incrorporates for 2 main functions:

Function 1 lets the user choose two movies and is presented with 3 potential outputs
* Selecting the first tickbox returns all actors that played in the selected movies (union)
* Selecting the second tickbox returns all actors that played in both movies, hence in movie 1 and movie 2 (intersection)
* Selecting the third tickbox returns all actors that played in one of the movies but not the other (difference)

Function 2 lets the user choose an actor and returns the movies in the list in which the actor starred, along with his costars in these movies.

## Instructions

The program comes with an interface with 2 main sections. The first section serves function 1 and the second serves function 2. Make sure to only select one of the tikboxes at once in the first section.

## Repository

* README file which contains a programe description and instructions
* movie.txt file as an example for a text file required by this programe
* Interface manual consisting of a screenshot with descriptive text
* Code as a JUPYTER file
* Code as a PYTHON file

## Requirements
The following programs were used for the project: 
* Python 3.10
* Jupyter Notebook and VS Code (visual studio code)

The following packages are required for the program: 
* datetime
* time
* tkinter

