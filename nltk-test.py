import nltk

import string

sample_file = open('murakami-norwood.txt')

print "\n\n"
print '-'*79
print "NLTK EXAMPLES for excerpt from 'Norwegian Wood' by Harumi Murakami"
print "by Tricia Decker for Hackbright Academy Fall 2015 Lightning Talk"
print '-'*79

print '\n'
print "CONVERT .txt file to raw text"
print "-"*79
raw_text = sample_file.read()
print raw_text[19:350] + ' ...'
user_pause = raw_input("> Press ENTER to continue.")

# no_punc_text = raw_text.strip().translate(string.maketrans("", ""), string.punctuation)
raw_no_punc = ''
for char in raw_text:
    if char.isalpha() or char == " " or char == '\n':
        raw_no_punc += char

raw_no_punc

# TOKENIZE by word
print '\n'
print "TOKENIZE by word:"
print "-"*79
tokens = nltk.word_tokenize(raw_text)
print tokens[6:61]
text = nltk.Text(tokens)
user_pause = raw_input("> Press ENTER to continue.")

# FILTER OUT PUNCTUATION
no_punc_tokens = [token for token in tokens if token.isalpha()]

# PRODUCE TEXT from tokens
text = nltk.Text(tokens)

# VOCABULARY
print '\n'
print "Create a VOCABULARY:"
print "-"*79
text_vocab = sorted(set(text))
print text_vocab[125:175]
user_pause = raw_input("> Press ENTER to continue.")

# collocations are bigrams that occur more often that we'd expect
# ex: red wine
print '\n'
print "Find COLLOCATIONS, bigrams that occur more often than we'd expect:"
print "(ex: 'red wine')"
print "-"*79
text.collocations() # returns None
# cols = [w for w in cols if w.isalpha()]
user_pause = raw_input("> Press ENTER to continue.")

print "\n"
# provide context for words with concordance
print "Provide context for words using CONCORDANCE."
print "-"*79
print "RESULTS for text.concordance('forest'):"
text.concordance('forest')
print "-"*79
print "RESULTS for text.concordance('canyon'):"
text.concordance('canyon')
user_pause = raw_input("> Press ENTER to continue.")

# search for other words used in similar context with similar
print '\n'
print "Search for other words used in SIMILAR context:"
print "-"*79
print "RESULTS for text.similar('forest')"
text.similar('forest')
print "-"*79
print "RESULTS for text.similar('doctor')"
text.similar('doctor')
user_pause = raw_input("> Press ENTER to continue.")

# WHAT MAKES TEXT DISTINCT?
fdist = nltk.FreqDist(tokens)
fdist.most_common(50)


# Create a Frequency Distribution of the tokens
print '\n'
print "What makes text distinct? Use Frequency Distributions"
print "-"*79
fdist2 = nltk.FreqDist(no_punc_tokens)

# Display the most common tokens and their frequencies
print "Fifty most-common words:"
print fdist2.most_common(50)
print

# Plot individual word frequencies, most common 50
print "Plot individual word frequencies, 50 most-common words:"
user_pause = raw_input("> Press ENTER to continue.")
fdist2.plot(50, cumulative=False)
print

# Plot cumulative word frequencies, most common 50
print "Plot cumulative word frequencies, 50 most-common words:"
user_pause = raw_input("> Press ENTER to continue.")
fdist2.plot(50, cumulative=True)
print


# examine longer words (7 characters or more)
long_words = [w for w in no_punc_tokens if len(w) > 7]
fdist3 = nltk.FreqDist(long_words)
print "Plot cumulative word frequencies, words with length > 7 characters:"
user_pause = raw_input("> Press ENTER to continue.")
fdist3.plot(30, cumulative=True)
print

# infrequent words
# hap_all = fdist2.hapaxes()
print "Examine infrequent words with HAPAXES:"
print '-'*79
hap_long = fdist3.hapaxes()
print "Sample of 20 words from 152 infrequent words:"
print hap_long[10:30]
user_pause = raw_input("> Press ENTER to continue.")
print

# meaningful --> frequent and not too long or short
meaningful = [w for w in no_punc_tokens if len(w) > 7 and fdist2[w] > 3]
print
print "MEANINGFUL WORDS: for example, words with length > 7 and frequency > 3"
print "-"*79
for w in set(meaningful):
    print w
print
print "CONCORDANCE for 'wrinkles':"
print '-'*79
print text.concordance('wrinkles')
user_pause = raw_input("> Press ENTER to finish.")