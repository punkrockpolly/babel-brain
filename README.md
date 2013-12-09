babel_brain is a neural network using a genetic algorithm
-------------

Supervised learning using a neural network
WIP: implement a genetric algorithm for machine learning optimization

- Learns from 2 input files (one english, one spanish)
- Uses letter-weighting to guess the language of an input sentence.

program flow
-------------
main.py 
- creates an instance of the babelbrain.Bot object
- trains
- prompts to save data (node activation weights)

babelbrain.py 
- an object with methods to train & guess

fitness.py
- feedforward
- cost function
- predict

genetic.py
- genetic algo
- needs to be integrated with this project

datamodel
- feature extraction
- random init for weights
- normalization

persistence
- read/write file
- create json

features - data points for each training example phrase
-------------
- num of words
- average word length
- frequency of letters: occurance frequency for each char in the ascii alphabet


