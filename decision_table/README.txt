A simple implementation of a decision table with the following abilities:
1.) store condition and action functions; these must return either True or 
	False, but can take arbitrary number of arguments
2.) store cases in which the conditions to care about, the expected results of 
	condition functions, and which actions to take are stored
3.) retrieval of actions bases on given conditions

Action and condition functions must be unique. The same action can be
associated with multiple cases. It is recommended that action functions only 
take one argument that is the same for all other action functions in order to 
make iterating through actions easier. I've included a jupyter notebook file 
with a toy example to see how the class works.

Note: I haven't implemented much type-checking yet, so the code can be broken 
	fairly easily, so be sure you know exactly what your feeding into the table
	
