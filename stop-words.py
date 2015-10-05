from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "Hackbright Academy is super awesome, and all of these words are extremely important."

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

print
print "example_sent"
print
print example_sent
print
print word_tokens
print
print filtered_sentence
