import string
import persistence

# inputs:
# nn_params: parameters for Theta1 and Theta2: weight matrices for a 2 layer NN
# input_layer_size: used to reshape Thetas
# hidden_layer_size: used to reshape Thetas
# num_labels: number of classifiers: used to reshape Thetas
# X: input matrix
# y: result vector
# lambda: regularization value

class LanguageBot(object):
    def __init__(self):
        self.english_correct = 0
        self.spanish_correct = 0
        self.feature_weights = persistence.get_knowledge()
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
