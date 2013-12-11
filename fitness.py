import numpy as np
import persistence as ps
import datamodel as dt


def sigmoid(z):
# g: the sigmoid function evaluated at z.
# This should work regardless if z is a matrix or a vector.
    return 1.0 / (1.0 + np.exp(-z))


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

    ft_weights = ps.get_knowledge()
    # feature vals
    ft_values = dt.extract_features(sentence)
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


def feed_forward(Theta1, Theta2, Ft_values):
# Part 1: Forward propagation for the hypothesis
#         Feedforward the neural network.

    m = np.size(Ft_values, 0)

    # Add biad terms (ones) to the Ft_values (A1) data matrix
    Ft_values = np.matrix([[1.0] + item for item in Ft_values])

    # Ft_values = np.matrix(Ft_values)
    # print(Ft_values.shape)
    # print(Ft_values)
    # print(np.matrix(Theta1).shape)
    # print(np.matrix(Theta1))

    # Hidden Layer
    Z2 = Ft_values.dot(np.transpose(Theta1))
    A2 = sigmoid(Z2)

    # Add ones to the A2 data matrix
    A2 = np.column_stack((np.ones((m, 1)), A2))
    print(A2.shape)
    print(A2)
    print(np.matrix(Theta2).shape)
    print(np.matrix(Theta2))
    # Output Layer (hypothesis = A3)
    Z3 = A2.dot(np.transpose(Theta2))
    A3 = sigmoid(Z3)
    return A3


def cost_function(nn_params,
                  input_layer_size,
                  hidden_layer_size,
                  num_labels,
                  Ft_values, y):
    # cost_function should return the cost in the variable J

    # INPUT VALUES:
    # input_layer_size: used to reshape Thetas
    # hidden_layer_size: used to reshape Thetas
    # num_labels: number of classifiers: used to reshape Thetas
    # Ft_values: input matrix
    # y: result vector
    # print(np.array(nn_params).size, input_layer_size,
    #                                    hidden_layer_size,
    #                                    num_labels)
    Theta1, Theta2 = dt.reshape_thetas(nn_params,
                                       input_layer_size,
                                       hidden_layer_size,
                                       num_labels)
    # print(Theta1.size, Theta2.size)
    A3 = feed_forward(Theta1, Theta2, Ft_values)

    # Setup some useful variables
    m = np.size(Ft_values, 0)
    J = 0

# y_matrix = zeros(size(A3`))

# for inum in range(1, m):
#     y_matrix(:, inum) = np.eye(num_labels)(:, y(inum, :))`

# J = sum(sum(-y_matrix .* log(A3`) - (1 - y_matrix) .* log(1 - A3`)) / m) + reg_term

# --------------------------------------
# Implement genetic.py to mutate Thetas
# --------------------------------------
    return J
