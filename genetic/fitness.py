import numpy


def classification_score(feature_values, feature_weights):
    # features values = featurename -> normalizedfeatureValue
    # feature weights  = featurename -> feature weight
    score = 0
    for f in feature_weights:
        score += feature_values[f] * feature_weights[f]
    return score

# genetic algorithm optimization for neural network:
# ----------------------------------

#    parameters for the neural network are "unrolled" into the vector
#    nn_params and need to be converted back into the weight matrices.

#    The returned parameter grad should be a "unrolled" vector of the
#    partial derivatives of the neural network.

# 1. implement neural network forward prop code (currently in Octave)
# 2. integrate genetic.py


# neural network forward prop code (currently in Octave)
# ----------------------------------

J = 0
Theta1_grad = numpy.zeros(size(Theta1))
Theta2_grad = numpy.zeros(size(Theta2))

# Part 1: Forward propagation for the hypothesis
#         Feedforward the neural network and
#         return the cost in the variable J.

# Add ones to the X (A1) data matrix
X = [numpy.ones(m, 1) X]

# Hidden Layer
Z2 = X * Theta1`
A2 = numpy.sigmoid(Z2)

# Add ones to the A2 data matrix
A2 = [numpy.ones(m, 1) A2]

# Output Layer (hypothesis = A3)
Z3 = A2 * Theta2`
A3 = numpy.sigmoid(Z3)


# --------------------------------------
# Implement genetic.py to mutate Thetas
# --------------------------------------


# --------------------------------------
# Cost Function
# --------------------------------------

# y(i)k : i-th row of the y column vector,
# converted to a 10 vector representation of the digit
# if i-th row - y(i,:) = 5: y = [0000100000]

# size(A3)
y_matrix = zeros(size(A3`))

for inum in range(1, m):
    y_matrix(:, inum) = numpy.eye(num_labels)(:, y(inum, :))`

J = sum(sum(-y_matrix .* log(A3`) - (1 - y_matrix) .* log(1 - A3`)) / m) + reg_term
