import string
import persistence
import fitness
import datamodel as dt
import sys


# Neural Network's five components:
# 1. A directed graph (network topology) whose arcs we refer to as links.
# 2. A state variable associated with each node, stored in layers.
# 3. A real-valued weight associated with each link.
# 4. A real-valued bias associated with each node.
# 5. A transfer function for each node which determines the state of a node as a function of
#    a) its bias b (bias node needs to be added to each layer)
#    b) the weights, (Thetas) of its links
#    c) the states, x, of the nodes connected to it by these links.
# This transfer function usually involves either a sigmoid or a step function.


class Bot(object):
    def __init__(self):
        # current number of features
        self.input_layer_size = 30
        # current number of nodes in hidden layer
        self.hidden_layer_size = 5
        # current number of output classifiers
        self.num_labels = 1
        # initialize correct
        self.correct = 0
        # generates training examples
        self.english_sentences = dt.sentences('english-sentences.txt')
        self.spanish_sentences = dt.sentences('spanish-sentences.txt')
        # initialize input matrix
        self.Ft_values = dt.build_training_examples(self.english_sentences
                                                         + self.spanish_sentences)
        # initialize results vector
        self.y = dt.vectorize_results(len(self.english_sentences),
                                      len(self.spanish_sentences))
        # initialize feature weights
        self.Theta1 = (dt.rand_init_ft_weights(
                       self.input_layer_size,
                       self.hidden_layer_size))
        self.Theta2 = (dt.rand_init_ft_weights(
                       self.hidden_layer_size,
                       self.num_labels))
        self.nn_params = dt.unroll(self.Theta1) + dt.unroll(self.Theta2)
        # imports saved feature weights
        # self.nn_params = persistence.get_knowledge()

    # refactor to train via fitness.py
    def train(self):
        print('\nTraining')
        print(fitness.cost_function(self.nn_params,
                                    self.input_layer_size,
                                    self.hidden_layer_size,
                                    self.num_labels,
                                    self.Ft_values,
                                    self.y))

        # for letter in string.ascii_lowercase:
        #     for x in range(-5, 6):
        #         sys.stdout.write('.')
        #         sys.stdout.flush()
        #         self.feature_weights[letter] = x
        #         self.new_score = (self.english_guesses_correct() +
        #                           self.spanish_guesses_correct())
        #         if self.new_score > self.best_score:
        #             self.best_score = self.new_score
        #             self.best_weights[letter] = x
        # return self.best_weights

    def __str__(self):
        output_string = '\n=====\n'
        output_string += 'total english:' + str(len(self.english_sentences)) + ' \n'
        output_string += 'total spanish:' + str(len(self.spanish_sentences)) + '\n'
        output_string += 'total correct:' + str(self.correct) + '\n'
        return output_string
