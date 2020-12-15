# PFSS-Python2
Planning for drunks; Programming for Social Sciences (Python) Assignment 2.

## Introduction
This repositary contains the final code produced for the second assignment in the 2020 module "Programming for Social Scientists: Core Skills in Python".

The code produces an Agent-Based Model (ABM); simulating the behvaiour of 'drunks' as they move around in the virtual environment - the environment cosists of data which was read in using the [drunk.plan.txt](drunk.plan.txt) file in this repository. The simulation of agent behaviours was achieved through an object-orientated approach due to the production of the Agent class which defines the behaviours of all instances of the agent.

## Repository contents

**The model**

[drunkframework.py](drunkframework.py): this file formulates the agent class.

[drunkmodel.py](drunkmodel.py): this file runs the model and -
1. Loads the town plan and visualises it
2. Simulates the movements of the drunks
3. Visualises the paths taken in a heat map
4. Writes out the the map to a file as text

If attempting to run the model, both files must exist in the same directory, and the [drunkframework.py](drunkframework.py) file must be imported at the top of the [drunkmodel.py](drunkmodel.py) file in order for the code to function correctly. Although this is included within the code, please bear this in mind if difficulties are encountered during any early stages. Generally, textual comments have been added which are signified when chunks of code are preceded by the hash key, these comments typically explain to readers what the following section of code is intended to do.

**Other files**

[drunk.plan.txt](drunk.plan.txt): a 300 x 300 town plan which is read into the environment.

[UML.png](UML.png): the UML diagram associated with the project/code.

[LICENSE](LICENSE): this file outlines that the project has been licensed under the MIT License.


## Running the model

```
python drunkmodel.py
```
After running the model, the code will be produce an output of a [density.txt](density.txt) file in the same directory as your Python files. A figure (“Figure 1”) will also be produced as part of the output in a new pop-up window, showing the movement of the drunks through the environment before they reach their homes.

*Note: Matplotlib library needs to be installed prior to running the model if this has not been done in the past.*

