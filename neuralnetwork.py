import string
import random


def sentences(filename):
    # builds list of sentences from input file, then strips empty lines

    sentences = open(filename)
    rawinput = sentences.read().lower()

    input_list = rawinput.split("\n")

    new_list = []
    for sentence in input_list:
        if sentence.strip() != "":
            new_list.append(sentence)

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


def classification_score(sentence, weights):
    # input sentence and weights, mutiply then return score
    score = 0

    for letter in string.ascii_lowercase:
            score += sentence.count(letter) * weights[letter]

    return score


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


def is_english(sentence, weights, threshold):
    score = classification_score(sentence, weights)
    if score > threshold:
        #print "We think this is English", sentence
        return True
    else:
        #print "We think this is Spanish", sentence
        return False


print sentence_length_normalized_score("a sent t ", 120)


class CharWeights(object):
    def __init__(self):
        self.english_correct = 0
        self.spanish_correct = 0
        self.threshold = 50
        self.weights = def_letter_weights()
        self.english_sentences = sentences('english-sentences.txt')
        self.spanish_sentences = sentences('spanish-sentences-short.txt')
        self.best_score = self.english_guesses_correct()

    def english_guesses_correct(self):
        self.english_correct = 0
        for sentence in self.english_sentences:
            if is_english(sentence, self.weights, self.threshold):
                self.english_correct += 1
        return self.english_correct

    def spanish_guesses_correct(self):
        self.spanish_correct = 0
        for sentence in self.spanish_sentences:
            if not is_english(sentence, self.weights, self.threshold):
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
        output_string += 'total english:' + str(len(self.english_sentences)) + '\n'
        output_string += 'english correct:' + str(self.english_correct) + '\n'
        output_string += 'total spanish:' + str(len(self.spanish_sentences)) + '\n'
        output_string += 'spanish correct:' + str(self.spanish_correct) + '\n'
        output_string += 'total correct:' + str(self.english_correct) + str(self.spanish_correct)
        return output_string

# Language_Bot.update_weights()

# for thischar in Chars:
#     bestWeigt = languageBot.findbestWeight(thisChar)
#     languageBot.updateWeight(thischar, bestWight)

# # now we have optimal weight
#     languageBot.showWeghts()

Language_Bot = CharWeights()
print Language_Bot
Language_Bot.best_weights()
print Language_Bot

