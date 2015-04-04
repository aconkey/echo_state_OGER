from gensim.models import Word2Vec as w2v
import numpy as np

"""
Purpose:    Encode text with the appropriate word vectors from a pre-trained 
            word2vec vector dictionary. 
"""

def get_vectorized_data(in_filename):
    model = w2v.load("trained_vectors")
    x = []
    y = []
    with open(in_filename) as text:
        for line in text:
            sentence = []
            target = []
            words = line.split()
            target_val = float(words[0])
            del words[0]
            for word in words:
                sentence.append(model[word])
                target.append(np.asarray([target_val])) # same target value for each sentence word
            x.append(np.asarray(sentence)) # one sentence per line
            y.append(np.asarray(target))
    return x,y






