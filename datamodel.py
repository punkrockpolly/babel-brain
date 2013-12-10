import string
import collections
import numpy


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
    W = numpy.zeros(shape=(L_out, 1 + L_in))

    # randomly initialize the weights to small values
    W = numpy.random.rand(L_out, 1 + L_in) * 2 * epsilon_init - epsilon_init

    return W


# Refactor to fix normalize_values_dict - DOES NOT WORK
def normalize_values_dict(feature_dict):
    feature_vector = dict_to_vector(feature_dict)
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


d = {}
d[1] = 11
d[2] = 22
d[3] = 33
d[4] = 44

# d2 = test_ft_rand_init(5, 1)
# print(d2)
s = "test #~`^&+-=]p\|...string number 23984!!534987"
# test_dict_to_vector(d)
# test_extract_features(s)
