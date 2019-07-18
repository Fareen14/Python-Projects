import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer

sentences = ['i love my dog',
             'I love my cat']

tokenizer = Tokenizer(num_words=100)
tokenizer.fit_on_text(sentences)
word_index = tokenizer.word_index
print(word_index)