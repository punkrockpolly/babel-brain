import string
import random


def sentences(filename):
    # builds list of sentances from input file, then strips empty lines

    sentences = open(filename)
    rawinput = sentences.read().lower()

    input_list = rawinput.split("\n")

    new_list = []
    for sentance in input_list:
        if sentance.strip() != "":
            new_list.append(sentance)

    return new_list


def def_letter_weights():
    # build dictionary of letters and their weights

    letterDic = {}
    for letter in string.ascii_lowercase:
        letterDic[letter] = 1
    return letterDic


def random_weights():
    # build dictionary of letters and their weights

    letterDic = {}
    for letter in string.ascii_lowercase:
        letterDic[letter] = random.randint(-10, 10)
    return letterDic


def classification_score(sentance, weights):
    # input sentance and weights, mutiply then return score
    score = 0

    for letter in string.ascii_lowercase:
            score += sentance.count(letter) * weights[letter]

    return score


def sentance_length_normalized_score(sentance, score):
    # returns a score that immune to sentance length,
    # thereby highlighing only the results of freq analysis
    total_valid_chars = 0
    for letter in string.ascii_lowercase:
            total_valid_chars += sentance.count(letter)
    if total_valid_chars != 0:
        return (float(score)/total_valid_chars)
    else:
        # this will have to change in the future as the thresholds
        # become more sophisticated.
        return 0


def is_english(sentence, weights, threshold):
    score = classification_score(sentence, weights)
    if score > threshold:
        #print "We think this is English", sentence
        return True
    else:
        #print "We think this is Spanish", sentence
        return False


print sentance_length_normalized_score("a sent t ", 120)


class CharWeights(object):
    def __init__(self):
        self.weights = def_letter_weights()
        self.best_score = self.english_guesses_correct()
        self.english_sentances = sentences('english-sentences.txt')
        self.spanish_sentances = sentences('spanish-sentences-short.txt')
        self.english_correct = 0
        self.spanish_correct = 0
        self.threshold = 50

    def english_guesses_correct(self):
        for sentence in self.english_sentances:
            if is_english(self.sentence, self.weights, self.threshold):
                self.english_correct += 1
        return self.english_correct

    def spanish_guesses_correct(self):
        for sentence in self.spanish_sentances:
            if not is_english(self.sentence, self.weights, self.threshold):
                self.spanish_correct += 1
        return self.spanish_correct

    def best_weights(self):
        self.best_weights = self.weights
        for letter in string.ascii_lowercase:
            for x in range(-5, 6):
                self.weights[letter] = x
                self.new_score = self.english_guesses_correct()
                if self.new_score > self.best_score:
                    self.best_score = self.new_score
                    self.best_weights[letter] = x
        return self.best_weights

    def __str__(self):
        output_string = ''
        output_string += 'total english:' + len(self.english_sentances) + '/n'
        output_string += 'english correct:' + self.english_correct + '/n'
        output_string += 'total spanish:', len(self.spanish_sentances) + '/n'
        output_string += 'spanish correct:', self.spanish_correct + '/n'
        output_string += 'total correct:', self.english_correct + self.spanish_correct
        return output_string

# Language_Bot = CharWeights()
# Language_Bot.update_weights()

# for thischar in Chars:
#     bestWeigt = languageBot.findbestWeight(thisChar)
#     languageBot.updateWeight(thischar, bestWight)

# # now we have optimal weight
#     languageBot.showWeghts()
