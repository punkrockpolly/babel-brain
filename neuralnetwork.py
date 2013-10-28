import string
import json
import collections


def isFile(filename):
    try:
        with open(filename):
            return True
    except IOError:
        return False


def dict_to_json(my_dict):
    return json.dumps(my_dict)


def json_to_dict(my_json):
    return json.loads(my_json)


def save_knowledge(knowledge_dict):
    write_to_file('knowledge.txt', dict_to_json(knowledge_dict))


def get_knowledge():
    if isFile('knowledge.txt'):
        return json_to_dict(get_file_contents('knowledge.txt'))
    else:
        print "A NEW DICT WAS GENERATED."
        return new_feature_weights()


def write_to_file(filename, data):
    target = open(filename, 'w')
    target.write(str(data))
    target.close
    return True


def get_file_contents(filename):
    txt = open(filename)
    text = txt.read()
    txt.close()
    return text


def new_feature_weights():
    # build dictionary of all features
    feature_dict = {}
    feature_dict = feat_init_letter_freq(feature_dict)
    save_knowledge(feature_dict)
    return feature_dict


def feat_init_letter_freq(feature_dict):
    # INIT ALL ASCII LETTER FREQS AT 1
    for letter in string.ascii_lowercase:
        feature_dict[letter] = 1
    return feature_dict


def sentences(filename):
    # builds list of sentences from input file, then strips empty lines
    sentences = open(filename)
    rawinput = sentences.read().lower()
    input_list = rawinput.split("\n")
    new_list = []
    for sentence in input_list:
        stripped = sentence.strip()
        if stripped != "":
            new_list.append(stripped)
    return new_list


def normalized_char_frequencies(string_input):
    return 0

'''
def avg_word_len(string_input):
    words = string_input.count(' ')
    total_chars_in_words = len(string_input.strip(' '))
    return total_chars_in_words / float(words)

def avg_sentance_len(string_input):
    words = string_input.count('.')
    total_chars_in_sent = len(string_input.strip('.'))
    return total_chars_in_sent / float(words)


def extract_features(string_input):
    charfreq = normalized_char_frequencies(string_input)
    avg_sentance_len = avg_sentance_len(string_input)
    avg_word_len = avg_word_len(string_input)
    features = dict()

    features['word_len'] = avg_word_len
    features['sent_len'] = avg_sentance_len
    features['char_freq'] = 0
    return features


def sentence_length_normalized_score(sentence, score):
    # returns a score that immune to sentence length,
    # thereby highlighing only the results of freq analysis
    total_valid_chars = 0
    for letter in string.ascii_lowercase:
            total_valid_chars += sentence.count(letter)
    if total_valid_chars != 0:
        return (float(score)/total_valid_chars)
    else:
        # this will have to change in the future as the thresholds
        # become more sophisticated.
        return 0


'''


def sentence_to_normailized_frequency_values_dict(sentence):
    # takes a sentence and returns dictionary
    feature_values = collections.Counter(sentence)
    sentance_length = len(sentence)
    for item in feature_values:
        feature_values[item] = feature_values[item] / float(sentance_length)
    return feature_values


def classification_score(feature_values, feature_weights):
    # features values = featurename -> normalizedfeatureValue
    # feature weights  = featurename -> feature weight
    score = 0
    for this_feature_weight in feature_weights:
        score += feature_values[this_feature_weight] * feature_weights[this_feature_weight]
    return score


def get_threshold():
    return 50


def guess_is_english(sentence):
    # get feature weights
    feature_weights = get_knowledge()
    # feature vals
    feature_values = sentence_to_normailized_frequency_values_dict(sentence)
    # calc score
    score = classification_score(feature_values, feature_weights)
    # get threshold
    threshold = get_threshold
    # compare score to threshhold
    if score > threshold:
        #print "We think this is English", sentence
        return True
    else:
        #print "We think this is Spanish", sentence
        return False


class LanguageBot(object):
    def __init__(self):
        self.english_correct = 0
        self.spanish_correct = 0
        self.feature_weights = get_knowledge()
        self.best_weights = self.feature_weights
        self.english_sentences = sentences('english-sentences.txt')
        self.spanish_sentences = sentences('spanish-sentences.txt')
        self.best_score = self.english_guesses_correct() + self.spanish_guesses_correct()

    def english_guesses_correct(self):
        self.english_correct = 0
        for sentence in self.english_sentences:
            if guess_is_english(sentence):
                self.english_correct += 1
        return self.english_correct

    def spanish_guesses_correct(self):
        self.spanish_correct = 0
        for sentence in self.spanish_sentences:
            if not guess_is_english(sentence):
                self.spanish_correct += 1
        return self.spanish_correct

    def guess_sentence(self, sentence, language):
    # checks guess
        if guess_is_english(sentence):
            if language == 'english':
                return True
        else:
            if language == 'spanish':
                return True
        return False

    def train(self):
        for letter in string.ascii_lowercase:
            for x in range(-5, 6):
                self.feature_weights[letter] = x
                self.new_score = self.english_guesses_correct() + self.spanish_guesses_correct()
                if self.new_score > self.best_score:
                    self.best_score = self.new_score
                    self.best_weights[letter] = x
        return self.best_weights

    def __str__(self):
        output_string = '=====\n'
        output_string += 'total english:' + str(len(self.english_sentences)) + '\n'
        output_string += 'english correct:' + str(self.english_correct) + '\n'
        output_string += 'total spanish:' + str(len(self.spanish_sentences)) + '\n'
        output_string += 'spanish correct:' + str(self.spanish_correct) + '\n'
        output_string += 'total correct:' + str(self.english_correct + self.spanish_correct)
        return output_string

# Language_Bot.update_weights()

# for thischar in Chars:
#     bestWeigt = languageBot.findbestWeight(thisChar)
#     languageBot.updateWeight(thischar, bestWight)

# # now we have optimal weight
#     languageBot.showWeghts()

Language_Bot = LanguageBot()
print Language_Bot.best_weights
print Language_Bot
Language_Bot.train()
print Language_Bot
print Language_Bot.best_weights

userinput = raw_input("Do you want to save new weights data: y/n ")
if userinput == 'y':
    save_knowledge(Language_Bot.best_weights)
