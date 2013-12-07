import fitness
import persistence
import datamodel


def get_threshold():
    return 50


def guess_is_english(sentence):
    # get feature weights
    feature_weights = persistence.get_knowledge()
    # feature vals
    feature_values = datamodel.normailized_frequency_values_dict(sentence)
    # calc score
    score = fitness.classification_score(feature_values, feature_weights)
    # get threshold
    threshold = get_threshold
    # compare score to threshhold
    if score > threshold:
        #print("We think this is English", sentence)
        return True
    else:
        #print("We think this is Spanish", sentence)
        return False


# Language_Bot.update_weights()

# for thischar in Chars:
#     bestWeigt = languageBot.findbestWeight(thisChar)
#     languageBot.updateWeight(thischar, bestWight)

# # now we have optimal weight
#     languageBot.showWeights()

Language_Bot = fitness.LanguageBot()
print(Language_Bot.best_weights)
print(Language_Bot)
Language_Bot.train()
print(Language_Bot)
print(Language_Bot.best_weights)

userinput = raw_input("Do you want to save new weights data: y/n ")
if userinput == 'y':
    persistence.save_knowledge(Language_Bot.best_weights)
