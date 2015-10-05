import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

# TRAINING: 2005 State of the Union address by Pres. George W. Bush
train_text = state_union.raw("2005-GWBush.txt")

# TESTING: 2006 State of the Union address by Pres. George W. Bush
sample_text = state_union.raw("2006-GWBush.txt")

# TRAIN the Punkt tokenizer
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

# tokenize
tokenized = custom_sent_tokenizer.tokenize(sample_text)


# iterate over text and tag POS per sentence
def process_content():
    try:
        for i in tokenized[:1]:
            words = nltk.word_tokenize(i)
            # convert unicode to str
            str_words = []
            for word in words:
                str_words.append(str(word))
            tagged = nltk.pos_tag(str_words)
            # <RB.?>* = "0 or more of any tense of adverb", followed by:
            # <VB.?>* = "0 or more of any tense of verb", followed by:
            # <NNP>+ = "1 or more proper nouns", followed by:
            # <NN>? = "0 or 1 singular noun".
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)

            print chunked
            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                print subtree

            chunked.draw()

    except Exception as e:
        print str(e)


process_content()