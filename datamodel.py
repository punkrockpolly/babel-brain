import string
import collections


def dict_to_vector(feature_dict):
    return map(lambda feature: feature_dict[feature], feature_dict)
        # list comprehension: [feature_dict[x] for x in keys in feature_dict


def test_dict_to_vector():
    dictionary = {}
    dictionary[1] = 11
    dictionary[2] = 22
    dictionary[3] = 33
    dictionary[4] = 44
    print("TEST PASSED")
    return dict_to_vector(dictionary)

# print(test_dict_to_vector())


def new_feature_weights():
    # build dictionary of all features
    feature_dict = {}
    feature_dict = feat_init_letter_freq(feature_dict)
    return feature_dict


def feat_init_letter_freq(feature_dict):
    # INIT ALL ASCII LETTER FREQS AT 1
    for letter in string.ascii_lowercase:
        feature_dict[letter] = 1
    return feature_dict


def normalized_char_frequencies(string_input):
    return 0


def avg_word_len(string_input):
    words = string_input.count(' ')
    total_chars_in_words = len(string_input.strip(' '))
    return total_chars_in_words / float(words)


def avg_sentance_len(string_input):
    words = string_input.count('.')
    total_chars_in_sent = len(string_input.strip('.'))
    return total_chars_in_sent / float(words)


def extract_features(string_input):
    freqs = normalized_char_frequencies(string_input)
    words = avg_sentance_len(string_input)
    chars = avg_word_len(string_input)
    features = {}
    features['word_len'] = chars
    features['sent_len'] = words
    features['char_freq'] = freqs
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


def sentence_to_normailized_frequency_values_dict(sentence):
    # takes a sentence and returns dictionary
    feature_values = collections.Counter(sentence)
    sentance_length = len(sentence)
    for item in feature_values:
        feature_values[item] = feature_values[item] / float(sentance_length)
    return feature_values
