import re

string = "The rain was coming. Everyone thought this would be a good thing. It hadn't rained in months and the earth was dry as a bone. It wasn't a surprise that everyone thought a good rain was what was needed, but they never expected how much rain would actually arrive."

# this finds all the words that start with the letter I or the letter T
word_list = re.findall(r'\b[tTiI]\w+', string)

print(word_list)