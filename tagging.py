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
            print tagged
    except Exception as e:
        print str(e)


process_content()

# start_str = ["PRESIDENT GEORGE W. BUSH'S ADDRESS BEFORE A JOINT SESSION OF THE CONGRESS ON THE STATE OF THE UNION\n\nJanuary 31, 2006\n\nTHE PRESIDENT: Thank you all."]
