import string
import random
import json


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
    write_to_file(dict_to_json(knowledge_dict))

def get_knowledge():
    if isFile('knowledge.txt'):
        return json_to_dict(file_contents('knowledge.txt'))
    else:
        return def_feature_weights()

def write_to_file(filename, data):
    target = open(filename, 'w')
    target.write(str(data))
    target.close
    return True

def file_contents(filename):
    txt = open(filename)
    text = txt.read()
    txt.close()
    return text



def isInCache(pLoc1,pLoc2):
    filename = filenameGen(pLoc1,pLoc2)
    return isFile(filename)


def def_feature_weights():
    # build dictionary of letters and their weights
    letterDic = {}
    for letter in string.ascii_lowercase:
        letterDic[letter] = 1
    return letterDic



def sentences(filename):
    # builds list of sentences from input file, then strips empty lines
    sentences = open(filename)
    rawinput = sentences.read().lower()
    input_list = rawinput.split("\n")

    num_removed = 0
    new_list = []
    for sentence in input_list:
        stripped = sentence.strip()
        if stripped != "":
            new_list.append(stripped)
        else:
            num_removed += 1

    print str(num_removed) + ":" + filename
    return new_list

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
    charfreq = normalized_char_frequencies(string_input)
    avg_sentance_len = avg_sentance_len(string_input)
    avg_word_len = avg_word_len(string_input)
    features = dict() 
    
    features['word_len'] = avg_word_len
    features['sent_len'] = avg_sentance_len
    features['char_freq'] = 0
    return features



def classification_score_general(feature_values,weights):
    # features dict = featurename:normalizedfeatureValue
    # weight dict = featurename -> weight val
    score = 0
    for feature_value in feature_values:
        score += feature_value * weights[feature_value]
    return score

def classification_score(sentence, weights):
    # input sentence and weights, mutiply then return score
    score = 0
    for letter in string.ascii_lowercase:
            score += sentence.count(letter) * weights[letter]
    return sentence_length_normalized_score(sentence, score)

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

def guess_is_english(sentence, weights, threshold=50):
    score = classification_score(sentence, weights)
    if score > threshold:
        #print "We think this is English", sentence
        return True
    else:
        #print "We think this is Spanish", sentence
        return False

class CharWeights(object):
    def __init__(self):
        self.english_correct = 0
        self.spanish_correct = 0
        self.weights = def_feature_weights()
        self.best_weights = self.weights
        self.english_sentences = sentences('english-sentences.txt')
        self.spanish_sentences = sentences('spanish-sentences.txt')
        self.best_score = self.english_guesses_correct()

    def english_guesses_correct(self):
        self.english_correct = 0
        for sentence in self.english_sentences:
            if guess_is_english(sentence, self.weights):
                self.english_correct += 1
        return self.english_correct

    def spanish_guesses_correct(self):
        self.spanish_correct = 0
        for sentence in self.spanish_sentences:
            if not guess_is_english(sentence, self.weights):
                self.spanish_correct += 1
        return self.spanish_correct

    def find_best_weights(self):
        for letter in string.ascii_lowercase:
            for x in range(-5, 6):
                self.weights[letter] = x
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

Language_Bot = CharWeights()
print Language_Bot.best_weights
print Language_Bot
Language_Bot.find_best_weights()
print Language_Bot
print Language_Bot.best_weights
