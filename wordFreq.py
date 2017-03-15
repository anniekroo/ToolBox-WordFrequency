import pickle
import nltk
from nltk.tokenize import TweetTokenizer
import collections
import string

def openFile(name):
    """Opens file and does pre-processing, including finding the begining and end of
    the book and making the book all lower case."""
    pickledName = name + '.pickle'
    opened = open(pickledName, 'rb')
    txt = pickle.load(opened)
    s = (txt.find('*** START OF THIS PROJECT GUTENBERG EBOOK ALICE’S ADVENTURES IN WONDERLAND ***'))+len('*** START OF THIS PROJECT GUTENBERG EBOOK ALICE’S ADVENTURES IN WONDERLAND ***')
    e = (txt.find('End of Project Gutenberg’s Alice’s Adventures in Wonderland, by Lewis Carroll'))+len('End of Project Gutenberg’s Alice’s Adventures in Wonderland, by Lewis Carroll')
    txt = txt[s:e]
    txt = txt.lower()
    return txt

def sortText(t):
    """Tokenizes the words in the book making a list of words in the book, then orders them
    according to frequency, removes non-alphabetic characters, and returns the first 100
    words of that list."""
    tknzr = TweetTokenizer()
    token = tknzr.tokenize(t)
    counts = collections.Counter(token)
    new_list = sorted(set(token), key=counts.get, reverse=True)
    chars_to_remove = string.punctuation + '’‘”“'
    for chars in chars_to_remove:
        if chars in new_list:
            new_list.remove(chars)
        else:
            continue
    return new_list[0:100]


print(sortText(openFile('alice')))
