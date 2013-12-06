import string
import fitness
import persistance


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
    feature_weights = persistance.get_knowledge()
    # feature vals
    feature_values = sentence_to_normailized_frequency_values_dict(sentence)
    # calc score
    score = classification_score(feature_values, feature_weights)
    # get threshold
    threshold = get_threshold
    # compare score to threshhold
    if score > threshold:
        #print("We think this is English", sentence)
        return True
    else:
        #print("We think this is Spanish", sentence)
        return False


class LanguageBot(object):
    def __init__(self):
        self.english_correct = 0
        self.spanish_correct = 0
        self.feature_weights = persistance.get_knowledge()
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
print(Language_Bot.best_weights)
print(Language_Bot)
Language_Bot.train()
print(Language_Bot)
print(Language_Bot.best_weights)

userinput = raw_input("Do you want to save new weights data: y/n ")
if userinput == 'y':
    persistance.save_knowledge(Language_Bot.best_weights)
