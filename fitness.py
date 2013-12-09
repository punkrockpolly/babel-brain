import numpy
import persistence
import datamodel


def sigmoid(z):
# g = SIGMOIDGRADIENT(z) computes the gradient of the sigmoid function
# evaluated at z. This should work regardless if z is a matrix or a
# vector. In particular, if z is a vector or matrix, you should return
# the gradient for each element.
    # g = numpy.zeros(size(z))
    # gz = 1.0 ./ (1.0 + exp(-z))
    # g = (gz .* (1.0 - gz))
    return


def predict(Theta1, Theta2, X):
# refactor from octave into python:

# function p = predict(Theta1, Theta2, X)
# PREDICT Predict the label of an input given a trained neural network
#    p = PREDICT(Theta1, Theta2, X) outputs the predicted label of X given
#    the trained weights of a neural network (Theta1, Theta2)

# Useful values
# m = size(X, 1);
# num_labels = size(Theta2, 1);

# p = zeros(size(X, 1), 1);

# h1 = sigmoid([ones(m, 1) X] * Theta1');
# h2 = sigmoid([ones(m, 1) h1] * Theta2');
# [dummy, p] = max(h2, [], 2);
    return


def classification_score(ft_values, ft_weights):
    # features values = featurename -> normalizedfeatureValue
    # feature weights  = featurename -> feature weight
    score = 0
    for f in ft_weights:
        score += ft_values[f] * ft_weights[f]
    return score


def guess_is_english(sentence):
    # get feature weights
    # refactor into forward prop code below

    ft_weights = persistence.get_knowledge()
    # feature vals
    ft_values = datamodel.extract_features(sentence)
    # calc score
    score = classification_score(ft_values, ft_weights)
    # get threshold
    threshold = 50
    # compare score to threshhold
    if score > threshold:
        #print("We think this is English", sentence)
        return True
    else:
        #print("We think this is Spanish", sentence)
        return False


# genetic algorithm optimization for neural network:
# ----------------------------------

#   parameters for the neural network are "unrolled" into the vector
#   nn_params and need to be converted back into the weight matrices.

#   The returned parameter grad should be a "unrolled" vector of the
#   partial derivatives of the neural network.

#   1. implement neural network forward prop code (currently in Octave)
#   2. integrate genetic.py


# neural network forward prop code (currently in Octave)
# ----------------------------------
# A feedforward network is one whoso topology has no closed paths.
# Its input nodes are the ones with no arcs to them, and its output nodes
# have no arcs away from them. All other nodes are hidden nodes.

def reshape_thetas(nn_params):
# Reshape nn_params back into the parameters Theta1 and Theta2,
# the weight matrices for this 2 layer neural network

# todo: need to initialize/set weights to actual values
    return


def initialize_thetas(hidden_layer_size, input_layer_size, num_labels):
    Theta1 = datamodel.rand_init_ft_weights(hidden_layer_size, input_layer_size)
    Theta2 = datamodel.rand_init_ft_weights(num_labels, hidden_layer_size)
    # Theta1_grad = numpy.zeros(Theta1)
    # Theta2_grad = numpy.zeros(Theta2)
    return Theta1, Theta2


def feed_forward(Theta1, Theta2, X):
# Part 1: Forward propagation for the hypothesis
#         Feedforward the neural network and
#         return the cost in the variable J.

    # Add ones to the X (A1) data matrix
    X = [numpy.ones]

    # Hidden Layer
    Z2 = X * Theta1.transpose
    A2 = numpy.sigmoid(Z2)

    # Add ones to the A2 data matrix
    A2 = [numpy.ones]

    # Output Layer (hypothesis = A3)
    Z3 = A2 * Theta2.transpose
    A3 = numpy.sigmoid(Z3)
    return A3


def cost_function(nn_params,
                  nput_layer_size,
                  hidden_layer_size,
                  num_labels,
                  X, y):

# nn_params: need to be converted back into the weight matrices
# parameters for Theta1 and Theta2: weight matrices for a 2 layer NN

# input_layer_size: used to reshape Thetas
# hidden_layer_size: used to reshape Thetas
# num_labels: number of classifiers: used to reshape Thetas

# X: input matrix
# y: result vector

# y(i)k : i-th row of the y column vector,
# converted to a 10 vector representation of the digit
# if i-th row - y(i,:) = 5: y = [0000100000]

    # Setup some useful variables
    m = numpy.size(X, 1)
    J = 0

# size(A3)
# y_matrix = zeros(size(A3`))

# for inum in range(1, m):
#     y_matrix(:, inum) = numpy.eye(num_labels)(:, y(inum, :))`

# J = sum(sum(-y_matrix .* log(A3`) - (1 - y_matrix) .* log(1 - A3`)) / m) + reg_term

# --------------------------------------
# Implement genetic.py to mutate Thetas
# --------------------------------------
    return J
