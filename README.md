# AI Final Project - Chess Agent
#### By: Collin Schmocker & Connor Curcio

---

## Basic Setup

### Running ```main.py```

The main library that is needed is pythons chess library. 
The easiest way to install is to run the following line in your command terminal.
```commandline
pip install chess
```
For setting up the for running a set of games go into ```main.py``` and change 
```player1``` to either ```"Basic"```,  ```"Better"```, or ```"Genetic"``` with 
each representing the different evaluation functions that will be used. To change 
the amount of games that will be simulated change ```game_amount``` to the amount 
of games that you want to simulate **[Warning]** it takes around 3 minutes to run 
a single game. If you want to change the agent behind ```player1``` and 
```player2``` you will need to comment and uncomment lines 49 and 50 as well as 
58 and 59 of ```main.py```. Once ```main.py``` is run after each game it will 
print what game it is on and the final turn count.

### Running ```GeneticAlgorithm.py```

For ```GeneticAlgorithm.py``` nothing is needed to run it at the start. To change 
population and/or epoch amount change the value for ```pop_size``` to change the 
population size and change the last input for ```Genetic_Algorithm``` to an int value. 
Once the program is finished running **[Warning]** it will take around 2 minutes 
per game and a game will be run for each member of the population. Once the method 
is done running it will print out a 2D array that can then be copy and pasted into 
```main.py``` and replace the value for ```genetic_eval```.

## Advanced Setup

### Downloading Games as a GIF

This part is if you want to save a game as a gif and watch it later **[Warning]** 
while this doesn't take much longer on the time it is recommended that you do this 
for a single game at a time. First try to install the library's needed. It's recommended 
to use the terminal again and run the commands below.
```commandline
pip install pipwin
pipwin install cairocffi
pip install CairoSVG
```
If the library's installed correctly you should now be able to download games as 
a gif by uncommenting various code. To start off in ```ChessGame.py``` uncomment 
all ```imports``` and uncomment the method ```downloadGame```. Then inside of 
```main.py``` change the ```clone``` parameter for ```ChessGame``` on line 38 to 
false. After this you should be able to run the method in ```main.py``` located 
at the very end of the file with the parameter to the method the name of the 
gif file without the extension.

--- 

Git Repo Link: https://github.com/schmockerc/AIFinalProject