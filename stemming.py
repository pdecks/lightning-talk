from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly", "pythonista"]

print example_words

for w in example_words:
    print ps.stem(w)

new_text = "It is important to be very pythonly while you are pythoning with python."

words = word_tokenize(new_text)


print new_text

for w in words:
    print ps.stem(w)