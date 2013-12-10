import string
import collections
import numpy as np


def sentences(filename):
    # builds list of sentences from input file, then strips empty lines
    sentences = open(filename)
    rawinput = sentences.read()
    clean_string = string_sanitize(rawinput)
    input_list = clean_string.split("\n")
    new_list = []
    for sentence in input_list:
        stripped = sentence.strip()
        if stripped != "":
            new_list.append(stripped)
    return new_list


def vectorize_results(num_english, num_spanish):
    return [1 for x in range(num_english)] + [0 for x in range(num_spanish)]


def string_sanitize(string_input):
    # forces lowercase and strips digits
    return string_input.lower().translate(None, string.digits + string.punctuation)


def init_new_features_dict():
    feature_dict = {}
    # add letter freqs as features
    for letter in string.ascii_lowercase:
        feature_dict[letter] = 0
    # add other features to dict
    feature_dict['word_len'] = 0
    feature_dict['num_words'] = 0
    feature_dict['threshold'] = 0
    feature_dict[' '] = 0
    return feature_dict


def unroll(matrix):
    # takes a matrix(list of lists) and unrolls/flattens into one list
    return [item for sublist in matrix for item in sublist]


def reshape_thetas(nn_params, input_layer_size, hidden_layer_size, num_labels):
    # Reshape nn_params back into the parameters Theta1 and Theta2,
    # the weight matrices for this 2 layer neural network
    Theta1_size = input_layer_size * hidden_layer_size
    Theta1_flat = np.array(nn_params[0: Theta1_size])
    Theta2_flat = np.array(nn_params[Theta1_size: -1])
    Theta1 = np.reshape(Theta1_flat, (hidden_layer_size, -1))
    Theta2 = np.reshape(Theta2_flat, (num_labels, -1))
    return (Theta1, Theta2)


def dict_to_vector(feature_dict):
    keys = sorted(feature_dict.keys())
    return [feature_dict[k] for k in keys]
    # return map(lambda key: feature_dict[key], feature_dict)


# def vect_to_dict(feature_dict, feature_vector):
#     for each k:v, assign


def rand_init_ft_weights(L_in, L_out, epsilon_init=0.12):
    # build a new 2-d array for Thetas: neural network layers

    # randomly initialize all features weights of a layer
    # with L_in incoming connections and L_out outgoing connections
    W = np.zeros(shape=(L_out, 1 + L_in))

    # randomly initialize the weights to small values
    W = np.random.rand(L_out, 1 + L_in) * 2 * epsilon_init - epsilon_init

    return W


# Refactor to fix normalize_values_dict - DOES NOT WORK
def normalize_values_dict(feature_dict):
    feature_vector = dict_to_vector(feature_dict)
    # returns a normalized version of X where the mean value of
    # each feature is 0 and the standard deviation is 1
    X_norm = feature_vector
    num_features = feature_vector.length()
    mu = np.zeros(1, num_features)
    sigma = np.zeros(1, num_features)

    # for i in range(1, num_features):
    #     mu[i] = np.mean(X(:, i))
    #     X_norm[:, i] = X(:, i) - mu(i)
    #     sigma[i] = np.std(X(:, i))
    #     X_norm[:, i] = X_norm(:, i) / sigma(i)

    normalization_dict = {}
    normalization_dict['X_norm'] = X_norm
    normalization_dict['mu'] = mu
    normalization_dict['sigma'] = sigma

    return normalization_dict


def avg_word_len(string_input):
    words = string_input.count(' ') + 1
    total_chars_in_words = len(string_input.replace(" ", ""))
    return float(total_chars_in_words) / words


def avg_sentance_len(string_input):
    return string_input.count(' ') + 1


def count_letter_freq(string_input):
    # takes a string and returns a dict of letter freq
    return collections.Counter(string_input)


def build_training_examples(training_data):
    # Builds a matrix of feature values for each training example.
    # Rows = examples, cols = features.
    feature_values = []
    for example in training_data:
        feature_values.append(dict_to_vector(extract_features(example)))
    return feature_values


def extract_features(string_input):
    # takes a string and returns a dict of all features
    features = init_new_features_dict()
    # forces lowercase and strips digits
    stripped_string = string_sanitize(string_input)
    letter_freq = count_letter_freq(stripped_string)
    features.update({k: v for k, v in letter_freq.iteritems() if v})
    features['word_len'] = avg_word_len(stripped_string)
    features['num_words'] = avg_sentance_len(stripped_string)
    return features


def sentence_length_normalized_score(sentence, score):
    # returns a score that immune to sentence length,
    # thereby highlighing only the results of freq analysis
    total_valid_chars = 0
    for letter in string.ascii_lowercase:
            total_valid_chars += sentence.count(letter)
    if total_valid_chars != 0:
        return (float(score) / total_valid_chars)
    else:
        # this will have to change in the future as the thresholds
        # become more sophisticated.
        return 0


# Unit Tests for functions


def test_dict_to_vector(d):
    print("Test passed: test_dict_to_vector")
    return dict_to_vector(d)


def test_extract_features(s):
    print("\n'{0}' contains the following features: \n{1} \nvector representation: {2}"
          .format(s, extract_features(s), dict_to_vector(extract_features(s))))
    print("\nnumber of features: {0}\n".format(len(dict_to_vector(extract_features(s)))))


def test_ft_rand_init(rows=2, cols=3):
    print("Test passed: ft_rand_init")
    return rand_init_ft_weights(rows, cols)


def test_build_training_examples(training_data):
    output = build_training_examples(training_data)
    print('len of output: {0}\n# of features: {1}'.format(len(output),
                                                          len(output[0])))
    return output


def test_reshape_thetas(vector):
    nn_params = vector
    input_layer_size = 2
    hidden_layer_size = 5
    num_labels = 1
    Theta1, Theta2 = reshape_thetas(nn_params, input_layer_size, hidden_layer_size, num_labels)
    print('Theta1: {0}\nTheta2: {1}'.format(Theta1, Theta2))

m = [[-1, 0, 1], [2, 3, 4], [5, 6, 7]]
vector = np.arange(16)

d = {}
d[1] = 11
d[2] = 22
d[3] = 33
d[4] = 44

testsentences = ['r14534ishitis a good boy',
                 'po is a good girl',
                 'this $dskdj',
                 '*&^&^&$^#~~!@@H']
# d2 = test_ft_rand_init(5, 1)
# print(d2)
s = "test #~`^&+-=]p\|...string number 23984!!534987"
# test_dict_to_vector(d)
test_extract_features(s)
# print(test_build_training_examples(testsentences))
# print(unroll(m))
# test_reshape_thetas(vector)
