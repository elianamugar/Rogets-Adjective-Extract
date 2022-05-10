#requires download of nltk in python
import os
import nltk
from nltk.corpus import *
import string

def main():
    file_content = open("/Users/EMWork/Desktop/Boston University/EVL/Adjective Analysis/rog_ads_raw.txt").read()
    tokens = nltk.word_tokenize(file_content)
    tagged_corpora = nltk.pos_tag(tokens)
    update_corpora = ""

    for i in range(len(tagged_corpora)):
        if ((('JJ' in tagged_corpora[i]) or ('JJR' in tagged_corpora[i]) or ('JJS' in tagged_corpora[i])) and (('such' not in tagged_corpora[i]) and ('Such' not in tagged_corpora[i]))):
            update_corpora += str(tagged_corpora[i][0]) + "\n"

    f = open(str(input("Enter filename for which you want the data text to be exported (with .txt): \n")), "w")
    f.write(update_corpora)

while True:
    answer = input("Run the Roget's Adjective Extractor program? (y/n): ")
    if answer not in ('y', 'n'):
        print("Invalid input.")
        break
    if answer == 'y':
        main()
    else:
        print("Goodbye.")
        break