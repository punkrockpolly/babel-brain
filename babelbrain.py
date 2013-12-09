import string
import persistence
import fitness


# Neural Network's five components:
# 1. A directed graph (network topology) whose arcs we refer to as links.
# 2. A state variable associated with each node, stored in layers.
# 3. A real-valued weight associated with each link.
# 4. A real-valued bias associated with each node.
# 5. A transfer function for each node which determines the state of a node as a function of
#    a) its bias b (bias node needs to be added to each layer)
#    b) the weights, (Thetas) of its links
#    c) the states, x, of the nodes connected to it by these links.
# This transfer function usually involves either a sigmoid or a step function.


class Bot(object):
    def __init__(self):
        self.input_layer_size = 50
        hidden_layer_size = 25
        num_labels = 2

        self.sentences = {}
        self.english_sentences = persistence.sentences('english-sentences.txt')
        self.spanish_sentences = persistence.sentences('spanish-sentences.txt')
        self.english_correct = 0
        self.spanish_correct = 0
        self.feature_weights = persistence.get_knowledge()
        self.best_weights = self.feature_weights
        self.best_score = (self.english_guesses_correct() +
                           self.spanish_guesses_correct())

    def english_guesses_correct(self):
        self.english_correct = 0
        for sentence in self.english_sentences:
            if fitness.guess_is_english(sentence):
                self.english_correct += 1
        return self.english_correct

    def spanish_guesses_correct(self):
        self.spanish_correct = 0
        for sentence in self.spanish_sentences:
            if not fitness.guess_is_english(sentence):
                self.spanish_correct += 1
        return self.spanish_correct

    # refactor to guess via fitness.predict
    def guess_sentence(self, sentence, language):
    # checks guess
        if fitness.guess_is_english(sentence):
            if language == 'english':
                return True
        else:
            if language == 'spanish':
                return True
        return False

    # refactor to train via fitness.py
    def train(self):
        for letter in string.ascii_lowercase:
            for x in range(-5, 6):
                self.feature_weights[letter] = x
                self.new_score = (self.english_guesses_correct() +
                                  self.spanish_guesses_correct())
                if self.new_score > self.best_score:
                    self.best_score = self.new_score
                    self.best_weights[letter] = x
        return self.best_weights

    def __str__(self):
        output_string = '=====\n'
        output_string += 'total english: \n' + str(len(self.english_sentences)) + ''
        output_string += 'english correct:' + str(self.english_correct) + '\n'
        output_string += 'total spanish:' + str(len(self.spanish_sentences)) + '\n'
        output_string += 'spanish correct:' + str(self.spanish_correct) + '\n'
        output_string += 'total correct:' + str(self.english_correct + self.spanish_correct)
        return output_string
