import string
import random


def sentences(filename):
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
        letterDic[letter] = random.randint(1, 10)
    return letterDic


def classification_score(sentance, weights):
    # input sentance
    score = 0

    for letter in string.ascii_lowercase:
            score += sentance.count(letter) * weights[letter]

    return score


def is_english(sentence, weights):
    score = classification_score(sentence, weights)
    if score > 50:
        print "We think this is English", sentence
        return True
    else:
        print "We think this is Spanish", sentence
        return False

guess = def_letter_weights()
guess['i'] = -2
guess['a'] = -4


def guess_weights(weights):
    print 'English sentences'
    english = sentences('english-sentences.txt')
    english_correct = 0
    for sentence in english:
        if is_english(sentence, weights):
            english_correct += 1

    print 'Spanish sentences'
    spanish = sentences('spanish-sentences-short.txt')
    spanish_correct = 0
    for sentence in spanish:
        if not is_english(sentence, weights):
            spanish_correct += 1

    print 'total english:', len(english)
    print 'english correct:', english_correct
    print 'total spanish:', len(spanish)
    print 'spanish correct:', spanish_correct
    print 'total correct:', english_correct + spanish_correct

guess_weights(guess)
