import persistence
import babelbrain


bot = babelbrain.Bot()

# bot.update_weights()

# for thischar in Chars:
#     bestWeigt = bot.findbestWeight(thisChar)
#     bot.updateWeight(thischar, bestWight)

# # now we have optimal weight
#     bot.showWeights()

print(bot.best_weights)
print(bot)
bot.train()
print(bot)
print(bot.best_weights)

userinput = raw_input("Do you want to save new weights data: y/n ")
if userinput == 'y':
    persistence.save_knowledge(bot.best_weights)
