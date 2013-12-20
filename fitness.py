import numpy as np
import datamodel as dt


def sigmoid(z):
# g: the sigmoid function evaluated at z.
# This should work regardless if z is a matrix or a vector.
    return 1.0 / (1.0 + np.exp(-z))


# genetic algorithm optimization for neural network:
# ----------------------------------


# neural network forward prop code
# ----------------------------------
# A feedforward network is one whoso topology has no closed paths.
# Its input nodes are the ones with no arcs to them, and its output nodes
# have no arcs away from them. All other nodes are hidden nodes.


def feed_forward(Theta1, Theta2, Ft_values):
# Part 1: Forward propagation for the hypothesis
#         Feedforward the neural network.
#         Predicts A3 (hypothesis) based on Thetas and Ft_values

    m = np.size(Ft_values, 0)  # number of training examples
    # n = np.size(Ft_values, 1)  # number of features

    # print(Ft_values.shape)
    # print(Ft_values)

    # Add bias terms (ones) to the Ft_values (A1) data matrix
    Ft_values = np.column_stack((np.ones((m, 1)), Ft_values))

    # print(np.matrix(Theta1).shape)
    # print(np.matrix(Theta1))

    # Hidden Layer
    Z2 = Ft_values.dot(np.transpose(Theta1))
    A2 = sigmoid(Z2)

    # Add ones to the A2 data matrix
    A2 = np.column_stack((np.ones((m, 1)), A2))
    # print(A2.shape)
    # print(A2)
    # print(np.matrix(Theta2).shape)
    # print(np.matrix(Theta2))
    # Output Layer (hypothesis = A3)
    Z3 = A2.dot(np.transpose(Theta2))
    # print(Z3)
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
    y = np.array(y)

    # print(y, A3)
    # wrong = np.sum(np.absolute(np.subtract(y, np.round(A3))))
    wrong = np.sum(y - A3)

    J = np.sum(np.sum(-y * (np.log(A3)) - (1 - y) * (np.log(1 - A3)))) / m
    return J, wrong

# --------------------------------------
# Implement genetic.py to mutate Thetas
# --------------------------------------


def test_sigmoid():
    z = [12, -423, 0]
    print sigmoid(np.array(z))

# test_sigmoid()
