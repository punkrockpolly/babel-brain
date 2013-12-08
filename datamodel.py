import string
import collections
import numpy


def init_new_features_dict():
    feature_dict = {}
    # add letter freqs as features
    for letter in string.ascii_lowercase:
        feature_dict[letter] = 0

    # add other features to dict
    feature_dict['word_len'] = 0
    feature_dict['num_words'] = 0
    feature_dict['threshold'] = 0

    return feature_dict


def dict_to_vector(feature_dict):
    return map(lambda feature: feature_dict[feature], feature_dict)
        # list comprehension: [feature_dict[x] for x in keys in feature_dict


def rand_init_feature_weights(L_in, L_out):
    # build a new dictionary
    # randomly initialize all features weights of a layer
    # with L_in incoming connections and L_out outgoing connections
    W = numpy.zeros(shape=(L_out, 1 + L_in))

    # randomly initialize the weights to small values
    epsilon_init = 0.12
    W = numpy.random.rand(L_out, 1 + L_in) * 2 * epsilon_init - epsilon_init

    return W


def normalize_values_dict(feature_vector):
    # returns a normalized version of X where the mean value of
    # each feature is 0 and the standard deviation is 1
    X_norm = feature_vector
    num_features = feature_vector.length()
    mu = numpy.zeros(1, num_features)
    sigma = numpy.zeros(1, num_features)

    # for i in range(1, num_features):
    #     mu[i] = numpy.mean(X(:, i))
    #     X_norm[:, i] = X(:, i) - mu(i)
    #     sigma[i] = numpy.std(X(:, i))
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


def extract_features(string_input):
    # takes a string and returns a dict of all features
    features = init_new_features_dict()
    letter_freq = count_letter_freq(string_input)
    features.update({k: v for k, v in letter_freq.iteritems() if v})
    features['word_len'] = avg_word_len(string_input)
    features['num_words'] = avg_sentance_len(string_input)
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


def test_dict_to_vector():
    dictionary = {}
    dictionary[1] = 11
    dictionary[2] = 22
    dictionary[3] = 33
    dictionary[4] = 44
    print("TEST PASSED")
    return dict_to_vector(dictionary)

# TEST CASES - prints need to be refactored into unit test methods
# print(test_dict_to_vector())
# print(dict_to_vector(init_feature_weights()))
# print(rand_init_feature_weights(2, 3))
s = "test string number 2"


def test_extract_features(s):
    print("'{0}' contains the following features: {1}".format(
          s, extract_features(s)))
    print(dict_to_vector(extract_features(s)))
